from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('/', views.index, name="index"),
    re_path(r'filter/(?P<currency>\D+)', views.filter, name="filter"),
    re_path(r'order/(?P<order_by>\D+)', views.order, name="order"),
    path('<int:id>/delete', views.delete, name="delete"),
    path('<int:id>/update', views.update, name="update"),
]
