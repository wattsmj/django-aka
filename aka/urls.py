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
Description: A module that defines the bookmark app URL routes
'''

from django.urls import path
from .views import AkaRedirectView, SearchView, ResultsView

urlpatterns = [
    path('', SearchView.as_view(), name=''),
    path('results', ResultsView.as_view(), name=''),
    path('<str:linklabel>', AkaRedirectView.as_view(), name=''),
]