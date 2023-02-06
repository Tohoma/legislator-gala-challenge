class GuestNode:
    def __init__ (self, name, avoid, pair):
        self.name = name
        self.avoid = avoid
        self.pair = pair
        self.added = False

def find_independent_vertex(current_node,guest_list_dict, vertex_set, prev_seen):
    vertex_set.add(current_node.name)
    current_node.added = True
    print(current_node.name)
    if len(current_node.avoid) == 0:
        return vertex_set
    for i in current_node.avoid:
        #current_node.avoid is ['C','D']
        # print("My options are ")
        # print(guest_list_dict[i].avoid)
        for guest in guest_list_dict[i].avoid:
            print("Checking if " + guest + " is an option ")
            print("Is " + guest + " not in vertex_set?")
            print(guest not in vertex_set)
            print("Does" + guest + " not have any edges touching previous vertexes?")
            print( not any(vertex in vertex_set for vertex in guest_list_dict[guest].avoid))
            if guest not in vertex_set and not any(vertex in vertex_set for vertex in guest_list_dict[guest].avoid) and not guest_list_dict[guest].added:
                print(guest + " is an independent vertex!")
                # print("I'm going to explore" + guest_list_dict[guest].name)
                vertex_set.update(find_independent_vertex(guest_list_dict[guest], guest_list_dict, vertex_set,prev_seen))
        # print("The vertex set is: ")
        # print(vertex_set)
        return vertex_set
    
    
def legislator(num_tables, guest_list, planner_preferences):
    solution_table = {}
    guest_list_graphs = {}
    for i in range(num_tables):
        table_name = "table_" + str(i + 1)
        solution_table[table_name] = []
    #Build guest list graph
    for i in planner_preferences:
        #print(i)
        if i["guests"][0] in guest_list_graphs.keys():
            if i["preference"] == "avoid":
                guest_list_graphs[i["guests"][0]].avoid.append(i["guests"][1])
            elif i["preference"] == "pair":
                guest_list_graphs[i["guests"][0]].pair.append(i["guests"][1])
            else: 
                raise Exception("Non supported preference input")
        else:
            if i["preference"] == "avoid":
                guest_list_graphs[i["guests"][0]] = GuestNode(i["guests"][0],[i["guests"][1]],[])
            elif i["preference"] == "pair":
                guest_list_graphs[i["guests"][0]] = GuestNode(i["guests"][0],[],[i["guests"][1]])
        if i["guests"][1] in guest_list_graphs.keys():
            if i["preference"] == "avoid":
                guest_list_graphs[i["guests"][1]].avoid.append(i["guests"][0])
            elif i["preference"] == "pair":
                guest_list_graphs[i["guests"][1]].pair.append(i["guests"][0])
            else: 
                raise Exception("Non supported preference input")
        else:
            if i["preference"] == "avoid":
                guest_list_graphs[i["guests"][1]] = GuestNode(i["guests"][1],[i["guests"][0]],[])
            elif i["preference"] == "pair":
                guest_list_graphs[i["guests"][1]] = GuestNode(i["guests"][1],[],[i["guests"][0]])
    #TODO: Find single node without avoid
    #Find independent vertex
    independent_vertex_set_list = []
    for key in guest_list_graphs:
        independent_vertex_set_list_size = len(independent_vertex_set_list)
        if  independent_vertex_set_list_size == 0 or key not in independent_vertex_set_list[independent_vertex_set_list_size - 1]:
            print('--------------------------------')
            print('Finding ind vertex for ' +guest_list_graphs[key].name )
            current_vertex_set = find_independent_vertex(guest_list_graphs[key], guest_list_graphs,set(),set())
            print("The current vertex set is: ")
            print(current_vertex_set)
            independent_vertex_set_list.append(current_vertex_set)
    print(independent_vertex_set_list)
    if len(independent_vertex_set_list) > num_tables:
        raise Exception("We need more tables, there are too many guests to sit that needs to be avoided")
    elif len(independent_vertex_set_list) == num_tables:
        for i in range(num_tables):
           table_name = "table_" + str(i + 1)
           solution_table[table_name] = list(independent_vertex_set_list[i]) 
           
    return solution_table

