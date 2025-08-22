#include <iostream>
#include <string.h>
using namespace std;

int main(){
	char A[10], B[10], C[10];
	int mai = 0, min = 0, vogais = 0, i;
	
	cout<<"Digite uma string: "<<endl;
	gets(A);
	cout<<"Digite outra string: "<<endl;
	gets(B);
	
	if(strlen(A) > strlen(B)){
		cout<<"A string A eh maior"<<endl;
	}
	else if(strlen(A) == strlen(B)){
		cout<<"As duas strings tem o mesmo tamanho"<<endl;
	}
	else{
		cout<<"A string B eh maior"<<endl;
	}
	
	cout<<"Digite outra string"<<endl;
	gets(C);
	
	for(i=0; i<strlen(C); i++){
		char c = C[i];
		if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'){
			vogais = vogais + 1;
			min = min + 1;
		}
			if(c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U'){
				vogais = vogais + 1;
				mai = mai + 1;
			}
	}
	
	cout<<"A string C eh: "<<C<<endl;
	cout<<"Quantidade de vogais: "<<vogais<<endl;
	cout<<"Quantidade de letras maiusculas: "<<mai<<endl;
	cout<<"Quantidade de letras minusculas: "<<min<<endl;
	
	return 0;
}
