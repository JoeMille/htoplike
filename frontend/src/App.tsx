import React, { useState, useEffect, use } from 'react';
import axios from 'axios';
import { SystemStats } from './types/SystemStats';
import './App.css';

const formatBytes = (bytes: number | null): string => {
    if (bytes == null || bytes === undefined) return 'N/A';
    if (bytes === 0) return '0 B';

    const units = ['B', 'KB', 'MB', 'GB', 'TB'];

    const unitIndex = Math.floor(Math.log2(bytes) / 10);

    const value = bytes / Math.pow(2, unitIndex * 10);

    return `${value.toFixed(1)} ${units[unitIndex]}`;
};

const formatPercentage = (percent: number | null): string => {
    if (percent === null || percent === undefined) return 'N/A';
    return `${percent.toFixed(1)}%`
}

const App: React.FC = () => {
    const [stats, setStats] = useState<SystemStats | null>(null);
    const [loading, setLoading] = useState<boolean>(true);
    const [error, setError] = useState<string | null>(null);

    const fetchStats = async (): Promise<void> => {
        try {
            setLoading(true);
            setError(null);

            const response = await axios.get<SystemStats>('http://localhost:8000/api/current-stats/');

            setStats(response.data);

            } catch (err) {
                console.error('Error fetching stats:', err);
                setError('Failed to fetch system stats');
            } finally {
                setLoading(false);
        }
    };

    useEffect(() => {
        fetchStats();

        const interval = setInterval(fetchStats, 5000);

        return () => clearInterval(interval);
    }), [];
    
    if (loading) {
        return (
            <div className='container'>
                <div className='error'>
                    {error}
                    <br />
                    <button className='refresh-button' onClick={fetchStats}>
                        Retry
                    </button>
                </div>
            </div>
        );
    }
    if (!stats) {
        return (
            <div className='container'>
                <div className='loading'>No data available</div>
            </div>
        );
    }

    return (
        <div className='container'>
            <header className='header'>
                <h1>System Monitor Dashboard</h1>
                <p>Real-Time Stats Monitoring</p>
            </header>

                  <div className="stats-grid">
        <div className="stat-item">
          <div className="stat-label">CPU Usage</div>
          {/* {} in JSX means "run JavaScript expression" */}
          <div className="stat-value">{formatPercentage(stats.cpu_percent)}</div>
        </div>

        <div className="stat-item">
          <div className="stat-label">Memory Usage</div>
          <div className="stat-value">{formatPercentage(stats.memory_percent)}</div>
        </div>

        <div className="stat-item">
          <div className="stat-label">Memory Used</div>
          <div className="stat-value">{formatBytes(stats.memory_used)}</div>
        </div>

        <div className="stat-item">
          <div className="stat-label">Memory Total</div>
          <div className="stat-value">{formatBytes(stats.memory_total)}</div>
        </div>

        <div className="stat-item">
          <div className="stat-label">Disk Usage</div>
          <div className="stat-value">{formatPercentage(stats.disk_percent)}</div>
        </div>

        <div className="stat-item">
          <div className="stat-label">CPU Cores</div>
          <div className="stat-value">
            {stats.cpu_count && stats.cpu_count_logical ?
                `${stats.cpu_count} (${stats.cpu_count_logical} threads)` :
                'N/A'
            }
        </div>
    </div>
</div>

<div className='timestamp'>
    Last updated: {new Date(stats.timestamp).toLocaleString()}
</div>
</div>
);};

export default App;