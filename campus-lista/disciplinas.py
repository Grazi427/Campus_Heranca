disc_optativas = [] # Armazena as optativas disponíveis

class Disciplina:
    # Representa uma disciplina vinculada a um curso específico
    def __init__(self, nome, carga_horaria):
        self.nome = nome
        self.carga_horaria = carga_horaria

    def __str__(self):
        return f"   -> Disciplina: {self.nome} | CH: {self.carga_horaria}h"

class DisciplinaOptativa(Disciplina):
    # Disciplinas que não pertencem a um curso fixo
    def __init__(self, nome, carga_horaria):
        super().__init__(nome, carga_horaria)
        self.tipo = "Optativa"

    def __str__(self):
        return f"   -> [OPTATIVA]: {self.nome} | CH: {self.carga_horaria}h"

