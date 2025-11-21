from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Profile

class ProfileAPITest(APITestCase):

    def setUp(self):
        self.profile = Profile.objects.create(
            name="Arul",
            age=28,
            gender="Male",
            location="Coimbatore"
        )

    def test_get_profiles(self):
        url = reverse("profiles")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_profile(self):
        url = reverse("profiles")
        data = {"name": "Sara", "age": 25, "gender": "Female", "location": "Chennai"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_profile(self):
        url = reverse("profile-detail", args=[self.profile.id])
        data = {"name": "Arul Updated", "age": 29, "gender": "Male", "location": "Coimbatore"}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_profile(self):
        url = reverse("profile-detail", args=[self.profile.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
