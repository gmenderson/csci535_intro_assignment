from PIL import Image, ImageDraw
import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('/home/grenders95/software_engineering/csci535_intro_assignment/data/com.giphy.messenger-1.xml')
root = tree.getroot()

# Function to recursively find all leaf nodes
def find_leaf_nodes(node, leaf_nodes):
    children = list(node)
    if not children:
        leaf_nodes.append(node)
    else:
        for child in children:
            find_leaf_nodes(child, leaf_nodes)

# Initialize a list to store leaf nodes
leaf_nodes = []

# Start the search for leaf nodes from the root node
find_leaf_nodes(root, leaf_nodes)

# Load the existing screenshot image
screenshot = Image.open('/home/grenders95/software_engineering/csci535_intro_assignment/data/com.giphy.messenger-1.png')
draw = ImageDraw.Draw(screenshot)

# Iterate through the leaf nodes, extract bounds, and draw bounding boxes
for node in leaf_nodes:
    bounds = node.get('bounds').strip('[]').split('][')
    left, top = map(int, bounds[0].split(','))
    right, bottom = map(int, bounds[1].split(','))
    draw.rectangle([left, top, right, bottom], outline="yellow", width=3)

# Save the modified image with bounding boxes
screenshot.save('screenshot_with_boxes.png', 'PNG')
