from django.shortcuts import render
from .train import predictor
# Create your views here.
from .forms import VariableForm
import numpy as np

def predict(request):

    if request.method == 'GET':

        form = VariableForm()

        return render(request ,  'home.html' , {'form': form})

    elif request.method == 'POST':
        form = VariableForm(request.POST)

        if form.is_valid():
            list = [int(x) for x in form.cleaned_data.values()]
            arr = np.array(list , ndmin=2)   
            pred = predictor(arr)
            {'predict': pred }

            return render(request ,  'result.html' , {'pred': pred})

        

    


        






    


