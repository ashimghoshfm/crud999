from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def home(request):
    all_employees = Employee.objects.all()
    return render(request, 'index.html', {"employees":all_employees})

#delete function:
def rem(request, id):
    dd = Employee.objects.get(id=id)
    dd.delete()
    return redirect(home)

#addnew function:
def addnew(request):
    varForm = EmployeeForm()
    if request.method == "POST":
        reqForm = EmployeeForm(request.POST)
        if reqForm.is_valid():
            reqForm.save()
            return redirect(home)
    return render(request, 'addnew.html', {"eform":varForm})


#edit function:
def edit(request, id):
    matchData = Employee.objects.get(id=id)
    varForm = EmployeeForm(instance=matchData)
    if request.method == "POST":
        reqForm = EmployeeForm(request.POST, instance=matchData)
        if reqForm.is_valid():
            reqForm.save()
            return redirect(home)
    return render(request, 'edit.html', {"eform":varForm})
