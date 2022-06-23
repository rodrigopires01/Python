class Enta:
    def __init__(self):
        self.idcurso = None
        self.nomecurso = None
        self.iddisc = None
        self.nomedisc = None
        self.cursos = []
        self.disciplinas = []

    def setcurso(self, idcurso, nomecurso):
        self.idcurso = idcurso
        self.nomecurso = nomecurso

    def getcurso(self):
        return self.idcurso, self.nomecurso

    def setdisc(self, iddisc, nomedisc):
        self.iddisc = iddisc
        self.nomedisc = nomedisc

    def getdisc(self):
        return self.iddisc, self.nomedisc


if __name__ == '__main__':
    escola = Enta()

    escola.setcurso('GRSI', 'Gestão de Rede e Sistemas Informáticos')
    escola.cursos.append(escola.getcurso())
    escola.setdisc('MAT', 'Matemática')
    escola.disciplinas.append(escola.getdisc())

    print(escola.getdisc())
