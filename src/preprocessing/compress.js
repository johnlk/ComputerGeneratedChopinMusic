function compress() {
	/*
	This function compresses MIDI text files by:
	1. Taking input from a textarea
	2. Skipping the first 2 lines (format lines)
	3. For each remaining line:
		- If it contains "BA" but not "Text" or "End":
			- Removes the first 3 tokens (BA, section number, CR)
			- Keeps the rest of the line
		- If it's an empty line:
			- Keeps it as a section separator
			- Increments block counter
	4. Joins the compressed lines back together
	5. Updates the textarea with compressed text
	*/

	const textArea = document.getElementById('toCompress');
	const lines = textArea.value.split('\n');
	let blockCounter = 0;
	const compressedText = [];

	// Skip first 2 format lines
	for (let i = 2; i < lines.length; i++) {
		const line = lines[i];
		const tokens = line.split(' ');

		if (line === '') {
			compressedText.push('');
			blockCounter++;
			continue;
		}

		const isBALine = tokens.indexOf('BA') !== -1;
		const hasText = tokens.indexOf('Text') !== -1;
		const hasEnd = tokens.indexOf('End') !== -1;

		if (isBALine && !hasText && !hasEnd) {
			// Skip first 3 tokens (BA, section number, CR) and join remaining
			const processedLine = tokens
				.slice(3)
				.filter(token => token !== '')
				.join(' ');
			compressedText.push(processedLine);
		}
	}

	textArea.value = compressedText.join('\n');
}