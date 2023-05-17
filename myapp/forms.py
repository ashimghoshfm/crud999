from django import forms
from .models import *

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
#for better look:
        widgets = {
            "eid":forms.NumberInput(attrs={'class':'form-control'}),
            "ename":forms.TextInput(attrs={'class':'form-control'}),
            "salary":forms.NumberInput(attrs={'class':'form-control'}),
        }