from django.shortcuts import render
from .models import StudentDetail
from .forms import *

# Create your views here.

def std_list(request):
    std_list = StudentDetail.objects.all()
    context = {'std_list': std_list}
    return render(request, 'Student/Studentlist.html', context)

def std_info(request, roll):
    std_info = StudentDetail.objects.get(roll=roll)
    context = {'std_info': std_info}
    return render(request, 'Student/StudentInfo.html', context)

def std_search(request):
    form = StudentInfoSearch(request.GET or None)
    context = {'form':form}

    if form.is_valid():
        std_class = form.cleaned_data["std_class"]
        roll = form.cleaned_data["roll"]

        if std_class and roll:
            try:
                std = StudentDetail.objects.get(roll=roll)
                context = {'std': std, 'form':form}
            except:
                context = {'error': "Sorry! Student not found.", 'form':form}

    return render(request, 'Student/StudentSearch.html', context)

def addStudent(request):
    form = StudentCreateForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('create-std')

    context = { 'form':form }
    return render(request, 'Student/AddStudent.html', context)