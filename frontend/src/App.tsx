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

    return ()
    };
