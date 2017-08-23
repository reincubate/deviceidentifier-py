import subprocess


def get_local_serial():
    ''' Retrieves the serial number from the executing host.
        For example, 'C02NT43PFY14'
    '''
    return [x for x in [subprocess.Popen("system_profiler SPHardwareDataType |grep -v tray |awk '/Serial/ {print $4}'", shell=True, stdout=subprocess.PIPE).communicate()[0].strip()] if x]
