from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import *
from .forms import CommentForm,MemberForm,CreationUserForm
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    
    confs = Configiration.objects.all()
    for conf in confs:

        context = {
            "conf":conf
        }
    return render(request, 'page/index.html', context)
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('ajcas_app:home')
        else:
            messages.info(request, 'information invalides')
    context = {


    }
    return render(request, 'page/login.html', context)
def logoutpage(request):
    logout(request)
    return redirect('ajcas_app:login')

def profile(request):
    user = request.user.member
    form = MemberForm(instance=user)
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
    context = {
        'form': form,
    }

    return render(request, 'page/profile.html', context)
def article_list(request):
    articles = Article.objects.all().order_by('-created_at')
    paginaton = Paginator(articles, 6)
    page = request.GET.get('page')
    try:
        articles = paginaton.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        articles = paginaton.page(1)
    except EmptyPage:
        # If page is out of range, deliver the last page
        articles = paginaton.page(paginaton.num_pages)
    return render(request, 'blog/article_list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    cat_articles = Article.objects.filter(categorie = article.categorie).exclude(pk = article.id)
    if 'viewed_articles' not in request.session:
        request.session['viewed_articles'] = []

    if pk not in request.session['viewed_articles']:
        article.views += 1
        article.save()
        request.session['viewed_articles'].append(pk)
        request.session.modified = True
    article.save()
    comments = article.comments.all()
  
  
    new_comment = None
   
    if request.method == 'POST' :
        comment_form = CommentForm(data=request.POST)
        user=Member.objects.filter(user = request.user)[0]
        
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.author = user
            new_comment.save()
            return redirect('ajcas_app:article_detail', pk=article.pk)
    else:
        comment_form = CommentForm()
   
    return render(request, 'blog/article_detail.html', {
        'article': article,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'cat_articles':cat_articles,
        'all_comments':Comment.objects.filter(article__id = pk).count()
        

    })

def like_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    user=Member.objects.filter(user = request.user)[0]
    like, created = Like.objects.get_or_create(article=article, user = user)
    
    if not created:
        like.delete()
   
    return redirect('ajcas_app:article_detail', pk=pk)

def membership_form(request):
    form = CreationUserForm()
    if request.method == 'POST':
        form = CreationUserForm(request.POST)
        try: 
            if form.is_valid:
                user = form.save()
                username = form.cleaned_data.get('username')
                user.is_staff = True
                user.save()
                group = Group.objects.get(name='user')
                user.groups.add(group)
                Member.objects.create(
                    user=user,
                    full_name = Member.full_name
                

                )

                messages.success(
                    request, f"l'utilisateur {username} a ete crée avec succès")
                return redirect('ajcas_app:login')
            else:
                form = CreationUserForm()
        except:
            messages.error(
                    request, f"incorrect")

    return render(request, 'formulaire/membership_form.html', {'form': form})



def form_success(request):
    return render(request, 'formulaire/form_success.html')