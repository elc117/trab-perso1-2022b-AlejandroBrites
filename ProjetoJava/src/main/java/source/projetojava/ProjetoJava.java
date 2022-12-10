package source.projetojava;

/**
 *
 * @author alejb
 */
public class ProjetoJava {

    public static void main(String[] args) {
        
        Pessoa p1 = new Pessoa("Roberto", "Barcelona");
        Jogador j1 = new Jogador("Neymar", "Brasil", "atacante", 10, 23000000);
        Torcedor T1 = new Torcedor("Bruno", "Internacional");
        Tecnico t1 = new Tecnico("Tite", "Brasil", 1650000);
        
        p1.apresentacao();
        j1.apresentacao();
        T1.apresentacao();
        t1.apresentacao();
        
        System.out.println("O salário de " + j1.getNome() + " é cerca de " + j1.calcularSalarioAnual() + " por ano");
        System.out.println("O salário de " + t1.getNome() + " é cerca de " + t1.calcularSalarioAnual() +  " por ano");
    }
}
