#include <iostream>

using namespace std;

int main() {
    float f;
    cout << "Escreva o valor em Fahrenheit: ";
    cin >> f;

    float c = (5*(f-32))/9;
    cout << "o valor em Celsius é " << c << endl;

    return 0;
}
