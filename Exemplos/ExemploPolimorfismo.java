public class ExemploPolimorfismo {
    
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
  
  public void apresentacao () {
      
    System.out.println(this.nome + " é uma pessoa que gosta do time " + this.time + ".");
    
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
  
  @Override
  public void apresentacao () {
      
    System.out.println(this.nome + " é o jogador camisa " + this.camisa + " do time " + this.time + ".");
    
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
  
  @Override
  public void apresentacao () {
      
    System.out.println(this.nome + " é o técnico do time " + this.time + ".");
    
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
  
  @Override
  public void apresentacao () {
      
    System.out.println(this.nome + " é um torcedor do time " + this.time + ".");
    
  }

}
