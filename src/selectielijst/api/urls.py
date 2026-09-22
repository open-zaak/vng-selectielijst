from django.urls import include, path, re_path

from drf_spectacular.views import (
    SpectacularRedocView,
)
from vng_api_common import routers

from selectielijst.selectielijst.api.viewsets import (
    ProcesTypeViewSet,
    ResultaatTypeOmschrijvingGeneriekViewSet,
    ResultaatViewSet,
)

from ..utils.views import SpectacularJSONAPIView, SpectacularYAMLAPIView
from .schema import custom_settings

router = routers.DefaultRouter()
router.register("procestypen", ProcesTypeViewSet)
router.register("resultaten", ResultaatViewSet)
router.register("resultaattypeomschrijvingen", ResultaatTypeOmschrijvingGeneriekViewSet)


# TODO: the EndpointEnumerator seems to choke on path and re_path

urlpatterns = [
    re_path(
        r"^v(?P<version>\d+)/",
        include(
            [
                re_path(r"^", include(router.urls)),
                path("", router.APIRootView.as_view(), name="root"),
                path(
                    "openapi.json",
                    SpectacularJSONAPIView.as_view(
                        urlconf="selectielijst.api.urls",
                        custom_settings=custom_settings,
                    ),
                    name="schema-json-selectielijst",
                ),
                path(
                    "openapi.yaml",
                    SpectacularYAMLAPIView.as_view(
                        urlconf="selectielijst.api.urls",
                        custom_settings=custom_settings,
                    ),
                    name="schema-yaml-selectielijst",
                ),
                path(
                    "schema/",
                    SpectacularRedocView.as_view(
                        url_name="schema-yaml-selectielijst",
                    ),
                    name="schema-redoc",
                ),
            ]
        ),
    )
]
