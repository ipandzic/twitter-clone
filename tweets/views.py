from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.db.models import Q
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView
    )

from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin
from .models import Tweet


class TweetCreateView(FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = "tweets/create_view.html"


class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
    template_name = "tweets/detail_view.html"


class TweetListView(ListView):
    queryset = Tweet.objects.all()
    template_name = "tweets/tweet_list.html"

    def get_queryset(self):
        im_following = self.request.user.profile.get_following()
        qs1 = Tweet.objects.filter(user__in=im_following)
        qs2 = Tweet.objects.filter(user=self.request.user)
        qs = (qs1 | qs2)
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        context["create_form"] = TweetModelForm()
        context["create_url"] = reverse_lazy("tweet:create")
        return context


class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    template_name = "tweets/update_view.html"
    form_class = TweetModelForm
    success_url = "/tweet/"


class TweetDeleteView(LoginRequiredMixin, DeleteView):
    queryset = Tweet.objects.all()
    template_name = "tweets/delete_confirm.html"
    success_url = reverse_lazy('tweet:list')
