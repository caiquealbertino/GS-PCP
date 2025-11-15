import openai
import os

class AgenteCarreiraAdaptativa:

    def __init__(self, client_instance=None, model_name="gpt-4o-mini"):
        """
        Inicializa o agente. O cliente OpenAI deve ser configurado externamente.
        """
        self.client = client_instance
        self.model_name = model_name

    def _gerar_conteudo(self, system_prompt, user_prompt):
        """
        Função auxiliar para chamar a API OpenAI (Chat Completions).
        """
        if self.client is None:
            return "Erro: O cliente OpenAI não foi inicializado."
            
        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.7,
                top_p=0.95
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Erro ao gerar conteúdo: {str(e)}"

    def f1_analise_e_recomendacao(self, profissao, competencias):
        """
        Analisa o perfil (profissão e competências) e gera recomendações de 
        carreiras futuras e trilhas de aprimoramento (Upskilling).
        """
        system_prompt = (
            "Você é o 'Agente de Carreira Adaptativa'. "
            "Sua tarefa é analisar um perfil profissional e gerar recomendações personalizadas"
            "para o futuro do trabalho"
            "focando nos três pontos principais:"
            "Análise e Recomendação de Carreira"
            "Profissão Analisada: [Nome da Profissão]"
            "Competências Fornecidas: [Lista de Competências]\n\n"
            "1. Recomendações de Carreira Futura"
            "Sugira 2-3 carreiras (ou papéis híbridos) que combinem o perfil e as tendências da IA. "
            "Carreira 1 (Ex: Data Storyteller): [Por que é adequada e qual o foco]"
            "Carreira 2 (Ex: Arquiteto de Prompt): [Por que é adequada e qual o foco]\n\n"
            "2. Trilha de Aprendizado (Hard Skills)"
            "Sugira 3 Hard Skills cruciais para o futuro e um recurso de aprendizado para cada uma.\n"
            "[Hard Skill 1]: [Recurso Sugerido]"
            "[Hard Skill 2]: [Recurso Sugerido]\n\n"
            "3. Áreas de Aprimoramento (Soft Skills)"
            "Sugira 2-3 Soft Skills (competências comportamentais) essenciais para aumentar a resiliência à automação."
            "[Soft Skill 1]: [Breve justificativa]"
            "[Soft Skill 2]: [Breve justificativa]"
        )

        user_prompt = (
            f"Profissão Atual: {profissao}\n"
            f"Competências (Técnicas e Comportamentais) do Usuário: {competencias}"
        )

        return self._gerar_conteudo(system_prompt, user_prompt)

    def f2_simulacao_reskilling(self, profissao_atual, interesse_transicao, analise_perfil_f1):
        """
        Sugere um caminho de Reskilling, mapeia habilidades transferíveis e 
        gera um desafio prático de entrevista para a nova área.
        """
        system_prompt = (
            "Você é o 'Agente de Carreira Adaptativa'. "
            "Sua tarefa é simular uma transição de carreira (Reskilling). "
            "Use as informações de perfil (F1) e o interesse de transição para gerar um "
            "plano de ação e um desafio prático para entrevista.\n\n"
            "Caminho de Reskilling e Desafio (F2)\n\n"
            "Transição Desejada: De [Profissão Atual] para [Nova Carreira]\n\n"
            "1. Mapeamento de Habilidades Transferíveis"
            "Com base no seu perfil, estas são as habilidades que você já possui e podem ser aproveitadas:\n"
            "[Habilidade 1]: [Aplicação na Nova Carreira]"
            "[Habilidade 2]: [Aplicação na Nova Carreira]\n\n"
            "2. Desafio Prático de Entrevista"
            "Para aprimorar sua preparação, considere este desafio prático de entrevista para a nova área:"
            "Cenário/Problema:[Crie um cenário relevante para a nova carreira]"
            "Pergunta Chave:[Uma pergunta que exige a aplicação de uma nova habilidade]"
            "Dica:[Sugestão de foco para a resposta (ex: Use o método STAR)]"
        )

        user_prompt = (
            f"Profissão Atual: {profissao_atual}\n"
            f"Interesse de Transição: {interesse_transicao}\n"
            f"Análise de Perfil Anterior (para contexto): {analise_perfil_f1}"
        )

        return self._gerar_conteudo(system_prompt, user_prompt)