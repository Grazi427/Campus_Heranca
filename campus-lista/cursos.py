class Curso:
    # Representa um curso oferecido por um campus
    def __init__(self, nome, duracao_semestres):
        self.nome = nome
        self.duracao_semestres = duracao_semestres
        self.disciplinas = [] # Lista para armazenar disciplinas do curso

    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    def __str__(self):
        # Mostra o curso e lista suas disciplinas
        base_str = f"Curso: {self.nome} ({self.duracao_semestres} semestres)"
        if self.disciplinas:
            disc_str = "\n".join([str(d) for d in self.disciplinas])
            return f"{base_str}\n{disc_str}"
        return f"{base_str} (Sem disciplinas cadastradas)"