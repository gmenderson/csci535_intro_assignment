from PIL import Image, ImageDraw
import xml.etree.ElementTree as ET
import sys
import os

# Function to parse the XML file and return the root of the tree
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
def annotate_png(png_file, annotated_png, leaf_nodes): 
    png = Image.open(png_file)
    draw = ImageDraw.Draw(png)

    # Extract each bound value from leaf elemenets
    for bounds in leaf_nodes: 
        values = bounds.split('][')
        pair1 = values[0].strip('[]').split(',')
        pair2 = values[1].strip('[]').split(',')
        x1 = int(pair1[0])
        y1 = int(pair1[1])
        x2 = int(pair2[0])
        y2 = int(pair2[1])
        draw.rectangle([x1, y1, x2, y2], outline="yellow", width=4)

    # Qualify the path of the dir where the annotated images are to be saved, and save the new image
    script_directory = os.path.dirname(os.path.realpath(__file__))
    annotated_dir = os.path.join(script_directory, "..", "data", "annotated_images")
    annotated_png_path = os.path.join(annotated_dir, annotated_png)
    png.save(annotated_png_path)
    print("Annotated image saved in current directory.")

# Main Function 
if __name__ == "__main__":
    while True: 
        # Obtain path of the XML/PNG pair, let the user specify name of the annotated image
        print("Enter the path of the XML file to parse:")
        xml_file = input()
        print("Enter the path of the PNG file to be annotated:")
        png_file = input()
        print("Enter the desired name of the new annotated image")
        annotated_png_file = input()
        
        # Find root of the XML tree
        root = parse_xml(xml_file)

        # Create an empty list for storing leaf nodes
        leaf_nodes = []
        find_leaf_nodes(root, leaf_nodes)

        # Annotate the PNG screenshot and save the new image
        annotate_png(png_file, annotated_png_file, leaf_nodes)

        # Reenter main loop, exit, or error handling
        while True: 
            print("Enter (y) to continue with another XML/PNG pair, or (n) to exit the program:")
            answer = input()

            if answer == 'y' or answer == 'Y': 
                break
            elif answer == 'n' or answer == 'N': 
                sys.exit(0)
            else: 
                print("Invalid input.")
                continue