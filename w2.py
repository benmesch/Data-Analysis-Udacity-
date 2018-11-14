import numpy as np

def parse_graph_dict(graph_list):
    results = {}
    for i in graph_list:
        if " -> " in i:
            _pos = i.find(" -> ")
            _start = int(i[:_pos])
            _finish = i[_pos+4:]
            _finish_list = [int(x) for x in _finish.split(",")]
            results[_start] = _finish_list
    return results

def EulerianCycle(graph_list, debug=False):
    '''form a cycle Cycle by randomly walking in Graph (don't visit the same edge twice!)
    while there are unexplored edges in Graph
        select a node newStart in Cycle with still unexplored edges
        form Cycle’ by traversing Cycle (starting at newStart) and then randomly walking
        Cycle ← Cycle’
    return Cycle
    '''
    results = []
    graph_dict = parse_graph_dict(graph_list)
    if debug: print ("starting...",graph_dict)
    nodes = [x for x in graph_dict.keys()]
    current_node = int(np.random.choice(nodes,1))
    #current_node = 6
    current_node = 1
    #current_node = 1954
    if debug: print ("initial: ",current_node)
    current_cycle = []
    while len(graph_dict)>0:
        if debug: print ("current_node",current_node," , ",len(graph_dict)," , current cycle: ",current_cycle)
        if current_node in graph_dict:
            current_cycle.append(current_node)
            edges = graph_dict[current_node]
            if len(edges)==1:
                next_node = edges[0]
                graph_dict.pop(current_node)
                current_node = next_node
                if len(graph_dict)==0:
                    if debug: print ("   subresult: ",current_cycle)
                    results += current_cycle
            else:
                next_node = int(np.random.choice(edges,1))
                graph_dict[current_node].remove(next_node)
                current_node = next_node
        else:
            results += current_cycle
            if debug: print ("   subresult: ",current_cycle)
            #print ("   remaining: ",graph_dict)
            current_node = None
            for candidate in results:
                if candidate in graph_dict:
                    current_node = candidate
                    break
            current_cycle = []
            if current_node is not None:
                current_cycle = []
                #print (results.index(current_node)) #reset results to START with new starter...
                if debug: print ("original ",results)
                results = results[results.index(current_node):] + results[:results.index(current_node)]
                if debug: print ("new      ",results)
            else:
                break
    results.append(results[0])
    return results


input = [
'0 -> 3'
,'1 -> 0'
,'2 -> 1,6'
,'3 -> 2'
,'4 -> 2'
,'5 -> 4'
,'6 -> 5,8'
,'7 -> 9'
,'8 -> 7'
,'9 -> 6']
#print (EulerianCycle(input, True))

input = []
with open('dataset_203_2.txt','r') as f: #dataset_203_2
    for line in f:
        read_line = line.rstrip('\n')
        input.append(read_line)
    f.close()

y = EulerianCycle(input)
x = [str(v) for v in y]

#print (input[0:5])
#print (input)
print ("->".join((x)))

#line_concat(EulerianCycle(input))
#print ("->".join(([str(v) for v in EulerianCycle(input)])))
