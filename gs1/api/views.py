from django.shortcuts import render
from .models import Student
from .serializars import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

# query_set to get single data (method= 1)
def student_detail(request,pk):
    stu=Student.objects.get(id=pk)
    serializer=StudentSerializers(stu)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

# query_set to get single data (method= 2) using the Jsonresponse
# def student_detail(request,pk):
#     stu=Student.objects.get(id=pk)
#     serializer=StudentSerializers(stu)
#     return JsonResponse(serializer.data)




#query_set to get all the data
def student_list(request):
    stu=Student.objects.all()   
    serializer=StudentSerializers(stu, many=True)  
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

