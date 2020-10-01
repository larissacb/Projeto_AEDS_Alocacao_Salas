class Turma:
    def __init__(self, curso, disciplina, professor, num_alunos, turno_pref): #construtor
        self.curso = curso
        self.disciplina = disciplina
        self.professor = professor
        self.num_alunos = num_alunos
        self.turno_pref = turno_pref

    def get_curso(self):
        return self.curso

    def get_disciplina(self):
        return self.disciplina

    def get_professor(self):
        return self.professor

    def get_num_alunos(self):
        return self.num_alunos

    def get_turno_pref(self):
        return self.turno_pref
    def imprimir_inf(self):
        print(self.curso, self.disciplina, self.professor, self.num_alunos)