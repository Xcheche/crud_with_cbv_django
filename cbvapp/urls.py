from django.urls import path
from .views import StudentListView
from . import views

urlpatterns = [
    path("", StudentListView.as_view(), name="student_list"),
    path("detail/<int:pk>/", views.StudentDetailView.as_view(), name="student_detail"),
    path("create/", views.StudentCreateView.as_view(), name="student_create"),
    path("update/<int:pk>/", views.StudentUpdateView.as_view(), name="student_update"),
    path("delete/<int:pk>/", views.StudentDeleteView.as_view(), name="student_delete"),
]
