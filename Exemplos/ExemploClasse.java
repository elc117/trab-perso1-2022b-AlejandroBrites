public class ExemploClasse {
    
}

public class Jogador {
  
  String nome, time, apelido, posicao;
  float salario;
  int camisa;
    
  public Jogador() {

    System.out.println("Jogador criado");
        
  }
    
  public Jogador(String nome, String time, String apelido, String posicao, int camisa, float salario) {
 
    this.nome = nome;
    this.time = time;
    this.apelido = apelido;
    this.posicao = posicao;
    this.camisa = camisa;
    this.salario = salario;
    System.out.println("Jogador criado");
        
  }
  
  public float calcularSalarioAnual () {  
    return (float) (this.salario*12.00);
  }
  
}
    
