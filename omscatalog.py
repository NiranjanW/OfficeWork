from lxml import etree as ET
import sys
import os
import re
from io import StringIO

def parseXML (file):
    # parser = ET.XMLParser()
    # doc = ET.parse(file)
    # root= doc.getroot()
    #
    # print(ET.tostring(root, encoding='utf8').decode('utf8'))
    #
    # parser = ET.XMLParser(ns_clean=True, recover=True, encoding='utf-8')
    # h = ET.fromstring(filename, parser=parser)
    # with open(h,'r') as fh:
    #
    #     contents = fh.read()
    #     root = ET.fromstring('<?xml version="1.0" encoding="UTF-8" standalone="no"?><ItemList>{}</ItemList>'.
    #                          format(''.join(re.findall('<Item.*?</Item>', contents, re.S)))
    #                          )


    re_strip_pi = re.compile('<\?xml [^?>]+\?>', re.M)
    re_strip_ItemList = re.compile(' xmlns:xsi="[^"]+\"', re.M)
    data = open(file,'r').read()
    match = re_strip_pi.search(data)
    data = re_strip_pi.sub('', data)
    march_ItemList = re_strip_ItemList.search(data)
    data1 = re_strip_ItemList.sub('',data)
    # data = b'<root>' + data.read_bytes() + b'</root>'

    # data = '<root>' + data + '</root>'
    doc = ET.fromstring("<catalog>" + data1+'\n' + "</catalog>")

    [  print(itm.tag , itm.attrib['ItemID'], priInf.attrib['ShortDescription'] ) for  itmLst in doc  if itmLst is not None for itm in itmLst  if itm is not None for priInf in itm if priInf.tag =='PrimaryInformation' ]
    # for c in doc.find('ItemList'):
    #     # get_element_by_id('ItemList'):
    #     if c is not None:
    #         for gc in c :
    #             print(gc.tag , gc.attrib['ItemID'])
    # # doc = ET.fromstring(data1)
    # for child in doc:
    #     for gchild in child:
    #         print(gchild.tag, gchild.attrib['ItemID'])
    # # cat = ET.tostring(doc)
    # parser = ET.XMLParser(ns_clean=True)
    # tree = ET.parse(StringIO(cat), parser)
    # catalog = ET.parse(doc)
    # root = catalog.getroot()
    # for elem in root:
    #     print(elem)
    #
    # tree = ET.fromstring(match.group() + data)
    # catalogTree = ET.parse(file)

if __name__ == "__main__":
    dir = os.path.dirname(os.path.abspath(__file__))
    file = 'item_catalog.xml'
    # file = 'item_catalog.xml'

    filename = os.path.join(dir,file)

    parseXML(filename)

    try:

        arg_commad = sys.argv[1]
        parseXML(arg_commad)
    except IndexError:
        arg_commad = ''
