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
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

"""First make the map into a graph with relationships
Each graph node will have friends"""

# Make the graph
graph = Graph()

# Make nodes of each room first
q = Queue() # This queue will help traverse the array
visited = {} # visited is to keep track if a node is made or not
q.enqueue(world.starting_room) #kick off the queue by adding the starting room
# while the queue is not empty..
while q.size() > 0:
    # dequeue a node
    something = q.dequeue()
    print(something.id, 'SIE')
    # Check if this node has been made if it hasn't then...
    if something.id not in visited:
        # Use the id to make a new node
        visited[something.id] = []
        # Check if other rooms are available
        print(len(visited), 'asdf')
        while len(visited) != 4:
            other_room = player.current_room.get_exits()
            player.travel(str(other_room[random.randrange(len(other_room))]))
            print(player.current_room)
            q.enqueue(player.current_room)
            traversal_path.append(other_room)
            print(other_room, 'OTHER ROOM  ')
    else:
        print(f'node of {something.id} has already been visited')
print('visited', visited)

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
