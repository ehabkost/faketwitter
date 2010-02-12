
import xml.etree.ElementTree as ET

class TwitterData:
    DEFAULT_TAG = None
    def __init__(self, xml=None, tag=None):
        if xml is None:
            if tag is None:
                tag = self.DEFAULT_TAG
            xml = ET.Element(tag)
        self._xml = xml
        self._props = {}
        for e in self._xml:
            self._props[e.tag] = TwitterData(e)

    def __getattr__(self, a):
        return self._props[a]

    def add(self, a, v=None):
        e = ET.Element(a)
        if v is not None:
            e.text = v
        self._xml.append(e)
        d = TwitterData(e)
        self._props[a] = d
        return d

    def __str__(self):
        return self._xml.text

    def __eq__(self, o):
        return str(self) == o

    def __call__(self):
        return str(self)

    def __repr__(self):
        return '<TwitterData: %r, %r>' % (str(self), self.props)

class Status(TwitterData):
    """A status post"""
    DEFAULT_TAG = 'status'
