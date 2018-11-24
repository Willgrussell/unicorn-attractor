import json
import datetime
from django.db import connections
from django.db.models import Count, Q 
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from tickets.models import Ticket

# Create your views here.
def promotion(request, *args, **kwargs):
    """A view that will display any promotion i choose to display"""
    return render(request, "promotions.html", {})
    
def issue_chart(request):
    """View issue type total by type from database"""
    
    # Dataset for issue_type
    dataset = Ticket.objects.all() \
        .values('issue_type') \
        .exclude(issue_type='') \
        .annotate(total=Count('issue_type')) \
        .order_by('issue_type') \

    type_display_name = dict()
    for type_tuple in Ticket.ISSUE_TYPE_CHOICES:
        type_display_name[type_tuple[0]] = type_tuple[1]
        
    chart = {
        'chart': {'type': 'pie'},
        'renderTo': 'issue',
        'title': {'text': 'Issue By Type'},
        'series': [{
            'name': 'Issue',
            'data': list(map(lambda row: {'name': type_display_name[row['issue_type']], 'y': row['total']}, dataset))
        }]
    }
    return JsonResponse(chart)
    
def status_chart(request):
    """View chart live status of tickets"""
    
    # Dataset for status
    dataset = (Ticket.objects.all()) \
        .values('status') \
        .annotate(total=Count('status')) \
        .order_by('status')
        
    status_display_name = dict()
    for status_tuple in Ticket.STATUS_CHOICES:
        status_display_name[status_tuple[0]] = status_tuple[1]
        
    chart = {
        'chart': {'type': 'pie'},
        'title': {'text': 'Live Ticket Status'},
        'renderTo': 'status',
        'series': [{
                'name': 'Status',
                'colorByPoint': True,
                'data': list(map(lambda row: {'name': status_display_name[row['status']], 'y': row['total']}, dataset))
            }]
    }
    return JsonResponse(chart)
    
def urgent_chart(request):
    """A View to display Ticket by Urgent total"""
    
    # dataset for urgent
    dataset = Ticket.objects.all() \
        .values('issue_type') \
        .filter(urgent=True) \
        .annotate(urgent_total=Count('urgent'))\
        .order_by('issue_type') \
    
    categories = list()
    urgent_total_data = list()
    # not_urgent_total_data = list()
    
    for entry in dataset:
        categories.append('%s ' % entry['issue_type'])
        urgent_total_data.append(entry['urgent_total'])
        # not_urgent_total_data.append(entry['not_urgent_total'])
    
    urgent_series = {
        'name': 'Urgent',
        'data': urgent_total_data, 
        'color': 'red'
    }
    
    chart = {
        'chart': {'type': 'column'},
        'title': {'text': 'Ticket Urgency by Type'},
        'renderTo': 'urgent',
        'xAxis': {'categories': categories},
        'series': [urgent_series]
    }
    return JsonResponse(chart)

def not_urgent_chart(request):
    """View to render not urgent data"""
    
    dataset = Ticket.objects.all() \
        .values('issue_type') \
        .filter(urgent=False) \
        .annotate(not_urgent_total=Count('urgent')) \
        .order_by('issue_type') \
        
    categories = list()
    not_urgent_total_data = list()
    
    for entry in dataset:
        categories.append('%s ' % entry['issue_type'])
        not_urgent_total_data.append(entry['not_urgent_total'])
        
    not_urgent_series = {
        'name': 'Not Urgent',
        'color': 'blue',
        'data': not_urgent_total_data
    }
    chart = {
        'chart': {'type': 'bar'},
        'title': {'text': 'Ticket Non-Urgency by Type'},
        'renderTo': 'Not Urgent',
        'xAxis': {'categories': categories},
        'series': [not_urgent_series]
    }
    return JsonResponse(chart)