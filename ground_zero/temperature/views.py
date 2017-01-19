from django.http import HttpResponseRedirect
from django.shortcuts import render
import datetime
from django.http import JsonResponse
import json


from forms import TemperatureForm
from models import Temperature


def home(request):

    # querying all the data from the database
    temp_data = Temperature.objects.all().order_by('-created_time')
    # list object that loops through the queried data then dumps them in a  list
    json_object = [item for item in temp_data]
    # this stores the values in a dictionary
    items = []
    # this is to allow the formatting of the data so as to display in the proper format
    for obj in temp_data:
        final_data = { }

        final_data["date"] = str(obj.created_time)
        final_data["temp"] = obj.temp_value

        # making a dictionary of dictionaries, by adding this dictionary to items
        items.append(final_data)

    print items

    return render(request, 'base/home.html', context={"json_object" : json.dumps(items)})


def get_temperature(request):

    """ This method gets temperature data and saves to database """
    form = TemperatureForm(request.POST)
    if form.is_valid():
        temp_value = form.cleaned_data['temp_value']
        temp = Temperature() # initializes the model table
        # temp.temp_value = temp_value # get first value
        temp.created_time = datetime.date # add second value
        temp = form.save(commit=False)
        temp.save() # save data
        return HttpResponseRedirect('/get_temp/')
    else:
        return render(request, 'base/temp_input.html')



# {% for object in json_object %}
# 	Time: {{ object.created_time }}
# 	temp: {{ object.temp_value }}
# {% endfor %}
