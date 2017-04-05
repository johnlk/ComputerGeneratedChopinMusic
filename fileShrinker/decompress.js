function decompress(){

	var textField = document.getElementById('toDecompress');
	var expandedText = "";

	var sectionCounter = 0;
	var rawText = textField.value.split("\n");
	
	for(var i = 0; i < rawText.length; i++){
		if(rawText[i].length == 0){
			expandedText += "\n";
			sectionCounter++;
		}else if(rawText[i].indexOf("format") == -1){
			expandedText += "BA " + sectionCounter + " CR " + rawText[i] + "\n";
		}else{
			expandedText += rawText[i] + "\n";
		}
	}

	//console.log(textField.value);
	
	textField.value = expandedText;

}
