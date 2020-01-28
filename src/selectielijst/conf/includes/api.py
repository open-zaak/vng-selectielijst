from vng_api_common.conf.api import *  # noqa - imports white-listed

API_VERSION = "1.0.0"

REST_FRAMEWORK = BASE_REST_FRAMEWORK.copy()
REST_FRAMEWORK[
    "DEFAULT_PAGINATION_CLASS"
] = "rest_framework.pagination.PageNumberPagination"
REST_FRAMEWORK["PAGE_SIZE"] = 100
REST_FRAMEWORK["DEFAULT_FILTER_BACKENDS"] = ("vng_api_common.filters.Backend",)

SWAGGER_SETTINGS = BASE_SWAGGER_SETTINGS.copy()
SWAGGER_SETTINGS.update(
    {"DEFAULT_INFO": "selectielijst.api.schema.info", "SECURITY_DEFINITIONS": {},}
)

SPEC_CACHE_TIMEOUT = 60 * 60 * 24  # 24 hours
