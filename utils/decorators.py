from django.contrib.auth.decorators import user_passes_test
from functools import wraps
from django.http import HttpResponseRedirect


def is_logged(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):

        if "is_logged" in request.session:
            # print(request.path == "/select-business/")
            if "customer_id" not in request.session:
                return HttpResponseRedirect("/login/")
            
            if "account_email" not in request.session:
                return HttpResponseRedirect("/login/")

            if "businesses" not in request.session:
                if request.path != "/select-business/":
                    return HttpResponseRedirect("/select-business/")

            if "active_business" not in request.session:
                if request.path != "/select-business/":
                    return HttpResponseRedirect("/select-business/")

            if "active_api_key" not in request.session:
                return HttpResponseRedirect("/login/")

            return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/login/')
    return wrap


def is_not_logged(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        # request.session['wallet_conn'] = True
        if "is_logged" in request.session:
            return HttpResponseRedirect('/dashboard/')
        else:
            return function(request, *args, **kwargs)

    return wrap

def is_logged_business(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        # request.session['wallet_conn'] = True
        if "is_logged" in request.session:
            return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/login/')

    return wrap


# def membership_required(fn=None):
#     def my_custom_authenticated(user):
#         # if user:
#         #     if user.is_authenticated():
#         #         return user.groups.filter(name=settings.MY_CUSTOM_GROUP_NAME).exists()
#         # return False
#         return True

#     decorator = user_passes_test(my_custom_authenticated)
#     if fn:
#         return decorator(fn)
#     return decorator
