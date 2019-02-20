import os
import re
import xml.etree.ElementTree as etree
from lxml import etree as ET
import sys
import pathlib

def get_item(file):


    file1 = file
    data = b'<root>' + file1.read_bytes() + b'</root>'
    print(data)
    doc = ET.fromstring(data)
    # ET.findall
    # ET.finall('group')

def splitXML(file):

    with open (file ) as in_fh:
        n = 0
        out_fh = None

        while True:
            line = in_fh.readline()
            if not line: break

            if line.startswith('<?xml'):
                if out_fh:
                    out_fh.close()
                n += 1
                out_fh = open('myfile_{:02}.txt'.format(n),'w')

            out_fh.write(line)

        out_fh.close()

def get_item(tag, attr):

    with open("result.csv", "w") as resultfile:
        for result in [txt for txt in os.listdir(os.getcwd()) if txt.endswith(".txt")]:
            item_cat = ET.parse(result)
            root = item_cat.getroot()
            found = [element.attrib[attr] for element in root.iter() if element.tag == tag]
            print(item_cat.xpath('//ItemList/Item/@ItemID')[0])
            print(item_cat.xpath('//element[text()="A"]')[0].tag)
            # print(found[0].text)
            if found:
                resultfile.write(found[0]+'\n')

            # if 'LZY_201_335_R10A01' and 'LZY_201_186_R5U01' in open(result).read():
            #     resultfile.write('Current MW in node is {1}'.format(result[:-4]))
            # else:
            #     resultfile.write('NOT {0}'.format(result[:-4]))





if __name__ == "__main__":
    dir = os.path.dirname(os.path.abspath(__file__))
    # file = 'item.xml'
    file = 'item.xml'


    filename = os.path.join(dir,file)
    # get_item(file)
    splitXML(filename)
    get_item('PrimaryInformation', 'Description')

    try:

        arg_commad = sys.argv[1]
        splitXML(arg_commad)
    except IndexError:
        arg_commad = ''