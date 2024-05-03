from Run.run_getdata import getdata_run
from Run.run_gethtml import gethtml_run
from Run.run_getzip import getzip_run


def run_execute(start,end):
    print('running process')
    # html_code = gethtml_run(start,end)
    getdata_run(start,end)

