key = "16n06a09t05a11k02e31v07e02n16m05a31t06h11e07u09s02"

# só pode conter até 40 caracteres, n pode ter '"\/[]{} e outros símbolos muito usados em programação
senha = "@#%ABCabc123"

#criptografador
def str_xor(s1, s2):
    return "".join([chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(s1, s2)])

criptografada = str_xor(senha, key)

descriptografada = str_xor(criptografada, key)

# retorno
print("Senha entrada: " + senha + "\n")
print("Senha guardada:" + criptografada + "\n")
print("Senha recuperada" + descriptografada + "\n")