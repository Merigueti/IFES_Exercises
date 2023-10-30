use std::io;

fn main(){

    println!("Escreva o Salário Bruto: ");

    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Falha ao Ler entrada!");

    let bruto: f64 = match input.trim().parse() {
        Ok(n) => n,
        Err(_) => {
            println!("Erro ao converter valor do Slário");
            return
        }
    };

    let ir = bruto*0.11;
    let inss = bruto*0.08;
    let sindicato = bruto*0.05;
    let liquido = bruto - ir - inss - sindicato;

    println!("\nSalário Bruto: R${}",bruto);
    println!("IR (11%): R${}",ir);
    println!("INSS (8%): R${}",inss);
    println!("Sindicato (5%): R${}",sindicato);
    println!("Salário Liquido: R${}",liquido);


}