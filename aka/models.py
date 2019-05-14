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
Description: A module that contains the bookmark app Django data-models classes
'''

import re
from django.db import models
from fuzzywuzzy import fuzz, process


class ResolveUrlManager(models.Manager):

    def __init__(self):
        super().__init__()
        self.queryset = None
        self.func = fuzz.partial_token_set_ratio

    def _sorted_match(self, linklabel):
        '''
        Returns sorted tuple of Redirect models as per the fuzzywuzzy sorting function.
        '''

        if self.queryset is None:
            self.queryset = self.get_queryset()

        if len(self.queryset.all()) <= 0:
            raise IndexError

        # Strip out any whitespace to improve fuzzywuzzy token matching
        whitespace_pattern = re.compile(r'\s+')
        linklabel = re.sub(whitespace_pattern, '', linklabel)

        return sorted(
            [(redirect, self.func(linklabel, re.sub(whitespace_pattern, '', redirect.linklabel)))
             for redirect in self.queryset.all()],
            key=lambda match: match[1],
            reverse=True
        )

    def from_linklabel(self, linklabel, limit=5, include_confidence_level=False):
        'Returns the selected number of matches as list of Redirect models in sorted order by best match.'
        return [match[0] if not include_confidence_level else match for match in self._sorted_match(linklabel)[:limit]]

    def from_top_linklabel(self, linklabel, include_confidence_level=False):
        'Finds the top match and returns that single Redirect model.'
        return [match[0] if not include_confidence_level else match for match in self._sorted_match(linklabel)].pop(0)


class Redirect(models.Model):
    '''
    Data model that represents a browser bookmark. It uses a URL, description
    and linklabel that is used to match against a users provided search term.
    '''

    linklabel = models.CharField(max_length=256)
    target_url = models.CharField(max_length=256)
    description = models.CharField(max_length=256, blank=True)
    objects = models.Manager()
    resolve_url = ResolveUrlManager()
