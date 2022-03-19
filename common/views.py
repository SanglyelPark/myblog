from django.shortcuts import render, redirect

from common.forms import UserForm

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
    else:
        form = UserForm()
    context = {'form': form}
    return render(request, 'common/signup.html', context)

# Create your views here.
