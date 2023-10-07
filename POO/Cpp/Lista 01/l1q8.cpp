#include <iostream>

using namespace std;

int main() {
    float bruto;
    
    cout << "Escreva o Salário Bruto: R$";
    cin >> bruto;

    float ir = bruto * 0.11;
    float inss = bruto * 0.08;
    float sindicato = bruto * 0.05;
    float liquido = bruto - ir - inss - sindicato;

    cout << "\nSalário Bruto: R$" << bruto << endl;
    cout << "IR (11%): R$" << ir << endl;
    cout << "INSS (8%): R$" << inss << endl;
    cout << "Sindicato (5%): R$" << sindicato << endl;
    cout << "Salário Líquido: R$" << liquido << endl;

    return 0;
}
