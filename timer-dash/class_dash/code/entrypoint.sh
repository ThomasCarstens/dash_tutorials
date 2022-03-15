#!/bin/bash
echo "test\n"
cd src
for include in $(cat ../includes.txt); do
    printf "Parsing $include\n"
    pandoc $include.tex -o ../_includes/paper/$include.html --bibliography main.bib #--pdf-engine=xelatex
    # python ../update-citations.py ../_includes/paper/$include.html
done

# # Also render the updated PDF
# pandoc -s 00-abstract-resume.tex -o "00-abstract-resume.pdf" --pdf-engine=xelatex  --bibliography main.bib --citeproc

# Fix permissions
cd ..
chmod 0777 _includes/*
echo "Files generated:"
ls _includes/paper