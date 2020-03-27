# The MIT License (MIT)
#
# Copyright (c) 2020 Dave Astels
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""
Neopixel zone support
--------------------------------------------------------------------------------
* Author: Dave Astels
"""


class ZoneCollection:
    def __init__(self, pixels):
        self._pixels = pixels
        self._zones = []

    def _add(self, zone):
        self._zones.append(zone)
        zone.collection = self
        return zone

    def add_zone(self, first, last_plus_one):
        #        if first < 0 or last > self._pixels.
        return self._add(Zone(first, last_plus_one))

    def add_zone_with_size(self, first, size):
        return self.add_zone(first, first + size)

    @property
    def brightness(self):
        return self._pixels.brightness

    @brightness.setter
    def brightness(self, brightness):
        self._pixels.brightness = brightness

    def __setitem__(self, index, val):
        self._pixels[index] = val

    def __getitem__(self, index):
        return self._pixels[index]

    def show(self):
        self._pixels.show()


class Zone:
    def __init__(self, first, last_plus_one):
        self._first = first
        self._last_plus_one = last_plus_one
        self._collection = None

    @property
    def collection(self):
        return self._collection

    @collection.setter
    def collection(self, coll):
        self._collection = coll

    def __setitem__(self, index, val):
        if isinstance(index, slice):
            self._collection[
                (index.start + self._first) : (index.stop + self._first) : (index.step)
            ] = val
        else:
            self._collection[index + self._first] = val

    def __getitem__(self, index):
        if isinstance(index, slice):
            return self._collection[
                (index.start + self._first) : (index.stop + self._first) : (index.step)
            ]
        else:
            return self._collection[index + self._first]

    def fill(self, color):
        for i in range(self._last_plus_one - self._first):
            self[i] = color

    def show(self):
        self._collections.show()
