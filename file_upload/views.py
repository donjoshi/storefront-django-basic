from django.shortcuts import render, redirect
from .forms import FileForm

def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page after successful upload
    else:
        form = FileForm()
    return render(request, 'upload.html', {'form': form})

def success(request):
    return render(request,'success.html')