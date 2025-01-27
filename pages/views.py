from django.shortcuts import render,HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model
# Create your views here.

def testpages(request):
    return HttpResponse ("Test page")

class UpdateProgile(generic.UpdateView):
    model = get_user_model()
    fields = ('age','first_name','email','last_name','date_joined',)
    template_name ='pages/profile.html'
    def get_success_url(self):
        return reverse_lazy('user_profile', kwargs={'pk': self.request.user.pk})

    def get_object(self, queryset=None):
        return self.request.user
