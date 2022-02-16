from django.shortcuts import render,redirect
from .forms import Project_Data
from django.http import HttpResponse
# Create your views here.
def hotel_image_view(request):
  
    if request.method == 'POST':
        form = Project_Data(request.POST, request.FILES)
        
  
        if form.is_valid() and form2.is_valid():
            form.save()
            return redirect('success')
    else:
        form = Project_Data()
        
    return render(request, 'projects/form.html', {'form' : form })
  
  
def success(request):
    return HttpResponse('successfully uploaded')