import csv
from datetime import datetime

class Pesquisa:
    def __init__(self):
        self.perguntas = [
            '1. Você já considerou contratar um seguro para o seu celular?',
            '2. Você decidiu não contratar um seguro de celular?',
            '3. Você acredita que o custo do seguro de celular é um fator importante na decisão de não contratá-lo?',
            '4. Você confia na capacidade das seguradoras de pagar em caso de necessidade?',
            '5. Você acha que os riscos de danos ou perda do celular são baixos o suficiente para não justificar a compra de um seguro?',
            '6. Você já teve experiências negativas com seguradoras que influenciaram sua decisão de não contratar um seguro de celular?',
            '7. Você acredita que a cobertura oferecida pelos seguros de celular é suficiente para suas necessidades?',
            '8. Você já considerou outras formas de proteger seu celular além de um seguro, como capas protetoras ou programas de garantia estendida?',
            '9. Se os seguros de celular oferecessem preços mais acessíveis ou benefícios adicionais, você reconsideraria contratar um seguro para o seu celular?'
        ]

    def iniciarPesquisa(self):
        with open('respostas.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            header = ['Idade', 'Gênero', *self.perguntas, 'Data e Hora']
            writer.writerow(header)

            while True:
                idade = input("Informe sua idade (00 para encerrar): ")
                if idade == '00':
                    break
                
                genero = input("Informe seu gênero (1 = Masculino, 2 = Feminino, 3 = Outros/Não responder): ")
                if genero not in ['1', '2', '3']:
   dataHora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                linha = [idade, genero, *respostas, dataHora]
                writer.writerow(linha)
                print("Respostas registradas com sucesso!")

if __name__ == "__main__":
    pesquisa = Pesquisa()
    pesquisa.iniciarPesquisa()                    print("Opção de gênero inválida. Tente novamente.")
                    continue

                respostas = []
                for pergunta in self.perguntas:
                    while True:
                        resposta = input(f"{pergunta} (1 = Sim, 2 = Não, 3 = Não sei responder): ")
                        if resposta in ['1', '2', '3']:
                            respostas.append(resposta)
                            break
                        else:
                            print("Resposta inválida. Por favor, responda com 1, 2 ou 3.")

                dataHora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                linha = [idade, genero, *respostas, dataHora]
                writer.writerow(linha)
                print("Respostas registradas com sucesso!")

if __name__ == "__main__":
    pesquisa = Pesquisa()
    pesquisa.iniciarPesquisa()