from django.shortcuts import render, redirect
from accounts.forms import UserLoginForm
from django.template.context_processors import csrf
from django.contrib import messages, auth
from django.core.urlresolvers import reverse

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():

            print "eee",request.POST.get('email')
            print "ppp",request.POST.get('password')

            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password'))

            print user

            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")
                return redirect(reverse('profile'))
            else:
                form.add_error(None, "Your email or password was not recognised")
        else:
            form.add_error(None, "Form invalid")

    else:
        form = UserLoginForm()

    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'login.html', args)