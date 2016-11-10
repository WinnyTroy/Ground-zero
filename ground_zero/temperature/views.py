from django.core.serializers import serialize
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
import datetime
from django.http import JsonResponse


from forms import TemperatureForm
from models import Temperature


def home(request):

    # querying all the data from the database
    temp_data = Temperature.objects.values().order_by('-created_time')
    # list object that loops through the queried data then dumps them in a  list
    json_object= [item for item in temp_data]

    return render(request, 'base/home.html', context={"json_object":json_object})


def get_temperature(request):

    """ This method gets temperature data and saves to database """
    form = TemperatureForm(request.POST)
    if form.is_valid():
        temp_value = form.cleaned_data['temp_value']
        temp = Temperature() # initializes the model table
        # temp.temp_value = temp_value # get first value
        temp.created_time = datetime.datetime.now() # add second value
        temp = form.save(commit=False)
        temp.save() # save data
        return HttpResponseRedirect('/get_temp/')
    else:
        return render(request, 'base/temp_input.html')


