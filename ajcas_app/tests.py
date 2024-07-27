# ajcas_app/tests.py
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Categorie, Member, Article, Comment, Like, Configiration
from django.test import TestCase, Client
from django.urls import reverse

class CategorieTest(TestCase):
    def setUp(self):
        self.categorie = Categorie.objects.create(name="Health")

    def test_categorie_creation(self):
        self.assertEqual(self.categorie.name, "Health")
        self.assertEqual(str(self.categorie), "Health")

class MemberTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.member = Member.objects.create(
            user=self.user,
            full_name="John Doe",
            birth_info="01/01/1990",
            gender="M",
            address="123 Street",
            profession="Doctor",
            phone1="1234567890",
            member_signature="John Doe",
            president_signature="President"
        )

    def test_member_creation(self):
        self.assertEqual(self.member.full_name, "John Doe")
        self.assertEqual(str(self.member), "John Doe")

class ArticleTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.member = Member.objects.create(
            user=self.user,
            full_name="John Doe",
            birth_info="01/01/1990",
            gender="M",
            address="123 Street",
            profession="Doctor",
            phone1="1234567890",
            member_signature="John Doe",
            president_signature="President",
            image=SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg')
        )
        self.categorie = Categorie.objects.create(name="Health")
        self.article = Article.objects.create(
            title="Health Tips",
            categorie=self.categorie,
            content="Some health tips.",
            author=self.member
        )

    def test_article_creation(self):
        self.assertEqual(self.article.title, "Health Tips")
        self.assertEqual(self.article.content, "Some health tips.")
        self.assertEqual(str(self.article.author), "John Doe")
    def test_article_detail_view(self):
        response = self.client.get(reverse('ajcas_app:article_detail', args=[self.article.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Article")

    def test_article_list_view(self):
        response = self.client.get(reverse('ajcas_app:article_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Article")
class CommentTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.member = Member.objects.create(
            user=self.user,
            full_name="John Doe",
            birth_info="01/01/1990",
            gender="M",
            address="123 Street",
            profession="Doctor",
            phone1="1234567890",
            member_signature="John Doe",
            president_signature="President"
        )
        self.categorie = Categorie.objects.create(name="Health")
        self.article = Article.objects.create(
            title="Health Tips",
            categorie=self.categorie,
            content="Some health tips.",
            author=self.member
        )
        self.comment = Comment.objects.create(
            article=self.article,
            author=self.member,
            content="Great tips!"
        )

    def test_comment_creation(self):
        self.assertEqual(self.comment.content, "Great tips!")
        self.assertEqual(str(self.comment.author), "John Doe")

class LikeTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.member = Member.objects.create(
            user=self.user,
            full_name="John Doe",
            birth_info="01/01/1990",
            gender="M",
            address="123 Street",
            profession="Doctor",
            phone1="1234567890",
            member_signature="John Doe",
            president_signature="President"
        )
        self.categorie = Categorie.objects.create(name="Health")
        self.article = Article.objects.create(
            title="Health Tips",
            categorie=self.categorie,
            content="Some health tips.",
            author=self.member
        )
        self.like = Like.objects.create(
            article=self.article,
            user=self.member
        )

    def test_like_creation(self):
        self.assertEqual(self.like.article.title, "Health Tips")
        self.assertEqual(str(self.like.user), "John Doe")

class ConfigirationTest(TestCase):
    def setUp(self):
        self.config = Configiration.objects.create(
            site_name="ajcas",
            site_adresse="ajcascongoasbl@gmail.com",
            site_phone="+243 828 757 690",
            site_location="Av, mateko n°26, kinshasa/lemba",
            site_intro="ENSEMBLE LUTTONS POUR L’AMÉLIORATION DE NOTRE ÉTAT SANITAIRE !!!!",
            site_intro_description="PROGRAMME ANNUEL DE L’ASSOCIATION DES JEUNES CONGOLAIS POUR L’ACCES A LA SANTE",
            assisted_people=100,
            projects=10,
            years_experiences=5,
            achievement=20
        )

    def test_configiration_creation(self):
        self.assertEqual(self.config.site_name, "ajcas")
        self.assertEqual(str(self.config), "ajcas")




# ajcas_app/tests.py

class ViewTests(TestCase):
    def setUp(self):
        # Set up test data
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.member = Member.objects.create(
            user=self.user,
            full_name="John Doe",
            birth_info="01/01/1990",
            gender="M",
            address="123 Street",
            profession="Doctor",
            phone1="1234567890",
            member_signature="John Doe",
            president_signature="President"
        )
        self.categorie = Categorie.objects.create(name="Health")
        self.article = Article.objects.create(
            title="Health Tips",
            categorie=self.categorie,
            content="Some health tips.",
            author=self.member
        )
        self.config = Configiration.objects.create(
            site_name="ajcas",
            site_adresse="ajcascongoasbl@gmail.com",
            site_phone="+243 828 757 690",
            site_location="Av, mateko n°26, kinshasa/lemba",
            site_intro="ENSEMBLE LUTTONS POUR L’AMÉLIORATION DE NOTRE ÉTAT SANITAIRE !!!!",
            site_intro_description="PROGRAMME ANNUEL DE L’ASSOCIATION DES JEUNES CONGOLAIS POUR L’ACCES A LA SANTE",
            assisted_people=100,
            projects=10,
            years_experiences=5,
            achievement=20
        )

    def test_index_view(self):
        response = self.client.get(reverse('ajcas_app:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'page/index.html')
        self.assertIn('conf', response.context)
    
    def test_login_view(self):
        response = self.client.post(reverse('ajcas_app:login'), {
            'username': 'testuser',
            'password': '12345'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful login
        self.assertRedirects(response, reverse('ajcas_app:home'))
    
    def test_logout_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('ajcas_app:logout'))
        self.assertEqual(response.status_code, 302)  # Redirect after logout
        self.assertRedirects(response, reverse('ajcas_app:login'))
    
    def test_profile_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('ajcas_app:profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'page/profile.html')
    
    def test_article_list_view(self):
        response = self.client.get(reverse('ajcas_app:article_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/article_list.html')
    
    def test_article_detail_view(self):
        response = self.client.get(reverse('ajcas_app:article_detail', args=[self.article.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/article_detail.html')
    
    def test_like_article_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('ajcas_app:like_article', args=[self.article.pk]))
        self.assertEqual(response.status_code, 302)  # Redirect after liking/unliking
        self.assertRedirects(response, reverse('ajcas_app:article_detail', args=[self.article.pk]))

    def test_membership_form_view(self):
        response = self.client.get(reverse('ajcas_app:membership_form'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'formulaire/membership_form.html')

        response = self.client.post(reverse('ajcas_app:membership_form'), {
            'username': 'newuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
            'full_name': 'New User'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful registration
        self.assertRedirects(response, reverse('ajcas_app:home'))


