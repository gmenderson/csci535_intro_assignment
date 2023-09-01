import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw

# Load the XML hierarchy from a file
xml_file_path = "/home/grenders95/software_engineering/csci535_intro_assignment/data/com.yelp.android.xml"
tree = ET.parse(xml_file_path)
root = tree.getroot()

# Capture a screenshot of the app's UI (replace with your screenshot capturing logic)
screenshot = Image.open("/home/grenders95/software_engineering/csci535_intro_assignment/data/com.yelp.android.png")

# Create an ImageDraw object to annotate the screenshot
draw = ImageDraw.Draw(screenshot)

# Function to check if a node is a leaf node
def is_leaf(node):
    return len(list(node)) == 0

# Loop through the nodes in the XML hierarchy and highlight leaf components
for node in root.iter("node"):
    if is_leaf(node):
        bounds = node.get("bounds")
        try:
            left, top, right, bottom = map(int, bounds.strip("[]").split(","))
            draw.rectangle([left, top, right, bottom], outline="red", width=2)
        except ValueError:
            print(f"Skipping node with invalid bounds: {bounds}")

# Save or display the annotated screenshot
screenshot.show()
#screenshot.save("annotated_screenshot.png")

