from django.shortcuts import render, redirect
from .forms import DashboardForm
from .models import Dashboard

# Create your views here.

#retrieve and display all the dashboards rows
def dashboard_list(request):
  context = {'dashoard_list':Dashboard.objects.all()}
  return render(request,"landing_page_register/dashboard_list.html", context)
#Insert and update ops
def dashboard_form(request,id=0):
  if request.method == "GET":
    if id==0:
      form = DashboardForm()
    else:
      dasboard = Dashboard.objects.get(pk=id)
      form = DashboardForm(instance=dasboard)
    return render(request,"landing_page_register/dashboard_form.html", {'form': form})
  else:
    if id==0:
      form = DashboardForm(request.POST)
    else:
      dasboard = Dashboard.objects.get(pk=id)
      form = DashboardForm(request.POST, instance=dasboard)
    
    if form.is_valid():
      form.save()
    return redirect('/')

def dashboard_delete(request, id):
  dasboard = Dashboard.objects.get(pk=id)
  dasboard.delete()
  return redirect('/')  

