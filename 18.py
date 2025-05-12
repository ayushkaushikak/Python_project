city=['Delhi', 'Faridabad', 'Kota', 'Mumbai', 'Shimla', 'prayagraj','Goa', 'Dharmshala', 'Banaras']

city_sort= sorted(city, key= lambda x:len(x))

print(city_sort)


print(sorted(city, key= lambda x:len(x)))
print(sorted(city, key= lambda x:len(x), reverse= True))
