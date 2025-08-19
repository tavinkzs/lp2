#include <iostream>
#include <string.h>
using namespace std;

int main(){
    char str[100], str2[100];
    
    cout<<"Digite uma string"<<endl;
    gets(str);
    cout<<"Digite outra string"<<endl;
    gets(str2);
    
    if(strcmp(str, str2) != 0){
        cout<<"São diferentes"<<endl;
        
        if(strlen(str) > strlen(str2)){
            cout<<"A primeira string é maior em comprimento"<<endl;
        }
        else if(strlen(str) < strlen(str2)){
            cout<<"A segunda string é maior em comprimento"<<endl;
        }
        else{
            cout<<"As duas têm o mesmo comprimento"<<endl;
        }
    }
    else{
        cout<<"São iguais"<<endl;
    }
    return 0;
}
