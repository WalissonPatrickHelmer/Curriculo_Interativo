/* =========================================
VERSÃO 01 - LÓGICA DO TERMINAL
========================================= */

const terminal = document.getElementById("terminal");
let digitando = false;

function limpar() {
    terminal.innerHTML = "";
}

function esperar(ms) {
    return new Promise(r => setTimeout(r, ms));
}

async function digitar(texto) {
    digitando = true;
    for (const letra of texto) {
        terminal.innerHTML += letra;
        await esperar(10); // Velocidade levemente aumentada para textos longos
    }
    terminal.innerHTML += "<br>";
    terminal.scrollTop = terminal.scrollHeight;
    digitando = false;
}

async function loadingTela() {
    await digitar("Carregando...");
    await esperar(400);
    limpar();
}

async function escreverTela(func) {
    if (digitando) return;
    limpar();
    await loadingTela();
    await func();
}

/* ============================
SAUDAÇÃO
============================ */

async function saudacao() {
    const hora = new Date().getHours();
    let msg = "Boa noite";
    if (hora < 12) msg = "Bom dia";
    else if (hora < 18) msg = "Boa tarde";
    await digitar(`${msg}! Bem-vindo ao currículo interativo feito em Python e convertido para Html css e js`);
}

/* ============================
TELAS
============================ */

function contato() {
    escreverTela(async () => {
        await digitar("=== CONTATO ===");
        await digitar("Contato: (31) 99373-6336 (WhatsApp)");
        await digitar("E-mail: wpatrickhelmer@gmail.com");
        await digitar("LinkedIn: linkedin.com/in/walissonpatrickhelmer");
        await digitar("GitHub: github.com/WalissonPatrickHelmer");
        await digitar("Cidade: Belo Horizonte - Bairro: Lindeia");
    });
}

function habilidades() {
    escreverTela(async () => {
        await digitar("=== HABILIDADES TÉCNICAS ===");
        await digitar("- Linguagens: Python, HTML5, CSS3, SQL");
        await digitar("- Sistemas: Neo4j, Banco de Dados, Excel, Power BI, N8N");
        await digitar("- Inteligência Artificial: Engenharia de Prompt");
        await digitar("- Design e Web: Photoshop, CorelDraw");
        await digitar("- Hardware e Suporte: Montagem e manutenção");
        await digitar("- Gestão: Equipes, vendas e atendimento");
    });
}

function cursos() {
    escreverTela(async () => {
        await digitar("=== CURSOS E CERTIFICAÇÕES ===");
        await digitar("- Embaixadores Universitários da DIO");
        await digitar("- Automação com N8N básico – 26h");
        await digitar("- Inteligência Artificial – 40h");
        await digitar("- HTML5 e CSS3 – 200h");
    });
}

function experiencia() {
    escreverTela(async () => {
        await digitar("=== EXPERIÊNCIA PROFISSIONAL ===");
        await digitar("2P Sacolas Personalizadas (2018 - 2026)");
        await digitar("AlmaViva do Brasil (2014 - 2017)");
    });
}

function objetivo() {
    escreverTela(async () => {
        await digitar("=== OBJETIVO PROFISSIONAL ===");
        await digitar("Busco estágio em Desenvolvimento ou Suporte TI.");
    });
}

function formacao() {
    escreverTela(async () => {
        await digitar("=== FORMAÇÃO ACADÊMICA ===");
        await digitar("Análise e Desenvolvimento de Sistemas (2027)");
    });
}

function projetos() {
    escreverTela(async () => {
        await digitar("=== PROJETOS ===");
        await digitar("Aguardando dados...");
    });
}

function curriculoCompleto() {
    escreverTela(async () => {
        await digitar("===== CURRÍCULO COMPLETO =====");
        await digitar("Walisson Patrick Helmer");
        await digitar("Contato: (31) 99373-6336 (WhatsApp)");
        await digitar("E-mail: wpatrickhelmer@gmail.com");
        await digitar("LinkedIn: linkedin.com/in/walissonpatrickhelmer");
        await digitar("GitHub: github.com/WalissonPatrickHelmer");
        await digitar("Cidade: Belo Horizonte | Bairro: Lindeia | CEP: 30690-260");
        await digitar("--------------------------------------------------");
        await digitar("OBJETIVO PROFISSIONAL:");
        await digitar("Busco oportunidade de estágio em Desenvolvimento de Sistemas ou Suporte em TI...");
        await digitar("--------------------------------------------------");
        await digitar("FORMAÇÃO ACADÊMICA:");
        await digitar("- ADS: Faculdade Impacta (Prev: Dez/2027)");
        await digitar("- Técnico em Programação e Jogos Digitais - 1200h");
        await digitar("--------------------------------------------------");
        await digitar("HABILIDADES TÉCNICAS:");
        await digitar("- Python, HTML5, CSS3, SQL, Neo4j, Excel, Power BI, N8N");
        await digitar("- IA: Engenharia de Prompt");
        await digitar("- Design: Photoshop, CorelDraw");
        await digitar("- Hardware: Montagem e Manutenção");
        await digitar("--------------------------------------------------");
        await digitar("CURSOS E CERTIFICAÇÕES:");
        await digitar("- Embaixadores DIO | N8N Básico | Jornada IA | HTML/CSS 200h");
        await digitar("--------------------------------------------------");
        await digitar("EXPERIÊNCIA PROFISSIONAL:");
        await digitar("- 2P Sacolas Personalizadas (01/2018 - 01/2026)");
        await digitar("- AlmaViva do Brasil (11/2014 - 12/2017)");
        await digitar("- Monticeli Buzzo (06/2010 - 02/2012)");
        await digitar("- Carrefour S.A. (10/2007 - 05/2010)");
    });
}

async function finalizar() {
    limpar();
    await digitar("Programa finalizado.");
}

window.onload = async () => {
    limpar();
    await saudacao();
};