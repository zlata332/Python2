from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Tour


def tour_list_view(request):
    search_query = request.GET.get('search', '').strip()

    tour_list = Tour.objects.all().order_by('-id')

    if search_query:
        tour_list = tour_list.filter(
            Q(title__icontains=search_query) |
            Q(category__name__icontains=search_query) |
            Q(leader__icontains=search_query)
        )

    return render(request, 'tour_list.html', {
        'tour_list': tour_list,
        'search_query': search_query
    })


def tour_detail_view(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)

    return render(request, 'tour_detail.html', {
        'tour': tour
    })