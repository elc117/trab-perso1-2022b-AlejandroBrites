package source.projetojava;

/**
 *
 * @author alejb
 */
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
