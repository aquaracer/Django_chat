from django.shortcuts import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .models import Messages
import logging
from .


logger = logging.getLogger(__name__)


class MessagesView(ListView):
    model = Messages
    context_object_name = 'messages'

    def get_queryset(self):
        count = Messages.objects.count() - 10

        if count >= 0:
            return Messages.objects.all()[count:]
        else:
            return Messages.objects.all()

    def post(self, request):
        user = User.objects.get(username=request.POST['user'])
        Messages.objects.create(user=user, messages=request.POST['message'])
        logger.info(f'{request.POST["user"]} : {request.POST["message"]}')
        return HttpResponseRedirect(reverse('chat:index'))


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('chat:index')
    template_name = 'registration/signup.html'
