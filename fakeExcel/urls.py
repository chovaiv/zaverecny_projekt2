from django.contrib import admin
from django.urls import include, path

from graf import views
from graf.views import TestChartView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('piechart/', TestChartView.as_view(), name='piechart'),
    path('', views.index, name='index'),
    path('pridat_objekt/', views.pridat_objekt, name='pridat_objekt'),
    path('odstranit/<int:id>/', views.odstranit, name='odstranit'),
    path('upravit_objekt/<int:id>', views.upravit_objekt, name='upravit_objekt'),

]
