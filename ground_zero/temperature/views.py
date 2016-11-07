from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
import datetime
import json
from django.forms.models import model_to_dict


from forms import TemperatureForm
from models import Temperature


def home(request):
    # temp_value = Temperature.objects.all()

    model_to_dict(Temperature)

    return render(request, 'base/temp_input.html')


def get_temperature(request):
    """ This method gets temperature data and saves to database """
    form = TemperatureForm(request.POST)
    if form.is_valid():
        temp_value = form.cleaned_data['temp_value']
        temp = Temperature() # initializes the model table
        temp.temp_value = temp_value # get first value
        temp.created_time = datetime.datetime.now() # add second value
        temp.save() # save data
        return HttpResponseRedirect('/home/')
    else:
        return render(request, 'base/temp_input.html')
