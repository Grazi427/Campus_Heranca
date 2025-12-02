from crud import adicionar_campus,excluir_campus,editar_campus,visualizar_campus,adicionar_curso,editar_curso,excluir_curso,adicionar_disciplina_regular,gerenciar_optativas
from campus import campus_list
from disciplinas import disc_optativas
from _init_ import Campus,Curso,Disciplina,DisciplinaOptativa

def exibir_menu():
    # Exibe o menu de opções
    print("\n" + "="*40)
    print("Sistema de Gestão Universitária da UFC")
    print("="*40)
    print("\n--- Gerenciamento de Campus ---")
    print("1. Adicionar Campus")
    print("2. Visualizar campus")
    print("3. Editar Campus (Endereço)")
    print("4. Excluir Campus")
    print("\n--- Gerenciamento de Cursos ---")
    print("5. Adicionar Curso")
    print("6. Editar Curso (Nome/Duração)")
    print("7. Excluir Curso")
    print("\n--- Gerenciamento de Disciplinas ---")
    print("8. Adicionar Discilina Obrigatória a um Curso")
    print("9. Gerenciar Disciplinas do Campus")
    print("0. Sair")
    print("="*40)

def main():
    # Função principal que executa o menu
        exibir_menu()
        escolha = input("Escolha uma opção: ").strip()
        
        if escolha == '1':
            adicionar_campus()
        elif escolha == '2':
            visualizar_campus()
        elif escolha == '3':
            editar_campus()
        elif escolha == '4':
            excluir_campus()
        elif escolha == '5':
            adicionar_curso()
        elif escolha == '6':
            editar_curso()
        elif escolha == '7':
            excluir_curso()
        elif escolha == '8':
            adicionar_disciplina_regular()
        elif escolha == '9':
            gerenciar_optativas()
        elif escolha == '0':
            print("Obrigado por usar o sistema! Encerrando...")
            return exit()
        else:
            print("Opção inválida. Por favor, tente novamente.")
        main()



#  Inicialização com dados de exemplo (opcional)

print("\n" + "="*40)
resp = input('Deseja inicializar com exemplos? (s/n): ').strip().lower()

if resp == 's':
    print("\n" + "="*40)
    c1 = Campus("Pici", "Av. Univ")
    c2 = Campus("Benfica", "Av. Carapinima")
    
    curso_dir = Curso("Direito", 10)
    curso_dir.adicionar_disciplina(Disciplina("Direito Civil I", 64))
    curso_dir.adicionar_disciplina(Disciplina("Direito Romano", 32))
    
    curso_ti = Curso("Eng. Software", 8)
    curso_ti.adicionar_disciplina(Disciplina("Algoritmos", 96))
    curso_ti.adicionar_disciplina(Disciplina("POO", 64))

    c1.adicionar_curso(curso_dir)
    c2.adicionar_curso(curso_ti)
    
    campus_list.extend([c1, c2])
    
    # Adicionando optativas globais de exemplo
    disc_optativas.append(DisciplinaOptativa("Libras", 64))
    disc_optativas.append(DisciplinaOptativa("Empreendedorismo", 32))

elif resp == 'n':
    print("\n" + "="*40)
    print('Sistema iniciado vazio.')


main()