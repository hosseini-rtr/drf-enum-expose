from typing import Any, Dict, List, Optional, Type

from django.core.cache import cache
from django.db import models


class EnumRegistry:
    """Central registry for Django enum classes."""

    def __init__(self):
        self._enums: Dict[str, Type[models.TextChoices]] = {}

    def register(
        self,
        name: Optional[str] = None,
        enum_class: Optional[Type[models.TextChoices]] = None,
    ):
        """Register an enum class."""

        if enum_class is None:

            def decorator(cls: Type[models.TextChoices]):
                enum_name = name or cls.__name__
                self._enums[enum_name] = cls

                if self._debug:
                    print(f"Registered enum: {enum_name}")

                self.clear_cache()
                return cls

            return decorator

        enum_name = name or enum_class.__name__
        self._enums[enum_name] = enum_class

        if self._debug:
            print(f"Registered enum: {enum_name}")

        self.clear_cache()
        return enum_class

    def get_all_enums(self) -> Dict[str, List[Dict[str, str]]]:
        result = {}

        for name, enum_class in self._enums.items():
            result[name] = [
                {
                    "value": value,
                    "label": label,
                }
                for value, label in enum_class.choices
            ]

        return result

    def get_enum_choices(
        self,
        name: str,
    ) -> Optional[List[Dict[str, Any]]]:
        enum_class = self._enums.get(name)

        if enum_class is None:
            return None

        return [
            {
                "value": value,
                "label": label,
            }
            for value, label in enum_class.choices
        ]

    def get_enum_names(self) -> List[str]:
        return list(self._enums.keys())

    def clear_cache(self):
        cache.delete("drf_enum_all_enums")

    def debug_info(self):
        return {
            "total_enums": len(self._enums),
            "enum_names": list(self._enums.keys()),
            "details": {
                name: {
                    "class": cls.__name__,
                    "module": cls.__module__,
                    "choices_count": len(cls.choices),
                    "choices": list(cls.choices),
                    "values": [c[0] for c in cls.choices],
                    "labels": [c[1] for c in cls.choices],
                }
                for name, cls in self._enums.items()
            },
        }

    _debug = True


registry = EnumRegistry()
