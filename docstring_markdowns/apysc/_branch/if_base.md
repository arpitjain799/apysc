# `apysc._branch.if_base` docstrings

## Module summary

This module is for the abstract base class implementation for if, else if, and else.

## `IfBase` class docstring

### `__enter__` method docstring

Method to be called when beginning of the with statement.<hr>

**[Returns]**

- `self`: IfBase
  - This instance.

### `__exit__` method docstring

Method to be called when ending of the with statement.<hr>

**[Parameters]**

- `exc_type`: Type
  - Exception type.
- `exc_value`: *
  - Exception value.
- `traceback`: *
  - Traceback value.

### `__init__` method docstring

A class to append if (else if and else) branch instruction expression.<hr>

**[Parameters]**

- `condition`: Boolean or None
  - Boolean value to be used for judgment.
- `locals_`: dict or None, default None
  - Current scope's local variables. Set locals() value to this argument. If specified, this interface reverts all local scope VariableNameInterface variables (like Int, Sprite) at the end of the `If` or the other branch scope. This setting is useful when you don't want to update each variable by implementing the `If` or the other scope.
- `globals_`: dict or None, default None
  - Current scope's global variables. Set the globals() value to this argument. This setting works the same way as the `locals_` argument.

<hr>

**[References]**

- [If document](https://simon-ritchie.github.io/apysc/en/if.html)
- [Elif document](https://simon-ritchie.github.io/apysc/en/elif.html)
- [Else document](https://simon-ritchie.github.io/apysc/en/else.html)
- [Each branch instruction class's scope variables reverting setting](https://simon-ritchie.github.io/apysc/en/branch_instruction_variables_reverting_setting.html)

### `_append_enter_expression` method docstring

Append branch instruction start expression.

### `_append_exit_expression` method docstring

Append if branch instruction ending expression.

### `_last_scope_is_if_or_elif` method docstring

Get a boolean value whether the last scope is If or Elif.<hr>

**[Returns]**

- `result`: bool
  - If the last scope is If or Else, this interface returns True.

### `_set_last_scope` method docstring

Set expression last scope value.