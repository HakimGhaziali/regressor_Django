from django import forms


class VariableForm(forms.Form):
    
    X1 = forms.CharField()
    X2 = forms.CharField()
    X3 = forms.CharField()
