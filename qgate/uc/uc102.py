"""
  UC102: Delete project(s)
"""

from qgate.uc.ucbase import UCBase
from qgate.nsolution import NSolution
from qgate.uc.ucoutput import UCOutput


class UC102(UCBase):

    def __init__(self, sln: NSolution, output: UCOutput):
        super().__init__(sln, output, self.__class__.__name__)


    @property
    def desc(self) -> str:
        return "Delete project(s)"

    def exec(self):
        self.sln.delete_projects(self)

