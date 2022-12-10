package source.projetojava;

/**
 *
 * @author alejb
 */
public class Pessoa {

  String nome, time;
  
  public Pessoa() {
        
  }
  
  public Pessoa(String nome, String time) {
      
    this.nome = nome;
    this.time = time;
      
  }

  public void apresentacao () {
      
    System.out.println(this.nome + " é uma pessoa que gosta do time " + this.time + ".");
    
  }
  
  public void setNome(String nome) {
    this.nome = nome;
  }

  public String getNome() {
    return this.nome;
  }

  public void setTime(String time) {
    this.time = time;
  }

  public String getTime() {
    return this.time;
  }
  
}