from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator


# Create your views here.


def index(request):

    a_lot_of_military = Military.objects.all().order_by('id')

    per_page = int(request.GET.get('per_page', 10))
    paginator = Paginator(a_lot_of_military, per_page)
    page = request.GET.get('page', 1)

    military_page = paginator.get_page(page)
    per_page_options = [10, 20, 50]
    return render(request, "index.html", {'military': military_page, 'per_page': per_page,
                                          'per_page_options': per_page_options})


