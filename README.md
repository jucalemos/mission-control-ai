# mission-control-ai

Projeto desenvolvido para a Global Solution 2026.1 da disciplina de Pensamento Computacional e Automação com Python.

## Sobre o Projeto

O Mission Control AI é um sistema desenvolvido em Python para simular o monitoramento de uma missão espacial experimental.

A aplicação analisa informações importantes da missão, como temperatura, comunicação, bateria, oxigênio e estabilidade operacional. Com base nesses dados, o sistema identifica situações de risco, classifica cada ciclo de monitoramento e gera recomendações para auxiliar na tomada de decisões.

## Objetivo

O objetivo do projeto é aplicar conceitos fundamentais de programação para criar um sistema capaz de:

* Monitorar ciclos de uma missão espacial;
* Analisar indicadores operacionais;
* Gerar alertas automáticos;
* Calcular níveis de risco;
* Identificar tendências da missão;
* Determinar a área mais afetada;
* Produzir um relatório final com os resultados obtidos.

## Funcionalidades

* Análise automática dos dados da missão;
* Classificação dos indicadores em Normal, Atenção ou Crítico;
* Cálculo da pontuação de risco por ciclo;
* Classificação geral de cada ciclo monitorado;
* Identificação da tendência da missão (melhora, piora ou estabilidade);
* Identificação da área mais afetada durante a operação;
* Geração de recomendações automáticas;
* Relatório final exibido no terminal.

## Estrutura dos Dados

O sistema utiliza uma matriz chamada `dados_missao`, em que cada linha representa um ciclo de monitoramento e cada coluna representa uma informação da missão:

```python
[temperatura, comunicacao, bateria, oxigenio, estabilidade]
```

Exemplo:

```python
dados_missao = [
    [24, 92, 88, 96, 90],
    [27, 80, 72, 94, 85],
    [31, 65, 58, 91, 70],
    [36, 42, 38, 87, 55],
    [39, 28, 19, 78, 35],
    [34, 55, 32, 82, 50]
]
```

## Tecnologias Utilizadas

* Python 3
* Matrizes e listas
* Estruturas condicionais
* Estruturas de repetição
* Funções

## Organização do Projeto

```text
mission-control-ai/
│
├── README.md
└── mission_control.py
```

## Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/jucalemos/mission-control-ai.git
```

2. Acesse a pasta do projeto:

```bash
cd mission-control-ai
```

3. Execute o programa:

```bash
python mission_control.py
```

## Informações da Missão

**Nome da Missão:** Acqua Vita

**Equipe:** Sideralis

### Integrantes

* Erick Banhos de Castro — RM 572131
* Erick Yu Xiang Li — RM 569305
* Júlia Lemos Souza — RM 569089

## Repositório

https://github.com/jucalemos/mission-control-ai.git

## Vídeo Pitch

https://youtu.be/Q9x5RE6Vph4

## Conclusão

O projeto permitiu aplicar conceitos de Python como listas, matrizes, funções, estruturas de repetição e condicionais.

Com a análise dos dados simulados da missão, o sistema consegue identificar situações de risco e apresentar um relatório com o estado geral da operação.
