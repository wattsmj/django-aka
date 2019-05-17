# AKA

Smart Bookmark Tool that redirects your web browser based on labels

## Quick start


1. Add "aka" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'aka',
    ]

2. Include the aka app URLconf in your project urls.py like this (import include() if required)::

    path('', include('aka.urls')),

3. Run `python manage.py makemigrations aka` to prepare the aka app models.

4. Run `python manage.py migrate` to create the aka app models.

5. Access the admin site and create redirect entries.

6. Access the app via a web browser using the labels you've added http://\<web server name\>/\<urlconf\>/\<search label\>. Labels are fuzzy matched, be lazy while typing (i.e. try just the first letter of the label).
