from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from cbvapp.forms import StudentForm
from cbvapp.models import Student

# Create your views here.


class StudentListView(ListView): # ListView
    model = Student
    template_name = "cbvapp/student_list.html"
    context_object_name = "students"


class StudentDetailView(DetailView):# DetailView
    model = Student
    template_name = "cbvapp/student_detail.html"
    context_object_name = "student"
    
    
class StudentCreateView(CreateView):# CreateView
    form = StudentForm
    model = Student
    template_name = "cbvapp/create_students.html"
    fields = "__all__"
    success_url = reverse_lazy("student_list")

    def form_valid(self, form):
        messages.success(self.request, "Student created successfully")
        return super().form_valid(form)
   
class StudentUpdateView(UpdateView):
    model = Student
    template_name = "cbvapp/student_update.html"
    form_class = StudentForm  # Use form_class if you have a custom form
    success_url = reverse_lazy("student_list")

    def form_valid(self, form):
        messages.success(self.request, "Student updated successfully")
        return super().form_valid(form)
    
    
    

class StudentDeleteView(DeleteView):
    model = Student
    template_name = "cbvapp/confirm_delete.html"
    success_url = reverse_lazy("student_list")

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, "Student deleted successfully")
        return response