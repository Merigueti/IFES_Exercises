use std::io;

fn main() {
    // Solicita ao usuário que insira um valor em segundos
    println!("Digite um valor em segundos:");
    
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Falha ao ler a linha");
    
    // Converte o valor digitado para um número inteiro
    let segundos: u64 = match input.trim().parse() {
        Ok(num) => num,
        Err(_) => {
            println!("Valor inválido. Por favor, insira um número válido.");
            return;
        }
    };
    
    // Calcula o tempo em horas, minutos e segundos
    let horas = segundos / 3600;
    let minutos = (segundos % 3600) / 60;
    let segundos_restantes = segundos % 60;
    
    // Imprime o resultado na tela
    println!(
        "{} segundos correspondem a {} horas, {} minutos e {} segundos",
        segundos, horas, minutos, segundos_restantes
    );
}
