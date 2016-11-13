from django.http import HttpResponseRedirect
from django.shortcuts import render
import datetime
from django.http import JsonResponse
import json


from forms import TemperatureForm
from models import Temperature


def home(request):

    # querying all the data from the database
    temp_data = Temperature.objects.values().order_by('-created_time')
    # list object that loops through the queried data then dumps them in a  list
    json_object = [item for item in temp_data]
    data = open('data.json', "w+")
    # this stores the values in a dictionary
    items = {}
    # this is to allow the formatting of the data so as to display in the format you want
    for obj in temp_data:
        items[obj['temp_value']] = "{}:{}".format(obj['created_time'].hour, obj['created_time'].minute)
    # the str() call converts the items dict to a string, because apparently you can not write a dict object to a file
    data.write(str(items))
    data.close()

    return render(request, 'base/home.html', context={"json_object": temp_data})


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



# {% for object in json_object %}
# 	Time: {{ object.created_time }}
# 	temp: {{ object.temp_value }}
# {% endfor %}
