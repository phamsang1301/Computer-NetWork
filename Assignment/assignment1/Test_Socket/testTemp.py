from pyspectator.processor import Cpu
from time import sleep
cpu = Cpu(monitoring_latency=1)

while True:
    print (cpu.temperature)
    sleep(1)