from django.urls import path

from .views import EnumsListView, EnumDetailsView, EnumStatsView

app_name = "drf_enum_expose"

urlpatterns = [
    path("", EnumsListView.as_view(), name="enum-list"),
    path("<str:enum_name>", EnumDetailsView.as_view(), name="enum-detail"),
    path("stats/", EnumStatsView.as_view(), name="enum-stats"),
]
management/commands/check_enums.py