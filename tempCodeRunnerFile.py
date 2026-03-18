# ==========================================
# IMPORTAÇÃO DE BIBLIOTECAS
# ==========================================
# finalizado

import time
import os
import sys
from datetime import datetime


# ==========================================
# CORES ANSI PARA TERMINAL
# ==========================================

verde = "\033[92m"
azul = "\033[94m"
amarelo = "\033[93m"
vermelho = "\033[91m"
reset = "\033[0m"


# ==========================================
# FUNÇÃO PARA LIMPAR TERMINAL
# ==========================================

def limpar():
    os.system("cls" if os.name == "nt" else "clear")


# ==========================================
# EFEITO TEXTO DIGITANDO
# ==========================================

def digitar(texto):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(0.02)
    print()


# ==========================================
# TEXTO PISCANDO
# ==========================================

def piscar(texto):
    print(f"\033[5m{texto}\033[0m")


# ==========================================
# LOADING INICIAL DO SISTEMA
# ==========================================

def loading():

    print(amarelo + "\nInicializando sistema...\n" + reset)

    for i in range(0, 101, 5):

        barra = "█" * (i // 5)
        espaco = " " * (20 - (i // 5))

        print(f"\rCarregando: [{barra}{espaco}] {i}%", end="")
        time.sleep(0.07)

    print("\n")
    time.sleep(0.6)


# ==========================================
# LOADING ENTRE TELAS
# ==========================================

def loading_tela():

    print("\nCarregando", end="")

    for i in range(3):
        time.sleep(0.25)
        print(".", end="", flush=True)

    print("\n")


# ==========================================
# SAUDAÇÃO AUTOMÁTICA
# ==========================================

def saudacao():

    hora = datetime.now().hour

    if hora < 12:
        msg = "Bom dia"
    elif hora < 18:
        msg = "Boa tarde"
    else:
        msg = "Boa noite"

    digitar(verde + f"\n{msg}! Bem-vindo ao currículo interativo em Python\n" + reset)


# ==========================================
# MENU DE NAVEGAÇÃO ENTRE TELAS
# ==========================================

def navegacao():

    print("\n")

    print("1 - Contato")
    print("2 - Habilidades técnicas")
    print("3 - Cursos e certificações")
    print("4 - Experiência profissional")
    print("5 - Objetivo profissional")
    print("6 - Formação acadêmica")
    print("8 - Exibir currículo completo")
    print("9 - Voltar ao menu")
    print("0 - Finalizar")

    escolha = input("\nEscolha: ")

    return escolha


# ==========================================
# CONTATO
# ==========================================

def contato():

    limpar()
    loading_tela()

    print(azul + "=== CONTATO ===\n" + reset)

    print("Contato: (31) 99373-6336 (WhatsApp)")
    print("E-mail: wpatrickhelmer@gmail.com")
    print("LinkedIn: linkedin.com/in/walissonpatrickhelmer")
    print("GitHub: github.com/WalissonPatrickHelmer")
    print("Cidade: Belo Horizonte")
    print("Bairro: Lindeia")
    print("CEP: 30690-260")

    return navegacao()


# ==========================================
# HABILIDADES TÉCNICAS
# ==========================================

def habilidades():

    limpar()
    loading_tela()

    print(azul + "=== HABILIDADES TÉCNICAS ===\n" + reset)

    print("- Linguagens: Python, HTML5, CSS3, SQL")
    print("- Sistemas: Neo4j, Banco de Dados, Excel, Power BI, N8N")
    print("- Inteligência Artificial: Engenharia de Prompt")
    print("- Design: Photoshop, CorelDraw")
    print("- Hardware: montagem e manutenção de computadores")
    print("- Gestão: equipes, vendas e atendimento ao cliente")

    return navegacao()


# ==========================================
# CURSOS E CERTIFICAÇÕES
# ==========================================

def cursos():

    limpar()
    loading_tela()

    print(azul + "=== CURSOS E CERTIFICAÇÕES ===\n" + reset)

    print("- Embaixadores Universitários da DIO")
    print("- Automação com N8N básico – 26h")
    print("- Inteligência Artificial – 40h (ênfase em Engenharia de Prompt)")
    print("- Jornada IA – 8h (Hashtag Treinamentos)")
    print("- Imersão em IA – 10h (Gran Faculdade)")

    print("\nDESENVOLVIMENTO WEB E DESIGN")
    print("- HTML5 e CSS3 – 200h (Curso em Vídeo)")
    print("- Web Design – 102h (Photoshop, Corel Draw, HTML, CSS)")
    print("- Design de Web: Introdução – 84h (Microsoft Brasil / SENAC Santo Amaro)")

    print("\nOUTROS CURSOS")
    print("- Introdução à Programação, Hardware e Manutenção – 96h")
    print("- Consultor de Vendas – 80h")

    return navegacao()


# ==========================================
# EXPERIÊNCIA PROFISSIONAL
# ==========================================

def experiencia():

    limpar()
    loading_tela()

    print(azul + "=== EXPERIÊNCIA PROFISSIONAL ===\n" + reset)

    print("2P Sacolas Personalizadas")
    print("2018 - 2026")
    print("Gestão de vendas, equipe, redes sociais e logística.\n")

    print("AlmaViva do Brasil")
    print("2014 - 2017")
    print("Atendimento ao cliente e suporte técnico.\n")

    print("Monticeli Buzzo 'Chame o Gênio'")
    print("2010 - 2012")
    print("Suporte técnico e pós-venda.\n")

    print("Carrefour S.A.")
    print("2007 - 2010")
    print("Vendas e atendimento ao cliente.")

    return navegacao()


# ==========================================
# OBJETIVO PROFISSIONAL
# ==========================================

def objetivo():

    limpar()
    loading_tela()

    print(azul + "=== OBJETIVO PROFISSIONAL ===\n" + reset)

    print("Estudante de Análise e Desenvolvimento de Sistemas,")
    print("com experiência em gestão de equipes, atendimento")
    print("ao cliente e suporte técnico.")
    print("Busco oportunidade de estágio em Desenvolvimento")
    print("de Sistemas ou Suporte em TI.")

    return navegacao()


# ==========================================
# FORMAÇÃO ACADÊMICA
# ==========================================

def formacao():

    limpar()
    loading_tela()

    print(azul + "=== FORMAÇÃO ACADÊMICA ===\n" + reset)

    print("Análise e Desenvolvimento de Sistemas")
    print("Graduação em andamento")

    return navegacao()


# ==========================================
# CURRÍCULO COMPLETO
# ==========================================

def completo():

    limpar()
    loading_tela()

    print(verde + "===== CURRÍCULO COMPLETO =====\n" + reset)

    print("Walisson Patrick Helmer\n")

    print("Contato: (31) 99373-6336 (WhatsApp)")
    print("E-mail: wpatrickhelmer@gmail.com")
    print("LinkedIn: https://www.linkedin.com/in/walissonpatrickhelmer/")
    print("GitHub: https://github.com/WalissonPatrickHelmer")
    print("Cidade: Belo Horizonte")
    print("Bairro: Lindeia")
    print("CEP: 30690-260\n")

    print("OBJETIVO PROFISSIONAL")
    print("Estudante de Análise e Desenvolvimento de Sistemas, com experiência previa em gestão de equipes, atendimento ao cliente e suporte técnico.")
    print("Busco oportunidade de estágio nas áreas de Desenvolvimento de Sistemas ou Suporte em TI.\n")

    print("FORMAÇÃO ACADÊMICA")
    print("- Análise e Desenvolvimento de Sistemas")
    print("  Faculdade Impacta (Conclusão prevista: dezembro/2027)")
    print("- Técnico em Programação e Jogos Digitais – 1200h\n")

    print("HABILIDADES TÉCNICAS")
    print("- Linguagens: Python, HTML5, CSS3, SQL")
    print("- Sistemas: Neo4j, Banco de Dados, Excel, Power BI, N8N")
    print("- Inteligência Artificial: Engenharia de Prompt")
    print("- Design e Web: Photoshop, CorelDraw")
    print("- Hardware e Suporte: Montagem e manutenção de computadores")
    print("- Gestão: administração de equipes, vendas e atendimento\n")

    print("CURSOS E CERTIFICAÇÕES")
    print("- Embaixadores Universitários da DIO")
    print("- Automação com N8N básico – 26h")
    print("- Inteligência Artificial – 40h (ênfase em Engenharia de Prompt)")
    print("- Jornada IA – 8h (Hashtag Treinamentos)")
    print("- Imersão em IA – 10h (Gran Faculdade)")
    print("- HTML5 e CSS3 – 200h (Curso em Vídeo)")
    print("- Web Design – 102h")
    print("- Design de Web: Introdução – 84h")
    print("- Introdução à Programação, Hardware e Manutenção – 96h")
    print("- Consultor de Vendas – 80h\n")

    print("EXPERIÊNCIA PROFISSIONAL")
    print("- 2P Sacolas Personalizadas – 2018 a 2026")
    print("- AlmaViva do Brasil – 2014 a 2017")
    print("- Monticeli Buzzo – 2010 a 2012")
    print("- Carrefour – 2007 a 2010")

    return navegacao()


# ==========================================
# MENU PRINCIPAL
# ==========================================

def menu():

    tela = None

    while True:

        if tela is None:

            limpar()

            print(verde + "=================================")
            print("   CURRÍCULO INTERATIVO PYTHON")
            print("=================================" + reset)

            print("\n1 - Contato")
            print("2 - Habilidades técnicas")
            print("3 - Cursos e certificações")
            print("4 - Experiência profissional")
            print("5 - Objetivo profissional")
            print("6 - Formação acadêmica")
            print("8 - Exibir currículo completo")
            print("\n0 - Finalizar\n")

            piscar(">>> Digite a opção desejada <<<")

            tela = input("➜ ")

        if tela == "1":
            r = contato()

        elif tela == "2":
            r = habilidades()

        elif tela == "3":
            r = cursos()

        elif tela == "4":
            r = experiencia()

        elif tela == "5":
            r = objetivo()

        elif tela == "6":
            r = formacao()

        elif tela == "8":
            r = completo()

        elif tela == "0":
            print(vermelho + "\nPrograma finalizado.")
            break

        else:
            tela = None
            continue

        if r == "0":
            break
        elif r == "9":
            tela = None
        else:
            tela = r


# ==========================================
# INÍCIO DO PROGRAMA
# ==========================================

limpar()
saudacao()
loading()
menu()
