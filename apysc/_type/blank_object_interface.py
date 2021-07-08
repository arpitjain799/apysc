"""Class implementation for the blank object interface.
This interface will be used by the custom event interface
or something else.
"""


class BlankObjectInterface:

    _is_blank_object_initialized: bool = False
    _blank_object_variable_name: str

    def _initialize_blank_object_if_not_initialized(self) -> None:
        """
        Initialize a blank object value if it hasn't been
        initialized yet.
        """
        from apysc._expression import expression_file_util
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names
        from apysc._expression.event_handler_scope import \
            TemporaryNotHandlerScope
        if self._is_blank_object_initialized:
            return
        with TemporaryNotHandlerScope():
            self._blank_object_variable_name = expression_variables_util.\
                get_next_variable_name(type_name=var_names.BLANK_OBJECT)
            expression: str = (
                f'var {self._blank_object_variable_name} = {{}};'
            )
            expression_file_util.append_js_expression(expression=expression)
            self._is_blank_object_initialized = True

    @property
    def blank_object_variable_name(self) -> str:
        """
        Get a blank object variable name.

        Returns
        -------
        blank_object_variable_name : str
            A blank object variable name.
        """
        self._initialize_blank_object_if_not_initialized()
        return self._blank_object_variable_name
