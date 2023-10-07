#include <iostream>

using namespace std;

int main() {
    float n1, n2;
    cout << "Escreva a nota 01: ";
    cin >> n1;

    cout << "Escreva a nota 02: ";
    cin >> n2;

    float media = (n1+n2)/2;
    cout << "Media = " << media << endl;

    if (media >= 9.5){
        cout << "Aprovado com Distinção" << endl;
    }else if (media >= 7){
        cout << "Aprovado" << endl;
    }else{
        cout << "Reprovado" << endl; 
    }

    return 0;
}
