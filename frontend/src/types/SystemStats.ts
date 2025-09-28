export interface SystemStats{
    id?: number;

    timestamp: string;
    cpu_percent: number | null;
    memory_total: number | null;
    memory_available: number | null;
    memory_percent: number | null;
    memory_used: number | null;
    swap_total: number | null;
    swap_used: number | null;
    swap_percent: number | null;
    cpu_count: number | null;
    cpu_count_logical: number | null;
    load_average: string | null;
    disk_total: number | null;
    disk_toal: number | null;
    disk_used: number | null;
    disk_free: number | null;
    disk_percent: number | null;
}