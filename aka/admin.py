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
Description: A module that contains the admin classes for the Django provided admin page
'''

from contextlib import contextmanager
from django import forms
from django.contrib import admin
from django.contrib.admin.helpers import ActionForm
from .models import Redirect


class UpdateActionForm(ActionForm):
    search_term = forms.CharField(required=False)


@contextmanager
def custom_resolve_url_queryset(queryset):
    Redirect.resolve_url.queryset = queryset
    yield Redirect
    Redirect.resolve_url.queryset = None


class RedirectAdmin(admin.ModelAdmin):
    '''
    Represents the Redirects database in the admin page
    '''

    fieldsets = [
        (None, {
            'fields': [
                'linklabel',
                'description',
                'target_url'
            ]
        })
    ]

    list_filter = (
        'description',
        'linklabel'
    )

    list_display = ('description',)

    actions = ['test_match']

    action_form = UpdateActionForm

    def test_match(self, request, queryset):
        'Returns the match confidenced for each redirect against the provided search term.'
        with custom_resolve_url_queryset(queryset) as Redirect:
            search_term = request.POST['search_term']
            message = [
                f' "{redirect.description}" = {confidence_level}'
                for redirect, confidence_level in Redirect.resolve_url.from_linklabel(search_term, include_confidence_level=True)
            ]
            self.message_user(request, ','.join(message))

    test_match.short_description = 'Get the match confidence for the selected bookmarks'


admin.site.register(Redirect, RedirectAdmin)
admin.site.site_header = 'AKA'
admin.site.site_title = 'Bookmark Administration'
admin.site.index_title = 'Bookmark Administration'
