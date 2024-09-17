from .models import Skill,Profile
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def paginationProfiles(request, profiles,results):
    page = request.GET.get('page',1)
    paginator = Paginator(profiles, results)
    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        profiles = paginator.page(1)
    except EmptyPage:
        profiles = paginator.page(paginator.num_pages)
    leftIndex = (int(page)-1) 
    page = int(page) if page else 1  
    leftIndex = max(1, page - 1)  
    rightIndex = min(page + 1, paginator.num_pages) 
    custom_range = range(leftIndex, rightIndex + 1)  
    return custom_range, profiles

def searchProfiles(request):
    search_query= ''
    if request.GET.get('search_query'):
        search_query=request.GET.get('search_query')

    skills=Skill.objects.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))
    profiles=Profile.objects.distinct().filter(Q(name__icontains=search_query) | Q(short_intro__icontains=search_query)
                                    | Q(skill__in=skills))

    return profiles,search_query
