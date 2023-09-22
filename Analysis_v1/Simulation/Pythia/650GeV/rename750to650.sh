#for f in *.py; do cat $f; done

for file in *750*.py; do
    newname="${file/750/650}"
    mv "$file" "$newname"
done
