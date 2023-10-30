use std::io;

fn main () {
    let mut input = String::new();
    println!("Escreva a nota 1: ");
    io::stdin().read_line(&mut input).expect("Erro ao ler linha!");
    let n1: f32 = match input.trim().parse() {
        Ok(n) => n,
        Err(_) => {
            println!("Erro ao converter Nota 1");
            return
        }
    };

    input = String::new();
    println!("Escreva a nota 2: ");
    io::stdin().read_line(&mut input).expect("Erro ao ler linha!");
    let n2: f32 = match input.trim().parse() {
        Ok(n) => n,
        Err(_) => {
            println!("Erro ao converte Nota 2");
            return
        }
    };

    let media = (n1+n2)/2.0;

    if media >= 9.5 {
        println!("Aprovado com Distinção");
    }
    else if media >= 7.0{
        println!("Aprovado");
    }
    else{
        println!("Reprovado");
    }

}