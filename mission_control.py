nome_missao = "Acqua Vita"
nome_equipe = "Sideralis"

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

dados_missao = [
    [24, 92, 88, 96, 90],
    [27, 80, 72, 94, 85],
    [31, 65, 58, 91, 70],
    [36, 42, 38, 87, 55],
    [39, 28, 19, 78, 35],
    [34, 55, 32, 82, 50]
]

def analisar_temperatura(valor):
    if valor < 18:
        return "ATENÇÃO", 1, "Temperatura abaixo do ideal"
    elif valor <= 30:
        return "NORMAL", 0, "Temperatura estável"
    elif valor <= 35:
        return "ATENÇÃO", 1, "Temperatura elevada"
    else:
        return "CRÍTICO", 2, "Risco de superaquecimento"


def analisar_comunicacao(valor):
    if valor < 30:
        return "CRÍTICO", 2, "Comunicação com a base em nível crítico"
    elif valor < 60:
        return "ATENÇÃO", 1, "Comunicação instável"
    else:
        return "NORMAL", 0, "Comunicação estável"


def analisar_bateria(valor):
    if valor < 20:
        return "CRÍTICO", 2, "Bateria em nível crítico"
    elif valor < 50:
        return "ATENÇÃO", 1, "Bateria abaixo do recomendado"
    else:
        return "NORMAL", 0, "Energia estável"


def analisar_oxigenio(valor):
    if valor < 80:
        return "CRÍTICO", 2, "Oxigênio em nível crítico"
    elif valor < 90:
        return "ATENÇÃO", 1, "Oxigênio abaixo do ideal"
    else:
        return "NORMAL", 0, "Oxigênio adequado"


def analisar_estabilidade(valor):
    if valor < 40:
        return "CRÍTICO", 2, "Estabilidade operacional crítica"
    elif valor < 70:
        return "ATENÇÃO", 1, "Estabilidade operacional reduzida"
    else:
        return "NORMAL", 0, "Estabilidade operacional adequada"


def classificar_ciclo(risco):
    if risco <= 2:
        return "MISSÃO ESTÁVEL"
    elif risco <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"


def gerar_recomendacao(risco):
    if risco <= 2:
        return "Manter operação estável e continuar monitoramento."
    elif risco <= 5:
        return "Monitorar sistemas em atenção e preparar plano de contingência."
    else:
        return "Ativar modo de segurança e priorizar suporte à vida, energia e comunicação."

def analisar_tendencia(primeiro, ultimo):
    if ultimo > primeiro:
        return "A missão apresentou tendência de piora."
    elif ultimo < primeiro:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão permaneceu estável em relação ao início."


def identificar_area_mais_afetada(pontos):
    maior = max(pontos)
    indice = pontos.index(maior)
    return areas_monitoradas[indice], maior


print("======================================================")
print("MISSION CONTROL AI")
print("======================================================")

print(f"Missão: {nome_missao}")
print(f"Equipe: {nome_equipe}")
print(f"Quantidade de ciclos analisados: {len(dados_missao)}")

print("======================================================")

riscos_ciclos = []
pontuacao_areas = [0, 0, 0, 0, 0]

soma_temperatura = 0
soma_comunicacao = 0
soma_bateria = 0
soma_oxigenio = 0
soma_estabilidade = 0

maior_risco = -1
ciclo_mais_critico = 0
quantidade_ciclos_criticos = 0

for indice, ciclo in enumerate(dados_missao):

    temperatura, comunicacao, bateria, oxigenio, estabilidade = ciclo

    soma_temperatura += temperatura
    soma_comunicacao += comunicacao
    soma_bateria += bateria
    soma_oxigenio += oxigenio
    soma_estabilidade += estabilidade

    print(f"\nCICLO {indice + 1}")
    print("---------------------------------------------------")

    risco_total = 0

    status, pontos, msg = analisar_temperatura(temperatura)
    risco_total += pontos
    pontuacao_areas[0] += pontos
    print(f"Temperatura: {temperatura}°C | {status} | {msg}")

    status, pontos, msg = analisar_comunicacao(comunicacao)
    risco_total += pontos
    pontuacao_areas[1] += pontos
    print(f"Comunicação: {comunicacao}% | {status} | {msg}")

    status, pontos, msg = analisar_bateria(bateria)
    risco_total += pontos
    pontuacao_areas[2] += pontos
    print(f"Bateria: {bateria}% | {status} | {msg}")

    status, pontos, msg = analisar_oxigenio(oxigenio)
    risco_total += pontos
    pontuacao_areas[3] += pontos
    print(f"Oxigênio: {oxigenio}% | {status} | {msg}")

    status, pontos, msg = analisar_estabilidade(estabilidade)
    risco_total += pontos
    pontuacao_areas[4] += pontos
    print(f"Estabilidade: {estabilidade}% | {status} | {msg}")

    classificacao = classificar_ciclo(risco_total)

    print(f"\nPontuação de risco do ciclo: {risco_total}")
    print(f"Classificação do ciclo: {classificacao}")
    print(f"Recomendação: {gerar_recomendacao(risco_total)}")

    riscos_ciclos.append(risco_total)

    if risco_total > maior_risco:
        maior_risco = risco_total
        ciclo_mais_critico = indice + 1

    if classificacao == "MISSÃO CRÍTICA":
        quantidade_ciclos_criticos += 1

media_temperatura = soma_temperatura / len(dados_missao)
media_comunicacao = soma_comunicacao / len(dados_missao)
media_bateria = soma_bateria / len(dados_missao)
media_oxigenio = soma_oxigenio / len(dados_missao)
media_estabilidade = soma_estabilidade / len(dados_missao)

risco_medio = sum(riscos_ciclos) / len(riscos_ciclos)

area_mais_afetada, pontos_area = identificar_area_mais_afetada(
    pontuacao_areas
)

classificacao_final = classificar_ciclo(round(risco_medio))

print("\n")
print("======================================================")
print("RELATÓRIO FINAL DA MISSÃO")
print("======================================================")

print(f"Missão: {nome_missao}")
print(f"Equipe: {nome_equipe}")

print(f"\nMédia de temperatura: {media_temperatura:.2f} °C")
print(f"Média de comunicação: {media_comunicacao:.2f}%")
print(f"Média de bateria: {media_bateria:.2f}%")
print(f"Média de oxigênio: {media_oxigenio:.2f}%")
print(f"Média de estabilidade: {media_estabilidade:.2f}%")

print(f"\nCiclo mais crítico: Ciclo {ciclo_mais_critico}")
print(f"Maior pontuação de risco: {maior_risco}")
print(f"Risco médio da missão: {risco_medio:.2f}")
print(f"Quantidade de ciclos críticos: {quantidade_ciclos_criticos}")

print("\nTendência da missão:")
print(analisar_tendencia(riscos_ciclos[0], riscos_ciclos[-1]))

print("\nPontuação acumulada por área:")

for i in range(len(areas_monitoradas)):
    print(f"{areas_monitoradas[i]}: {pontuacao_areas[i]} pontos")

print(f"\nÁrea mais afetada: {area_mais_afetada}")

print(f"\nClassificação final da missão: {classificacao_final}")

print("\nConclusão:")

if classificacao_final == "MISSÃO ESTÁVEL":
    print("A missão manteve condições seguras durante toda a operação.")
elif classificacao_final == "MISSÃO EM ATENÇÃO":
    print("A missão apresentou instabilidades moderadas e requer monitoramento contínuo.")
else:
    print("A missão apresentou riscos críticos e exige intervenção imediata.")

print("======================================================")
