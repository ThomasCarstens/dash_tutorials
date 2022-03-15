from imutils import paths
import argparse
import requests
import cv2
import os

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-l", "--latex", required=True,
	help="path to latex to fetch captions")
ap.add_argument("-o", "--html", required=True,
	help="path to html file to add captions")
args = vars(ap.parse_args())


# grab the list of URLs from the input file, then initialize the
# total number of images downloaded thus far
# cd /home/txa/Documents/portfolio/_includes/paper
# python3.9 /home/txa/Documents/portfolio/_includes/paper -u testbed.html -o testbed_edit.html

import codecs
latex = codecs.open(args["latex"], "r", "utf-8")

stagedfile=""

# <div class="img-container">
# <p><img src="../../assets/images/testbed/testbed_arch/virtual_pin.png" style="width:5.8cm" alt="image" /></p>
# <figcaption>Fig.1 - Trulli, Puglia, Italy.</figcaption>
# </div>

## STEP 1: stealing captions
list_of_captions = []
for each in latex.read().strip().split("caption{"):
    caption = each[:100].split("\\")[0].split("}")[0]
    list_of_captions.append(caption)
latex.close()

l = open(args["latex"], "r")
with open(args["latex"]) as f:
    mylist = list(f)
mynewlist=""
for line in mylist:
    # to_convert = line.replace("\Circle", "&#9673;").replace("\CIRCLE", "&#9678;")
    # to_convert = line.replace("\&\#9673;", "\"&#9673;\"").replace("\&\#9678;", "\"&#9678;\"")
    to_convert = line.replace("\CIRCLE", "\&\#9673;").replace("\Circle", "\&\#9678;")
    to_convert = to_convert.replace("\ding{51}", "TICK").replace("\ding{55}", "CROSS")

    mynewlist+=to_convert
l.close()

latex = open(args["latex"], "w")
latex.write(mynewlist)

import codecs
html = codecs.open(args["html"], "r", "utf-8")


sec_figcaption=html.read().strip().split("<figcaption aria-hidden=\"true\">image")
stagedfile=sec_figcaption[0]
print(len(list_of_captions))
list_of_captions = list_of_captions[1:]
for each in sec_figcaption[1:]:
    next = list_of_captions[::-1].pop()
    list_of_captions = list_of_captions[1:]
    each = "<figcaption>"+ next + each
    # print("NEXT \n", each)
    stagedfile+=each

stagedfile = stagedfile.replace("&amp;#9673;", "&#9673;").replace("&amp;#9678;", "&#9678;")
stagedfile = stagedfile.replace("TICK", "&#10003;").replace("CROSS", "	&#10060;")

split=stagedfile.split("<div class=\"minted\">")
exec_choreography="myswarm = swarmInterface(all_ids = [1,3,5])\nsm0 = myswarm.execTrajandOctogon (ids = [1,3], traj_shape = 8)\nmyswarm.start_sm_on_thread(sm0)"
stagedfile = stagedfile.replace("TICK", exec_choreography)


html.close()

o = args["html"]
f = open(o, "w")

f.write(stagedfile)

f.close()
# python3.9 -u /home/txa/Documents/portfolio/_includes/paper/testbed.html  -u /home/txa/Documents/portfolio/_includes/paper/testbed_edit.html


# initial_code = open(args["urls"]).read().strip().split("images/")
# print (initial_code)
# elements = initial_code.split("more words yada yada yada")