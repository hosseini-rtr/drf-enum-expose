from typing import Optional

from .registry import registry


def register_enum(name: Optional[str] = None):
    """
    Decorator to register an enum for API exposure

    usae:
        @regiser_enum
        class Content_type(models.TextChoices):
            VIDEO = "VIDEO","Video"

        @register_enum
        class ActivityType(models.TextChoices):
            LEARNING = "LEARNING", "Learning"

    """
    return registry.register(name)
