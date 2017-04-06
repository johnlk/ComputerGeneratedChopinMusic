function compress(){

	var textArea = document.getElementById('toCompress');
	var rawText = textArea.value.split('\n');
	var blockCounter = 0;

	var compressedText = [];

	for(var i = 0; i < rawText.length; i++){
		if(i === 0 || (rawText[i].split(" ").indexOf("Text") === -1 && rawText[i].split(" ").indexOf("End") === -1
					 && rawText[i].split(" ").indexOf("BA") !== -1)){
			var line = "";
			var count = 0;//want to get rid of the first three bits of text per line
			for(var j = 0; j < rawText[i].split(" ").length; j++){
				if(rawText[i].split(" ")[j] != ""){
					if(i === 0 || count >= 3){
						line += rawText[i].split(" ")[j] + " ";
					}					
					count++;
				}
			}
			compressedText.push(line.trim());
		}else if(rawText[i] == ""){
			compressedText.push("");
			blockCounter++;
		}
	}

	textArea.value = compressedText.join("\n");

}