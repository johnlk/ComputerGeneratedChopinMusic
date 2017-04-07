for fileName in ./*.txt; do
	cat "$fileName" >> "congregatedFiles.txt";
done