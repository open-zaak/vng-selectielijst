from django.db import models
from django.db.models import Case, QuerySet, Value, When


class ResultaatQuerySet(QuerySet):
    def tree_order(self):
        """
        Order from generic -> specific, by numbers.
        """
        case_generic = Case(
            When(generiek_resultaat__isnull=True, then="nummer"),
            When(generiek_resultaat__isnull=False, then="generiek_resultaat__nummer"),
            output_field=models.PositiveSmallIntegerField(),
        )

        case_specific = Case(
            When(generiek_resultaat__isnull=True, then=Value(0)),
            When(generiek_resultaat__isnull=False, then="nummer"),
            output_field=models.PositiveSmallIntegerField(),
        )

        return self.order_by("proces_type__nummer", case_generic, case_specific)
