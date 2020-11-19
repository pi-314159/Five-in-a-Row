import os
def cpuNum(numCPU):
    try:
        cpu_num = len(os.sched_getaffinity(0))
    except:
        # Literally, who cares?
        try:
            cpu_num = os.cpu_count() - 1
        except:
            cpu_num = numCPU
    if cpu_num < 1:
        cpu_num = 1
    return cpu_num
