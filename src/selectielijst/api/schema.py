from django.conf import settings

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

custom_settings = {
    "TITLE": "Selectielijst API",
    "DESCRIPTION": DESCRIPTION,
    "VERSION": settings.API_VERSION,
    "SERVERS": [{"url": f"/api/v{settings.API_SCHEMA_VERSION}"}],
}
