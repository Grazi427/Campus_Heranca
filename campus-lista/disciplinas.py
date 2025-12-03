disc_optativas = [] # Armazena as optativas disponíveis

class Disciplina:
    # Representa uma disciplina vinculada a um curso específico
    def __init__(self, nome, carga_horaria):
        self.nome = nome

        try:
            self.carga_horaria = int(carga_horaria)
        except ValueError:
            self.carga_horaria = 0

    def get_tipo(self):
        return 'Obrigaória'

    def __str__(self):
        return f"   -> Disciplina: {self.nome} | CH: {self.carga_horaria}h | Tipo: {self.get_tipo()}"

class DisciplinaOptativa(Disciplina):
    # Disciplinas que não pertencem a um curso fixo
    def __init__(self, nome, carga_horaria):
        super().__init__(nome, carga_horaria)
    
    def get_tipo(self):
        return 'Optativa'

