import random

def graph_min_cut(filename, num_of_trials = 1):
    """
    Randomly searches for minimum cut of graph
    filename - first element in each line is verticle id,
               followed by tab separated conected edges
    num_of_trials - number of tries.

    returns minimum cut value
    """
    found_min_cuts = []
    iteration = 0

    for _ in range(num_of_trials):
        iteration += 1
        print 'iteration', iteration
        
        graph = []
        f = open(filename, "r")
        for line in f:
            graph.append(line.rstrip().split("\t"))
        
        while len(graph) > 2:
            #randomly choose edge:
            u = random.randint(0, len(graph)-1)
            vert = random.choice(graph[u][1:])
            for i in range(len(graph)):
                if graph[i][0] == vert:
                    v = i
            
            # merge 2 verticies into 1:
            graph[u].extend(graph[v][1:])
            for element in graph[v][1:]:
                for vertex in range(len(graph)):
                    if graph[vertex][0] == element:
                        v_index = graph[vertex].index(graph[v][0])      
                        graph[vertex][v_index] = graph[u][0]
            
            # remove self loops:
            distinct_u = [graph[u][0]]
            for element in graph[u][1:]:
                if element != graph[u][0]:
                    distinct_u.append(element)
            graph[u] = distinct_u

            # remove merged vertex:
            del graph[v]

        print 'minimum cut =', len(graph[0][1:])
        found_min_cuts.append(len(graph[0][1:]))
    min_cut = min(found_min_cuts)

    print ''
    print 'minimum cut after', num_of_trials, 'attemps:', min_cut
    return min_cut

graph_min_cut('min_cut_test.txt')

graph_min_cut('kargerMinCut.txt',2)