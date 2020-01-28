from rest_framework.test import APITestCase
from vng_api_common.tests import reverse

from selectielijst.selectielijst.tests.factories import ProcesTypeFactory


class ProcesTypeTests(APITestCase):
    def test_create_forbidden(self):
        url = reverse("procestype-list")

        response = self.client.post(url, {"naam": "foo", "omschrijving": "bar"})

        self.assertGreater(response.status_code, 400)
        self.assertLess(response.status_code, 500)

    def test_update_forbidden(self):
        procestype = ProcesTypeFactory.create()
        url = reverse("procestype-detail", kwargs={"uuid": procestype.uuid})
        detail_data = self.client.get(url).data

        response = self.client.put(url, detail_data)

        self.assertGreater(response.status_code, 400)
        self.assertLess(response.status_code, 500)

        response = self.client.patch(url, {"nummer": 1234})

        self.assertGreater(response.status_code, 400)
        self.assertLess(response.status_code, 500)
