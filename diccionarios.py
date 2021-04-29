dic = {

    "nombre":"Alex"
}
print(dic)

dic.update({"nombre":"gabriel"})

#print(dir(dic))

#num = input()

# if int(num) < 10 or int(num) > 20:
#     print("el numero esta fuera del rango")
# else:
#     print(f"el numero {num} esta entre 10 y 20")

lista = (1,2,3,4,5,6,7)
dicc = {"nombre": "alex","apellido": "varela","nombre":"keidy","apellido":"castro"}



# metodos y propiedades diccionarios

# ['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']


midiccionario = {"Alemania":"Berlin", "Francia":"Paris"}

print(midiccionario)

midiccionario["Francia"]="marsella"#modifica elementos del diccionario colocando la clave y asignando el nuevo valor

midiccionario["Portugal"] = "lisboa"#agregamos elementos al dicciionario colocando entre corchetes la nueva clave y su valor

print(midiccionario)

del midiccionario['Alemania']#elimina elementos del dccionario colocando el nombre de la clave
print(midiccionario)

otrodic = {23 : "alex", "alex":[1,2]}
otrodic[23]="varela"
print(otrodic)

a,b = otrodic["alex"]

print("valor de a: ", a, " valor de b: ", b)

mitupla = ["venezuela","colombia"]
midicci = {mitupla[0]:"caracas", mitupla[1]:"bogota"}
print(midicci)

print(midicci.keys())#devuelve el nombre de las claves
print(midicci.values())#devuelve los valores de las claves
print(len(midicci))#devuelve la longitud del diccionarioi







