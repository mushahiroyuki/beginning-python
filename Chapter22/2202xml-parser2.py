#ファイル名 Chapter22/2202xml-parser2.py
from xml.sax.handler import ContentHandler
from xml.sax import parse

class TestHandler(ContentHandler):
    def startElement(self, name, attrs):
        print(name, attrs.keys())

parse('website.xml', TestHandler())

