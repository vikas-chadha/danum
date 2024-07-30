from django.shortcuts import render
from .forms import ContactForm
from django.http import JsonResponse

# Create your views here.

def home(request):
    return render(request, 'app/home.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ContactForm()
    return render(request, 'your_template.html', {'form': form})