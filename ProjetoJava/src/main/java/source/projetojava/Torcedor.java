package source.projetojava;

/**
 *
 * @author alejb
 */
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
