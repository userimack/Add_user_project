from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from trackuser.forms import NameForm,LoginForm,ProfileForm
from trackuser.models import Create,Profile




# Create your views here.
def home(request):
    return render(request,'trackuser/base.html',{})


def register(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = NameForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save()

            # Now call the index() view.
            # The user will be shown the homepage.
            #return userlist(request)
            return HttpResponseRedirect('/login/')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print(form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form =  NameForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'trackuser/register.html', {'form': form})


def userlist(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
  
    data =Create.objects.all()
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request,'trackuser/users.html', {'data': data})



def login(request):
    """
    Log In view
    """
    try:
        if request.session['username']:
            return HttpResponseRedirect('/success/')
    except:
        pass
    

    if request.method == 'POST':
        #print (request.POST) //For printing the data in command line
        form =LoginForm(request.POST)
        if form.is_valid():
            try:
                user = Create.objects.filter(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
                if len(user) == 1:
                    request.session['username'] = user[0].username
                    return HttpResponseRedirect('/success/')
                else:
                    return HttpResponse("Login Credentials didn't match, Please try again")
            except DoesNotExit:
                return None
    else:
        form = LoginForm()

    return render(request,'trackuser/login.html',{'form':form})


def success(request):
    if request.session['username']:
        return render(request,'trackuser/success.html',{})
    else:
        return HttpResponseRedirect('/login/')

def logout(request):
    del request.session['username']
    return HttpResponseRedirect('/login/')


def profile(request):
    if request.session['username']:
        if request.method == 'POST' :
            a = Create.objects.get(username=request.session['username'])
            try:
                b = Profile.objects.get(user=a)
            except:
                b = Profile(user=a)
                b.save()
                b = Profile.objects.get(user=a)

            form = ProfileForm(request.POST,instance=b)

            if form.is_valid():
                # Save the new category to the database.
                form.save()

                # Now call the index() view.
                # The user will be shown the homepage.
                #return userlist(request)
                return HttpResponseRedirect('/login/')
            else:
                # The supplied form contained errors - just print them to the terminal.
                return render(request,'trackuser/profile.html',{'form':form})

        else:
            a= Create.objects.get(username=request.session['username'])
            try:
                b = Profile.objects.get(user=a)
            except:
                b=Profile(user=a)
                b.save()
                b=Profile.objects.get(user=a)

            form = ProfileForm(instance=b)
            return render(request,'trackuser/profile.html',{'form':form})


    else:
        # If the request was not a POST, display the form to enter details.
        return HttpResponseRedirect('/login/')



def profile_view(request):   
    if request.session['username']:
        a = Create.objects.get(username=request.session['username'])
        try:
            b=Profile.objects.get(user=a)
        except:
            b=Profile(user=a)
            b.save()
            b=Profile.objects.get(user=a)
        return render(request,'trackuser/profile_view.html', {'profile':b})
    else:
        return HttpResponseRedirect('/login/')


