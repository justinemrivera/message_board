from django.views.generic import (
    TemplateView,
    ListView,
    DetailView
)

from .models import Post


# Create your views here.


class HomePageView(TemplateView):
    template_name = "home.html"


class MessagesPageView(ListView):
    template_name = "messages.html"
    model = Post


class MessageDetailView(DetailView):
    model = Post
    template_name = "message_detail.html"
