lista_nome = {
    'Nome': "",
    'Idade': "",
    'Email': "",
    'Área de Interesse': "",
    'Escolaridade': "",
}

lista_competencias = {
    'Lógica': 0,
    'Trabalho em Equipe': 0,
    'Comunicação': 0,
    'Resolução de Problemas': 0,
    'Adaptabilidade': 0,
}

def cadastrar_usuario():
    """Coleta e exibe os dados básicos do usuário."""
    print("\n--- Cadastro de Usuário ---\n")
    dados_usuario = lista_nome.copy() 
    for chave in dados_usuario.keys():
        dados_usuario[chave] = input(f"Por favor, insira seu {chave}: ")
    print("\n\n[Cadastro] Detalhes do usuário cadastrado:")
    for chave, valor in dados_usuario.items():
        print(f"{chave}: {valor}")
        
    return dados_usuario

def pontuar_competencias():
    """Coleta a pontuação (1 a 5) das competências comportamentais."""
    print("\n--- Pontuação de Competências ---\n")
    print("Por favor, avalie suas competências de 1 a 5:")
    pontuacoes = lista_competencias.copy()
    
    for chave in pontuacoes.keys():
        while True:
            try:
                valor = int(input(f"Qual sua pontuação em '{chave}' (1 a 5)? "))
                if 1 <= valor <= 5:
                    pontuacoes[chave] = valor
                    break
                else:
                    print("Por favor, insira um número entre 1 e 5.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número inteiro.")

    print("\n\n[Cadastro] Pontuações de competências registradas com sucesso!\n\n")
    return pontuacoes

if __name__ == '__main__':
    DADOS_USUARIO = cadastrar_usuario()
    COMPETENCIAS_USUARIO = pontuar_competencias()
else:
    pass