public class ExemploHeranca {
    
}

public class Pessoa {

  String nome, time;
  
  public Pessoa() {

    System.out.println("Pessoa criada");
        
  }
  
  public Pessoa(String nome, String time) {
      
    this.nome = nome;
    this.time = time;
    System.out.println("Pessoa criada");
      
  }
  
}

public class Jogador extends Pessoa {
  
  String apelido, posicao;
  float salario;
  int camisa;
    
  public Jogador() {

    System.out.println("Jogador criado");
        
  }
    
  public Jogador(String nome, String time, String apelido, String posicao, int camisa, float salario) {
  
    super (nome, time);
    this.apelido = apelido;
    this.posicao = posicao;
    this.camisa = camisa;
    this.salario = salario;
    System.out.println("Jogador criado");
        
  }
    
}

public class Tecnico extends Pessoa {

  float salario;
  
  public Tecnico() {

    System.out.println("Técnico criado");
        
  }
  
  public Tecnico(String nome, String time, float salario) {
  
    super (nome, time);
    this.salario = salario;
    System.out.println("Técnico criado");
      
  }
  
}

public class Torcedor extends Pessoa {
  
  public Torcedor() {

    System.out.println("Torcedor criado");
      
  }

  public Torcedor(String nome, String time) {

    super (nome, time);
    System.out.println("Torcedor criado");
    
  }

}