function decompress(){

	var textField = document.getElementById('toDecompress');
	var expandedText = "";

	var sectionCounter = 1;
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

	expandedText += "BA " + sectionCounter + " CR 0 TR 0 CH 16 End of track"; //adds a flag for end of music

	expandedText = "format=1 tracks=7 division=480\n\n" + expandedText;
	
	textField.value = expandedText;

}
