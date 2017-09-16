#!/bin/bash
# Go to ~/Shared/synchro
# Scan R1 Directory
# Search duplicate files into R2 Directory
# Delete duplicate files ONLY into R2 Directory

# Search duplicate files into only one directory
# find -not -empty -type f -printf "%s\n" | sort -rn | uniq -d | xargs -I{} -n1 find -type f -size {}c -print0 | xargs -0 md5sum| sort | uniq -w32 --all-repeated=separate | less

cd ~/Shared/synchro

echo "Scan size on R1"
time find R1 -not -empty -type f -printf "%s|%p\n" > R1_size_filename.txt

echo "Scan size on R2"
time find R2 -not -empty -type f -printf "%s|%p\n" > R2_size_filename.txt

echo "Search duplicate size"
cat R1_size_filename.txt | cut -d'|' -f1 | sort -u > R1_size.txt
cat R2_size_filename.txt | cut -d'|' -f1 | sort -u > R2_size.txt
join -j 1 R1_size.txt R2_size.txt > join_size.txt

echo "Search duplicate files on R1 and R2"
cat join_size.txt | sed 's/^\(.*\)$/^\1|/g' > join_size_grep.txt
grep -f join_size_grep.txt R1_size_filename.txt > R1_duplicates.txt
grep -f join_size_grep.txt R2_size_filename.txt > R2_duplicates.txt

echo "Compute md5sum for duplicate files on R1"
time cat R1_duplicates.txt | cut -d'|' -f2 | sort -u | xargs -d'\n' md5sum | sort | sed 's/^\([^ ]\{32\}\)  /\1|/g' > R1_md5.txt

echo "Compute md5sum for duplicate files on R2"
time cat R2_duplicates.txt | cut -d'|' -f2 |  sort -u | xargs -d'\n' md5sum | sort | sed 's/^\([^ ]\{32\}\)  /\1|/g' > R2_md5.txt

echo "----------"
echo "----------"
join -j 1 -t '|' -o 2.2 R1_md5.txt R2_md5.txt | grep -e '^R2/' | sort -u | xargs -d'\n' rm -v

echo "----------"
echo "----------"

echo "Check these files deeply"
cat R1_md5.txt R2_md5.txt | cut -d'/' -f2- | sort | uniq -d | sort -rn > check_deeply.txt

while read file
do
    if [ -s "R2/${file}" -a -s "R1/${file}"  ]
    then
        rm -v "R2/${file}"
    fi
done < check_deeply.txt

find R2/ -type d -empty -delete
mkdir R2
