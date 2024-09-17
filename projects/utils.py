from .models import Project, Tag
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def paginationProjects(request, projects,results):
    page = request.GET.get('page',1)
    paginator = Paginator(projects, results)
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)
    leftIndex = (int(page)-1) 
    page = int(page) if page else 1  
    leftIndex = max(1, page - 1)  
    rightIndex = min(page + 1, paginator.num_pages) 
    custom_range = range(leftIndex, rightIndex + 1)  
    return custom_range, projects


def searchProjects(request):
    search_query= ''
    if request.GET.get('search_query'):
        search_query=request.GET.get('search_query')

    tags=Tag.objects.filter(name__icontains=search_query)
    
    projects=Project.objects.distinct().filter(
        Q(title__icontains=search_query)|
        Q(description__icontains=search_query)|
        Q(owner__name__icontains=search_query)|
        Q(tags__in=tags)
    )
    return projects, search_query

