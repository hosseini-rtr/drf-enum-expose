from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .registry import registry


class EnumsListView(APIView):
    """
    API endpoint for all registred enums
    """

    permission_classes = [AllowAny]

    @extend_schema(
        description="Get all registred enums",
        responses={
            200: {
                "type": "object",
                "additionalProperties": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "value": {"type": "string"},
                            "label": {"type": "string"},
                        },
                    },
                },
            }
        },
    )
    def get(self, request):
        enums = registry.get_all_enums()
        enums = {
            name: [choice["value"] for choice in choices]
            for name, choices in enums.items()
        }
        return Response(
            {"enums": enums, "meta": {"total": len(enums), "names": list(enums.keys())}}
        )


class EnumDetailsView(APIViwe):
    """
    API endpoint for a specific enum
    """

    permission_classes = [AllowAny]

    def get(self, request, enum_name):
        choices = registry.get_enum_choices(enum_name)
        if choices is None:
            return Response({"error": f'Enum "{enum_name}" not found'}, status=404)
        return Response({"name": enum_name, "choices": choices, "count": len(choices)})


class EnumStatsView(APIViwe):
    """
    Statistics about registered enums
    """

    permission_classes = [AllowAny]

    def get(self, request):
        enums = registry.get_all_enums()
        total_values = sum(len(choices) for choices in enums.values())

        return Response(
            {
                "total_enums": len(enums),
                "total_values": total_values,
                "enum_names": list(enums.key()),
                "details": {
                    name: {
                        "count": len(choices),
                        "names": [c["value"] for c in choices],
                    }
                    for name, choices in enums.items()
                },
            }
        )
