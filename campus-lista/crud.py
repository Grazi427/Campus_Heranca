from campus import campus_list
from disciplinas import disc_optativas
from _init_ import Campus,Curso,DisciplinaOptativa,Disciplina


def encontrar_campus(nome_campus):
    # Auxiliar para buscar um Campus na lista global por nome
    for campus in campus_list:
        if campus.nome == nome_campus:
            return campus
    return None

def adicionar_campus():
    # Adiciona um novo campus ao sistema
    print("\n"+"-"*15," Adicionar Novo Campus "+"-"*15)
    nome = input("Nome do Campus: ").strip()
    if not nome:
        print("O nome do campus não pode ser vazio.")
        return
        
    # Busca na lista se o nome já existe
    if encontrar_campus(nome):
        print(f"O Campus '{nome}' já existe.")
        return
        
    endereco = input("Endereço do Campus: ").strip()
    
    novo_campus = Campus(nome, endereco)
    # Adiciona à lista
    campus_list.append(novo_campus)
    print(f"Campus '{nome}' adicionado com sucesso!")

def visualizar_campus():
    # Exibe todos os campus e seus cursos (iterando pela lista)
    print("\n"+"-"*15," Campus Cadastrados "+"-"*15)
    if not campus_list:
        print("Nenhum campus cadastrado.")
        return
        
    for campus in campus_list:
        print('\n')
        print(campus)


def editar_campus():
    # Edita o endereço de um campus existente
    visualizar_campus()
    if not campus_list:
        return
        
    print("\n"+"-"*15," Editar Campus "+"-"*15)
    nome = input("Digite o nome do Campus que deseja editar: ").strip()
    
    campus_encontrado = encontrar_campus(nome)
    
    if campus_encontrado:
        print(f"Campus selecionado: {campus_encontrado.nome} (Endereço atual: {campus_encontrado.endereco})")
        novo_endereco = input("Digite o NOVO endereço (ou deixe vazio para manter o atual): ").strip()
        
        if novo_endereco:
            campus_encontrado.endereco = novo_endereco
            print(f"Endereço do Campus '{nome}' atualizado para: {novo_endereco}")
        else:
            print("Nenhuma alteração de endereço realizada.")
    else:
        print(f"Campus '{nome}' não encontrado.")

def excluir_campus():
    # Exclui um campus do sistema (removendo da lista)
    visualizar_campus()
    if not campus_list:
        return
        
    print("\n+"-"*15, Excluir Campus "+"-"*15)
    nome = input("Digite o nome do Campus que deseja EXCLUIR: ").strip()
    
    campus_para_excluir = encontrar_campus(nome)
    
    if campus_para_excluir:
        confirmacao = input(f"Tem certeza que deseja excluir o Campus '{nome}' e todos os seus cursos? (s/n): ").lower().strip()
        if confirmacao == 's':
            # Remove o objeto Campus da lista
            campus_list.remove(campus_para_excluir)
            print(f"Campus '{nome}' excluído com sucesso!")
        else:
            print(f"Exclusão do Campus '{nome}' cancelada.")
    else:
        print(f"Campus '{nome}' não encontrado.")


def selecionar_campus(select):
    # Auxiliar para selecionar um campus para ações de curso.
    visualizar_campus()
    if not campus_list:
        print("Por favor, adicione um campus primeiro.")
        return None
        
    print("\n"+"-"*15,f" {select} Curso "+"-"*15)
    nome_campus = input("Digite o nome do Campus onde o curso será gerenciado: ").strip()
    
    return encontrar_campus(nome_campus)

def adicionar_curso():
    # Adiciona um novo curso a um campus
    campus = selecionar_campus("Adicionar")
    if not campus:
        return
        
    nome_curso = input("Nome do Novo Curso: ").strip()
    if not nome_curso:
        print("O nome do curso não pode ser vazio.")
        return
        
    # Verifica a existência na lista de cursos do campus
    if campus.encontrar_curso(nome_curso):
        print(f"O Curso '{nome_curso}' já existe no Campus '{campus.nome}'.")
        return
        
    try:
        duracao = int(input("Duração (semestres): ").strip())
        campus.adicionar_curso(Curso(nome_curso, duracao))
        print("Curso adicionado!")
    except ValueError:
        print("Duração inválida.")

def editar_curso():
    # Edita o nome ou duração de um curso
    campus = selecionar_campus("Editar")
    if not campus:
        return

    if not campus.cursos:
        print(f"O Campus '{campus.nome}' não possui cursos para editar.")
        return

    print("\nCursos existentes neste campus:")
    # Itera pela lista de cursos
    for curso in campus.cursos:
        print(f"- {curso}")
        
    nome_curso_antigo = input("Digite o nome do Curso que deseja editar: ").strip()
    
    curso_encontrado = campus.encontrar_curso(nome_curso_antigo)
    
    if curso_encontrado:
        print(f"\nCurso selecionado: {curso_encontrado.nome} (Duração atual: {curso_encontrado.duracao_semestres} semestres)")
        
        # Editar Nome
        novo_nome = input("Digite o NOVO nome do curso (ou deixe vazio para manter): ").strip()
        if novo_nome and novo_nome != nome_curso_antigo:
            # Verifica se o novo nome já existe
            if campus.encontrar_curso(novo_nome):
                print(f"O nome '{novo_nome}' já está em uso. Alteração de nome cancelada.")
                return
            
            # Basta atualizar o atributo nome no objeto Curso
            curso_encontrado.nome = novo_nome
            print(f"Nome do curso alterado de '{nome_curso_antigo}' para '{novo_nome}'.")
            
        # Editar Duração
        while True:
            nova_duracao_str = input(f"Digite a NOVA duração em semestres (atual: {curso_encontrado.duracao_semestres}, ou deixe vazio para manter): ").strip()
            if not nova_duracao_str:
                break
            try:
                nova_duracao = int(nova_duracao_str)
                if nova_duracao > 0:
                    curso_encontrado.duracao_semestres = nova_duracao
                    print(f"Duração do curso '{curso_encontrado.nome}' atualizada para {nova_duracao} semestres.")
                    break
                else:
                    print("A duração deve ser um número positivo.")
            except ValueError:
                print("Por favor, digite um número inteiro ou deixe vazio.")
    else:
        print(f"Curso '{nome_curso_antigo}' não encontrado no Campus '{campus.nome}'.")

def excluir_curso():
    # Exclui um curso de um campus
    campus = selecionar_campus("Excluir")
    if not campus:
        return
        
    if not campus.cursos:
        print(f"O Campus '{campus.nome}' não possui cursos para excluir.")
        return

    print("\nCursos existentes neste campus:")
    for curso in campus.cursos:
        print(f"- {curso}")

    nome_curso = input("Digite o nome do Curso que deseja EXCLUIR: ").strip()
    
    # Chama o método que remove da lista
    if campus.remover_curso(nome_curso):
        print(f"Curso '{nome_curso}' excluído do Campus '{campus.nome}' com sucesso!")
    else:
        print(f"Curso '{nome_curso}' não encontrado no Campus '{campus.nome}'.")

def adicionar_disciplina_regular():
    # Adiciona uma disciplina normal dentro de um curso específico
    campus = selecionar_campus("Selecionar Campus")
    if not campus: return

    print("\nCursos do Campus:")
    for c in campus.cursos: print(f"- {c.nome}")
    
    nome_curso = input("Nome do Curso: ").strip()
    curso = campus.encontrar_curso(nome_curso)
    
    if not curso:
        print("Curso não encontrado.")
        return

    nome_disc = input("Nome da Disciplina: ").strip()
    try:
        ch = int(input("Carga Horária da Disciplina(horas): ").strip())
        nova_disc = Disciplina(nome_disc, ch)
        curso.adicionar_disciplina(nova_disc)
        print(f"Disciplina '{nome_disc}' adicionada ao curso '{curso.nome}' com sucesso!")
    except ValueError:
        print("Carga horária deve ser número.")

def gerenciar_optativas():
    # Cria disciplinas optativas no banco global
    campus = selecionar_campus("Selecionar Campus")
    if not campus: return

    print(f"\n--- Banco de Disciplinas Optativas do Campus ---")
    if disc_optativas:
        for opt in disc_optativas:
            print(opt)
    else:
        print("Nenhuma optativa cadastrada.")
    
    print("\n1. Criar Nova Optativa")
    print("0. Voltar")
    op = input("Opção: ").strip()
    
    if op == '1':
        nome = input("Nome da Optativa: ").strip()
        try:
            ch = int(input("Carga Horária: ").strip())
            nova_opt = DisciplinaOptativa(nome, ch)
            disc_optativas.append(nova_opt)
            print(f"Optativa '{nome}' criada para o Campus com sucesso!")
        except ValueError:
            print("Valor inválido.")