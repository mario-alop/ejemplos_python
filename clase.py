class Demo:
    atrib_estatico = 123 # compartido por todos los objetos 
    def __init__(self,numero):
        self.atrib_instancia = numero # específico de cada objeto

c1 = Demo(456)
c2 = Demo(789)

#Valorinicial
print(f"C1:Estatico {c1.atrib_estatico} - Instancia: {c1.atrib_instancia}") 
#output: C1:Estatico123 - Instancia:456 
print(f"C2:Estatico{ c2.atrib_estatico} - Instancia: {c2.atrib_instancia}")
#output: C2:Estatico123 - Instancia:789

Demo.atrib_estatico=-1

print(f"C2:Estatico {c2.atrib_estatico} - Instancia: {c2.atrib_instancia}") 
#output: C2:Estatico -1 - Instancia: 789 
print(f"C2:Estatico {c2.atrib_estatico} - Instancia: {c2.atrib_instancia}") 
#output: C2:Estatico -1 - Instancia: 789

c1.atrib_instancia = 999

print(f"C1:Estatico {c1.atrib_estatico} - Instancia: {c1.atrib_instancia}")
#output:C1:Estatico -1 - Instancia: 999

print(f"C2: Estatico {c2.atrib_estatico} - Instancia: {c2.atrib_instancia}")
#output: C2: Estatico -1 - Instancia: 789