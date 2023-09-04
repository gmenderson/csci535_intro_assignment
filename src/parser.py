from PIL import Image, ImageDraw
import xml.etree.ElementTree as ET

# Function to parse the XML file
def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    return root

# Function to recursively find all leaf nodes
def find_leaf_nodes(node, leaf_nodes):
    if len(node) == 0: 
        if 'bounds' in node.attrib:
            leaf_nodes.append(node.attrib['bounds'])
    else:
        for child in node: 
            find_leaf_nodes(child, leaf_nodes) 

# Function to annotate a PNG file
def annotate_png(png_file): 
     print("test")

if __name__ == "__main__":
    print("Enter the path of the XML file to parse:")
    xml_file = input()
    print("Enter the path of the PNG file to be annotated:")
    png_file = input()
    
    root = parse_xml(xml_file)

    leaf_nodes = []
    find_leaf_nodes(root, leaf_nodes)

    png = Image.open(png_file)
    