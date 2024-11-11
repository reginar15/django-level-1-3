from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord

# Create your views here.
def index (request):
    Webpage_list = AccessRecord.objects.order_by('data')
    date_dict = {'access_record': Webpage_list}
    return render(request, 'first_app/index.html', context=date_dict)
