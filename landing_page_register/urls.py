from django.urls import path, include
from . import views

urlpatterns = [
    path('insert/', views.dashboard_form,name='dashboard_insert'), # get and Post requests for insert ops
    path('<int:id>/', views.dashboard_form,name="dashboard_update"), # get and Post requests for Update ops.
    path('delete/<int:id>/', views.dashboard_delete,name="dashboard_delete"),
    path('',views.dashboard_list,name='dashboard_list') # GET request to retrieve and display records.
]