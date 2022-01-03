from django.shortcuts import render
import json
def index(request):
    if request.method=="POST":
        objects = request.POST['myobjects']
        print(objects) 
        objects= json.loads(objects)
        for item in objects:
            print(item['field'], item['value'])
    template = "base.html"
    return render(request,template)