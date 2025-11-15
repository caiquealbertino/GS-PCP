import os
import openai
from agente_aca import AgenteCarreiraAdaptativa
from cadastro import cadastrar_usuario, pontuar_competencias

try:
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY') 
    if not OPENAI_API_KEY:
        print("AVISO: Variável OPENAI_API_KEY não definida. As chamadas à API falharão.")
        client = None 
    else:
        client = openai.OpenAI(api_key=OPENAI_API_KEY)

    print("\n=======================================================")
    print("Agente de Carreira Adaptativa- Inicializando")
    print("=======================================================\n")

    DADOS_USUARIO = cadastrar_usuario()
    COMPETENCIAS_PONTUADAS = pontuar_competencias()

    competencias_formatadas = (
        f"Hard Skill: {DADOS_USUARIO.get('Área de Interesse')}. "
        f"Soft Skills: {COMPETENCIAS_PONTUADAS}"
    )

    agente = AgenteCarreiraAdaptativa(client_instance=client, model_name="gpt-4o-mini")

    print("\n--- ETAPA F1: Análise e Recomendação de Carreira ---\n")
    
    profissao_base = DADOS_USUARIO.get('Área de Interesse', 'Profissional Desconhecido')
    
    resultado_f1 = agente.f1_analise_e_recomendacao(
        profissao=profissao_base, 
        competencias=competencias_formatadas
    )
    
    print("\nResultado da Análise F1:")
    print(resultado_f1)

    print("\n--- ETAPA F2: Simulação de Reskilling e Desafio ---\n")
    
    transicao_interesse = input("\nPara qual nova área você gostaria de fazer um Reskilling (Ex: Data Scientist)? ")

    resultado_f2 = agente.f2_simulacao_reskilling(
        profissao_atual=profissao_base,
        interesse_transicao=transicao_interesse,
        analise_perfil_f1=resultado_f1 
    )

    print("\n\nResultado da Simulação F2:")
    print(resultado_f2)

except Exception as e:
    print(f"\nOcorreu um erro na execução do main.py: {e}")
    print("Verifique se o arquivo 'agente_aca.py' existe e se o cliente OpenAI está configurado.")