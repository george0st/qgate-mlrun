from qgate_sln_mlrun.qualityreport import QualityReport
from qgate_sln_mlrun import output, setup
import unittest
import os


class TestProjects(unittest.TestCase):

    INPUT_FILE = "qgate_sln_mlrun-sln-mlrun.env"

    @classmethod
    def setUpClass(cls):
        # setup relevant path
        if not os.path.isfile(os.path.join(".", TestProjects.INPUT_FILE)):
            os.chdir(os.path.dirname(os.getcwd()))

    @classmethod
    def tearDownClass(cls):
        pass

    def test_main(self):
        stp = setup.Setup("0-size-100",
                          ["qgate-sln-mlrun-private.env", "qgate-sln-mlrun.env"])
        out = output.Output(stp, ['./qgate_sln_mlrun/templates/qgt-mlrun.txt',
                                  './qgate_sln_mlrun/templates/qgt-mlrun.html'])
        report = QualityReport(stp, out)
        report.execute()
