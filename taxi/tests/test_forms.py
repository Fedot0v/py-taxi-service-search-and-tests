from django.test import TestCase

from taxi.forms import DriverCreationForm


class DriverFormsTests(TestCase):
    def setUp(self):
        pass

    def test_driver_creation_with_license_first_name_last_name_is_valid(self):
        form_data = {
            "username": "new_user",
            "password1": "user12test",
            "password2": "user12test",
            "first_name": "Test_first",
            "last_name": "Test_last",
            "license_number": "SSD12345",
        }
        form = DriverCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
        self.assertEqual(form.cleaned_data.get("license_number"), "SSD12345")
