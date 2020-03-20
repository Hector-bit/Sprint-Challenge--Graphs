from room import Room
from player import Player
from world import World
from util import Queue
from graphs import Graph

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
# visited is keep track of nodes
visited = set()
# list of all rooms entered
room_list = []
# recursively fill room_list
def dft_recursive(room_id):
    # add the first room to room_list
    room_list.append(room_id)
    # check is he room has been visited
    if room_id not in visited:
        # if it wasn't visited then add it to visited
        visited.add(room_id)
        for direction, id in room_graph[room_id][1].items():
            print(direction, 'THIS IS KEY')
            print(id, 'THIS IS ID')
            # check if id had been visited
            if id not in visited:
                # recurse with the unvisited id
                dft_recursive(id)
                room_list.append(room_id)

def traverse_rooms(rooms):
    # add to the traversal_path with room_list
    for i in range(len(rooms) - 1):
        # from room_graph pull the direction and id
        for direction, room_id in room_graph[rooms[i]][1].items():
            # check if the id's match
            if room_id == rooms[i + 1]:
                # add the direction to the traversal_path
                traversal_path.append(direction)

dft_recursive(player.current_room.id)
traverse_rooms(room_list)
# print('ROOM LIST', room_list)
# # Make the graph
# graph = Graph()

# # Make nodes of each room first
# q = Queue() # This queue will help traverse the array
# visited = {} # visited is to keep track if a node is made or not
# q.enqueue(world.starting_room) #kick off the queue by adding the starting room
# # while the queue is not empty..
# while q.size() > 0:
#     # dequeue a node
#     something = q.dequeue()
#     # Check if this node has been visited if it hasn't then...
#     if something.id not in visited:
#         # Use the id to add the node to visited
#         visited[something.id] = []
#         # Check if all rooms have been visited
#         if len(visited) != 12:
#             # other_room is set to a list of possible exits
#             other_room = player.current_room.get_exits()
#             print('OTHER ROOM - list of pos exits', other_room)
#             # random_room is set to random direction in string form
#             random_room = str(other_room[random.randrange(len(other_room))])
#             print('SHOULD BE A DIRECTION AND A STRING', type(random_room), random_room)
#             # move player to the next room based on random_room
#             player.travel(random_room)
#             print(player.current_room)
#             # add the current room to the queue
#             q.enqueue(player.current_room)
#             # add the random_room direction to the traversal_path
#             traversal_path.append(random_room)
#     else:
#         print(f'node of {something.id} has already been visited')
#         # other_room is set to a list of possible exits
#         other_room = player.current_room.get_exits()
#         print('OTHER ROOM - list of pos exits', other_room)
#         # random_room is set to random direction in string form
#         random_room = str(other_room[random.randrange(len(other_room))])
#         print('SHOULD BE A DIRECTION AND A STRING', type(random_room), random_room)
#         # move player to the next room based on random_room
#         player.travel(random_room)
#         print(player.current_room)
#         # add the current room to the queue
#         q.enqueue(player.current_room)
#         # add the random_room direction to the traversal_path
#         traversal_path.append(random_room)
# print('visited', visited)

print('YOUR TRAVERSEL PATH', traversal_path)

# rooms is list of available exits of current room
rooms = player.current_room.get_exits()
print(rooms[0], 'ROOMS')
if rooms is not None:
    player.travel(player.current_room.get_exits())
print(player.current_room.id, 'current room id')
print(player.current_room.get_exits(), 'current room exits')
"""Second, like the social problem return the routes to
each node"""


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
