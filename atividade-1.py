# Atividade 1 : Fibonacci

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