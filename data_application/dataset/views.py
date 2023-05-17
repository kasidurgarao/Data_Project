from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

from .forms import UploadForm
# from .models import Dataset, ComputedData, PlottedData
import pandas as pd
import plotly.express as px
from django.views.generic import DetailView


# Create your views here.
def base(request):
    return render(request, 'dataset/base.html')


def home(request):
    return render(request, 'dataset/home.html')


# def data(request):
#     return render(request,'dataset/data.html')

def plot(request):
    return render(request, 'dataset/plot.html')


# def data(request):
#     return render(request, 'dataset/data.html')


def data(request):
    if request.method == 'POST':
        upload_files = UploadForm(request.POST, request.FILES)
        data_files=request.FILES['data_file']
        print(upload_files)
        if upload_files.is_valid():
            upload_files.save()
            return HttpResponse("successfully uploaded")
            #return redirect('list_datasets')
        print("form is not valid")
    else:
        upload_files = UploadForm()
    return render(request, 'dataset/data.html', {'form': upload_files})


def list_datasets(request):
    datasets = Dataset.objects.all()
    context = {'datasets': datasets}
    return render(request, 'dataset/data.html', context)


def compute(request, id):
    dataset = Dataset.objects.get(pk=id)
    if request.method == 'POST':
        column_name = request.POST['column_name']
        operation = request.POST['operation']
        data = pd.read_csv(dataset.data_file.path)
        result = None
        if operation == 'min':
            result = data[column_name].min()
        elif operation == 'max':
            result = data[column_name].max()
        elif operation == 'sum':
            result = data[column_name].sum()
        computed_data = ComputedData(dataset=dataset, column_name=column_name, operation=operation)
        computed_data.save()
        context = {'result': result}
        return render(request, 'dataset/compute_result.html', context)
    return render(request, 'dataset/compute.html', {'dataset': dataset})


def output(request, id):
    dataset = Dataset.objects.get(pk=id)
    if request.method == 'GET':
        column_x = request.GET['column_x']
        column_y = request.GET['column_y']
        data = pd.read_csv(dataset.data_file.path)
        fig = px.scatter(data, x=column_x, y=column_y)
        fig_html = fig.to_html(full_html=False)
        plotted_data = PlottedData(dataset=dataset, column_x=column_x, column_y=column_y)
        plotted_data.save()
        context = {'plot': fig_html}
        return render(request, 'dataset/plot_result.html', context)
    return render(request, 'dataset/plot.html', {'dataset': dataset})


        # name = request.POST.get('dataset-name')
        # data_file = request.FILES['data_file']
        # dataset = Dataset(name=name, data_file=data_file)
        # dataset.save()
        # return redirect('list_datasets')