'''
Author - Kasun Herath <kasunh01 at gmail.com>
'''

====================
Django Resolve Time
====================

This is a templatetag to convert a datetime object to a format that reflects the time difference between now and the time of given datetime object

Following are some example return values of the filter

6 s
10 mins
3 hours and 20 mins
2 months
4 days


====================
Installation
====================

Move the folder 'resolvetime' to your project path.

Add resolvetime to INSTALLED_APPS in settings.py:

{{{
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.sessions',

    'resolvetime',
)
}}}

====================
Usage
====================

import resolvetime tags by adding the following line in the required template

{% load timeresolve_tags %}

use the following filter to format a datetime object, where time is a datetime object

{{ time|resolvetime }}
