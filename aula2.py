# names = []
# numbers = [10, 5, 7, 9, 1]
# products = ["notbook", "mouse", "teclado", "headset"]

# products.append("celular")
# products.append("tablet")

# for i in products:
#     print(i)
    
# print(products)

# products.insert(0, "PC")

# print(products)
# removido = products.pop(2)

# print(products)
# print(removido)

series = [
            "Breaking Bad", "Wandinha",
            "Friends", "Black Mirror", 
            "La Casa de Papel", "Prision Break", 
            "Game of Thrones", "You", 
            "Panico","Black List",
            "The Mentalist", "Suits"            
          ]
print("-"*60)
print("Minha lista de series")
print("_"*60)
print(series)
print(len(series))
print("As 5 primeiras sao:", series[0:5])
print("As 4 ultimas sao: ", series[-4:])
print(f"Em ordem afabetica:{sorted(series)}")
print(f"Posicao do seriado PANICO {series.index('Panico')}")