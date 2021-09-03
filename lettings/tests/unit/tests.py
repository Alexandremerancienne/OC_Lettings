from django.test import TestCase
from django.urls import reverse
from ...models import Letting, Address


class LettingsMainPageViewTest(TestCase):

    def test_lettings_url_exists_at_proper_location(self):
        resp = self.client.get(reverse('lettings_index'))
        self.assertEqual(resp.status_code, 200)

    def test_lettings_url_return_correct_content(self):
        resp = self.client.get(reverse('lettings_index'))
        self.assertIn(b'Lettings', resp.content)
        self.assertIn(b'Home', resp.content)
        self.assertIn(b'Profiles', resp.content)

    def test_lettings_url_return_correct_title(self):
        self.client.get(reverse('lettings_index'))
        self.assertInHTML('Lettings', '<h1>Lettings</h1>')

    def test_views_uses_correct_template(self):
        resp = self.client.get(reverse('lettings_index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'lettings/index.html')


class LettingsDetailedPageViewTest(TestCase):

    def setUp(self):
        Address.objects.create(number=7415, street='Melvin Street',
                               city='Los Angeles', state='CA',
                               zip_code=90001, country_iso_code='USA')
        address = Address.objects.first()
        Letting.objects.create(title='Travis guesthouse', address=address)

    def test_lettings_url_exists_at_proper_location(self):
        letting = Letting.objects.first()
        resp = self.client.get(reverse('letting', args=[letting.id]))
        self.assertEqual(resp.status_code, 200)

    def test_lettings_url_return_correct_content(self):
        letting = Letting.objects.first()
        resp = self.client.get(reverse('letting', args=[letting.id]))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b'Back', resp.content)
        self.assertIn(b'Home', resp.content)
        self.assertIn(b'Profiles', resp.content)

    def test_lettings_url_return_correct_title(self):
        letting = Letting.objects.first()
        resp = self.client.get(reverse('letting', args=[letting.id]))
        self.assertEqual(resp.status_code, 200)
        self.assertInHTML('Lettings', '<h1>Lettings</h1>')

    def test_letting_view_uses_correct_template(self):
        letting = Letting.objects.first()
        resp = self.client.get(reverse('letting', args=[letting.id]))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'lettings/letting.html')
