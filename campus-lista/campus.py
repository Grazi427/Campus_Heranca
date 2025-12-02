campus_list = []
class Campus:
    # Representa um campus da universidade com seus cursos
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.cursos = []
        
    def encontrar_curso(self, nome_curso):
        # Auxiliar para buscar um Curso na lista por nome
        for curso in self.cursos:
            if curso.nome == nome_curso:
                return curso
        return None

    def adicionar_curso(self, curso):
        # Adiciona um objeto Curso à lista de cursos
        self.cursos.append(curso)

    def remover_curso(self, nome_curso):
        # Remove um curso pelo nome, iterando pela lista
        curso_para_remover = self.encontrar_curso(nome_curso)
        if curso_para_remover:
            self.cursos.remove(curso_para_remover)
            return True
        return False

    def __str__(self):
        # Percorre a lista de cursos para a string de exibição
        cursos_str = "\n    ".join(str(curso) for curso in self.cursos)
        if not cursos_str:
            cursos_str = "Nenhum curso cadastrado."
            
        return (
            f"---- Campus: {self.nome} ----\n"
            f"  Endereço: {self.endereco}\n"
            f"  Cursos:\n    {cursos_str}"
        )
    