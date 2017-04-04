function compress(){

	var textArea = document.getElementById('toCompress');
	var rawText = textArea.value.split('\n');
	var blockCounter = 1;

	var compressedText = ["balls", "man", "", "balls"];

	for(var i = 0; i < rawText.length; i++){
		console.log(rawText[i]);
	}


	textArea.value = compressedText.join("\n");

}