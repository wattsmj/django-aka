'''
Smart Bookmark Tool that redirects your web browser based on labels
Copyright (C) 2019  Matthew Watts

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Author: wattsmj
Contact: Please raise an issue on www.github.com/wattsmj/django-aka
Description: A module that contains the bookmark app Django view classes
'''

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
