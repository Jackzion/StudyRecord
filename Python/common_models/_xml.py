from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax start_element: %s , attrs:%s' % (name,str(attrs)))
    def end_element(self, name):
        print('sax end_element: %s' % (name))
    def char_data(self, text):
        print('sax:char_data: %s' % (text))

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)

from urllib import request

class WeatherHandler(object):
    def __init__(self):
        self.data = {}
    def start_element(self, name, attrs):
        self.pointer = name
        if name == 'location':
            self.data['location'] = {}
    def end_element(self, name):
        self.pointer = ''
    def char_data(self, text):
        if self.data.get('location') is not None and self.pointer == 'name':
            self.data['location'] = text
    
handler = WeatherHandler()
def parseXml(xml_str):
    print(xml_str)
    # sax 解析 xml
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml_str)

# 测试:
URL = 'https://api.weatherapi.com/v1/current.xml?key=b4e8f86b44654e6b86885330242207&q=Beijing&aqi=no'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
print(handler.data)