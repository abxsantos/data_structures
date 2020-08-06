def poisonous_plants(plants):
    position = 0
    for current_plant in plants:
        if position == 0:
            pass
        else:
            left_plant = plants[position-1]
            if left_plant < current_plant:
                plants.pop(position)
        position += 1
    return plants

initial_plants = [6,5,8,4,7,10,9]
# plants = [3, 2, 5, 4]
# plants = [4, 3, 7, 5, 6, 4, 2]

days = 1
last_day_plants = [[6,5,8,4,7,10,9]]
list_of_days = []
while days < 5:
    last_day_plants.append(poisonous_plants(last_day_plants.pop()))
    days += 1
print(last_day_plants)