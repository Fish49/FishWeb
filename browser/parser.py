import xml.etree.ElementTree as ET

def parse(string):
    data = ET.XML(string)
    return data