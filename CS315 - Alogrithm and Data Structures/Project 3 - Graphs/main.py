import heapq
graph = {}


def make_vertices(file):
    file = open(file, "r")
    lines = file.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].rstrip("\n")
        graph[lines[i]] = ""


def insert_edges(file):
    file = open(file, "r")
    lines = file.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].rstrip("\n")
        lines[i] = lines[i].split(",")

        directed = {}
        undirected = {}
        if graph[lines[i][0]] == "":
            directed[lines[i][1]] = int(lines[i][2])
            graph[lines[i][0]] = directed
        else:
            directed.update(graph[lines[i][0]])
            directed[lines[i][1]] = int(lines[i][2])
            graph[lines[i][0]] = directed

        if graph[lines[i][1]] == "":
            undirected[lines[i][0]] = int(lines[i][2])
            graph[lines[i][1]] = undirected
        else:
            undirected.update(graph[lines[i][1]])
            undirected[lines[i][0]] = int(lines[i][2])
            graph[lines[i][1]] = undirected


def print_graph(adjacency_list):
    for vertex in graph:
        print(f"{vertex} ---> ", end="")
        for edges in graph[vertex].keys():
            print(f"{edges}", end="")
            if edges == list(graph[vertex].keys())[-1]:
                print(".", end="")
            else:
                print(", ", end="")
        print()


def print_path(path_list):
    for city in path_list:
        print(f"{city}", end="")
        if city == path_list[-1]:
            print(".")
        else:
            print(" -> ", end="")


def breadth_first_search(graph, source_node, destination_node):
    v = []
    q = [[source_node]]
    if source_node == destination_node:
        print("Already there!")
        return

    while q:
        path = q.pop(0)
        node = path[-1]
        if node not in v:
            neighbours = graph[node]

            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                q.append(new_path)
                if neighbour == destination_node:
                    print(
                        f"The shortest path from {source_node} to {destination_node} using BFS is ",
                        end="",
                    )
                    print_path(new_path)
                    return
            v.append(node)

    print(f"No path exists from {source_node} to {destination_node}")
    return


def dijsktra(graph, source, destination):
    vertices = 10
    node_data = {}
    for node in graph:
        node_data[node] = {"cost": float("inf"), "predecessor": []}
    node_data[source]["cost"] = 0
    node_data[source]["cost"] = 0
    v = []
    temp = source
    for i in range(vertices):
        if temp not in v:
            v.append(temp)
            min_heap = []
            for j in graph[temp]:
                if j not in v:
                    cost = node_data[temp]["cost"] + graph[temp][j]
                    if cost < node_data[j]["cost"]:
                        node_data[j]["cost"] = cost
                        node_data[j]["predecessor"] = node_data[temp][
                            "predecessor"
                        ] + temp.split(" ")
                    heapq.heappush(min_heap, (node_data[j]["cost"], j))
        heapq.heapify(min_heap)
        temp = min_heap[0][1]
    print(
        f"The Shortest Distance from {source} to {destination} using Dijkstra's is {node_data[destination]['cost']}."
    )
    print(
        f"The shortest Path from {source} to {destination} using Dijkstra's is ", end=""
    )
    print_path(node_data[destination]["predecessor"])


# Create the graph as an adjacency list
make_vertices("RomaniaVertices.txt")
insert_edges("RomaniaEdges.txt")

# Print the adjacency list
print("The following is the adjacency list structured as a dictionary of dictionaries:")
print(graph)

print()
print("**********Represent the Graph as an Adjacency List (20 Points)**********")
print_graph(graph)

# Implement breadth first search of the graph
print()
print("**********Breadth First Search (30 points)**********")
breadth_first_search(graph, "Arad", "Sibiu")
breadth_first_search(graph, "Arad", "Craiova")
breadth_first_search(graph, "Arad", "Bucharest")

# Implement Dijkstra's
print()
print("**********Dijkstra’s Algorithm! (30 points)**********")
dijsktra(graph, "Arad", "Bucharest")
