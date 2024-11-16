import unittest
from datetime import datetime
from Project3 import get_JSON_data, graph

class TestProject3(unittest.TestCase):
    def test_get_JSON_data_valid(self):
        # test valid inputs
        symbol = "AAPL"
        time_series = "daily"
        start_date = datetime(2022, 1, 1)
        end_date = datetime(2022, 1, 10)
        data = get_JSON_data(symbol, time_series, start_date, end_date)
        self.assertIsInstance(data, dict)  # Expecting a dictionary

   # def test_get_JSON_data_invalid_symbol(self):
        # test invalid stock symbols
       # symbol = "INVALID"
       # time_series = "daily"
       # start_date = datetime(2022, 1, 1)
       # end_date = datetime(2022, 1, 10)
       # data = get_JSON_data(symbol, time_series, start_date, end_date)
       # self.assertIn("Error", data)  # Expecting an error response from API

   # def test_get_JSON_data_invalid_time_series(self):
        # test invalid dates
       # symbol = "AAPL"
       # time_series = "invalid_series"
       # start_date = datetime(2022, 1, 1)
       # end_date = datetime(2022, 1, 10)
       # with self.assertRaises(KeyError):  # Expecting a KeyError due to invalid time series
       #     get_JSON_data(symbol, time_series, start_date, end_date)

    def test_graph_valid(self):
        # Test valid graph creation
        symbol = "AAPL"
        time_series = "daily"
        start_date = datetime(2022, 1, 1)
        end_date = datetime(2022, 1, 10)
        chart_type = "line"
        # Mocking JSON data response
        mock_data = {
            "Time Series (Daily)": {
                "2022-01-10": {"1. open": "172.7", "2. high": "174.1", "3. low": "171.2", "4. close": "173.0"},
                "2022-01-09": {"1. open": "171.3", "2. high": "173.6", "3. low": "170.8", "4. close": "172.1"}
            }
        }
        result = graph(mock_data, symbol, time_series, start_date, end_date, chart_type)
        self.assertEqual(result, "chart.svg")  # Expecting the output file name

    def test_graph_no_data(self):
        # Test graph creation with no available data
        symbol = "AAPL"
        time_series = "daily"
        start_date = datetime(2022, 1, 1)
        end_date = datetime(2022, 1, 10)
        chart_type = "line"
        # Empty mock data
        mock_data = {"Time Series (Daily)": {}}
        result = graph(mock_data, symbol, time_series, start_date, end_date, chart_type)
        self.assertIsNone(result)  # Expecting None as there's no data to plot

if __name__ == "__main__":
    unittest.main()
