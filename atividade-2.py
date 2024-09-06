# Atividade 2: Quantidade de vezes de um caractere
import re

def encontrarCaractere(string, caractere):
    x = re.findall(f"[{caractere}]", string, re.IGNORECASE)
    print(len(x))

encontrarCaractere("A vida é uma paraíso", 'a')
