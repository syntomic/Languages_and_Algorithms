def toposort(graph):
    """拓扑排序算法"""
    vnum = graph.vertex_num()
    indegree, toposeq = [0]*vnum, []
    zerov = -1

    for vi in range(vnum):
        for v, w in graph.out_edges(vi): #pylint: disable=unused-variable
            indegree[v] += 1
        
    for vi in range(vnum):
        if indegree[vi] == 0:
            indegree[vi] = zerov
            zerov = vi

    for n in range(vnum):  #pylint: disable=unused-variable
        if zerov == -1:
            return False
        
        vi = zerov
        zerov = indegree[zerov]
        toposeq.append(vi)

        for v, w in graph.out_edges(vi):
            indegree[v] -= 1
            if indegree[v] == 0:
                indegree[v] = zerov
                zerov = v
    
    return toposeq


def critical_paths(graph):
    """关键路径算法"""
    def events_earliest_time(vnum, graph, toposeq):
        ee = [0] * vnum

        for i in toposeq:
            for j, w in graph.out_edges(i):
                if ee[i] + w > ee[j]:
                    ee[j] = ee[i] + w

        return ee

    def event_latest_time(vnum, graph, toposeq, eelast):
        le = [eelast]*vnum

        for k in range(vnum-2, -1, -1):
            i = toposeq[k]
            for j, w in graph.out_edges(i):
                if le[j] - w < le[i]:
                    le[i] = le[j] - w
        
        return le

    def crt_paths(vnum, graph, ee, le):
        crt_actions = []

        for i in range(vnum):
            for j, w in graph.out_edges(i):
                if ee[i] == le[j] - w:
                    crt_actions.append((i, j, ee[i]))

        return crt_actions

    toposeq = toposort(graph)
    if not toposeq:
        return False

    vnum = graph.vertex_num()
    ee = events_earliest_time(vnum, graph, toposeq)
    le = event_latest_time(vnum, graph, toposeq, ee[vnum-1])

    return crt_paths(vnum, graph, ee, le)
