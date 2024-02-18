from django.shortcuts import render
from .models import MyModel

def my_view(request):
    obj = MyModel(name='Sample Name', description='Sample Description')
    obj.save()

    queryset = MyModel.objects.all()

    return render(request, 'my_template.html', {'objects': queryset})
