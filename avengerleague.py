import random
dc_list = "Flash", "Mooney", "Fish", "Super", "Man", "Super", "girl", "Cat", "Woman",\
          "Joker", "Bain", "Green", "Arrow", "Penguin", "Doctor", "Freeze", "Poison", "Ivy", "Cyborg", "Beast", "Boy"

marvel_list = "Iron", "Thor", "Captain", "America", "Spider", "Man", "Hulk", \
              "Doctor", "Strange", "Black", "Panther", "Thanos", "Ghost", "Rider", "Venom", "winter", "Soldier", "Sand",\
              "Wanda", "Vision"

while True:
    print(dc_list[random.randint(1, 15)], end=" ")
    print(marvel_list[random.randint(1, 17)])
