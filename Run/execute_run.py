from Run.run_getdata import getdata_run
from Run.run_gethtml import gethtml_run
from Run.run_getzip import getzip_run


def run_execute(start,end):
    html_code = gethtml_run(start,end)
    if html_code ==0:
        getdata_run(start,end)
        # getzip_run(start,end)
