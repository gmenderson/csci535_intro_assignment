import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw

# Parse the XML file
xml_file = '/home/grenders95/software_engineering/csci535_intro_assignment/data/com.dropbox.android.xml'
tree = ET.parse(xml_file)
root = tree.getroot()

