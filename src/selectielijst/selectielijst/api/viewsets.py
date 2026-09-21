from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
)
from rest_framework import viewsets

from ..models import ProcesType, Resultaat, ResultaatTypeOmschrijvingGeneriek
from .filters import ProcesTypeFilter, ResultaatFilter
from .serializers import (
    ProcesTypeSerializer,
    ResultaatSerializer,
    ResultaatTypeOmschrijvingGeneriekSerializer,
)


@extend_schema_view(
    list=extend_schema(
        summary="Ontsluit de selectielijst procestypen.",
    ),
    retrieve=extend_schema(
        summary="Ontsluit de selectielijst procestypen.",
    ),
)
class ProcesTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Procestypen worden gerefereerd in zaaktypecatalogi - bij het configureren
    van een zaaktype wordt aangegeven welk procestype van toepassing is, zodat
    het archiefregime van zaken bepaald kan worden.

    Zie https://vng.nl/files/vng/20170706-selectielijst-gemeenten-intergemeentelijke-organen-2017.pdf
    voor de bron van de inhoud.
    """

    queryset = ProcesType.objects.order_by("nummer")
    serializer_class = ProcesTypeSerializer
    lookup_field = "uuid"
    filterset_class = ProcesTypeFilter
    pagination_class = None


@extend_schema_view(
    list=extend_schema(
        summary="Ontsluit de selectielijst resultaten.",
    ),
    retrieve=extend_schema(
        summary="Ontsluit de selectielijst resultaten.",
    ),
)
class ResultaatViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Bij een procestype horen meerdere mogelijke resultaten, al dan niet
    generiek/specifiek. Bij het configureren van een resultaattype in het ZTC
    wordt aangegeven welke selectielijstklasse van toepassing is, wat een
    referentie is naar een item van deze resource.

    Zie https://vng.nl/files/vng/20170706-selectielijst-gemeenten-intergemeentelijke-organen-2017.pdf
    voor de bron van de inhoud.
    """

    queryset = Resultaat.objects.tree_order()
    serializer_class = ResultaatSerializer
    lookup_field = "uuid"
    filterset_class = ResultaatFilter


@extend_schema_view(
    list=extend_schema(
        summary="Raadpleeg de generieke resultaattypeomschrijvingen.",
    ),
    retrieve=extend_schema(
        summary="Raadpleeg de generieke resultaattypeomschrijvingen.",
    ),
)
class ResultaatTypeOmschrijvingGeneriekViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ResultaatTypeOmschrijvingGeneriek.objects.order_by("omschrijving")
    serializer_class = ResultaatTypeOmschrijvingGeneriekSerializer
    lookup_field = "uuid"
    pagination_class = None
