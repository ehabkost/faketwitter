import unittest
import xml.etree.ElementTree as ET
import faketwitter.objects

class TestXml(unittest.TestCase):
    def assertDataEquals(self, data, s):
        self.assertEquals(str(data), s)
        self.assertEquals(data, s)
        self.assertEquals(data(), s)

    def testSimpleXml(self):
        s = """<status>
        <text>foo</text>
        <user><id>123</id><name>jack</name></user>
        </status>
        """
        x = ET.XML(s)
        d = faketwitter.objects.TwitterData(x)
        self.assertDataEquals(d.text, 'foo')
        self.assertDataEquals(d.user.id, '123')
        self.assertDataEquals(d.user.name, 'jack')
