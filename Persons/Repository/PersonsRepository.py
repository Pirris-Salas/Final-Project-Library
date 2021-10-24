#Database diccionary - This is the default data for Persons
# Clean Arquitecture Principles

#import Persons.Ui.PersonsMenu as menu

personsArray = {1:["Nayarit Aguirre Aguirre", "nayari@gmail.com"],
                2:["Antonio José Araya Ruiz", "antonio@gmail.com"],
                3:["María Fernanda Arguedas González", "maria@gmail.com"],
                4:["José Daniel Benavides Obando", "jose@gmail.com"],
                5:["Carlos Andrés Berrocal Espinoza", "carlos@gmail.com"],
                6:["Rita Irene Chang Rodriguez", "rita@gmail.com"],
                7:["Jorge Andrés Chaves Gomez", "jorge@gmail.com"],
                8:["Daniel Cordero Araya", "daniel@gmail.com"],
                9:["Jonathan Andrés Flores Cedeño", "jonathan@gmail.com"],
                10:["Wilfredo Gomez Herrera", "wilfredo@gmail.com"],
                11:["David Gomez Zumbado", "david@gmail.com"],
                12:["Stefany Andrea Masis Aguilar", "stefany@gmail.com"],
                13:["Magaly Matamoros Zamora", "magaly@gmail.com"],
                14:["Danny Mendoza González", "danny@gmail.com"],
                15:["Ronald Fabian Meneses Montero", "ronald@gmail.com"],
                16:["Gabriel Alberto Serrano Rosabal", "gabriel@gmail.com"],
                17:["Víctor José Porras Herrera", "victor @gmail.com"]}

persons = personsArray


"""
contador = 0
resultsID = []
for datos in persons.items():
    listaPersonas = list(datos)
    contador = contador + 1
    
    if str.__contains__(str(listaPersonas[1]), "luis".capitalize()):
        resultsID.append(contador)

          
if(len(resultsID) > 0):
    print("*********************************************")
    print("* W E  F O U N D  T H E S E   R E S U L T S *")
    print("******************************************\n")
    for id in resultsID:
        person = persons.get(int(id)) 
        print("*********************************************************")
        print(f"ID: {id}\nName: {person[0]}\nEmail: {person[1]}\n")
        print("*********************************************************")                   
else:
        print("\nNo Results Found!. Please try again.")
    #general.clear()
    #continue
  """  