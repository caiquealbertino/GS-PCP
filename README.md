README: Agente de Carreira Adaptativa (ACA)

Este projeto implementa um Agente de Carreira Adaptativa (ACA), um sistema orientado a objetos em Python que simula uma ferramenta inteligente de orientação de carreiras. O objetivo principal é analisar o perfil profissional de um usuário (competências técnicas e comportamentais) e gerar recomendações personalizadas para o futuro do trabalho, incluindo sugestões de novas carreiras, trilhas de aprendizado (Upskilling) e caminhos de transição (Reskilling), utilizando o poder de processamento de linguagem natural (LLM) da OpenAI.

Propósito do Projeto

O projeto conecta a lógica de programação e a automação (via API de LLMs) ao desenvolvimento humano e profissional.

O ACA atende aos seguintes objetivos:

    Organização e Análise de Dados: Utiliza estruturas de dados nativas do Python (dict, list) para armazenar informações do perfil e pontuações de competências.
    
    Análise Inteligente: Emprega a IA (LLM gpt-4o-mini) para analisar o perfil e o mercado de trabalho, estimando o impacto da automação.
    
    Recomendação Personalizada: Gera recomendações práticas de Upskilling (aprimoramento na carreira atual) e Reskilling (transição para novas carreiras) para preparar o usuário para o trabalho do futuro.

Pré-requisitos e Configuração

Para executar este projeto, você precisa ter o Python instalado e uma chave de API válida da OpenAI.

1. Instalação de Dependências
Instale a biblioteca openai (a flag -q é usada para uma instalação "quiet", ou seja, sem exibir todos os logs): !pip install -q openai

3. Configuração da Chave de API
O projeto utiliza a variável de ambiente OPENAI_API_KEY para autenticar as chamadas à API. Você DEVE configurar esta variável antes de executar o script main.py.

No Windows (Prompt de Comando): set OPENAI_API_KEY="SUA_CHAVE_AQUI"

No macOS/Linux (Terminal): export OPENAI_API_KEY="SUA_CHAVE_AQUI"

Estrutura e Funcionamento do Código

O projeto é dividido em três arquivos principais:

    cadastro.py	Contém as estruturas de dados (lista_nome, lista_competencias) e as funções interativas (cadastrar_usuario, pontuar_competencias) para coletar os dados de entrada do usuário via terminal.
    
    agente_aca.py	Define a classe principal AgenteCarreiraAdaptativa. É o coração do projeto, onde as chamadas à API da OpenAI são realizadas.
    
    main.py	Orquestra a execução. Importa dados de cadastro.py, inicializa o Agente de agente_aca.py e chama as funções de análise e recomendação.


Classe AgenteCarreiraAdaptativa (em agente_aca.py)

A classe possui as seguintes funcionalidades principais:

    f1_analise_e_recomendacao(profissao, competencias):
    Propósito: Analisa o perfil com base na profissão e nas competências pontuadas.
    Resultado: Gera recomendações de Carreiras Futuras, Trilhas de Hard Skills e Áreas de Soft Skills para aprimoramento (Upskilling).

    f2_simulacao_reskilling(profissao_atual, interesse_transicao, analise_perfil_f1):
    Propósito: Foca na transição de carreira (Reskilling).
    Resultado: Mapeia Habilidades Transferíveis da carreira antiga para a nova e apresenta um Desafio Prático de Entrevista para a nova área.

Execução do Projeto

Após configurar a API Key e instalar a dependência, basta rodar o arquivo principal: python main.py

O programa guiará o usuário pelas seguintes etapas interativas no terminal:

    Coleta de Dados: Solicitará o preenchimento de informações básicas (nome, email, área de interesse, etc.) e a pontuação das competências (Lógica, Comunicação, etc., de 1 a 5).
    
    Análise F1: O Agente usará as informações para gerar o relatório de análise e o plano de Upskilling.
    
    Análise F2: O Agente perguntará sobre uma área de transição desejada e fornecerá o caminho de Reskilling e o desafio prático.
