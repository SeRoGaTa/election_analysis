counties_dict = {}
counties_dict["Arapahoe"]=422829
counties_dict["Denver"]=463353
counties_dict["Jefferson"]=432438
# print(counties_dict)
# print(len(counties_dict))
# print(counties_dict.items())
# print(counties_dict.keys())
# print(counties_dict.values())
# print(counties_dict.get("Denver"))

voting_data=[]
voting_data.append({"county":"Arapahoe","registered_voters":422829})
voting_data.append({"county":"Denver","registered_voters": 463353})
voting_data.append({"county":"Jefferson","registered_voters": 432438})
# print(len(voting_data))
# voting_data.append({"county":"El paso","registered_voters": 461149})
# voting_data.remove({"county":"Arapahoe","registered_voters":422829})
# print(voting_data)
# voting_data.remove({"county":"El paso","registered_voters": 461149})
# voting_data.append({"county":"Denver","registered_voters": 463353})
# print(voting_data)

# counties=["Arapahoe", "Denver", "Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])

# counties=["Arapahoe","Denver","Jefferson"]
# if "El paso" in counties:
#     print("El paso is in the list of counties.")
# else :
#     print("El paso is not in list of counties.")

# if "El paso" in counties and "Arapahoe" in counties:
#     print("El paso and Arapahoe are in the list of counties.")
# else :
#     print("El paso and Arapahoe are not in list of counties.")

# if "El paso" in counties or "Arapahoe" in counties:
#     print("El paso or Arapahoe are in the list of counties.")
# else :
#     print("El paso and Arapahoe are not in list of counties.")

# for county in counties:
#     print(county)

# #Esto me va a traer todas las keys de una lista
# for i in range(len(counties)):
#     print(counties[i])

#Esto me va a traer todas las keys de un diccionario
# for county in counties_dict:
#     print(county)

#Esto me va a traer todas las keys de un diccionario
# for county in counties_dict.keys():
#     print(county)

# #Esto me va a traer todos los valores del diccionario (Values)
# for voters in counties_dict.values():
#     print(voters)

# #Esto me va a traer todos los valores del diccionario (Values)
# for county in counties_dict:
#     print(counties_dict[county])

# #Esto me va a traer todos los valores del diccionario (Values)
# for county in counties_dict:
#     print(counties_dict.get(county))

# #Esto me va a traer las keys y los valores de un diccionario (siempre la primer variable son las keys y la segunda los valores en un for)
# for county, voters in counties_dict.items():
#     # print(county, voters)
#     print(f'{county} county has {voters} registered voters.')

#Esto me imprime todos los dicionarios dentro de un diccionario
# for county_dict in voting_data:
#     print(county_dict)

# Esto me imprime las keys y los valores de un diccionario anidado
# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)

# for county, voters in counties_dict.items():
#     print(f'{county} county has {voters} registered voters')

