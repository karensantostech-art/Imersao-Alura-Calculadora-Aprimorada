# 🧮 CalculaPy - Calculadora Inteligente e Multidisciplinar em Python

Uma aplicação interativa de terminal em **Python** desenvolvida para resolver desde cálculos do cotidiano até problemas de matemática aplicada, geometria plana e geometria espacial. O projeto combina conceitos de programação limpa, tratamento robusto de erros e uma interface CLI amigável e colorida.

---

## 📌 Funcionalidades

O sistema está estruturado em um menu principal com opções diretas e submenus especializados:

### 1. Operações Básicas
* **Soma (`+`)**: Adição de números reais.
* **Subtração (`-`)**: Diferença entre dois valores.
* **Multiplicação (`×`)**: Produto com suporte a números decimais.
* **Divisão (`÷`)**: Quociente com proteção contra divisão por zero.

### 2. Matemática Aplicada e Estatística
* **Porcentagem (`%`)**: Cálculo de taxa percentual sobre valor base.
* **Escala Cartográfica (`1:N`)**: Determinação do fator de proporção a partir de medidas no desenho/mapa e medidas reais.
* **Regra de Três Simples Direta (`A → B | C → X`)**: Resolução direta da incógnita $X = \frac{B \times C}{A}$.
* **Probabilidade Simples (`P(E)`)**: Razão entre casos favoráveis e casos possíveis, com validações de consistência e exibição em porcentagem.

### 3. Geometria Plana (Submenu `[9]`)
* **Área do Retângulo**: $A = b \times h$
* **Área do Quadrado**: $A = L^2$
* **Área do Triângulo Geral**: $A = \frac{b \times h}{2}$
* **Área do Triângulo Equilátero**: $A = \frac{L^2\sqrt{3}}{4}$
* **Círculo**: Cálculo simultâneo de Área ($A = \pi r^2$) e Comprimento/Perímetro ($C = 2\pi r$)
* **Área do Trapézio**: $A = \frac{(B + b) \times h}{2}$
* **Teorema de Pitágoras**: Cálculo da hipotenusa $a = \sqrt{b^2 + c^2}$

### 4. Geometria Espacial (Submenu `[10]`)
* **Volume do Paralelepípedo / Prisma**: $V = c \times l \times h$
* **Volume do Cilindro**: $V = \pi r^2 h$
* **Volume da Esfera**: $V = \frac{4}{3} \pi r^3$
* **Relação de Euler para Poliedros Convexos**:
  * Aplicação da fórmula $V - A + F = 2$.
  * **Modo Descoberta:** Ao digitar `0` na incógnita desconhecida (Vértices, Arestas ou Faces), o algoritmo calcula o valor correspondente.
  * **Modo Verificação:** Ao informar os três valores, o sistema verifica se o poliedro obedece à relação de Euler.

---

## 🎯 Destaques de Implementação & Engenharia de Software

* **Separação de Responsabilidades (*Separation of Concerns*)**: Funções matemáticas puras que realizam apenas cálculos e lançam exceções, sem acoplamento com `input` ou `print`.
* **Despacho Dinâmico por Dicionários**: Menus e submenus flexíveis, onde cada operação define seus próprios prompts, funções e formatações de saída.
* **Navegação Recursiva Reutilizável**: A função `executar_fluxo()` gerencia qualquer menu ou submenu sem duplicação de código.
* **Resiliência a Falhas**:
  * Aceita tanto ponto (`.`) quanto vírgula (`,`) como separador decimal.
  * Captura de erros como `ZeroDivisionError` e `ValueError` (ex: lados ou raios negativos/nulos).
  * Repetição automática de perguntas caso o usuário insira caracteres inválidos.
* **Estilização Terminal com ANSI**: Cores que melhoram a usabilidade visual (títulos em azul, destaques em amarelo, sucessos em verde e erros em vermelho).

---

## 📂 Estrutura de Arquivos

```text
Projeto_Imersão_IA_Karen/
│
├── CalculaPy.py             # Código-fonte principal da aplicação
├── testes_calculadora.py    # Suíte com 22 testes automatizados (unittest)
└── README.md                # Documentação detalhada do projeto
```

---

## 🚀 Como Executar

O projeto utiliza **exclusivamente a biblioteca padrão do Python** (`math`, `os`, `time`, `sys`, `unittest`), o que significa que **não é necessário instalar nenhuma dependência externa** (nenhum `pip install` é exigido).

### Pré-requisitos
* Ter o **Python 3.10 ou superior** instalado ([download em python.org](https://www.python.org/downloads/)).
* Ter o **Git** instalado (opcional, para clonar o repositório).

---

### Passo a Passo

#### 1. Obter o Código

**Via Git (recomendado):**
```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO
```

*Ou baixe o arquivo ZIP diretamente pelo botão verde **Code > Download ZIP** no GitHub e descompacte a pasta no seu computador.*

#### 2. Executar a Aplicação
No terminal ou prompt de comando (dentro da pasta do projeto), execute:

* **No Windows:**
  ```bash
  python CalculaPy.py
  ```
  *(caso tenha mais de uma versão, pode usar `py CalculaPy.py`)*

* **No Linux / macOS:**
  ```bash
  python3 CalculaPy.py
  ```

---

### 🧪 Executando os Testes Automatizados

Para verificar se todas as funções estão respondendo perfeitamente na máquina:

* **No Windows:**
  ```bash
  python testes_calculadora.py
  ```
* **No Linux / macOS:**
  ```bash
  python3 testes_calculadora.py
  ```

Exemplo de saída esperada:
```text
......................
----------------------------------------------------------------------
Ran 22 tests in 0.009s

OK
```

---

## 💡 Exemplos de Uso

### 1. Cálculo de Regra de Três
```text
» Operação Selecionada: Regra de Três Simples

Digite o valor A (está para B): 2
Digite o valor B: 10
Digite o valor C (está para X): 4

✔ Resultado: Se 2 → 10, então 4 → 20 (X = 20)
```

### 2. Relação de Euler (Descobrindo Faces de um Cubo)
```text
» Operação Selecionada: Relação de Euler (Poliedros)

Digite a qtd de Vértices (V) [0 para calcular]: 8
Digite a qtd de Arestas (A)  [0 para calcular]: 12
Digite a qtd de Faces (F)    [0 para calcular]: 0

✔ Resultado: Faces (F) = 6  [Fórmula: F = A - V + 2]
```

---

## 👩‍💻 Autoria e Aprendizado

Desenvolvido com foco no aprofundamento prático em Python, abrangendo:
* Estruturas de dados (`dict`, `list`, `tuple`).
* Funções anônimas (`lambda`), empacotamento/desempacotamento de argumentos (`*args`).
* Tratamento de exceções (`try / except / raise`).
* Testes unitários com `unittest`.
