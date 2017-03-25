#include <stdio.h>
#include <string.h>

void readFile(FILE*);

int main(){

	FILE *fp = fopen("./test.txt", "r");
	if(fp){
		readFile(fp);
	}
	fclose(fp);

	printf("%s\n", "you suck");
	return 0;
}

void readFile(FILE* file){
	char line[200];
	while(!feof(file)){
		fscanf(file, "%s", word);
		printf("%s\n", line);
	}
}