package source.projetojava;

/**
 *
 * @author alejb
 */
public class Jogador extends Pessoa {
  
  String posicao;
  float salario;
  int camisa;
    
  public Jogador() {

    System.out.println("Jogador criado");
        
  }
    
  public Jogador(String nome, String time, String posicao, int camisa, float salario) {
  
    super (nome, time);
    this.posicao = posicao;
    this.camisa = camisa;
    this.salario = salario;
    System.out.println("Jogador criado");
        
  }

  @Override
  public void apresentacao () {
      
    System.out.println(this.nome + " é o jogador camisa " + this.camisa + " do time " + this.time + ".");
    
  }

  public void setPosicao(String posicao) {
    this.posicao = posicao;
  }

  public String getPosicao() {
    return this.posicao;
  }

  public void setCamisa(int camisa) {
    this.camisa = camisa;
  }

  public int getCamisa() {
    return this.camisa;
  }

  public void setSalario(float salario) {
    this.salario = salario;
  }
  
  public float getSalario() {
    return this.salario;
  }
  
  public float calcularSalarioAnual () {  
    return (float) (this.salario*12.00);
  }
    
}
