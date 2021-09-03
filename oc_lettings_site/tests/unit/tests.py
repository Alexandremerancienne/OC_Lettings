from django.test import TestCase
from django.urls import reverse


class WelcomePageViewTest(TestCase):

    def test_welcome_page_url_exists_at_proper_location(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)

    def test_welcome_page_url_return_correct_content(self):
        resp = self.client.get(reverse('index'))
        self.assertIn(b'Welcome to Holiday Homes', resp.content)
        self.assertIn(b'Profiles', resp.content)
        self.assertIn(b'Lettings', resp.content)

    def test_lettings_url_return_correct_title(self):
        self.client.get(reverse('index'))
        self.assertInHTML('Welcome to Holiday Homes',
                          '<h1>Welcome to Holiday Homes</h1>')

    def test_views_uses_correct_template(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'index.html')
