from django.views.generic.base import RedirectView, TemplateView
from .models import Redirect
from fuzzywuzzy import process


class AkaRedirectView(RedirectView):
    '''
    Returns a HTTP Redirect to the users browser with the URL of the matched
    bookmark for the linklabel parameter from the querystring.
    '''

    permanent = False
    query_string = True
    pattern_name = ''

    def get_redirect_url(self, *args, **kwargs):
        try:
            self.url = Redirect.resolve_url.from_top_linklabel(
                kwargs['linklabel']).target_url
        except IndexError:
            self.url = '/'
        return super().get_redirect_url(*args, **kwargs)


class SearchView(TemplateView):
    '''
    Returns the home page of the site where the user can discover bookmarks
    or go directly to the top match. Uses search.html template.
    The form results are sent to the ResultsView controller.
    '''

    template_name = "search.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ResultsView(TemplateView):
    '''
    When the user clicks on "Suggest Top Five" their browser is directed to
    this view controller. It displays the top five results in order of match
    confidence using the results.html template.
    '''

    template_name = "results.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        linklabel = self.request.GET.get('linklabel')

        try:
            context['results'] = Redirect.resolve_url.from_linklabel(linklabel)
        except IndexError:
            context['results'] = [{
                'target_url': '/',
                'description': 'Please add some bookmarks first!'
            }]
        return context
