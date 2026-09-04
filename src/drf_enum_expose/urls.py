from django.urls import path

from .views import EnumDetailsView, EnumsListView, EnumStatsView

app_name = "drf_enum_expose"

urlpatterns = [
    path("stats/", EnumStatsView.as_view(), name="enum-stats"),
    path("", EnumsListView.as_view(), name="enum-list"),
    path("<str:enum_name>/", EnumDetailsView.as_view(), name="enum-detail"),
]
