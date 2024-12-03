# Bungein J Cheng & Jose Lechuga
# PA1
# 10/02/2024
import time # for timing
import random # for error generation

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def h1_zero(a, b): #All zeros
    """H1: All zeros"""
    return 0

def h2_manhattan(a, b):#Manhattan distance
    """H2: Manhattan distance"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) 

def h3_modified_manhattan(a, b):#Modified Manhattan distance
    """H3: Modified Manhattan distance"""
    # This is an example modification. You should replace this with your own variation.
    dx = abs(a[0] - b[0])
    dy = abs(a[1] - b[1])
    return max(dx, dy) + 0.5 * min(dx, dy)

def h4_manhattan_with_error(a, b):#Manhattan distance with error
    """H4: Manhattan distance with error"""
    base = h2_manhattan(a, b)
    error = random.choice([-3, -2, -1, 1, 2, 3])
    return max(0, base + error)

def astar(maze, start, end, heuristic_func):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""
    start_time = time.time()
    nodes_created = 0

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)
    nodes_created += 1 # Increment nodes created

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = min(open_list, key=lambda x: x.f)
        current_index = open_list.index(current_node)

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            cost = current_node.g
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            end_time = time.time()
            runtime = (end_time - start_time) * 1000  # Convert to milliseconds
            return cost, path[::-1], nodes_created, runtime  # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # Adjacent squares (Up, Down, Left, Right)

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] == 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)
            nodes_created += 1

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            if len([closed_child for closed_child in closed_list if child == closed_child]) > 0:
                continue

            # Create the f, g, and h values
            child.g = current_node.g + maze[child.position[0]][child.position[1]]
            child.h = heuristic_func(child.position, end_node.position)
            child.f = child.g + child.h

            # Child is already in the open list
            if len([open_node for open_node in open_list if child == open_node and child.g > open_node.g]) > 0:
                continue

            # Add the child to the open list
            open_list.append(child)

    # If we get here, no path was found
    end_time = time.time() # Get end time
    runtime = (end_time - start_time) * 1000  # Convert to milliseconds
    return -1, "NULL", nodes_created, runtime

def main():
    # Test cases
    test_cases = [
        {
            "maze": [
                [2, 4, 2, 1, 4],
                [5, 2, 0, 1, 2],
                [3, 5, 3, 1, 2],
                [0, 4, 4, 1, 2],
                [4, 2, 5, 5, 3]
            ],
            "start": (1, 2),
            "goal": (4, 3)
        },
        {
            "maze": [
                [1, 3, 2, 5, 1, 4, 3],
                [2, 1, 3, 1, 3, 2, 5],
                [3, 0, 5, 0, 1, 2, 2],
                [5, 3, 2, 1, 5, 0, 3],
                [2, 4, 1, 0, 0, 2, 0],
                [4, 0, 2, 1, 5, 3, 4]
            ],
            "start": (3, 6),
            "goal": (5, 1)
        },
        {
            "maze": [
                [2, 0, 2, 0, 2, 0, 0, 2, 2, 0],
                [1, 2, 3, 5, 2, 1, 2, 5, 1, 2],
                [2, 0, 2, 2, 1, 2, 1, 2, 4, 2],
                [2, 0, 1, 0, 1, 1, 1, 0, 0, 1],
                [1, 1, 0, 0, 5, 0, 3, 2, 2, 2],
                [2, 2, 2, 1, 0, 1, 2, 1, 0, 1],
                [0, 2, 1, 3, 1, 4, 3, 0, 1, 2],
                [0, 5, 1, 5, 2, 1, 2, 4, 1, 1],
                [2, 2, 2, 0, 2, 0, 1, 1, 0, 5],
                [1, 2, 1, 1, 1, 2, 0, 1, 2, 1]
            ],
            "start": (1, 2),
            "goal": (8, 8)
        },
        # First custom test
        {
          "maze": [
                [5, 2, 5, 1, 2, 5, 5, 3, 2, 3],
                [6, 1, 8, 1, 2, 9, 8, 8, 2, 7],
                [8, 2, 1, 2, 8, 6, 1, 9, 9, 5],
                [9, 9, 8, 3, 3, 8, 5, 5, 9, 6],
                [1, 6, 7, 7, 7, 7, 1, 8, 2, 5],
                [1, 1, 8, 1, 9, 3, 9, 8, 6, 7],
                [6, 6, 2, 8, 4, 6, 2, 4, 8, 6],
                [4, 7, 5, 3, 3, 3, 1, 5, 5, 5],
                [2, 6, 7, 5, 4, 3, 3, 2, 3, 2],
                [1, 6, 3, 4, 7, 1, 7, 6, 7, 7]
            ],  
            "start": (5, 2),
            "goal": (6, 7)
        },
        # Second custom test
        {
            "maze": [
                [1, 2, 9, 1, 5, 9, 3, 8, 2, 4],
                [9, 8, 2, 3, 2, 1, 5, 2, 1, 8],
                [3, 6, 6, 6, 1, 4, 4, 9, 5, 6],
                [8, 8, 8, 5, 1, 3, 1, 4, 5, 1],
                [6, 3, 8, 8, 2, 2, 1, 2, 2, 9],
                [3, 6, 4, 1, 1, 4, 3, 9, 8, 9],
                [2, 6, 1, 5, 8, 5, 5, 8, 8, 5],
                [4, 3, 8, 9, 3, 4, 5, 7, 3, 3],
                [7, 4, 1, 8, 3, 7, 3, 7, 7, 1],
                [7, 2, 4, 8, 6, 6, 1, 3, 1, 1]
            ],
            "start": (3, 9),
            "goal": (5, 6)
        }
    ]
    # Test case heuristics
    heuristics = [
        ("H1: All zeros", h1_zero), 
        ("H2: Manhattan distance", h2_manhattan),
        ("H3: Modified Manhattan distance", h3_modified_manhattan),
        ("H4: Manhattan distance with error", h4_manhattan_with_error)
    ]

    results = {h[0]: [] for h in heuristics} # We create a dictionary to store the results

    for i, case in enumerate(test_cases):# Loop through test cases
        print(f"\nTest Case {i + 1}:")# print test case number
        for heuristic_name, heuristic_func in heuristics: # Loop through heuristics
            cost, path, nodes_created, runtime = astar(case["maze"], case["start"], case["goal"], heuristic_func)
            results[heuristic_name].append({# Store the results
                "cost": cost,
                "nodes_created": nodes_created,
                "runtime": runtime
            })
            print(f"\n{heuristic_name}:")
            print(f"1) Cost of the path found: {cost}")
            print(f"2) Path: {path}")
            print(f"3) Number of nodes created: {nodes_created}")
            print(f"4) Runtime: {runtime:.2f} ms")

    # Here we print the summary tables
    print("\n----- Summary Tables -----")
    for metric in ["cost", "nodes_created", "runtime"]:# Loop through metrics
        print(f"\n{metric.capitalize()} Table:")
        print("Heuristic\t" + "\t".join(f"Case {i+1}" for i in range(len(test_cases))))
        for heuristic_name in results:# Loop through heuristics
            values = [str(round(result[metric], 2) if metric == "runtime" else result[metric]) for result in results[heuristic_name]]
            print(f"{heuristic_name}\t" + "\t".join(values))

if __name__ == '__main__':
    main()