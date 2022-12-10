# Java vs Python


## Objetivos

Comparar as linguagens de programação Java e Python e analisar as diferenças existentes entre a Programação Orientada a Objetos dessas duas linguagens de programação.


### Criando uma Classe/Construtor/Métodos

Uma classe é uma maneira de definir um tipo de dado, sendo que esse tipo de dado é composto por dados, que são denominados “atributos” e por comportamentos que são denominados "métodos''.

Para comparar o modo de criação de uma classe nas linguagens Java e Python iremos analisar 3 partes que constituem uma classe: os atributos, o construtor e os métodos da classe.

Para exemplificar a situação serão usados os códigos “ExemploClasse.java” e “ExemploClasse.py” que se referem a criação de uma classe nas linguagens Java e Python, respectivamente.

``` Java
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

```

```Python

class Jogador:

    def __init__(self, nome, time, apelido, posicao, camisa, salario):
        self.__nome = nome
        self.__time = time
        self.__apelido = apelido
        self.__posicao = posicao
        self.__camisa = camisa
        self.__salario = salario
        print("Jogador Criado")

    def calcularSalrioAnual (self):
        return self.__salario*12


```

### Atributos de uma Classe

A primeira diferença a ser observada comparando a criação de uma classe é a declaração dos atributos da classe.

Na linguagem Java ao se criar uma classe é necessário definir os atributos da classe junto com seus respectivos tipos e visibilidade.

Já na linguagem Python essa definição de atributo não é necessária, já que os atributos da classe são definidos no próprio construtor da classe juntamente com sua visibilidade.

Enquanto na linguagem Java é necessário definir os atributos da classe juntamente com seus respectivos tipos e visibilidade na linguagem Python isso não é necessário, fazendo com que a linguagem Python nesse aspecto seja um pouco mais simples em comparação a linguagem Java.

### Construtor de uma Classe

Analisando o construtor de uma classe em Java e em Python podem ser observados muitas similaridades, entretanto ainda assim existem algumas diferenças.

O construtor de uma classe em Java é identificado por ser um método da classe que possui o mesmo nome da classe, no caso de exemplo se trata do método “Jogador”, já em Python o construtor de uma classe será identificado pelo método “def __init__”.

Outra diferença que ocorre na criação do construtor de uma classe usando linguagem Python é o fato de que nessa linguagem no construtor da classe são definidas a visibilidade de cada atributo da classe.

Abaixo se encontra a equivalência de visibilidade entre Python e Java, junto com as definições de cada tipo de visibilidade.

Python | Java
-------|----------
self.atributo | public atributo
self._atributo | protected atributo
self.__atributo | private atributo

### Public

Os atributos com visibilidade “public” podem ser acessados por qualquer classe.

### Private

Os atributos “private” podem ser acessados apenas pelos métodos da própria classe a qual pertence

### Protected

Os atributos “protected” podem ser acessados pela própria classe e pelas classes filhas da classe à qual pertencem.


Para finalizar, outra diferença existente entre as linguagens Java e Python é que na linguagem Python é possível existir apenas um construtor na classe, enquanto na linguagem Java é possível ter múltiplos construtores em uma mesma classe, podendo isso ser considerado uma desvantagem da linguagem Python.

### Métodos de uma Classe

Quando se trata de um método de uma classe, ambas as linguagens se assemelham muito.

A maior diferença existente é que na linguagem Python não é necessário definir o tipo da variável de retorno de um método, como ocorre na linguagem Java, mostrando novamente a simplicidade da linguagem Python.


### Encapsulamento

O Encapsulamento é um conceito de Programação Orientada a Objetos que consiste em separar o código em objetos que possuem seus próprios métodos e atributos.

Tanto a linguagem Java quanto a linguagem Python seguem esse recurso sendo possível definir atributos e métodos em uma mesma classe, apesar de existirem as diferenças mencionadas acima no tópico “Classe/Contrutor/Métodos”.

Para exemplificar usaremos o último exemplo mencionado, novamente, que se trata de uma uma classe que possui atributos e um método tudo encapsulado em uma classe única sendo possível criar diversos objetos a partir dessa classe, com esses objetos possuindo os mesmos atributos e mesmos métodos.

``` Java
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

```

```Python

class Jogador:

    def __init__(self, nome, time, apelido, posicao, camisa, salario):
        self.__nome = nome
        self.__time = time
        self.__apelido = apelido
        self.__posicao = posicao
        self.__camisa = camisa
        self.__salario = salario
        print("Jogador Criado")

    def calcularSalrioAnual (self):
        return self.__salario*12


```

### Herança

Outro conceito muito importante na Programação Orientada a Objetos é o conceito de Herança que consiste na capacidade de uma classe “filha” herdar os atributos e métodos de uma classe “mãe”.

Abaixo está um exemplo de herança nas linguagens Java e Python

Agora vejamos algumas diferenças existentes entre a herança na linguagem Java e Python.

Na declaração de uma classe “filha”, na linguagem Java, é utilizada a palavra-chave “extends” seguida do nome da classe “mãe” para indicar o relacionamento de herança. Enquanto na linguagem Python são utilizados parênteses contendo o nome da classe “mãe” para indicar essa relação de herança.

Em relação ao construtor das classes mãe e filha em Java é utilizado o comando ”super(atributos);” no construtor da classe “filha”, para inicializar o construtor da classe “mãe”. Já em Python o comando equivalente é o “super.__init__(atributos)”, sendo uma pequena diferença de sintaxe mas ainda assim possuem a mesma funcionalidade.

Agora vejamos um exemplo prático de herança entre classes em ambas as linguagens, utilizando os códigos “ExemploHeranca.java” e “ExemploHeranca.py”.

```Java
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

```

```Python
class Pessoa:

    def __init__(self, nome, time):
        self._nome = nome
        self._time = time


class Técnico(Pessoa):

    def __init__(self, nome, time, salario):
        super().__init__(nome, time)
        self.__salario = salario
        print("Técnico Criado")


class Jogador(Pessoa):

    def __init__(self, nome, time, apelido, posicao, camisa, salario):
        super().__init__(nome, time)
        self.__apelido = apelido
        self.__posicao = posicao
        self.__camisa = camisa
        self.__salario = salario
        print("Jogador Criado")

class Torcedor(Pessoa):

    def __init__(self, nome, time):
        super().__init__(nome, time)
        print("Torcedor Criado")

```

### Polimorfismo

Para finalizar, o último conceito a ser abordado será o conceito de Polimorfismo, que é outro conceito bastante utilizado na Programação Orientada Objetos.
O conceito de polimorfismo consiste na capacidade de várias classes “filhas” possuírem um mesmo método, com mesma identificação e em cada uma dessas classes filhas esse método tem um comportamento distinto para cada uma delas.

Agora vejamos as diferenças existentes entre Java e Python relacionadas à utilização de polimorfismo

Em relação a esse conceito não existem muitas diferenças, que ainda não tenham sido mencionadas nos tópicos anteriores, uma diferença pequena é que na linguagem Java existe a notação “@Override” ela é utilizada para indicar que houve uma “sobrescrita”, o que significa que a classe filha sobrescrever um método da classe mãe, sendo um indicativo de polimorfismo.

Analisando de forma geral a funcionalidade do polimorfismo é igual em ambas as linguagens tanto em Java quanto em Python, apesar de apresentarem pequenas diferenças de sintaxe.

No caso agora vejamos um exemplo prático em ambas as linguagens utilizando os códigos “ExemploPolimorfismo.java” e “ExemploPolimorfismo.py”, no caso o método que sofre polimorfismo nesse exemplo é o método "apresentacao".

```Java
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
```

```Python
class Pessoa:

    def __init__(self, nome, time):
        self._nome = nome
        self._time = time

    def apresentacao(self):
        print(self._nome + " é uma pessoa que gosta do time " + self._time ".")


class Técnico(Pessoa):

    def __init__(self, nome, time, salario):
        super().__init__(nome, time)
        self.__salario = salario
        print("Técnico Criado")

    def apresentacao(self):
        print(self._nome + " é o técnico do time " + self._time ".")


class Jogador(Pessoa):

    def __init__(self, nome, time, apelido, posicao, camisa, salario):
        super().__init__(nome, time)
        self.__apelido = apelido
        self.__posicao = posicao
        self.__camisa = camisa
        self.__salario = salario
        print("Jogador Criado")

    def apresentacao(self):
        print(self._nome + " é o jogador camisa" + self.__camisa + " do time " + self._time ".")

class Torcedor(Pessoa):

    def __init__(self, nome, time):
        super().__init__(nome, time)
        print("Torcedor Criado")

    def apresentacao(self):
        print(self._nome + " é um torcedor do time " + self._time ".");

```

## Projetos

Para finalizar foram criados dois projetos, “ProjetoJava” e “ProjetoPython” um utilizando linguagem Java e outro utilizando linguagem Python combinando todos os conceitos mencionados acima, juntamente com a criação de alguns métodos adicionais para o melhor funcionamento da funcionamento da classes. Ademais foi criado uma classe main em ambos os projetos para exemplificar a criação e manipulação de alguns objetos, esses projetos podem ser utilizados para comparar de maneira mais prática as diferenças já mencionadas, nos tópicos anteriores, entre as linguagens.


## Conclusão

Comparando as linguagens Java e Python é possível notar algumas diferenças existentes entre as duas linguagens. Entretanto ambas as linguagens seguem os mesmos conceitos do Paradigma de Programação Orientada a Objetos, com ambas as linguagens aplicandos os conceitos de Encapsulamento, Herança e Polimorfismo.

Desse modo é possível concluir que apesar de se tratarem de linguagens diferentes, por possuírem o mesmo paradigma ambas possuem muitas semelhanças e algumas diferenças, na maioria das vezes se tratando apenas na variação das palavras-chaves utilizadas em cada uma das linguagens.

Em questão de aprendizagem é possível afirmar que se torna muito mais simples e fácil aprender a trabalhar com uma dessas linguagens tendo um conhecimento prévio da outra, sendo necessário aprender as pequenas diferenças, mais particulares, existente entre as linguagens, já que ambas seguem os mesmos conceitos do Paradigma de Programação Orientada a Objetos.


