from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    run="no"
    to=0
    length=0
    from_unit=""
    to_unit=""

    units = {
        "meters": 1,
        "kilometers": 1000,
        "millimeters": 0.001,
        "centimeters": 0.01,
        "miles": 1609.344,
        "feet": 0.3048,
        "yards": 0.9144,
        "inches": 0.0254
    }
    if request.method == "POST":
        run="yes"
        length = float(request.POST.get("length"))
        from_unit = request.POST.get("from_unit")
        to_unit = request.POST.get("to_unit")
        val = units[from_unit]
        val2 = units[to_unit]
        to_meters = length * val
        to = to_meters / val2
    return render(request,"UnitConverter/index.html", {
        "to" : to,
        "length" : length,
        "from_unit" : from_unit,
        "to_unit" : to_unit,
        "run" : run

    })



def weight(request):
    run="no"
    w = 0
    from_unit=""
    to_unit=""
    to=0
    units={
        "kilogram" :1,
        "gram" :0.001,
        "milligram" :0.000001,
        "ounce" :0.0283495,
        "pound": 0.453592
    }
    if request.method == "POST":
        run="yes"
        w = float(request.POST.get("w"))
        from_unit =  request.POST.get("from_unit")
        to_unit = request.POST.get("to_unit")
        val= units[from_unit]
        val1 = units[to_unit]
        to_kilograms = w * val
        to = to_kilograms / val1
    return render(request,"UnitConverter/weight.html", {
        "w" : w,
        "from_unit" : from_unit,
        "to_unit" : to_unit,
        "to" : to,
        "run" : run
    })


def temp(request):
    run="no"
    from_unit=""
    to_unit=""
    to=0
    temperature=0
    conversion = {
        ("Celsius", "Fahrenheit") : lambda c:c*1.8+32,
        ("Fahrenheit", "Celsius") : lambda f:(f - 32) * 0.125,
        ("Celsius", "Kelvin") : lambda c:c+273.15,
        ("Kelvin", "Celsius") : lambda k:k-273.15,
        ("Fahrenheit", "Kelvin") : lambda f:((f-32)*5/9)+273.15,
        ("Kelvin", "Fahrenheit") : lambda k: (k -273.15) *1.8 +32
    }
    if request.method == "POST":
        run="yes"
        temperature = float(request.POST.get("temperature"))
        from_unit= request.POST.get("from_unit")
        to_unit= request.POST.get("to_unit")
        to= conversion[(from_unit, to_unit)](temperature)
    return render(request,"UnitConverter/temperature.html",{
        "temperature" : temperature,
        "from_unit" : from_unit,
        "to_unit" : to_unit,
        "to" : to,
        "run" : run

    } )


