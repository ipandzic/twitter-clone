from django.views.generic import DetailView, ListView, CreateView
from .forms import TweetModelForm
from .models import Tweet


class TweetCreateView(CreateView):
    form_class = TweetModelForm
    template_name = "tweets/create_view.html"
    success_url = "/tweet/create/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TweetCreateView, self).form_valid(form)


class TweetDetailView(DetailView):
    template_name = "tweets/detail_view.html"
    queryset = Tweet.objects.all()


class TweetListView(ListView):
    template_name = "tweets/list_view.html"
    queryset = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        return context
