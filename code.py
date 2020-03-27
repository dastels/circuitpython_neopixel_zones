import time
from random import randint
import digitalio
import board
import neopixel
import neopixel_zones

enable = digitalio.DigitalInOut(board.D10)
enable.direction = digitalio.Direction.OUTPUT
enable.value = True

strip = neopixel.NeoPixel(board.D5, 60, brightness=1, auto_write=False)

collection = neopixel_zones.ZoneCollection(strip)

zone_1 = collection.add_zone(0, 20)
zone_2 = collection.add_zone_with_size(20, 20)
zone_3 = collection.add_zone(40, 60)

for _ in range(10):
    zone_1.fill((randint(128, 255), randint(0, 255), randint(0, 255)))
    zone_2.fill((randint(0, 255), randint(128, 255), randint(0, 255)))
    zone_3.fill((randint(0, 255), randint(0, 255), randint(128, 255)))
    collection.show()
    time.sleep(0.5)

for _ in range(4):
    for i in range(1, 20):
        strip.fill((0x00, 0x00, 0x00))
        zone_1[i] = (0xFF, 0x00, 0x00)
        zone_2[i] = (0x00, 0xFF, 0x00)
        zone_3[i] = (0x00, 0x00, 0xFF)
        collection.show()
        time.sleep(0.2)
    for i in range(18, -1, -1):
        strip.fill((0x00, 0x00, 0x00))
        zone_1[i] = (0xFF, 0x00, 0x00)
        zone_2[i] = (0x00, 0xFF, 0x00)
        zone_3[i] = (0x00, 0x00, 0xFF)
        collection.show()
        time.sleep(0.2)

for _ in range(4):
    for i in range(20):
        strip.fill((0x00, 0x00, 0x00))
        start = i
        end = min(i + 5, 20)
        size = end - start
        zone_1[start:end] = [(0xFF, 0x00, 0x00)] * size
        zone_2[start:end] = [(0x00, 0xFF, 0x00)] * size
        zone_3[start:end] = [(0x00, 0x00, 0xFF)] * size
        collection.show()
        time.sleep(0.2)

while True:
    strip.fill((0, 0, 0))
    zone_1[randint(0, 19)] = (randint(0, 255), randint(0, 255), randint(0, 255))
    zone_2[randint(0, 19)] = (randint(0, 255), randint(0, 255), randint(0, 255))
    zone_3[randint(0, 19)] = (randint(0, 255), randint(0, 255), randint(0, 255))
    collection.show()
    time.sleep(0.1)
