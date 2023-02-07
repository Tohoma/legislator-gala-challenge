import sys

class GuestNode:
    def __init__ (self, name, avoid, pair):
        self.name = name
        self.avoid = avoid
        self.pair = pair
        self.added = False
        self.seen = False

def find_all_ind_vertex(current_vertex, visited_vertexes, graph_dict):
    result = []
    combined_avoid = []
    new_visited_vertexes = [current_vertex]+ visited_vertexes
    for v in new_visited_vertexes:
        combined_avoid.extend(graph_dict[v].avoid)
    possible_ind_vertex = list(filter(lambda g: g not in combined_avoid, graph_dict.keys()))
    possible_ind_vertex = list(filter(lambda g: g not in new_visited_vertexes, possible_ind_vertex))
    #base case
    if len(possible_ind_vertex) == 0:
        return [[current_vertex]]
    for  v in possible_ind_vertex:
        sub_verticies = find_all_ind_vertex(v, new_visited_vertexes, graph_dict)
        for vList in sub_verticies:
            new_vList = [current_vertex] + vList 
            result.append(new_vList)
    return result

def legislator(num_tables, guest_list, planner_preferences):
    solution_table = {}
    for i in range(num_tables):
        table_name = "table_" + str(i + 1)
        solution_table[table_name] = []
    #Create Graph
    graph_dict= {}
    for name in guest_list:
        graph_dict[name] = GuestNode(name, [],[])
    for plan in planner_preferences:
        if plan["preference"] == "avoid":
             name1 = plan["guests"][0]
             name2 = plan["guests"][1]
             graph_dict[name1].avoid.append(name2)
             graph_dict[name2].avoid.append(name1)
        if plan["preference"] == "pair":
            name1 = plan["guests"][0]
            name2 = plan["guests"][1]
            graph_dict[name1].pair.append(name2)
            graph_dict[name2].pair.append(name1)
    
    #Find all possible independent vertexes for each vertex in graph
    seen_vertex = set()
    table_counter = 0
    for vertex in graph_dict:
        if vertex in seen_vertex:
            continue
        table_counter = table_counter + 1
        if table_counter > num_tables:
            raise Exception("We need more tables, there are too many guests to sit that needs to be avoided")
        possible_ind_vertex = []
        processed_graph_dict = {key: val for key,
        val in graph_dict.items() if key not in seen_vertex}
        unfiltered_possible_vertex = find_all_ind_vertex(vertex,[], processed_graph_dict)
        #remove duplicate set
        for uList in unfiltered_possible_vertex:
            if set(uList) not in possible_ind_vertex:
                possible_ind_vertex.append(set(uList))
        #find largetst set size
        largest_set = set()
        for vertex_set in possible_ind_vertex:
            if len(vertex_set) > len(largest_set):
                largest_set = vertex_set
        seen_vertex.update(largest_set)
        solution_table["table_" + str(table_counter)] = list(largest_set)
    return solution_table

if __name__ == "__main__":
    num_tables = sys.argv[0]
    guest_list = sys.argv[1]
    planner_preferences = sys.argv[2]
    with open("output.json", "w") as f:
        output = legislator(num_tables, guest_list, planner_preferences)
        json.dump(output, f, indent=2)