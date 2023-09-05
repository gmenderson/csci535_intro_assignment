# csci535_intro_assignment
Repository for CSCI 535 introductory assignment

To compile and run this code, first clone the repository in your desired directory. Create a Python venv and activate it. Navigate to the src directory, where you should use the command "pip install -r requirements.txt" to install the required library. Once this is done, you can invoke the main script with the command "python parser.py". Be sure to know the absolute paths for the XML/PNG files you want to use in the annotation, as these will be asked in the parser.py script. Newly generated annotated images can be found in the /annotated_images directory under data. 

<ins>Explaination</ins>

I will briefly provide an explaination for the parser.py source code. Starting with the libraries used, Pillow was chosen as the image processing tool because it is simple and fast, an ideal tool for annotating simple images. Xml.etree.ElementTree was chosen to parse the xml files because it is a built in python module fore parsing XML files. Sys and os were used for behind the scenes operations such as generating file paths and exiting the script. 

Moving on to the functions, parse_xml is a simple function that parses an existing XML file and returns the root of the element tree. The find_leaf_nodes recursively searches the XML tree for leaf node. It stores a list of the bounds parameters for each leaf node. The annotate_png function is used to draw a rectangles on the leaf components on the screenshot PNG file, corresponding to the bounds of leaf components obtained from the XML. This image is then saved to the annotated_images directory. 

Because parser.py is a relatively small and simple program, I decided to contain the functions and main in the same file. The main function asks for the paths of the XML/PNG pairs and the name of the new image. It the annotates and saves the image in /annotated_images. The user can then choose to loop the main function with a different XML/PNG pair. Users can also exit the program if desired.
