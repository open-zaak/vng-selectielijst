from django.utils.functional import Promise
from django.utils.translation import gettext_lazy as _

from vng_api_common.choices import TextChoicesWithDescriptions


class Procestermijnen(TextChoicesWithDescriptions):
    NIHIL = "nihil", _("Nihil")
    BESTAANSDUUR_PROCESOBJECT = (
        "bestaansduur_procesobject",
        _("De bestaans- of geldigheidsduur van het procesobject."),
    )
    INGESCHATTE_BESTAANSDUUR_PROCESOBJECT = (
        "ingeschatte_bestaansduur_procesobject",
        _("De ingeschatte maximale bestaans- of geldigheidsduur van het procesobject."),
    )
    VAST_TE_LEGGEN_DATUM = (
        "vast_te_leggen_datum",
        _(
            "De tijdens het proces vast te leggen datum waarop de geldigheid "
            "van het procesobject komt te vervallen. "
        ),
    )
    SAMENGEVOEGD_MET_BEWAARTERMIJN = (
        "samengevoegd_met_bewaartermijn",
        _("De procestermijn is samengevoegd met de bewaartermijn."),
    )

    @classmethod
    def descriptions(cls) -> dict[str, str | Promise]:
        return {
            cls.NIHIL: _(
                "Er is geen aparte procestermijn, de bewaartermijn "
                "start direct na de procesfase."
            ),
            cls.BESTAANSDUUR_PROCESOBJECT: _(
                "De lengte van de procestermijn is afhankelijk van het "
                "procesobject. Nadat het procesobject haar geldigheid heeft "
                "verloren of niet meer bestaat, gaat de bewaartermijn lopen."
            ),
            cls.INGESCHATTE_BESTAANSDUUR_PROCESOBJECT: _(
                "Er wordt een inschatting gemaakt van de maximale bestaans- "
                "of geldigheidsduur van het procesobject, ongeacht de "
                "daadwerkelijke duur. Dit kan bijvoorbeeld al vastgelegd "
                "worden in het zaaktype, zodat procestermijn en bewaartermijn "
                "samen een bewaartermijn vormen die direct kan gaan lopen "
                "na de procesfase."
            ),
            cls.VAST_TE_LEGGEN_DATUM: _(
                "Tijdens de procesuitvoering wordt de datum bepaald wanneer "
                "het procesobject zijn geldigheid zal verliezen en de "
                "procestermijn beëindigd wordt."
            ),
            cls.SAMENGEVOEGD_MET_BEWAARTERMIJN: _(
                "De procestermijn en bewaartermijn zijn samengevoegd als "
                "totaalwaarde bij de bewaartermijn. De datum waarop deze "
                "bewaartermijn moet gaan lopen is benoemd in de toelichting "
                "bij de categorie en kan ook in het verleden liggen, "
                "bijvoorbeeld op basis van een geboortedatum."
            ),
        }
