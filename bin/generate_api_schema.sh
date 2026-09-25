#!/bin/sh
#
# Generate the API schema from the code into the output file.
#
# Run this script from the root of the repository:
#
#   ./bin/generate_api_schema.sh [outfile]
#
# 'outfile' defaults to `src/selectielijst/openapi.yml`
#
# For multiple API specifications (different components or multiple major versions),
# take a look at the Open Zaak configuration.
#

src/manage.py spectacular \
    --validate \
    --fail-on-warn \
    --lang=nl \
    --urlconf selectielijst.api.urls \
    --file src/openapi.yaml \
    --custom-settings selectielijst.api.urls.custom_settings