
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def profile(request):
    if not request.user.is_authenticated:
        return redirect(reverse('accounts:login'))
    username = request.user.username
    context = {
        'username': username
    }
    return render(request, 'user_office/profile.html', context)