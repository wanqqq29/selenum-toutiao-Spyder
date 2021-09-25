from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import spyder.mainSpyder as ms
import json
# Create your views here.

def go(request):
    if request.method == 'GET':
        return render(request, template_name='submit2Spyder.html')
    elif request.method == 'POST':
        groupID = request.POST.get('groupID')
        jsonData=ms.spyder(groupID)
        return JsonResponse(jsonData)
