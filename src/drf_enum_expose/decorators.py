
from typing import Optional, Type

from django.db import models

from .registry import registry


def register_enum(
    cls: Optional[Type[models.TextChoices]] = None,
    *,
    name: Optional[str] = None,
):
    """
    Decorator to register an enum for API exposure

    usage:
        @register_enum
        class Content_type(models.TextChoices):
            VIDEO = "VIDEO","Video"

        @register_enum(name="activity")
        class ActivityType(models.TextChoices):
            LEARNING = "LEARNING", "Learning"

    """
    def decorator(enum_class: Type[models.TextChoices]):
        enum_name = name or enum_class.__name__

        registry.register(
            name=enum_name,
            enum_class=enum_class,
        )

        return enum_class

    if cls is not None:
        return decorator(cls)

    return decorator
