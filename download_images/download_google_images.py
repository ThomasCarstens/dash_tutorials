# import the necessary packages
from imutils import paths
import argparse
import requests
import cv2
import os


## JS IN-BROWSER INJECT
# urls = Array.from(document.querySelectorAll('.rg_i'))

#     var arr = [];
#     for (var i = 0 in urls) {
#         var a = urls[i].src;
#         if (a.includes('https')) {
#             arr.push(a);
#             }

#     }

#     window.open('data:text/csv;charset=utf-8,' + escape(arr.join('\n')));

## DOWNLOAD LOCALLY
# python3.9 download_google_images.py -u download.csv -o pics

# # construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-u", "--urls", required=True,
# 	help="path to file containing image URLs")
# ap.add_argument("-o", "--output", required=True,
# 	help="path to output directory of images")
# args = vars(ap.parse_args())
# # grab the list of URLs from the input file, then initialize the
# # total number of images downloaded thus far
# rows = open(args["urls"]).read().strip().split("\n")
# total = 0

# # loop the URLs
# for url in rows:
# 	try:
# 		# try to download the image
# 		r = requests.get(url, timeout=60)
# 		# save the image to disk
# 		p = os.path.sep.join([args["output"], "{}.jpg".format(
# 			str(total).zfill(8))])
# 		f = open(p, "wb")
# 		f.write(r.content)
# 		f.close()
# 		# update the counter
# 		print("[INFO] downloaded: {}".format(p))
# 		total += 1
# 	# handle if any exceptions are thrown during the download process
# 	except:
# 		print("[INFO] error downloading {}...skipping".format(p))

# EDIT html OUTPUT		
#pandoc 02_project1.tex -o ../_includes/paper/testbed.html --bibliography main.bib 


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
# python3.9 download_google_images.py testbed.html testbed_edit.html

import codecs
file = codecs.open(args["urls"], "r", "utf-8")

stagedfile=file.read().strip().split("images/")[0]


## STEP 1: correct relative path to images
for each in file.read().strip().split("images/")[1:]:
	filename="../../assets/images/"+each
	stagedfile+=filename

# imagefile = codecs.open("/home/txa/Documents/portfolio/_includes/paper/testbed.html", "r", "utf-8")

## STEP 2: correct author citation for in-text bibliography
# data-cites
finalfile=""

for each in stagedfile.split("data-cites=\""):
	# print(each[-100:-23])
	author = each[:100].split("\"")[0]
	filename= each[:-23] + "{% cite "+ author + "%}" + each[-23:]+"data-cites=\""
	finalfile+=filename

o = args["output"]
f = open(o, "w")

f.write(finalfile)
f.close()
# python3.9 -u /home/txa/Documents/portfolio/_includes/paper/testbed.html  -u /home/txa/Documents/portfolio/_includes/paper/testbed_edit.html


# initial_code = open(args["urls"]).read().strip().split("images/")
# print (initial_code)
# elements = initial_code.split("more words yada yada yada")