# Program to parse the xml files to find leaf GUI components
import xml.etree.ElementTree as ET

def find_xml_leaves(node):
    if len(node) == 0: 
        print("Leaf node:", node.tag)
    else:
        for child in node: 
            find_xml_leaves(child)

tree = ET.parse('/home/grenders95/software_engineering/csci535_intro_assignment/data/com.dropbox.android.xml')
root = tree.getroot()

find_xml_leaves(root)

