from django.contrib.auth.decorators import user_passes_test
from functools import wraps
from django.http import HttpResponseRedirect

def is_logged(function):
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