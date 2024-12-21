for fileName in ./*.txt; do
	cat "$fileName" >> "input.txt";
done