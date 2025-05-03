from django.shortcuts import render
from cars.models import Car
from django.core.paginator import Paginator

def cars_viws(request):
    cars = Car.objects.all().order_by('model')
    search = request.GET.get('search')

    if search:
        cars = cars.filter(model__icontains=search)

    # Paginação - 50 carros por página
    paginator = Paginator(cars, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'cars': page_obj,  
        'total_results': paginator.count,
        'start_index': page_obj.start_index(),
        'end_index': page_obj.end_index(),
        'search': search  
    }

    return render(request, "cars.html", context)
