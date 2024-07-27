from django.db import models
from django.contrib.auth.models import User, AbstractUser
class Categorie(models.Model):
    name = models.CharField(max_length=233)
    def __str__(self):
        return self.name
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='member', null=True)
    GENDER_CHOICES = [
        ('F', 'Féminin'),
        ('M', 'Masculin'),
        ('O', 'Autres'),
    ]

    full_name = models.CharField(max_length=255)
    birth_info = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', null=True,)
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20, blank=True, null=True)
    member_declaration = models.BooleanField(default=False)
    monthly_contribution = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=50, blank=True, null=True)
    donation_method = models.CharField(max_length=50, blank=True, null=True)
    donation_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    date_signed = models.DateTimeField(auto_now=True)
    member_signature = models.CharField(max_length=255)
    president_signature = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name
class Article(models.Model):
    title = models.CharField(max_length=200)
    categorie = models.ForeignKey(Categorie, related_name="categorie", on_delete=models.CASCADE, null=True)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', null=True,)
    author = models.ForeignKey(Member, on_delete=models.CASCADE, null=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)

class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(Member, on_delete=models.CASCADE, null=True,)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    article = models.ForeignKey(Article, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(Member, models.CASCADE, null=True, related_name="users")


 
       
class Configiration(models.Model):
    site_name = models.CharField(max_length=44, default="ajcas")
    site_adresse = models.CharField(max_length=56, default="ajcascongoasbl@gmail.com")
    site_phone = models.CharField(max_length=56, default=" +243 828 757 690")
    site_location = models.CharField(max_length=233, default=" Av, mateko n°26, kinshasa/lemba")
    site_intro = models.TextField(default="ENSEMBLE LUTTONS POUR L’AMÉLIORATION DE NOTRE ÉTAT SANITAIRE !!!!")
    site_intro_description = models.TextField(default="PROGRAMME ANNUEL DE L’ASSOCIATION DES JEUNES CONGOLAIS POUR L’ACCES A LA SANTE")
    assisted_people = models.IntegerField()
    projects = models.IntegerField()
    years_experiences = models.IntegerField()
    achievement = models.IntegerField()
    def __str__(self):
        return self.site_name