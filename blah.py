# A sample world map as a 2D array
# P represents the player's position
# F represents part of a forest/a forest biome
# To represents a town
world_map = [["P", " ", "F", "To"],
             [" ", "F", "F", "F"],
             [" ", " ", "", "F"]]

# This global variable stores the previous value of a given index before the player moves
current_position = " "

# These two global variables store the coordinates of the player on the map
# At the start of the game, the player's starting position is world_map[0][0]
position_x = 0
position_y = 0

# This function iterates through the larger list and then the smaller lists/arrays, gets the player's position on 
# a map
def get_player_position():
    global position_x
    global position_y
    for x in range(len(world_map)):
        for y in range(len(world_map[x])):
            if (world_map[x][y] == "P"):
                position_x = x
                position_y = y
                print(position_x, position_y)
                
# # This function finds the position of the player and moves the player east, if possible  
# def travel_east():
#     global current_position
#     global position_x
#     global position_y
#     for x in range(len(world_map)):
#         for y in range(len(world_map[x])):
#             if (world_map[x][y] == "P"):
#                 position_x = x
#                 position_y = y
#                 print(position_x, position_y)
#     if (position_y < len(world_map[position_x]) - 1):
#         next_area = world_map[position_x][position_y + 1]
#         world_map[position_x][position_y + 1] = "P"
#         world_map[position_x][position_y] = current_position
#         current_position = next_area
#         print("\nYou travel a little east before stopping to take a rest.")
#         print(current_position)
#         print(world_map)        
#     elif (position_y == len(world_map[x]) - 1):
#         print("\n There is nothing beyond this point. You cannot travel further east. \n")
#                 # playerActions()
                
# travel_east()
# travel_east()
# travel_east()
# travel_east()

# This function finds the position of the player and moves the player west, if possible
# def travel_west():
#     global current_position
#     global position_x
#     global position_y
#     for x in range(len(world_map)):
#         for y in range(len(world_map[x])):
#             if (world_map[x][y] == "P"):
#                 position_x = x
#                 position_y = y
#                 print(position_x, position_y)
#     if (position_y == 0):
#         print("\n There is nothing beyond this point. You cannot travel further west. \n")
#         print(world_map)
#     if (position_y > 0 ):
#         next_area = world_map[position_x][position_y - 1]
#         world_map[position_x][position_y - 1] = "P"
#         world_map[position_x][position_y] = current_position
#         current_position = next_area
#         print("\nYou travel a little west before stopping to take a rest.")
#         print(current_position)
#         print(world_map)
        
# travel_west()
# travel_west()
# travel_west()
# travel_west()

# This functions finds the position of the player and moves the player north, if possible
# def travel_north():
#     global current_position
#     global position_x
#     global position_y
#     for x in range(len(world_map)):
#         for y in range(len(world_map[x])):
#             if (world_map[x][y] == "P"):
#                 position_x = x
#                 position_y = y
#                 print(position_x, position_y)
#     if (position_x == 0):
#         print("\n There is nothing beyond this point. You cannot travel further north. \n")
#         print(world_map)
#     if (position_x > 0):
#         next_area = world_map[position_x - 1][position_y]
#         world_map[position_x - 1][position_y] = "P"
#         world_map[position_x][position_y] = current_position
#         current_position = next_area
#         print("\nYou travel a little north before stopping to take a rest.")
#         print(current_position)
#         print(world_map)
        
# travel_north()
# travel_north()
# travel_north()

# This function finds the position of the player and moves the player south, if possible
def travel_south():
    global current_position
    global position_x
    global position_y
    for x in range(len(world_map)):
        for y in range(len(world_map[x])):
            if (world_map[x][y] == "P"):
                position_x = x
                position_y = y
                print(position_x, position_y)
    if (position_x < len(world_map) - 1):
        next_area = world_map[position_x + 1][position_y]
        world_map[position_x + 1][position_y] = "P"
        world_map[position_x][position_y] = current_position
        current_position = next_area
        print("\nYou travel a little south before stopping to take a rest.")
        print(current_position)
        print(world_map)
    elif (position_x == len(world_map) - 1):
        print("\n There is nothing beyond this point. You cannot travel further south. \n")
        print(world_map)
        
travel_south()
travel_south()
travel_south()
travel_south()