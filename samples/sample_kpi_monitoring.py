import utest
from prometheus_client import Gauge

class TestKPIMonitoring(utest.TestCase):
    def test_kpi_gauge(self):
        kpi_gauge = Gauge('test_kpi', 'Test KPI')
        kpi_gauge.set(100)
        self.assertEqual(kpi_gauge._value.get(), 100)

if __name__ == "__main__":
    utest.main()
