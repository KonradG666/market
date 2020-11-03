print("Lista zakupów:")

lista_zakupów = {
"piekarnia": ['chleb', 'bułki', 'pączek'],
"warzywniak": ['marchew', 'seler', 'rukola']
}

capitalize_list = {k.capitalize():[ele.capitalize() for ele in v] for k, v in lista_zakupów.items()}

for sklep, produkty in capitalize_list.items():
        print(f"idę do {sklep} i kupuję tu następujące rzeczy:{produkty}")

print (f"W sumie kupuję {sum([len(lista_zakupów[x]) for x in lista_zakupów if isinstance(lista_zakupów[x] , list)])} produktów")
