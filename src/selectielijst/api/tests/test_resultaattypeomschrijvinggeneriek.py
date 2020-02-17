from django.test import override_settings

from dateutil.relativedelta import relativedelta
from rest_framework import status
from rest_framework.test import APITestCase
from vng_api_common.tests import reverse

from selectielijst.selectielijst.tests.factories import (
    ResultaatTypeOmschrijvingGeneriekFactory,
)


class ResultaatTypeOmschrijvingGeneriekTests(APITestCase):
    def test_lijst_resultaattypeomschrijvingen(self):
        url = reverse("resultaattypeomschrijvinggeneriek-list")
        ResultaatTypeOmschrijvingGeneriekFactory.create_batch(5)

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()
        self.assertEqual(len(response_data), 5)

        # assert we can follow urls
        detail_url = response_data[2]["url"]

        detail = self.client.get(detail_url)

        self.assertEqual(detail.status_code, status.HTTP_200_OK)
