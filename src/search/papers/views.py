from django.shortcuts import render

from django.views.generic import TemplateView, ListView

from .models import Paper


class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Paper
    template_name = 'search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        # mandar o input
        print(query)
        object_list = []
        return object_list
# Create your views here.
