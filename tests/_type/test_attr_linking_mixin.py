import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._type.attr_linking_mixin import AttrLinkingMixIn


class TestAttrLinkingMixIn:
    @apply_test_settings()
    def test__initialize_attr_linking_stack(self) -> None:
        interface: AttrLinkingMixIn = AttrLinkingMixIn()
        interface._initialize_attr_linking_stack(attr_name="x")
        assert interface._attr_linking_stack == {"x": []}
        interface._attr_linking_stack["x"].append(ap.Int(10))
        interface._initialize_attr_linking_stack(attr_name="x")
        assert interface._attr_linking_stack == {"x": [ap.Int(10)]}

    @apply_test_settings()
    def test__append_attr_to_linking_stack(self) -> None:
        interface: AttrLinkingMixIn = AttrLinkingMixIn()
        attr: ap.Int = ap.Int(10)
        interface._append_attr_to_linking_stack(attr=attr, attr_name="x")
        assert interface._attr_linking_stack == {"x": [ap.Int(10)]}

        interface._append_attr_to_linking_stack(attr=attr, attr_name="x")
        assert interface._attr_linking_stack == {"x": [ap.Int(10)]}

    @apply_test_settings()
    def test__append_applying_new_attr_val_exp(self) -> None:
        expression_data_util.empty_expression()
        interface: AttrLinkingMixIn = AttrLinkingMixIn()
        attr_1: ap.Int = ap.Int(10)
        attr_2: ap.Int = ap.Int(20)
        new_attr: ap.Int = ap.Int(30)
        interface._append_attr_to_linking_stack(attr=attr_1, attr_name="x")
        interface._append_attr_to_linking_stack(attr=attr_2, attr_name="x")
        interface._append_attr_to_linking_stack(attr=new_attr, attr_name="x")
        interface._append_applying_new_attr_val_exp(new_attr=new_attr, attr_name="x")
        expression: str = expression_data_util.get_current_expression()
        assert f"{attr_1.variable_name} = {new_attr.variable_name};" in expression
        assert f"{attr_2.variable_name} = {new_attr.variable_name};" in expression
        assert f"{new_attr.variable_name} = {new_attr.variable_name};" not in expression

    @apply_test_settings()
    def test__is_target_attr_already_linked(self) -> None:
        interface: AttrLinkingMixIn = AttrLinkingMixIn()
        attr: ap.Int = ap.Int(10)
        assert not interface._is_target_attr_already_linked(attr=attr, attr_name="x")

        interface._append_attr_to_linking_stack(attr=attr, attr_name="x")
        assert interface._is_target_attr_already_linked(attr=attr, attr_name="x")
