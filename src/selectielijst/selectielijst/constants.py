from django.db import models
from django.utils.translation import gettext_lazy as _


class Procestermijnen(models.TextChoices):
    nihil = (
        "nihil",
        _(
            "Nihil. "
            "Er is geen aparte procestermijn, de bewaartermijn start direct "
            "na de procesfase."
        ),
    )

    bestaansduur_procesobject = (
        "bestaansduur_procesobject",
        _(
            "De bestaans- of geldigheidsduur van het procesobject. "
            "De lengte van de procestermijn is afhankelijk van het procesobject. "
            "Nadat het procesobject haar geldigheid heeft verloren of niet meer "
            "bestaat, gaat de bewaartermijn lopen."
        ),
    )

    ingeschatte_bestaansduur_procesobject = (
        "ingeschatte_bestaansduur_procesobject",
        _(
            "De ingeschatte maximale bestaans- of geldigheidsduur van het "
            "procesobject. "
            "Er wordt een inschatting gemaakt van de maximale bestaans- of "
            "geldigheidsduur van het procesobject, ongeacht de daadwerkelijke "
            "duur. Dit kan bijvoorbeeld al vastgelegd worden in het zaaktype, "
            "zodat procestermijn en bewaartermijn samen een bewaartermijn "
            "vormen die direct kan gaan lopen na de procesfase."
        ),
    )

    vast_te_leggen_datum = (
        "vast_te_leggen_datum",
        _(
            "De tijdens het proces vast te leggen datum waarop de geldigheid "
            "van het procesobject komt te vervallen. "
            "Tijdens de procesuitvoering wordt de datum bepaald wanneer het "
            "procesobject zijn geldigheid zal verliezen en de procestermijn "
            "beëindigd wordt."
        ),
    )

    samengevoegd_met_bewaartermijn = (
        "samengevoegd_met_bewaartermijn",
        _(
            "De procestermijn is samengevoegd met de bewaartermijn. "
            "De procestermijn en bewaartermijn zijn samengevoegd als "
            "totaalwaarde bij de bewaartermijn. De datum waarop deze "
            "bewaartermijn moet gaan lopen is benoemd in de toelichting "
            "bij de categorie en kan ook in het verleden liggen, "
            "bijvoorbeeld op basis van een geboortedatum."
        ),
    )
