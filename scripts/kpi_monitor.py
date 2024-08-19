import time
from prometheus_client import start_http_server, Gauge

kpi_gauge = Gauge('network_slice_kpi', 'The Key Performance Indicator — KPI — of the Network Slice')

def monitor_kpis():
    while True:
        kpi_value = 100  # Placeholder for the real KPI value
        kpi_gauge.set(kpi_value)
        time.sleep(5)

if __name__ == "__main__":
    start_http_server(8000)
    monitor_kpis()
