'''
Parse XML document and read data lines.
'''
import sys
import os
from lxml import etree


output_file = open(sys.argv[1],'w')
for root, dirs, files in os.walk("."):
    for filename in files:                      # read all the files in the current directory
        if filename.endswith('.xml.gz'):            # choose the .gz files
            tree = etree.parse(filename)        # parsing the data from the files
            root = tree.getroot()               # start traversing from root node
            for child in root:
                if child.get('type') == 'story':    # Get child nodes of type story
                    for sub_child in child:
                        if sub_child.tag == 'TEXT':
                            for p_tags in sub_child:        # Read non-empty paragraphs
                                if type(p_tags.text) == str:
                                    output_file.write(p_tags.text)          # Write data to the output text file
                                output_file.write('\n')


# Display 100 output lines on console
output_file = open(sys.argv[1], 'r')
for i in range(0,99):
    print(output_file.readline())

output_file.close()





