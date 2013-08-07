import sys
import threading
threading.stack_size(2**27)
sys.setrecursionlimit(10**9)


def build_graph(filename):
    """
    Reads data and creates direct and reversed graphs
    """
    f = open(filename, "r")
    dir_g = {}
    
    for line in f:
        pair = line.split()
        dir_g[int(pair[0])] = (dir_g[int(pair[0])] + [int(pair[1])] if int(pair[0]) in dir_g else [False, int(pair[1])])
    
    return dir_g

def build_reversed_graph(filename):
    f = open(filename, "r")
    rev_g = {}
    
    for line in f:
        pair = line.split()
        rev_g[int(pair[1])] = (rev_g[int(pair[1])] + [int(pair[0])] if int(pair[1]) in rev_g else [False, int(pair[0])])
    
    return rev_g

def dfs_first_loop(graph):
    global t
    t = 0 
    times = {}
    
    def dfs(graph, node):
        global t
        if node in graph:
            graph[node][0] = True
            for j in graph[node][1:]:
                if j in graph:
                    if not graph[j][0]:
                        dfs(graph, j)
                else:
                    graph[j] = [False]
                    dfs(graph, j)
        else:
            graph[node] = [True]
        t += 1
        times[node] = t

    for i in range(max(graph), 0, -1):
        if i in graph and not graph[i][0]:
            dfs(graph,i)
    return times


def dfs_second_loop(graph):
    global s
    s = None
    leaders = {}
    
    def dfs(graph, node):
        global s
        leaders[s] = (leaders[s] + 1 if s in leaders else 1)
        if node in graph:
            graph[node][0] = True
            for j in graph[node][1:]:
                if j in graph and not graph[j][0]:
                    dfs(graph, j)

    for i in range(max(graph), 0, -1):
        if i in graph and not graph[i][0]:
            s = i
            dfs(graph,i)
    return leaders


def scc(filename):
    print 'building  reversed graph...'
    reversed_graph = build_reversed_graph(filename)

    print 'first dfs loop...'
    rgt = dfs_first_loop(reversed_graph)

    print 'building actual graph...'
    actual_graph = build_graph(filename)

    print 'creating helper graph...'
    normal_renamed = {}
    for i in range(1, max(rgt)+1):
        if i in rgt:
            if i in actual_graph:
                normal_renamed[rgt[i]] = [False] + [rgt[element] for element in actual_graph[i][1:]]
            else:
                normal_renamed[rgt[i]] = [False]

    scc = dfs_second_loop(normal_renamed) 
    biggest_cliques = [v for (k,v) in scc.items()]
    
    print 'biggest cluques found:'
    print sorted(biggest_cliques, reverse = True)[:5]


def main():
    scc("SCC.txt")


if __name__ == '__main__':
    thread = threading.Thread(target=main)
    thread.start()
    

# scc("scc_t1.txt")
# print "3 3 3 0 0"

# scc("scc_t2.txt")
# print "3 3 2 0 0"

# scc("scc_t3.txt")
# print "3 3 1 1 0"

# scc("scc_t4.txt")
# print "7 1 0 0 0"

# scc("scc_t5.txt")
# print "6 3 2 1 0"

# scc("scc_t6.txt")
# print "6 1 1 0 0"

# scc("scc_t7.txt")
# print "3 2 2 2 1"


