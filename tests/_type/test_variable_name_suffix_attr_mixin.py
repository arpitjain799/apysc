from random import randint

from retrying import retry

from apysc._type.variable_name_suffix_attr_mixin import VariableNameSuffixAttrMixIn
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn


class _TestClass1(VariableNameSuffixAttrMixIn):
    pass


class _TestClass2(VariableNameSuffixMixIn, VariableNameSuffixAttrMixIn):
    pass


class TestVariableNameSuffixAttrMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_attr_variable_name_suffix(self) -> None:
        instance_1: _TestClass1 = _TestClass1()
        assert instance_1._get_attr_variable_name_suffix(attr_identifier="x") == ""

        instance_2: _TestClass2 = _TestClass2()
        assert instance_2._get_attr_variable_name_suffix(attr_identifier="x") == ""

        instance_2._variable_name_suffix = "test_instance"
        assert (
            instance_2._get_attr_variable_name_suffix(attr_identifier="x")
            == "test_instance__x"
        )
