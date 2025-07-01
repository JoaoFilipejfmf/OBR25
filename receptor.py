from pybricks.hubs import PrimeHub
from pybricks.tools import wait

hub = PrimeHub(broadcast_channel=2, observe_channels=[114])

# Aguarda mensagem do cliente
while True:
    info = hub.ble.observe(114)
    if(info == 1):
        hub.speaker.beep(frequency=100, duration=100)
        wait(1000)
    if(info == 2):
        hub.speaker.beep(frequency=200, duration=100)
        wait(1000)
    wait(10)