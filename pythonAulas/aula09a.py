frase = "Curso em Vídeo Python"
print(len(frase))

print(frase)
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15:2])
print(frase[1::2])
print(frase.count('o'))
print(frase.upper().count('O'))
print(frase.replace('Python', 'Android')) # se imprimir, estará com Python ainda. Nesse caso, se quiser alterar a frase colocar ela numa nova variável

print('-' * 20)

frase1 = "   Curso em Vídeo Python"
print(len(frase1))
print(len(frase1.strip()))
print(frase1.find('Vídeo'))
print(frase1.lower().find('vídeo'))
print(frase1.split()) # cria uma lista separada por itens
dividido = frase1.split()
print(dividido[0])
print(dividido[3][1])