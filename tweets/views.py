from django import forms
from django.forms.utils import ErrorList
from django.views.generic import DetailView, ListView, CreateView
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin
from .models import Tweet


class TweetCreateView(FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = "tweets/create_view.html"
    success_url = "/tweet/create/"

    # def form_valid(self, form):
    #     if self.request.user.is_authenticated():
    #         form.instance.user = self.request.user
    #         return super(TweetCreateView, self).form_valid(form)
    #     else:
    #         form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in to continue"])
    #         return self.form_invalid(form)


class TweetDetailView(DetailView):
    template_name = "tweets/detail_view.html"
    queryset = Tweet.objects.all()


class TweetListView(ListView):
    template_name = "tweets/list_view.html"
    queryset = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        return context
