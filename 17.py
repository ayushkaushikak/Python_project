city=['Delhi', 'Faridabad', 'Kota', 'Mumbai', 'Shimla', 'prayagraj','Goa', 'Dharmshala', 'Banaras']
def length(city):
    return len(city)
city_sort= sorted(city, key= length)
print(city_sort)