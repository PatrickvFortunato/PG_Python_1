import csv
from datetime import datetime

class Questionario:
    def __init__(self):
        self.perguntas = [
       
    
    def coletar_respostas(self):
        respostas = []
        for pergunta in self.perguntas:
            resposta = input(pergunta)
            if resposta == '00':
                return None
            respostas.append(resposta)
        respostas.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        return respostas

class ArmazenadorCSV:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
    
    def escrever_no_csv(self, respostas):
        with open(self.nome_arquivo, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(respostas)

def main():
    questionario = Questionario()
    armazenador = ArmazenadorCSV('respostas.csv')
    
    with open('respostas.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Idade", "Gênero", "Resposta_1", "Resposta_2", "Resposta_3", "Resposta_4", "Data e Hora"])
    
    while True:
        respostas = questionario.coletar_respostas()
        if not respostas:
            break
        armazenador.escrever_no_csv(respostas)
    
    print("Respostas registradas com sucesso!")

if __name__ == "__main__":
    main()