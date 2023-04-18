#Atividade contínua 03

#Faça um programa web que exiba os 100 primeiros números primos, 

#rode em um container docker.

#A entrega é o link do repositorio do github com os arquivos Dockerfile e primos.py e o print do resultado do programa no navegador.

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def numerosPrimos():
    qtd = 100
    n = 2
    primos = []
    ehPrimo = 1
    
    while len(primos) < qtd:
        for i in range(2, int(n**0.5) + 1):
        #for i in range(2, n):
            if n % i == 0:
                ehPrimo = 0
                break
        if ehPrimo == 1:
            primos.append(n)
        ehPrimo = 1
        n += 1

    return primos


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050)