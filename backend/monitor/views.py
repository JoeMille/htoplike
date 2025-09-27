from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SystemStats
from .services import SystemMonitorService
import json

@api_view(['GET'])
def current_stats(request):
    try:
        stats = SystemMonitorService.get_system_stats()
        stats['timestamp'] = SystemMonitorService.save_current_stats().timestamp
        return Response(stats, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    

@api_view(['GET'])
def historical_stats(request):
    try:

        limit = int(request.GET.get('limit', 50))

        stats = SystemStats.objects.all()[:limit]
        
        stats_list = []
        for stat in stats: 
            stats_list.append({
                'id': stat.id,
                'timestamp': stat.timestamp,
                'cpu_percent': stat.cpu_percent,
                'memory_total': stat.memory_total,
                'memory_available': stat.memory_available,
                'memory_percent': stat.memory_percent,
                'memory_used': stat.memory_used,
                'swap_total': stat.swap_total,
                'swap_used': stat.swap_used,
                'swap_percent': stat.swap_percent,
                'cpu_count': stat.cpu_count,
                'cpu_count_logical': stat.cpu_count_logical,
                'load_average': stat.load_average,
                'disk_total': stat.disk_total,
                'disk_used': stat.disk_used,
                'disk_free': stat.disk_free,
                'disk_percent': stat.disk_percent,
            })
        
        return Response(stats_list, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response(
            {'error': str(e)}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

def home(request):
    """simple landing page to get backend going"""
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>System Monitor Backend</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .endpoint { margin: 20px 0; padding: 15px; background: #f5f5f5; }
        </style>
    </head>
    <body>
        <h1>System Monitor Backend</h1>
        <p>Django backend is running successfully!</p>
        
        <h2>Available API Endpoints:</h2>
        <div class="endpoint">
            <strong>GET /api/current-stats/</strong><br>
            Get current system statistics
        </div>
        <div class="endpoint">
            <strong>GET /api/historical-stats/</strong><br>
            Get historical system statistics<br>
            Optional parameter: ?limit=100
        </div>
        
        <h2>Test the API:</h2>
        <p><a href="/api/current-stats/">Current Stats</a></p>
        <p><a href="/api/historical-stats/">Historical Stats</a></p>
        <p><a href="/api/historical-stats/?limit=10">Historical Stats (Last 10)</a></p>
    </body>
    </html>
    """

    from django.http import HttpResponse
    return HttpResponse(html_content)