from django.urls import path
from django.conf.urls import url
from devices import views

urlpatterns = [
    #path('data/<float:ph>/<float:temperature>/<float:dissolved_oxygen>/', views.configuration, name="data_configuration"),
    url(r"^data/(?P<ph>\d+\.\d+)/(?P<temperature>\d+\.\d+)/(?P<dissolved_oxygen>\d+\.\d+)/$", views.configuration, name="data_configuration"),
    path('plot/', views.plot, name="data_plot"),
    path('graph/', views.graph, name="data_graph"),
    path('eg/', views.eg, name="eg"),
]
