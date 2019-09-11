import networkx as nx
import math
import random


class DataCollection:
    def __init__(self,name=None, graphs=None):
        if name is not None and graphs is not None:
            self.graphs = graphs
            self.lens = len(graphs)
            self.saving_name = name
            h, w = 11, self.lens
            self.Matrix = [[0 for x in range(w)] for y in range(h)]
            return

    def get_graph_by_list(self,index):
        return self.graphs[index]

    def get_graph_by_gen(self, type_of_graph, vertex_num):
        if type_of_graph == "ER":
            graph = nx.fast_gnp_random_graph(vertex_num, 0.5)
        if type_of_graph == "ERlog":
            graph = nx.fast_gnp_random_graph(vertex_num, math.log(vertex_num)/vertex_num)
        if type_of_graph == "UN":
            graph = nx.fast_gnp_random_graph(vertex_num, random.random())
        if type_of_graph == "WS":
            ring_num = random.randint(2, vertex_num - 1)
            graph = nx.watts_strogatz_graph(vertex_num, ring_num, random.random())
        if type_of_graph == "BA":
            graph = nx.barabasi_albert_graph(vertex_num, random.randint(1, vertex_num - 1))
        if type_of_graph == "GE":
            graph = nx.random_geometric_graph(vertex_num, random.random())
        return graph

    def standardized_data_analysis(self, graph, num_vertex):
        vec = self.data_analysis(graph)
        G = nx.path_graph(num_vertex)
        max_stat_list = [1, 1, 1, nx.average_shortest_path_length(G), 1, num_vertex - 1, 1, 1, num_vertex - 1,
                         num_vertex - 1]
        for k in range(len(max_stat_list)):
            vec[k] = float(vec[k]) / max_stat_list[k]
        return vec
    
    def data_analysis(self, graph):
        data_vec = [0] * 10
        # print graph.edges
        data_vec[0] = nx.transitivity(graph)
        # print(Matrix[0])
        try:
            data_vec[1] = nx.average_clustering(graph)
        except:
            data_vec[1] = 0

        dic = nx.square_clustering(graph).values()
        summation = 0
        for e in dic:
            summation = summation + e
        try:
            data_vec[2] = summation / len(dic)
        except:
            data_vec[2] = 0

        if nx.number_connected_components(graph) != 1:
            Gc = max(nx.connected_component_subgraphs(graph), key=len)
            if nx.number_of_nodes(Gc) != 1:
                data_vec[3] = nx.average_shortest_path_length(Gc)
        else:
            data_vec[3] = nx.average_shortest_path_length(graph)

        try:
            data_vec[4] = nx.degree_assortativity_coefficient(graph)
        except:
            data_vec[4] = 0
        if math.isnan(data_vec[4]) is True:
            data_vec[4] = 0

        if nx.number_connected_components(graph) != 1:
            Gc = max(nx.connected_component_subgraphs(graph), key=len)
            data_vec[5] = nx.diameter(Gc)
        else:
            data_vec[5] = nx.diameter(graph)

        data_vec[6] = nx.density(graph)

        # triangle part, calculate the ratio of triangle
        node_N = nx.number_of_nodes(graph)
        if node_N < 3:
            data_vec[7] = 0
        else:
            triangle = sum(nx.triangles(graph).values()) / 3
            C_Triangle = math.factorial(node_N) / math.factorial(node_N - 3) / math.factorial(3)
            data_vec[7] = float(triangle) / C_Triangle

        data_vec[8] = nx.node_connectivity(graph)
        data_vec[9] = nx.edge_connectivity(graph)
        # print data_vec
        return data_vec

    def get_ran(self):
        if self.genType == "ER" or self.genType == "GE":
            num = float(self.get_random_based_on_population())
            max_e = self.vertex_num*(self.vertex_num-1)/2
            if num == 0: return 0
            if num == max_e: return 1
            # print (random.random()-0.5)/max_e + num/max_e
            return (random.random()-0.5)/max_e + num/max_e
        return self.get_random_based_on_population()

    def get_random_based_on_population(self):
        if self.genType == "ER" or self.genType == "GE":
            index = random.randint(1,self.ram_dist[len(self.ram_dist)-1])
            for i in range(len(self.ram_dist)):
                if index <= self.ram_dist[i]:
                    return i
        index = random.randint(1,len(self.ram_dist))
        return self.ram_dist[index]



