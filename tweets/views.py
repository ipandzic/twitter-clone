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

    def get_queryset(self, *args, **kwargs):
        queryset = Tweet.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            queryset = queryset.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
                )
        return queryset

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
