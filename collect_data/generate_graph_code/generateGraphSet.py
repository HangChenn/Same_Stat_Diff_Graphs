from dataCollect import DataCollection
from dataCollect_new import DataCollection_new
import csv
import networkx as nx

class generateGraphSet:

    def __init__(self):
        # self.ana_tool = DataCollection()
        self.ana_tool = DataCollection_new()
        self.connected_exp = True
        self.bunchsize = 10000

    def generate_graph_generator(self, gen_name, vertex_num, graphs_num, file_name):
        graphs_list_as_g6 = b""
        stat_list = []
        with open(file_name + '.csv', 'w', newline='') as stat_file, open(file_name + '.g6', 'wb') as graph_file:
            stat_file_writer = csv.writer(stat_file, delimiter=',')
            for i in range(graphs_num):
                if (i+1) % self.bunchsize == 0:
                    stat_file_writer.writerows(stat_list)
                    graph_file.write(graphs_list_as_g6)
                    graphs_list_as_g6 = b""
                    stat_list = []
                g = self.ana_tool.get_graph_by_gen(gen_name, vertex_num)
                graphs_list_as_g6 += nx.to_graph6_bytes(g)
                stat_list.append(self.ana_tool.standardized_data_analysis(g, vertex_num))
            stat_file_writer.writerows(stat_list)
            graph_file.write(graphs_list_as_g6)


    def calculate_gt_property(self, vertex_num, file_name, gt_path):
        stat_list = []
        with open(file_name + '.csv', 'w',newline='') as stat_file, open(gt_path+'.g6', 'rb') as graph_file:
            stat_file_writer = csv.writer(stat_file,delimiter=',')
            counter = 0
            for graph_compressed in graph_file.readlines():
                if (counter+1) % self.bunchsize == 0:
                    stat_file_writer.writerows(stat_list)
                    stat_list = []
                graph = nx.from_graph6_bytes(graph_compressed.rstrip())
                if self.connected_exp and (not nx.is_connected(graph)):
                    continue
                stat_list.append(self.ana_tool.standardized_data_analysis(graph, vertex_num))
                counter += 1
            stat_file_writer.writerows(stat_list)

if __name__ == '__main__':
    ###
    #  see following examples for use the functions
    ###
    gn = generateGraphSet()
    generator_type = ["ER", "ERlog"]
    # 'geo' means 'GE' in the paper. sorry for inconsistent
    # for generator in generator_type:
    #     for vertex_num in [4,5,6,7]:
    #     # [8, 9, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]:
    #         num_graph_to_generate = 1000
    #         name_or_path = './graphs_'+generator+'_'+str(vertex_num)
    #         gn.generate_graph_generator(generator, vertex_num, num_graph_to_generate, name_or_path)
    for v_n in range(9,10):
    	gn.calculate_gt_property(v_n, "./gt_v="+str(v_n)+"_prop_connected", "./Graph"+str(v_n)+"")
