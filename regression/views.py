from django.shortcuts import render
from .train import predictor
# Create your views here.
from .forms import VariableForm
import numpy as np
from .models import Regres , parameters


def predict(request):

    if request.method == 'GET':

        form = VariableForm()

        return render(request ,  'home.html' , {'form': form})

    elif request.method == 'POST':

        form = VariableForm(request.POST)

        if form.is_valid():

            X_list=form.cleaned_data['X'].split(',')
            X_list = [int(i) for i in X_list]
            X= np.array((X_list))
            X= np.reshape(X , (-1,1))

            Y_list=form.cleaned_data['Y'].split(',')
            Y_list = [int(i) for i in Y_list]
            Y= np.array((Y_list))
            Y= np.reshape(Y , (-1,1))
            

            Z_list=form.cleaned_data['Z'].split(',')
            Z_list = [int(i) for i in Z_list]
            Z= np.array((Z_list))
            Z= np.reshape(Z , (-1,1))
            
            
            pred , coe , inter = predictor(X,Y,Z)

            print( pred )
            print(coe)
            context = {'pred':pred[0,0] , 'coe':coe[0,0] , 'inter': inter}


            print(context)
        
            return render(request ,  'result.html' , context=context )

        

    


        






    


