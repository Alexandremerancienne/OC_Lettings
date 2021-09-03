from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ...models import Profile


class ProfilesMainPageViewTest(TestCase):

    def test_profiles_url_exists_at_proper_location(self):
        resp = self.client.get(reverse('profiles_index'))
        self.assertEqual(resp.status_code, 200)

    def test_profiles_url_return_correct_content(self):
        resp = self.client.get(reverse('profiles_index'))
        self.assertIn(b'Profiles', resp.content)
        self.assertIn(b'Home', resp.content)
        self.assertIn(b'Lettings', resp.content)

    def test_lettings_url_return_correct_title(self):
        self.client.get(reverse('profiles_index'))
        self.assertInHTML('Profiles', '<h1>Profiles</h1>')

    def test_views_uses_correct_template(self):
        resp = self.client.get(reverse('profiles_index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'profiles/index.html')


class ProfilesDetailedPageViewTest(TestCase):

    def setUp(self):
        User.objects.create(username='In DaWild', first_name='Howie',
                            last_name='Starts', email='howie.starts@bot.com')
        user = User.objects.first()
        Profile.objects.create(user=user, favorite_city='Cape Town')

    def test_profiles_url_exists_at_proper_location(self):
        user = User.objects.first()
        resp = self.client.get(reverse('profile', args=[user.username]))
        self.assertEqual(resp.status_code, 200)

    def test_profiles_url_return_correct_content(self):
        user = User.objects.first()
        resp = self.client.get(reverse('profile', args=[user.username]))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b'Back', resp.content)
        self.assertIn(b'Home', resp.content)
        self.assertIn(b'Lettings', resp.content)

    def test_profiles_url_return_correct_title(self):
        user = User.objects.first()
        resp = self.client.get(reverse('profile', args=[user.username]))
        self.assertEqual(resp.status_code, 200)
        self.assertInHTML(user.username, '<h1>' + user.username + '</h1>')

    def test_profile_view_uses_correct_template(self):
        user = User.objects.first()
        resp = self.client.get(reverse('profile', args=[user.username]))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'profiles/profile.html')
