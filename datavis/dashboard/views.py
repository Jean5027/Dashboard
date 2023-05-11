from django.shortcuts import render
from .models import PeDeGoiaba

dt = [

]

def index(request):
    dt = []
    values = PeDeGoiaba.objects.all()
    for v in values:
        dt.append(v.value)
    return render(request, 'index.html', {'dt2': dt})

