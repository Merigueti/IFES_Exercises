#include <iostream>

using namespace std;

int main() {
    int valor_em_segundos;
    cout << "Escreva um valor em segundos:";
    cin >> valor_em_segundos;

    int horas = valor_em_segundos / (60 * 60);  // Verifica a quantidade de horas
    int segundos = valor_em_segundos % (60 * 60);  // Pega o restante de segundos
    int minutos = segundos / 60;  // Converte o restante em minutos
    segundos = segundos % 60;  // Pega o restante de segundos novamente

    cout << valor_em_segundos << " segundos possuem " << horas << " horas, " << minutos << " minutos e " << segundos << " segundos" << endl;

    return 0;
}
