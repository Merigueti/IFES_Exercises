use std::io;

fn main() {
    println!("Escreva o valor em Fahrenheit");

    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Falha ao ler a linha");
    match input.trim().parse::<f64>() {
        Ok(f) => {
            println!("Valor em C: {}", (5.0 * (f - 32.0)) / 9.0);
        }
        Err(_) => {
            println!("Valor inválido!");
        }
    }

    return

}