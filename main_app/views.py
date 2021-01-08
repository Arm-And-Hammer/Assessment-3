from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Widgit

# Create your views here.

def index(request):
    widgits = Widgit.objects.all()
    return render(request, 'index.html', {'widgits': widgits})

class WidgitCreate(CreateView):
    model = Widgit
    fields = "__all__"
    
def delete_widgit(request, widgit_id):
    Widgit.objects.get(id=widgit_id).delete()
    return redirect('/')