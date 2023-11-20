import qgate.solution as qgate
from qgate.solution import Solution
import os.path
from qgate.uc import uc101, uc102, uc201, uc301, uc401, uc501
from qgate.uc import ucsetup, ucoutput, ucbase
import sys


if __name__ == '__main__':

    setup = ucsetup.UCSetup("0-size-100",
                            ["qgate-sln-mlrun-private.env", "qgate-sln-mlrun.env"])
    output = ucoutput.UCOutput(setup)
    sln = Solution(setup)

    usecase_fns = [uc101.UC101, uc201.UC201, uc301.UC301, uc401.UC401]
    usecase_test = uc501.UC501
    NoDelete=False

    # support parametr 'NoDelete' and 'Test' for switch-off the UC102: Delete project(s)
    if len(sys.argv)>1:
        for arg in sys.argv[1:]:
            arg=arg.lower()
            if arg=="nodelete":
                NoDelete=True
            elif arg=="test":
                usecase_fns.append(usecase_test)
    if NoDelete == False:
        usecase_fns.append(uc102.UC102)

    for usecase_fn in usecase_fns:
        uc = usecase_fn(sln, output)
        try:
            uc.exec()
            uc.state = ucbase.UCState.OK
        except Exception as ex:
            uc.state = ucbase.UCState.Error
            uc.logln("{0}: {1}", type(ex).__name__, str(ex))
    output.Close()