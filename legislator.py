class GuestNode:
    def __init__ (self, name, avoid, pair):
        self.name = name
        self.avoid = avoid
        self.pair = pair

def find_independent_vertex(current_node,guest_list_dict, vertex_set, prev_seen):
    vertex_set.add(current_node.name)
    prev_seen.add(current_node)
    if len(current_node.avoid) == 0:
        return vertex_set
    for i in current_node.avoid:
        prev_seen.add(i)
        for guest in guest_list_dict[i].avoid:
            vertex_set = find_independent_vertex(guest_list_dict[i]m guest_list_dict, vertex_set, prev_seen)
    return vertex_set
    
def legislator(num_tables, guest_list, planner_preferences):
    solution_table = {}
    guest_list_graphs = {}
    for i in range(num_tables):
        table_name = "table_" + str(i + 1)
        solution_table[table_name] = []
    #Build guest list graph
    for i in planner_preferences:
        if i.guests[0] in guest_list_graphs.keys():
            if i.preference == "avoid":
                guest_list_graphs[i.guests[0]].avoid.push(i.guests[1])
            elif i.preferences == "pair":
                guest_list_graphs[i.guests[0]].pair.push(i.guests[1])
            else: 
                raise Exception("Non supported preference input")
        else:
            if i.preference == "avoid":
                guest_list_graphs[i.guests[0]] = GuestNode(i.guests[0],[i.guests[1]],[])
            elif i.preferences == "pair":
                guest_list_graphs[i.guests[0]] = GuestNode(i.guests[0],[],[i.guests[1]])
        if i.guests[1] in guest_list_graphs.keys():
            if i.preference == "avoid":
                guest_list_graphs[i.guests[1]].avoid.push(i.guests[0])
            elif i.preferences == "pair":
                guest_list_graphs[i.guests[1]].pair.push(i.guests[0])
            else: 
                raise Exception("Non supported preference input")
        else:
            if i.preference == "avoid":
                guest_list_graphs[i.guests[1]] = GuestNode(i.guests[1],[i.guests[0]],[])
            elif i.preferences == "pair":
                guest_list_graphs[i.guests[1]] = GuestNode(i.guests[1],[],[i.guests[0]])
    #TODO: Find single node without avoid
    #Find independent vertex
    independent_vertex_set_list = []
    for key in guest_list_graphs:
        independent_vertex_set_list_size = len(independent_vertex_set_list)
        if  independent_vertex_set_list_size == 0 or key not in independent_vertex_set_list[independent_vertex_set_list_size]:
            independent_vertex_set_list.push(find_independent_vertex(guest_list_graphs[key], guest_list_graphs,{},{}))
    if len(independent_vertex_set_list) > num_tables:
        raise Exception("We need more tables, there are too many guests to sit that needs to be avoided")
    elif len(independent_vertex_set_list) == num_tables:
        for i in range(num_tables):
           table_name = "table_" + str(i + 1)
           solution_table[table_name] = list(independent_vertex_set_list[i]) 
           return solution_table
    return solution_table

