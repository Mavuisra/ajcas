from django.contrib import admin
from .models import Article, Comment, Like, Member,Configiration, Categorie
from django.contrib.admin import AdminSite


class MyAdminSite(AdminSite):
    site_header = 'Ajcas admin'
    site_title = 'Espace admin'
    index_title = 'Bienvenu dans site admin'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            # Vous pouvez ajouter des URL personnalisées ici
        ]
        return custom_urls + urls

admin_site = MyAdminSite(name='Ajcas')




@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title',  'created_at', 'views', 'categorie')
    search_fields = ('title', 'content', 'author__fullname')
    list_filter = ('created_at',)
    readonly_fields = ('created_at', 'views')
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'image', 'author','categorie')
        }),
        ('Statistics', {
            'fields': ('created_at', 'views')
        }),
    )

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'author', 'created_at')
    search_fields = ('content', 'author__username', 'article__title')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)
    fieldsets = (
        (None, {
            'fields': ('article', 'author', 'content')
        }),
        ('Metadata', {
            'fields': ('created_at',)
        }),
    )

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('article', 'user')
    search_fields = ('user__username', 'article__title')
    list_filter = ('article', 'user')
    
@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('name',)
  

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'profession', 'gender', 'date_signed')
    
    fieldsets = (
        (None, {
            'fields': ('user','full_name', 'image', 'birth_info', 'gender', 'address', 'profession',  'phone1', 'phone2' )
        }),
        ('Adhesion Info', {
            'fields': ('member_declaration', 'monthly_contribution', 'payment_method', 'donation_method', 'donation_amount', 'member_signature', 'president_signature')
        }),
    )
@admin.register(Configiration)
class ConfigirationAdmin(admin.ModelAdmin):
    list_display = ('site_name','site_adresse','site_phone','site_location','site_intro','site_intro_description','assisted_people','projects','years_experiences','achievement')