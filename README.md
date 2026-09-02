# DRF Enum Expose

Simple and automatic enum management for Django with REST API exposure.

## Installation

```bash
pip install drf-enum-expose
```

## Quick Start

1. Add `drf_enum_expose` to `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    'drf_enum_expose',
]
```

2. Register your enums:
```python
from django.db import models
from drf_enum_expose import register_enum

@register_enum
class ContentType(models.TextChoices):
    VIDEO = "VIDEO", "Video"
    AUDIO = "AUDIO", "Audio"
```

3. Include URLs:
```python
urlpatterns = [
    path('api/enums/', include('drf_enum_expose.urls')),
]
```

4. Access API:
```bash
GET /api/enums/
GET /api/enums/ContentType/
GET /api/enums/stats/
```

## Features

- 🔄 Automatic enum registration with decorator
- 📡 REST API for all enums
- 💾 Built-in caching
- 📊 Statistics endpoint
- 🔍 Management command for checking enums
