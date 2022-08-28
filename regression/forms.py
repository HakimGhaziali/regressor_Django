from django import forms


class VariableForm(forms.Form):
    
    
    X = forms.CharField(widget=forms.Textarea)
    Y = forms.CharField(widget=forms.Textarea)
    Z = forms.CharField()
