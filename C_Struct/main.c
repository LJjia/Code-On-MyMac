#include <stdio.h>



typedef struct{
    int w;
    int h;
    int num;
    float score;
}INFO;
int main(int argc,char *argv[])
{
    FILE* pFile=0;
    INFO stInfo;
    pFile=fopen("tmp.bin","w");
    stInfo.w=1;
    stInfo.h=2;
    stInfo.num=5;
    stInfo.score=0.6;
    fwrite(&stInfo,sizeof(stInfo),1,pFile);
    fclose(pFile);
    return 0;

}
