from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', resultado=(''))


@app.route('/verificar', methods=['POST'])  # Define uma rota '/verificar' que aceita apenas requisições POST
def verificar():

    # Obtém o número enviado no formulário HTML e verifica o maior e o menor

   maior = 0
   menor = 999
   soma = 0
   qntd = 0
   media = 0

   for qntd in range(10):
        numero = int(request.form['numero' + str(qntd)])
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
        soma += numero
        qntd += 1

   media = soma / qntd
   return render_template('index.html', maior=maior, menor=menor, media=media)

if __name__ == '__main__':
    # Inicia o servidor Flask em modo de depuração se este script for executado diretamente
    app.run(debug=True)