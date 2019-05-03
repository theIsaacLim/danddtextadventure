import random
'''
Key for dungeon map generation:
0 ---> No room / Empty space
1 ---> Normal room / Empty room
2 ---> Encounter room / Monster room
3 ---> Dungeon start / Entrance
4 ---> Portal room / Exit
5 ---> Treasure room
'''
dungeon_map = [[0,0,0,0,0,0,0,0,0,0]]
for i in range(9):
    dungeon_map.append([0,0,0,0,0,0,0,0,0,0])

dungeon_start = [ ## Presets with the entrance to the dungeon
    [[0,0,1,0,0], # Entrance 1 - The loop
    [1,1,1,1,0],
    [1,0,0,1,1],
    [1,0,0,1,0],
    [3,1,1,1,5]],
    [[1,1,1,0,0], # Entrance 2 - The pincers
    [1,0,0,0,0],
    [1,1,5,0,1],
    [1,0,1,0,1],
    [3,1,1,1,1]],
    [[0,0,1,0,0], # Entrance 3 - The broken fish
    [5,0,1,0,0],
    [1,1,1,1,1],
    [1,0,1,0,1],
    [3,1,1,0,0]],
    [[0,0,1,0,0], # Entrance 4 - The thingy-ma-bob
    [5,1,1,0,0],
    [0,1,0,1,1],
    [1,1,1,1,0],
    [3,0,0,0,0]],
    [[5,0,1,0,0], # Entrance 5 - The weird cross
    [1,0,1,0,0],
    [1,1,1,1,1],
    [0,0,1,0,0],
    [3,1,1,0,0]]
]
dungeon_end = [
    [[0,0,1,0,4], # Exit 1 - The rabbit
    [1,1,1,1,1],
    [1,0,1,0,0],
    [0,1,1,0,0],
    [0,0,1,1,5]],
    [[0,0,1,1,4], # Exit 2 - The two golf clubs
    [0,0,1,0,0],
    [1,1,1,1,1],
    [0,0,1,0,1],
    [0,0,1,0,5]],
    [[0,0,0,0,4], # Exit 3 - The dog head
    [0,1,1,1,1],
    [1,1,0,1,0],
    [0,0,1,1,5],
    [0,0,1,0,0]],
    [[5,1,1,1,4], # Exit 4 - The fish
    [0,1,0,0,1],
    [1,1,0,0,1],
    [0,1,1,1,1],
    [0,0,1,0,0]],
    [[1,1,1,1,4], # Exit 5 - The rabbit ears
    [1,0,1,0,1],
    [1,0,5,1,1],
    [0,0,0,0,1],
    [0,0,1,1,1]]
]
dungeon_preset = [
    [[0,1,1,1,5], # Preset 1 - The Monster face
    [0,1,0,1,1],
    [1,1,0,0,1],
    [0,1,1,1,0],
    [0,0,1,0,0]],
    [[0,0,1,0,0], # Preset 2 - The staircase
    [0,1,1,1,1],
    [1,1,0,5,1],
    [1,0,0,0,0],
    [1,1,1,0,0]],
    [[1,1,1,0,0], # Preset 3 - The lambda
    [1,0,1,0,0],
    [1,0,1,1,1],
    [0,5,1,0,0],
    [0,0,1,0,0]],
    [[1,1,1,1,1], # Preset 4 - The bent loop
    [1,0,0,5,1],
    [1,1,1,0,1],
    [0,0,1,0,1],
    [0,0,1,1,1]],
    [[0,0,1,1,0], # Preset 5 - The hooked string
    [0,0,0,1,0],
    [1,1,1,1,1],
    [0,1,0,0,0],
    [5,1,1,0,0]],
    [[0,0,1,0,1], # Preset 6 - The rabbit
    [0,0,1,1,1],
    [1,1,1,0,1],
    [0,1,1,1,5],
    [0,0,1,0,0]]
]

def putTile (yAxis, xAxis, tile):
    for i in range(5):
        for e in range(5):
            dungeon_map[i+yAxis][e+xAxis] = tile[i][e]
'''
ran_num = random.randint(0, len(dungeon_start)) # Randomly choose a start tile to use
for i in range(5): # Randomly set the entrance 'tile'
    for e in range(5):
        dungeon_map[i+5][e] = dungeon_start[ran_num][i][e]

ran_num = random.randint(0, len(dungeon_end)) # Randomly choose a start tile
for i in range(5): # Randomly set the exit 'tile'
    for e in range(5):
        dungeon_map[i][e+5] = dungeon_end[ran_num][i][e]
'''
ran_num = random.randint(0, len(dungeon_start)-1) # Randomly choose a start tile to use
putTile (5, 0, dungeon_start[ran_num])

ran_num = random.randint(0, len(dungeon_end)-1) # Randomly choose a start tile to use
putTile (0, 5, dungeon_end[ran_num])

ran_num = random.randint(0, len(dungeon_preset)-1) # Randomly choose a preset tile to use
putTile (0, 0, dungeon_preset[ran_num])

ran_num = random.randint(0, len(dungeon_preset)-1) # Randomly choose a preset tile to use
putTile (5, 5, dungeon_preset[ran_num])

for i in range(10):
    print(dungeon_map[i])
