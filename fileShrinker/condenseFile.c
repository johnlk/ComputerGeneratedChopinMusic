#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//void readFile(FILE*);
unsigned char *dat;

int main(int ac,char **av){

    FILE *fpi;
    int pr,siz,p;
    
    fpi=fopen(av[ac-1],"rb");
    
    if(!fpi){
        fprintf(stderr,"Couldn't open %s\n",av[ac-1]);
        exit(1);
    }
    
    fseek(fpi,0,SEEK_END);
    siz = ftell(fpi);
    rewind(fpi);
    
    if(pr>=1)
        printf("# File size %d byte%s\n",siz,siz==1?"":"s");
    dat = (unsigned char*)malloc(siz);
    if(!dat){
        fprintf(stderr,"Couldn't malloc %d bytes\n",siz);
        exit(1);
    }
    
    fread(dat,1,siz,fpi);
    
    p=0;
    
    fclose(fpi);
    
    //for loop with p
    
    printf("%c\n", &dat);
    
	return 0;
}

//void readFile(FILE* file){
//    char word[100];
//    while(fscanf(file, "%s", word) != EOF){
//        printf("%s\n", word);
//    }
//}
