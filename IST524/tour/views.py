from django.shortcuts import render
from django.shortcuts import get_object_or_404
from . import models
from .models import Tour

def tour_list_view(request):
    if request.method == 'GET':
        tour_list = models.Tour.objects.all().order_by('-id')
    return render(request, template_name='tour_list.html', context={'tour_list': tour_list})

def tour_detail_view(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)

    return render(request, 'tour_detail.html', {
        'tour': tour
    })