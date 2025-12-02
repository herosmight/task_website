from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("new_task/", views.create_task, name="new_task"),
    path("task/<int:id>/", views.task_detail, name="detail"),
    path("task/<int:id>/edit/", views.edit_task, name="edit_task"),
    path("task/<int:id>/complete/", views.complete_task, name="complete"),
    path("task/<int:id>/delete/", views.delete_task, name="delete")
]