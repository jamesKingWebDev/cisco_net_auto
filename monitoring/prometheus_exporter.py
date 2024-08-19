from prometheus_client import start_http_server, Gauge
import time

def prometheus_export_runner():
    kpi_gauge = Gauge('network_slice_kpi', 'This is the Key Performance Indicator — KPI — of the Network Slice')
    start_http_server(8000)

    while True:
        kpi_gauge.set(100)  # A sample KPI value
        time.sleep(5)

if __name__ == "__main__":
    prometheus_expor_runner()
