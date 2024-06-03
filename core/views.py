from django.shortcuts import render
from .models import Category, Forum
# Create your views here.

def home(request):
    categores = Category.objects.all()
    
   
    context = {
        'categories': categores,
    }
    return render(request, 'index.html', context)



def forum_cat(request,pk):
    category_id = Category.objects.get(pk=pk)
    forum_cat = Forum.objects.filter(Category_name = category_id).order_by('-published_date')
    count_content = forum_cat.count()
    context = {
        'forum_cat': forum_cat,
        'count_content':count_content,
        'category_id':category_id,
    }
    return render(request, 'forum_category.html', context)

def forum_detail(request, pk):
    forum_detail = Forum.objects.get(pk=pk)
    context = {
        'forum_detail': forum_detail
    }
    return render(request, 'forum-detail.html', context)