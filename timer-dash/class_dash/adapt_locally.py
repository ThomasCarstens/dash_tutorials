from imutils import paths
import argparse
import requests
import cv2
import os

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-u", "--urls", required=True,
	help="path to file containing image URLs")
ap.add_argument("-o", "--output", required=True,
	help="path to output directory of images")
args = vars(ap.parse_args())
# grab the list of URLs from the input file, then initialize the
# total number of images downloaded thus far
# cd /home/txa/Documents/portfolio/_includes/paper
# python3.9 /home/txa/Documents/portfolio/_includes/paper -u testbed.html -o testbed_edit.html

import codecs
file = codecs.open(args["urls"], "r", "utf-8")


centerstyle= "<style>\n.img-container {\ntext-align: center;\n}\n</style>"
rowstyle= "<style>\n.row {\nmargin-left:-5px;\nmargin-right:-5px;\n}\n</style>"
columnstyle= "<style>\n.column {\nfloat: left;\nwidth: 50%;\npadding: 5px;\n}\n</style>"
allstyles=centerstyle+rowstyle+columnstyle

# <div class="img-container">
# <p><img src="../../assets/images/testbed/testbed_arch/virtual_pin.png" style="width:5.8cm" alt="image" /></p>
# <figcaption>Fig.1 - Trulli, Puglia, Italy.</figcaption>
# </div>
html = file.read().strip().split("images/")
stagedfile=html[0]

## STEP 1: correct relative path to images + center images + add caption
for each in html[1:]:
    filename="../../assets/images/"+each
    stagedfile+=filename
    
stagedfile=allstyles+stagedfile


#center images:
stagedfile=stagedfile.replace("figure*","img-container").replace("<figure>","").replace("</figure>","").replace("marginfigure","img-container")
# print(each)

# imagefile = codecs.open("/home/txa/Documents/portfolio/_includes/paper/testbed.html", "r", "utf-8")
# pandoc 02_project1.tex -o ../_includes/paper/testbed.html -f latex+table_captions  --bibliography main.bib 
## STEP 2: correct author citation for in-text bibliography
# data-cites

sec_datacite= stagedfile.split("data-cites=\"")
finalfile=sec_datacite[0]

for each in sec_datacite[1:]:
	author = each[:100].split("\"")[0]
	filename= each[:-23] + "{% cite "+ author + "%}" + each[-23:]+"data-cites=\""
	finalfile+=filename


## STEP 3: code
## html doesn't format right. Maybe fix this a lvl above.

# <!-- <div class="figure*">
# <div class="minted"> -->

# ```
#     <launch>
#         <group>
#             <remap from='_goTo' to='drone1_goTo'/>
#             <node name='drone1' pkg='crazyswarm' type='ros_action_server.py'>
#             </node>
#         </group>

#         <group>
#             ...
#         </group>

#     </launch>       
# ```

# <p>And so on for drone2, drone3...</p> 

o = args["output"]
f = open(o, "w")

f.write(finalfile)
f.close()
# python3.9 -u /home/txa/Documents/portfolio/_includes/paper/testbed.html  -u /home/txa/Documents/portfolio/_includes/paper/testbed_edit.html


# initial_code = open(args["urls"]).read().strip().split("images/")
# print (initial_code)
# elements = initial_code.split("more words yada yada yada")