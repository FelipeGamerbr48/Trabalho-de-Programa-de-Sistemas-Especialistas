# ============================================================
# SISTEMA ESPECIALISTA - ASSISTENCIA TECNICA DE COMPUTADORES
# Area: Gabinete e monitor
# Tecnica: Regras de producao
# Motor de inferencia: Encadeamento para frente
# ============================================================


# ------------------------------------------------------------
# 1. BASE DE CONHECIMENTO
# ------------------------------------------------------------

# Armazena os fatos identificados durante a consulta ao usuario.
fatos = set()

# Armazena os diagnosticos encontrados pelo sistema.
diagnosticos = set()


# ------------------------------------------------------------
# 2. REGRAS DE PRODUCAO
# ------------------------------------------------------------

regras = [
    # REGRA 1
    {
        "nome": "Regra 1",
        "condicoes": {"pc_liga", "monitor_sem_imagem"},
        "conclusao": "possivel_problema_video"
    },
    # REGRA 2
    {
        "nome": "Regra 2",
        "condicoes": {"pc_nao_liga", "led_apagado"},
        "conclusao": "possivel_problema_fonte"
    },
    # REGRA 3
    {
        "nome": "Regra 3",
        "condicoes": {"pc_nao_liga", "led_acende"},
        "conclusao": "possivel_problema_energia_interna"
    },
    # REGRA 4
    {
        "nome": "Regra 4",
        "condicoes": {"pc_desliga_sozinho", "pc_esquenta"},
        "conclusao": "possivel_superaquecimento"
    },
    # REGRA 5
    {
        "nome": "Regra 5",
        "condicoes": {"pc_liga", "bipes"},
        "conclusao": "possivel_problema_memoria_ram"
    },
    # REGRA 6
    {
        "nome": "Regra 6",
        "condicoes": {"pc_liga", "imagem_distorcida"},
        "conclusao": "possivel_problema_placa_video"
    },
    # REGRA 7
    {
        "nome": "Regra 7",
        "condicoes": {"pc_liga", "monitor_sem_sinal"},
        "conclusao": "possivel_problema_conexao_video"
    },
    # REGRA 8
    {
        "nome": "Regra 8",
        "condicoes": {"monitor_apaga", "pc_continua_ligado"},
        "conclusao": "possivel_problema_monitor"
    },
    # REGRA 9
    {
        "nome": "Regra 9",
        "condicoes": {"pc_lento", "armazenamento_cheio"},
        "conclusao": "possivel_problema_armazenamento"
    },
    # REGRA 10
    {
        "nome": "Regra 10",
        "condicoes": {"pc_liga", "nao_inicia_sistema"},
        "conclusao": "possivel_problema_boot"
    },
    # REGRA 11
    {
        "nome": "Regra 11",
        "condicoes": {"caiu_liquido", "pc_apresenta_falhas"},
        "conclusao": "possivel_dano_por_liquido"
    },
    # REGRA 12
    {
        "nome": "Regra 12",
        "condicoes": {"houve_batida", "pc_nao_liga"},
        "conclusao": "possivel_dano_fisico_interno"
    },
    # REGRA 13
    {
        "nome": "Regra 13",
        "condicoes": {"sujeira_acumulada", "pc_esquenta"},
        "conclusao": "possivel_superaquecimento_por_sujeira"
    },
    # REGRA 14
    {
        "nome": "Regra 14",
        "condicoes": {"aplicativo_nao_oficial", "pc_lento"},
        "conclusao": "possivel_software_malicioso"
    },
    # REGRA 15
    {
        "nome": "Regra 15",
        "condicoes": {"mau_contato", "pc_desliga_sozinho"},
        "conclusao": "possivel_mau_contato_interno"
    },
    # REGRA 16
    {
        "nome": "Regra 16",
        "condicoes": {"pouca_ram", "pc_lento"},
        "conclusao": "possivel_insuficiencia_memoria_ram"
    },
]



# ------------------------------------------------------------
# 3. MOTOR DE INFERENCIA
# ------------------------------------------------------------

def motor_inferencia(fatos):

    # Indica se alguma regra foi ativada.
    houve_inferencia = True

    # Continua verificando enquanto novas conclusoes aparecem.
    while houve_inferencia:

        houve_inferencia = False

        # Percorre todas as regras da base de conhecimento.
        for regra in regras:

            # Verifica se todas as condicoes da regra
            # estao presentes na base de fatos.
            if regra["condicoes"].issubset(fatos):

                conclusao = regra["conclusao"]

                # Evita repetir uma conclusao ja encontrada.
                if conclusao not in fatos:

                    # Adiciona a conclusao como novo fato.
                    fatos.add(conclusao)

                    # Armazena o diagnostico.
                    diagnosticos.add(conclusao)

                    # Indica que uma nova inferencia ocorreu.
                    houve_inferencia = True

                    print("\nRegra ativada:", regra["nome"])

                    print("Conclusao:", conclusao)

    # Retorna os diagnosticos encontrados.
    return diagnosticos


# ------------------------------------------------------------
# 4. COLETA DE INFORMACOES
# ------------------------------------------------------------

def perguntar(pergunta, fato_sim, fato_nao):

    resposta = input(pergunta + " (s/n): ").strip().lower()

    # Registra o fato correspondente a resposta.
    if resposta == "s":

        fatos.add(fato_sim)

    elif resposta == "n":

        fatos.add(fato_nao)

    else:

        print("Resposta invalida. Considere apenas s ou n.")

        # Repete a pergunta em caso de resposta invalida.
        return perguntar(pergunta, fato_sim, fato_nao)


# ------------------------------------------------------------
# 5. INTERFACE DO SISTEMA
# ------------------------------------------------------------

def iniciar_sistema():

    print("=" * 55)

    print(" SISTEMA ESPECIALISTA - ASSISTENCIA TECNICA")

    print("=" * 55)

    print("\nEste sistema analisa problemas relacionados ao gabinete")
    print("e ao monitor do computador.")

    print("\nNao realiza diagnosticos de perifericos.")

    print("\nResponda as perguntas com s (sim) ou n (nao).")

    print("-" * 55)


   # --------------------------------------------------------
    # Perguntas sobre o computador e o monitor
    # --------------------------------------------------------

    perguntar(
        "O computador liga?",
        "pc_liga",
        "pc_nao_liga"
    )

    perguntar(
        "O LED do gabinete acende?",
        "led_acende",
        "led_apagado"
    )

    perguntar(
        "O monitor apresenta imagem?",
        "monitor_com_imagem",
        "monitor_sem_imagem"
    )

    perguntar(
        "O monitor apresenta a mensagem sem sinal?",
        "monitor_sem_sinal",
        "monitor_com_sinal"
    )

    perguntar(
        "O computador emite bipes ao ligar?",
        "bipes",
        "sem_bipes"
    )

    perguntar(
        "A imagem apresenta distorcoes?",
        "imagem_distorcida",
        "imagem_normal"
    )

    perguntar(
        "O computador desliga sozinho?",
        "pc_desliga_sozinho",
        "pc_nao_desliga_sozinho"
    )

    perguntar(
        "O computador apresenta aquecimento excessivo?",
        "pc_esquenta",
        "pc_nao_esquenta"
    )

    perguntar(
        "O monitor apaga enquanto o computador continua ligado?",
        "monitor_apaga",
        "monitor_nao_apaga"
    )

    perguntar(
        "O computador esta lento?",
        "pc_lento",
        "pc_nao_lento"
    )

    perguntar(
        "O armazenamento esta cheio?",
        "armazenamento_cheio",
        "armazenamento_normal"
    )

    perguntar(
        "O computador liga, mas nao inicia o sistema operacional?",
        "nao_inicia_sistema",
        "inicia_sistema"
    )

    # --------------------------------------------------------
    # Perguntas referentes as novas regras (Regras 11 a 16)
    # --------------------------------------------------------

    perguntar(
        "O computador sofreu alguma batida ou queda?",
        "houve_batida",
        "sem_batida"
    )

    perguntar(
        "Caiu algum liquido no computador?",
        "caiu_liquido",
        "sem_liquido"
    )

    perguntar(
        "Depois disso, o computador comecou a apresentar falhas?",
        "pc_apresenta_falhas",
        "pc_sem_falhas"
    )

    perguntar(
        "Existe sujeira acumulada dentro do gabinete?",
        "sujeira_acumulada",
        "sem_sujeira"
    )

    perguntar(
        "Foi baixado ou instalado algum aplicativo nao oficial?",
        "aplicativo_nao_oficial",
        "sem_aplicativo_nao_oficial"
    )

    perguntar(
        "Existe suspeita de mau contato em algum componente ou conexao?",
        "mau_contato",
        "sem_mau_contato"
    )

    perguntar(
        "O computador possui pouca memoria RAM?",
        "pouca_ram",
        "ram_suficiente"
    )


    # --------------------------------------------------------
    # 6. EXECUCAO DO MOTOR DE INFERENCIA
    # --------------------------------------------------------

    print("\n" + "=" * 55)

    print(" ANALISANDO AS INFORMACOES")

    print("=" * 55)

    resultado = motor_inferencia(fatos)


    # --------------------------------------------------------
    # 7. APRESENTACAO DOS RESULTADOS
    # --------------------------------------------------------

    print("\n" + "=" * 55)

    print(" RESULTADO DO DIAGNOSTICO")

    print("=" * 55)


    # Se encontrou algum diagnostico:
    if resultado:

        print("\nPossiveis problemas identificados:")

        for diagnostico in resultado:

            # Converte o nome interno para uma descricao.
            descricao = diagnostico.replace(
                "possivel_", ""
            ).replace("_", " ")

            print("- " + descricao.capitalize())

        print("\nObservacao:")

        print("O resultado representa uma possibilidade.")

        print("A confirmacao depende de uma avaliacao tecnica.")


    # Se nenhuma regra conseguiu identificar o problema:
    else:

        print("\nO sistema nao conseguiu identificar")
        print("um possivel problema com as informacoes fornecidas.")

        print("\nRecomendacao:")

        print("Procure diretamente a assistencia tecnica")
        print("para realizar uma avaliacao especializada.")


    print("\n" + "=" * 55)

    print(" FIM DO DIAGNOSTICO")

    print("=" * 55)


# ------------------------------------------------------------
# 8. EXECUCAO DO PROGRAMA
# ------------------------------------------------------------

iniciar_sistema()