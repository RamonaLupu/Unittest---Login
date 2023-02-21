import unittest
from tema9 import Login
import HtmlTestRunner

class TestTema(unittest.TestCase):
    def test_suite(self):
        test_derulat = unittest.TestSuite()
        test_derulat.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Login))
        runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_title="My Report", report_name="Report Name", open_in_browser=True)
        runner.run(test_derulat)