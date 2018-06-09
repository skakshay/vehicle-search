import json
from django.http import HttpResponse, JsonResponse
from .forms import SearchForm
from .models import Vehicle
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST


@require_GET
def index(request):
	form = SearchForm()
	return render(request, 'index.html', {'form':form})

@require_GET
def search_model(request):
	search_string = request.GET.get('search_string')
	model_list = [d['search_string'] for d in Vehicle.objects.filter(search_string__icontains=search_string).order_by('-search_count').values("search_string")]
	return JsonResponse({"model_list": model_list})

@require_POST
def select_model(request):
	search_string = request.POST['search_string']
	vehicle = Vehicle.objects.get(search_string=search_string)
	if vehicle:
		vehicle.search_count += 1
		vehicle.save()
		return JsonResponse({'Message': 'Select count updated'})
	else :
		return JsonResponse({'Message': 'Invalid model'})
	
