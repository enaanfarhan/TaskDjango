from django.shortcuts import render
from .models import StudentDetail

# Create your views here.

def std_list(request):
    std_list = StudentDetail.objects.all()
    context = {'std_list': std_list}
    return render(request, 'Student/Studentlist.html', context)

def std_info(request, roll):
    std_info=StudentDetail.objects.get(roll=roll)
    context = {'std_info': std_info}
    return render(request, 'Student/StudentInfo.html', context)