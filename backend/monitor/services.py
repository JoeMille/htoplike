import psutil 
import os 
from datetime import datetime
from .models import SystemStats

class SystemMonitorService:
    @staticmethod
    def get_system_stats():

        stats = {}

        try:
            stats['cpu_percent'] = psutil.cpu_percent(interval=1)
            stats['cpu_count'] = psutil.cpu_count(logical=False)
            stats['cpu_count_logical'] = psutil.cpu_count(logical=True)

            # memory 
            memory = psutil.virtual_memory()
            stats['memory_total'] = memory.total
            stats['memory_available'] = memory.available
            stats['memory_percent'] = memory.percent
            stats['memory_used'] = memory.used
            # swap
            swap = psutil.swap_memory()
            stats['swap_total'] = swap.total
            stats['swap_used'] = swap.used
            stats['swap_percent'] = swap.percent

            # linux load averages
            if hasattr(os, 'getloadavg'):
                load_avg = os.getloadavg()

                stats['load_average'] = ','.join(map(str,load_avg))

            disk = psutil.disk_usage('/')
            stats['disk_total'] = disk.total
            stats['disk_used'] = disk.used
            stats['disk_free'] = disk.free

            stats['disk_percent'] = (disk.used / disk.total) * 100
        
        except Exception as e:
            print(f"Error collecting stats: {e}")
        return stats
    
    @staticmethod
    def save_current_stats():
        stats = SystemMonitorService.get_system_stats()
        system_stats = SystemStats(**stats)

        system_stats.save()

        return system_stats