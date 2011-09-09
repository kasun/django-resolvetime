'''
Author - Kasun Herath <kasunh01 at gmail.com>
'''

from datetime import datetime

from django import template

register = template.Library()

@register.filter
def resolvetime(time):
    """ format a time to a format to elaborate the time difference from now"""
    resolvedtime = ''
    
    now = datetime.now()
    diff = now - time    
    
    if (diff.days > 0 and diff.days < 31):
        resolvedtime = str(diff.days) + ' days'
    elif (diff.days > 31 and diff.days < 365):
        resolvedtime = str(diff.days/30) + 'months'
    elif diff.days >= 365:
        resolvedtime = 'more than 1 year'
    elif diff.seconds < 60:
        resolvedtime = str(diff.seconds) + ' s'
    elif diff.seconds < 60 * 60:
        resolvedtime = str(diff.seconds/60) + ' mins'
    elif diff.seconds < 60 * 60 * 24:
        hours = diff.seconds / (60*60)
        mins = (diff.seconds % (60*60)) / 60
        resolvedtime = str(hours) + ' hours and ' + str(mins) + ' mins' 
        
    return resolvedtime
        
