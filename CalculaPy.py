import math
import os
import time

# Constantes de cores ANSI para estilizar o terminal
VERDE = "\033[92m"
VERMELHO = "\033[91m"
AZUL = "\033[94m"
AMARELO = "\033[93m"
NEGRITO = "\033[1m"
RESET = "\033[0m"


def limpar_tela() -> None:
    """Limpa o terminal de acordo com o sistema operacional (Windows/Linux/Mac)."""
    os.system("cls" if os.name == "nt" else "clear")


# ---------------- OPERAÇÕES MATEMÁTICAS BÁSICAS E GERAIS ---------------- #

def somar(a: float, b: float) -> float:
    return a + b

def subtrair(a: float, b: float) -> float:
    return a - b

def multiplicar(a: float, b: float) -> float:
    return a * b

def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Não é possível realizar divisão por zero.")
    return a / b

def calcular_porcentagem(taxa: float, total: float) -> float:
    """Calcula a porcentagem de um valor (ex: taxa% de total)."""
    return (taxa * total) / 100

def calcular_escala(desenho: float, real: float) -> float:
    """Calcula o fator N de uma escala 1 : N (desenho / real)."""
    if desenho <= 0 or real <= 0:
        raise ValueError("As medidas do desenho e real devem ser maiores que zero.")
    return real / desenho

def regra_de_tres(a: float, b: float, c: float) -> float:
    """
    Calcula o valor X em uma regra de três simples direta:
    A está para B assim como C está para X (X = (B * C) / A).
    """
    if a == 0:
        raise ZeroDivisionError("O valor A não pode ser zero na regra de três.")
    return (b * c) / a

def calcular_probabilidade(favoraveis: float, total: float) -> float:
    """Calcula a probabilidade de um evento (casos favoráveis / total de casos)."""
    if total <= 0:
        raise ZeroDivisionError("O total de eventos possíveis deve ser maior que zero.")
    if favoraveis < 0:
        raise ValueError("O número de casos favoráveis não pode ser negativo.")
    if favoraveis > total:
        raise ValueError("O número de casos favoráveis não pode ser maior que o total.")
    return favoraveis / total


# ---------------- FÓRMULAS DE GEOMETRIA PLANA ---------------- #

def area_retangulo(base: float, altura: float) -> float:
    if base <= 0 or altura <= 0:
        raise ValueError("A base e a altura devem ser maiores que zero.")
    return base * altura

def area_quadrado(lado: float) -> float:
    if lado <= 0:
        raise ValueError("O lado deve ser maior que zero.")
    return lado ** 2

def area_triangulo(base: float, altura: float) -> float:
    if base <= 0 or altura <= 0:
        raise ValueError("A base e a altura devem ser maiores que zero.")
    return (base * altura) / 2

def area_triangulo_equilatero(lado: float) -> float:
    if lado <= 0:
        raise ValueError("O lado deve ser maior que zero.")
    return ((lado ** 2) * math.sqrt(3)) / 4

def circulo_area_comprimento(raio: float) -> tuple[float, float]:
    if raio <= 0:
        raise ValueError("O raio deve ser maior que zero.")
    area = math.pi * (raio ** 2)
    comprimento = 2 * math.pi * raio
    return area, comprimento

def area_trapezio(base_maior: float, base_menor: float, altura: float) -> float:
    if base_maior <= 0 or base_menor <= 0 or altura <= 0:
        raise ValueError("As bases e a altura devem ser maiores que zero.")
    return ((base_maior + base_menor) * altura) / 2

def teorema_pitagoras(cateto_b: float, cateto_c: float) -> float:
    if cateto_b <= 0 or cateto_c <= 0:
        raise ValueError("Os catetos devem ser maiores que zero.")
    return math.hypot(cateto_b, cateto_c)


# ---------------- FÓRMULAS DE GEOMETRIA ESPACIAL ---------------- #

def volume_paralelepipedo(comprimento: float, largura: float, altura: float) -> float:
    if comprimento <= 0 or largura <= 0 or altura <= 0:
        raise ValueError("Comprimento, largura e altura devem ser maiores que zero.")
    return comprimento * largura * altura

def volume_cilindro(raio: float, altura: float) -> float:
    if raio <= 0 or altura <= 0:
        raise ValueError("O raio e a altura devem ser maiores que zero.")
    return math.pi * (raio ** 2) * altura

def volume_esfera(raio: float) -> float:
    if raio <= 0:
        raise ValueError("O raio deve ser maior que zero.")
    return (4 / 3) * math.pi * (raio ** 3)

def relacao_euler(vertices: float, arestas: float, faces: float) -> str:
    """
    Relação de Euler para poliedros convexos: V - A + F = 2.
    Informe 0 na incógnita que deseja calcular.
    """
    valores = [vertices, arestas, faces]
    if any(v < 0 for v in valores):
        raise ValueError("Vértices, arestas e faces não podem ser valores negativos.")
    
    zeros = [v for v in valores if v == 0]
    if len(zeros) > 1:
        raise ValueError("Informe ao menos 2 valores conhecidos (digite 0 apenas na incógnita).")

    if vertices == 0:
        v_calc = int(arestas - faces + 2)
        if v_calc <= 0:
            raise ValueError("Combinação geométrica impossível para um poliedro convexo.")
        return f"Vértices (V) = {v_calc}  [Fórmula: V = A - F + 2]"
    elif arestas == 0:
        a_calc = int(vertices + faces - 2)
        if a_calc <= 0:
            raise ValueError("Combinação geométrica impossível para um poliedro convexo.")
        return f"Arestas (A) = {a_calc}  [Fórmula: A = V + F - 2]"
    elif faces == 0:
        f_calc = int(arestas - vertices + 2)
        if f_calc <= 0:
            raise ValueError("Combinação geométrica impossível para um poliedro convexo.")
        return f"Faces (F) = {f_calc}  [Fórmula: F = A - V + 2]"
    else:
        resultado = vertices - arestas + faces
        if resultado == 2:
            return f"Poliedro Convexo Válido! ({vertices:g} - {arestas:g} + {faces:g} = 2)"
        else:
            return f"Não obedece à Relação de Euler ({vertices:g} - {arestas:g} + {faces:g} = {resultado:g} ≠ 2)"


# ---------------- DICIONÁRIOS DE OPERAÇÕES E SUBMENUS ---------------- #

GEOMETRIA_PLANA = {
    "1": {
        "nome": "Área do Retângulo",
        "simbolo": "b × h",
        "funcao": area_retangulo,
        "prompts": ["Digite a base: ", "Digite a altura: "],
        "exibir": lambda v, r: f"Base: {v[0]:g}, Altura: {v[1]:g} → Área = {r:g}",
    },
    "2": {
        "nome": "Área do Quadrado",
        "simbolo": "L²",
        "funcao": area_quadrado,
        "prompts": ["Digite o valor do lado (L): "],
        "exibir": lambda v, r: f"Lado: {v[0]:g} → Área = {r:g}",
    },
    "3": {
        "nome": "Área do Triângulo",
        "simbolo": "(b × h) / 2",
        "funcao": area_triangulo,
        "prompts": ["Digite a base (b): ", "Digite a altura (h): "],
        "exibir": lambda v, r: f"Base: {v[0]:g}, Altura: {v[1]:g} → Área = {r:g}",
    },
    "4": {
        "nome": "Área do Triângulo Equilátero",
        "simbolo": "(L²√3) / 4",
        "funcao": area_triangulo_equilatero,
        "prompts": ["Digite o lado (L): "],
        "exibir": lambda v, r: f"Lado: {v[0]:g} → Área = {r:.4f}",
    },
    "5": {
        "nome": "Área e Comprimento do Círculo",
        "simbolo": "πr² / 2πr",
        "funcao": circulo_area_comprimento,
        "prompts": ["Digite o raio (r): "],
        "exibir": lambda v, r: f"Raio: {v[0]:g} → Área = {r[0]:.4f} | Comprimento = {r[1]:.4f}",
    },
    "6": {
        "nome": "Área do Trapézio",
        "simbolo": "((B+b)×h)/2",
        "funcao": area_trapezio,
        "prompts": [
            "Digite a base maior (B): ",
            "Digite a base menor (b): ",
            "Digite a altura (h): ",
        ],
        "exibir": lambda v, r: f"B = {v[0]:g}, b = {v[1]:g}, h = {v[2]:g} → Área = {r:g}",
    },
    "7": {
        "nome": "Teorema de Pitágoras",
        "simbolo": "a = √(b²+c²)",
        "funcao": teorema_pitagoras,
        "prompts": ["Digite o cateto b: ", "Digite o cateto c: "],
        "exibir": lambda v, r: f"Catetos: {v[0]:g} e {v[1]:g} → Hipotenusa a = {r:.4g}",
    },
}

GEOMETRIA_ESPACIAL = {
    "1": {
        "nome": "Volume Paralelepípedo / Prisma",
        "simbolo": "c × l × h",
        "funcao": volume_paralelepipedo,
        "prompts": [
            "Digite o comprimento: ",
            "Digite a largura: ",
            "Digite a altura: ",
        ],
        "exibir": lambda v, r: f"Dimensões: {v[0]:g} × {v[1]:g} × {v[2]:g} → Volume = {r:g}",
    },
    "2": {
        "nome": "Volume do Cilindro",
        "simbolo": "πr²h",
        "funcao": volume_cilindro,
        "prompts": ["Digite o raio da base (r): ", "Digite a altura (h): "],
        "exibir": lambda v, r: f"Raio: {v[0]:g}, Altura: {v[1]:g} → Volume = {r:.4f}",
    },
    "3": {
        "nome": "Volume da Esfera",
        "simbolo": "4/3 πr³",
        "funcao": volume_esfera,
        "prompts": ["Digite o raio (r): "],
        "exibir": lambda v, r: f"Raio: {v[0]:g} → Volume = {r:.4f}",
    },
    "4": {
        "nome": "Relação de Euler (Poliedros)",
        "simbolo": "V - A + F = 2",
        "funcao": relacao_euler,
        "prompts": [
            "Digite a qtd de Vértices (V) [0 para calcular]: ",
            "Digite a qtd de Arestas (A)  [0 para calcular]: ",
            "Digite a qtd de Faces (F)    [0 para calcular]: ",
        ],
        "exibir": lambda v, r: r,
    },
}

OPERACOES = {
    "1": {
        "nome": "Soma",
        "simbolo": "+",
        "funcao": somar,
        "prompts": ["Digite o 1º número: ", "Digite o 2º número: "],
        "exibir": lambda v, r: f"{v[0]:g} + {v[1]:g} = {r:g}",
    },
    "2": {
        "nome": "Subtração",
        "simbolo": "-",
        "funcao": subtrair,
        "prompts": ["Digite o 1º número: ", "Digite o 2º número: "],
        "exibir": lambda v, r: f"{v[0]:g} - {v[1]:g} = {r:g}",
    },
    "3": {
        "nome": "Multiplicação",
        "simbolo": "×",
        "funcao": multiplicar,
        "prompts": ["Digite o 1º número: ", "Digite o 2º número: "],
        "exibir": lambda v, r: f"{v[0]:g} × {v[1]:g} = {r:g}",
    },
    "4": {
        "nome": "Divisão",
        "simbolo": "÷",
        "funcao": dividir,
        "prompts": ["Digite o 1º número: ", "Digite o 2º número: "],
        "exibir": lambda v, r: f"{v[0]:g} ÷ {v[1]:g} = {r:g}",
    },
    "5": {
        "nome": "Porcentagem",
        "simbolo": "%",
        "funcao": calcular_porcentagem,
        "prompts": ["Digite a porcentagem (%): ", "Digite o valor base: "],
        "exibir": lambda v, r: f"{v[0]:g}% de {v[1]:g} = {r:g}",
    },
    "6": {
        "nome": "Escala (1:N)",
        "simbolo": "1:N",
        "funcao": calcular_escala,
        "prompts": ["Digite a medida no desenho/mapa: ", "Digite a medida real (mesma unidade): "],
        "exibir": lambda v, r: f"Escala 1 : {r:g} (1 un. no desenho = {r:g} un. na realidade)",
    },
    "7": {
        "nome": "Regra de Três Simples",
        "simbolo": "A→B",
        "funcao": regra_de_tres,
        "prompts": [
            "Digite o valor A (está para B): ",
            "Digite o valor B: ",
            "Digite o valor C (está para X): ",
        ],
        "exibir": lambda v, r: f"Se {v[0]:g} → {v[1]:g}, então {v[2]:g} → {r:g} (X = {r:g})",
    },
    "8": {
        "nome": "Probabilidade",
        "simbolo": "P(E)",
        "funcao": calcular_probabilidade,
        "prompts": [
            "Digite o número de casos favoráveis: ",
            "Digite o total de casos possíveis: ",
        ],
        "exibir": lambda v, r: f"P(E) = {v[0]:g} / {v[1]:g} = {r:.4g} ({r * 100:.2f}%)",
    },
    "9": {
        "nome": "Geometria Plana",
        "simbolo": "Submenu",
        "submenu": GEOMETRIA_PLANA,
    },
    "10": {
        "nome": "Geometria Espacial",
        "simbolo": "Submenu",
        "submenu": GEOMETRIA_ESPACIAL,
    },
}


# ---------------- ENTRADAS E INTERFACE ---------------- #

def obter_numero(mensagem: str) -> float:
    """Solicita um número ao usuário, aceita vírgula e valida a entrada."""
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            return float(entrada)
        except ValueError:
            print(f"{VERMELHO}⚠ Entrada inválida! Por favor, digite um número real.{RESET}")


def exibir_cabecalho(titulo: str = "CALCULADORA INTELIGENTE") -> None:
    print(f"{AZUL}{NEGRITO}┌───────────────────────────────────────────┐")
    print(f"│{titulo:^43}│")
    print(f"└───────────────────────────────────────────┘{RESET}")


# ---------------- FLUXO DE EXECUÇÃO REUTILIZÁVEL ---------------- #

def executar_fluxo(titulo: str, mapa_operacoes: dict, texto_voltar: str = "Sair") -> None:
    """Controla a navegação de menus e execução de cálculos de forma genérica e reutilizável."""
    while True:
        limpar_tela()
        exibir_cabecalho(titulo)
        
        for chave, dados in mapa_operacoes.items():
            print(f"  {AMARELO}[{chave:>2}]{RESET} {dados['nome']} ({dados['simbolo']})")
        print(f"  {AMARELO}[ 0]{RESET} {texto_voltar}")
        print(f"{AZUL}─────────────────────────────────────────────{RESET}")

        opcao = input(f"\n{NEGRITO}Escolha uma opção: {RESET} ").strip()

        if opcao == "0":
            if texto_voltar == "Sair":
                limpar_tela()
                print(f"{VERDE}Obrigado por usar a calculadora! Encerrando...{RESET}")
                time.sleep(1.5)
            break

        if opcao not in mapa_operacoes:
            print(f"{VERMELHO}Opção inválida! Escolha uma opção do menu.{RESET}")
            time.sleep(1.2)
            continue

        item = mapa_operacoes[opcao]

        # Navegação para submenu
        if "submenu" in item:
            executar_fluxo(item["nome"].upper(), item["submenu"], texto_voltar="Voltar")
            continue

        # Execução de cálculo
        print(f"\n{AZUL}» Operação Selecionada: {item['nome']}{RESET}\n")

        entradas = [obter_numero(prompt) for prompt in item["prompts"]]

        try:
            resultado = item["funcao"](*entradas)
            mensagem_resultado = item["exibir"](entradas, resultado)
            print(f"\n{VERDE}{NEGRITO}✔ Resultado: {mensagem_resultado}{RESET}")
        except (ZeroDivisionError, ValueError) as erro:
            print(f"\n{VERMELHO}{NEGRITO}✖ Erro: {erro}{RESET}")

        print(f"\n{AZUL}─────────────────────────────────────────────{RESET}")
        input("Pressione [Enter] para continuar...")


def main() -> None:
    executar_fluxo("CALCULADORA INTELIGENTE", OPERACOES, texto_voltar="Sair")


if __name__ == "__main__":
    main()
