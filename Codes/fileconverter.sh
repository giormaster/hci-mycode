#!/bin/bash

indir=./
outdir=./results

mkdir -p $outdir

read -p "Enter Filename:" input_file

echo "Select Format:"
echo "1) HTML"
echo "2) MICROSOFT WORD"

read -p "Enter format number: " output_format

for f in $indir/*.md
do
  elif [[ "$output_format" == "1" ]]; then
    pandoc $f -s -o $outdir/$(basename $f .md).html  --quiet
  elif [[ "$output_format" == "2" ]]; then
    pandoc $f -s -o $outdir/$(basename $f .md).docx --extract-media=.
  else
    echo "Error"
    exit 1
  fi
done
