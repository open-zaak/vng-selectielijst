from django.conf import settings

from drf_yasg import openapi

DESCRIPTION = """
Een API de Gemeentelijke Selectielijst 2017 te benaderen.

## Selectielijst

De [Gemeentelijke Selectielijst](https://vng.nl/selectielijst) is relevant
in het kader van archivering.

**Zaakgericht werken**

Bij het configureren van zaaktypes (en resultaattypes) in de catalogus API
refereren een aantal resources naar resources binnen de Selectielijst API. Het
gaat dan om de `ProcesType` en `Resultaat` resources.

## Autorisatie

Deze APIs zijn alleen-lezen, en behoeven geen autorisatie.

## Inhoud

De inhoud wordt beheerd door VNG Realisatie. De Gemeentelijke Selectielijst werd in
2017 vastgesteld en is statisch tot er een nieuwe versie uitgebracht wordt.

De inhoud werd geïmporteerd vanuit de gepubliceerde Excel-bestanden.
"""

info = openapi.Info(
    title="Selectielijst API",
    default_version=settings.API_VERSION,
    description=DESCRIPTION,
    contact=openapi.Contact(
        email="support@maykinmedia.nl",
        url="https://github.com/oopen-zaak/vng-selectielijst",
    ),
    license=openapi.License(
        name="EUPL 1.2", url="https://opensource.org/licenses/EUPL-1.2"
    ),
)
