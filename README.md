# Etapa Técnica Target

## Questão 1 : Fibonacci
```
def fibonacci(num):
    posterior = 0
    ultimoPosterior = 1
    numeroPerteceASequencia = False

    print(posterior)
    print(ultimoPosterior)
    proximovalor = 0
    while proximovalor < num:
        proximovalor = posterior + ultimoPosterior
        posterior = ultimoPosterior
        ultimoPosterior = proximovalor
        if proximovalor == num:
            numeroPerteceASequencia = True
        if proximovalor > num:
            break
        print(proximovalor)
    print(f"O número pertence à sequência: ","Sim" if numeroPerteceASequencia is True else "Não")
fibonacci(45)
```

## Questão 2: Quantidade de vezes de um caractere
```

import re

def encontrarCaractere(string, caractere):
    x = re.findall(f"[{caractere}]", string, re.IGNORECASE)
    print(len(x))

encontrarCaractere("A vida é uma paraíso", 'a')
```

## Questão 3:
Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);

Reposta  = 77

## Questão 4:
 a) 9 b)128 c)49 d)81 e)13 f) 20

 ## Questão 5:
Primeiro eu ligava o interruptor A, ligava o Interruptor B por 3 min e apagava e deixava o Interruptor C desligado , entrava na primeira sala. Se fosse a acessa, o interruptor A era dela, se estivesse apagada porém quente o interruptor B era dela, caso apagada e fria o interruptor era C.
Segundo eu ligava outro interruptor, e deixava outro apagado. Entrava na segunda sala, se acessa o interruptor ligado era dela e se não o interruptor era o desligado. Assim descobrindo o interruptor de cada lâmpada.
