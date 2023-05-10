from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
 
from .forms import StudentForm          
 
def index(request):
   return HttpResponse("This is index page")
def get_student(request):    
  if request.method == 'POST':          
    form = StudentForm(request.POST)     
    if form.is_valid():
        s_name = form.cleaned_data['name']
        s_roll = form.cleaned_data['roll']
        s_degree = form.cleaned_data['degree']        
        s_branch = form.cleaned_data['branch']
 
    return HttpResponseRedirect('/student/')
  else: 
      form =StudentForm()
      return render(request, 'StudentForm.html', {'form': form})