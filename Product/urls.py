from django.urls import path

from . import views


app_name='Product'

urlpatterns = [

    path('',views.product_list,name='home'),

    path('create/',views.create_product,name='create'),
path("view/<int:product_id>/", views.product_view, name="view"),
    path("edit/<int:product_id>/", views.edit_product, name="edit"),

    path("delete/<int:id>/", views.product_delete, name="delete")


]

