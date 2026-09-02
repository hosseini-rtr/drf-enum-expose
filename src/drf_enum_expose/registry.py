from typing import Dict, List, Type, Optional
from django.db import models
from django.core.cache import cache


class EnumRegistry:
    """
    Central registry for Django enum classes
    """

    _instance = None
    _enums: Dict[str, Type[models.TextChoices]] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._enums = {}
        return cls._instance

    def register(
        self,
        name: Optional[str] = None,
        enum_class: Optional[Type[models.TextChoices]] = None,
    ):
        """Register an enum class"""
        if enum_class is None:

            def decorator(cls):
                enum_name = name or cls.__name__
                self._enums[enum_name] = cls
                return cls

            return decorator

        enum_name = name or enum_class.__name__
        self._enum[enum_name] = enum_class
        return enum_class

    def get_all_enums(self) -> Dict[str, List[Dict[str, str]]]:
        """Get all registered enums in API formant"""
        cache_key = "drf_enum_all_enums"
        cached = cache.get(cache_key)
        if cached:
            return cached

        result = {}
        for name, enum_class in self._enums.items():
            result[name] = [
                {"value": choice[0], "lable": choice[1]}
                for choice in enum_class.choices
            ]
        # TODO: Dynamic set cache time rom settings django or .env
        cache.set(cache_key, result, 3600)  # Cache for 1 hour
        return result

    def get_enum_choices(self, name: str) -> Optional[List[Dict[str, str]]]:
        """Get list of all registred enum names"""
        return list(self._enums.keys)

    def clear_cache(self):
        cache.delete("drf_enum_all_enums")


registry = EnumRegistry()
