n = [1, 2, 3, 4, 5]
n_str = list(map(str,n))
print(f"Lista de números como strings: {', '.join(n_str)}")

Ramos = ["Programación", "Física", "Cálculo", "Habilidades Comunicativas"]
long = list(filter(lambda x: len(x) > 7, Ramos))
print(long)

a = [1, 2, 3, 4]
b = ["A", "B", "C", "D"]

comprimir = list(zip(a,b))
print(comprimir)