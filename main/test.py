from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Contact
from django.contrib.auth.models import User
from .serializers import ContactSerializer


class BaseViewTest(APITestCase):
    client = APIClient()


    @staticmethod
    def create_contact(username,first_name,email,surname):
        Contact.objects.create(username=username, first_name=first_name,email=email, surname=surname)
    
    def setUp(self):
        # add user test data
        User.objects.create_user("MyUserName1", first_name="Name One", email="email1@mailserver.com", "Person1")
        User.objects.create_user("MyUserName2", first_name="Name Two", email="email2@mailserver.com", "Person2")
        User.objects.create_user("MyUserName3", first_name="Name Three", email="email3@mailserver.com", "Person3")
        User.objects.create_user("MyUserName4", first_name="Name Four", email="email4@mailserver.com", "Person4")
        

class GetAllBooks(BaseViewTest):

    def test_get_all_contacts(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("contacts-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Contact.objects.all()
        serialized = ContactSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
