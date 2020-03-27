Logical NeoPixel chains

This lets you layer logical groups of NeoPixels over a longer physical strip/ring. It lets you treat contiguous subsets of pixels as separate strips.

Setup requires 3 steps:
- create the physical NeoPixel object
- create a zone collection on top of that
- add zones to the collection

Each zone added (and returned) can be treated the same as a NeoPixel object.

    strip = neopixel.NeoPixel(board.D5, 60, brightness=1, auto_write=False)

    collection = ZoneCollection(strip)

    zone_1 = collection.add_zone(0, 20)
    zone_2 = collection.add_zone_with_size(20, 20)
    zone_3 = collection.add_zone(40, 60)

They can be filled with a color:

    zone_1.fill((randint(128, 255), randint(0, 255), randint(0, 255)))

Individual elements can be set:

    zone_2[i] = (0x00, 0xFF, 0x00)

As can slices:

    zone_3[start:end] = [(0x00, 0x00, 0xFF)] * size

If the NeoPixel is created with `auto_write=False`, it can be updated by calling its `show()` method, the `ZoneCollection`'s or a `Zone`'s. Calling `show()` on a `Zone` will cause `show()` to be called on its collection, updating all the zones.

See code.py for more usage examples
