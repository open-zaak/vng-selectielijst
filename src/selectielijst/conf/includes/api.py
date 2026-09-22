from vng_api_common.conf.api import *  # noqa - imports white-listed

API_VERSION = "1.0.0"
API_SCHEMA_VERSION = "1"
REST_FRAMEWORK = BASE_REST_FRAMEWORK.copy()
REST_FRAMEWORK["DEFAULT_PAGINATION_CLASS"] = (
    "rest_framework.pagination.PageNumberPagination"
)
REST_FRAMEWORK["PAGE_SIZE"] = 100

SPEC_CACHE_TIMEOUT = 60 * 60 * 24  # 24 hours

SPECTACULAR_SETTINGS = {
    "CONTACT": {
        "url": "https://github.com/open-zaak/vng-selectielijst",
        "name": "Maykin Media",
        "email": "support@maykinmedia.nl",
    },
    "SERVE_INCLUDE_SCHEMA": False,
    "SWAGGER_UI_DIST": "SIDECAR",
    "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    "REDOC_DIST": "SIDECAR",
    "SCHEMA_PATH_PREFIX": r"/v[0-9]+",
    "SCHEMA_PATH_PREFIX_TRIM": True,
    "ENUM_GENERATE_CHOICE_DESCRIPTION": False,
    "POSTPROCESSING_HOOKS": [
        "drf_spectacular.hooks.postprocess_schema_enums",
        "drf_spectacular.contrib.djangorestframework_camel_case.camelize_serializer_fields",
    ],
    "LICENSE": {
        "name": "EUPL 1.2",
        "url": "https://opensource.org/licenses/EUPL-1.2",
    },
}
