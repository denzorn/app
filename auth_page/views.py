from django.shortcuts import render
from django.views.generic.edit import FormView
from auth_page.forms import UserCreationForm

# Create your views here.

class UserCreationForm(FormView):
    form_class = UserCreationForm
    success_url = '/'
    template_name = 'index.html'

    def form_valid(self, form):
        form.save()
        return super(UserCreationForm, self).form_valid(form)




