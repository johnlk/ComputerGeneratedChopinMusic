function decompress() {
	/*
	This function decompresses MIDI text files by:
	1. Taking compressed text from a textarea
	2. For each line:
		- If empty line: Adds newline and increments section counter
		- If not a format line: Adds back "BA {section} CR" prefix
		- If format line: Keeps as-is
	3. Adds format header at start
	4. Adds end of track marker at end
	5. Updates textarea with decompressed text
	*/

	const textField = document.getElementById('toDecompress');
	let expandedText = '';
	let sectionCounter = 1;
	const rawText = textField.value.split('\n');

	for (const line of rawText) {
		if (line.length === 0) {
			expandedText += '\n';
			sectionCounter++;
		} else if (!line.includes('format')) {
			expandedText += `BA ${sectionCounter} CR ${line}\n`;
		} else {
			expandedText += `${line}\n`;
		}
	}

	// Add header and footer
	expandedText = `format=1 tracks=7 division=480\n\n${expandedText}`;
	expandedText += `BA ${sectionCounter} CR 0 TR 0 CH 16 End of track`;
	
	textField.value = expandedText;
}
