"""Nested list structures where element in list could be value or another list"""


from typing import Union


class NestedInteger:
    _val: Union[int, list["NestedInteger"]]

    def __init__(self, val: Union[int, list["NestedInteger"]]) -> None:
        self._val = val

    def is_integer(self) -> bool:
        return isinstance(self._val, int)

    def get_integer(self) -> int:
        assert isinstance(self._val, int)
        return self._val

    def get_list(self) -> list["NestedInteger"]:
        assert isinstance(self._val, list)
        return self._val

    @classmethod
    def from_list(cls, values: list) -> "NestedInteger":
        nested_list = []
        for el in values:
            if isinstance(el, int):
                nested_list.append(cls(el))
            else:
                nested_list.append(cls.from_list(el))

        return cls(nested_list)
