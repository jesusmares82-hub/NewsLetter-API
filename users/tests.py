from rest_framework.test import APITestCase
from newsletters.models import NewsLetters
from tags.models import Tags
from users.models import Users


# Create your tests here.
class UsersTestCase(APITestCase):

    def setUp(self):
        self.url = 'http://localhost:8000'

        self.user = Users.objects.create(
            name='Jesus',
            lastName='Mares',
            email='mares@test.com',
            password='hello'
        )
        self.tag = Tags.objects.create(
            name='Economy',
            slug='Economy'
        )
        self.tag2 = Tags.objects.create(
            name='Sports',
            slug='Sports'
        )
        self.newsletter = NewsLetters.objects.create(
            name='Hello CDMX',
            description='The best newsletter',
            image='assets/newsletters/chat.png',
            meta='metameta',
            frequency='15'
        )
        self.newsletter2 = NewsLetters.objects.create(
            name='The Economist',
            description='The best economy newsletter',
            image='assessts/newsletters/chat.png',
            meta='metamessta',
            frequency='135'
        )
        self.newsletter.tags.add(self.tag)
        self.newsletter.users.add(self.user)
        self.newsletter2.users.add(self.user)
        self.newsletter2.tags.add(self.tag2)

    def test_get_newsletters_by_id(self):
        new_url = self.url + f'/api/v1/users/{self.user.id}/newsletters/'
        response = self.client.get(new_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_post_newsletters_by_id(self):
        new_url = self.url + f'/api/v1/users/{self.user.id}/newsletters/'
        response = self.client.post(new_url, {'id': [f'{self.newsletter2.id}'], })
        self.assertEqual(response.status_code, 201)

    def test_delete_newsletters_by_id(self):
        new_url = self.url + f'/api/v1/users/{self.user.id}/newsletters/'
        response = self.client.delete(new_url, {'id': [f'{self.newsletter2.id}'], })
        self.assertEqual(response.status_code, 204)
