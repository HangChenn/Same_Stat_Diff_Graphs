from dataCollect import DataCollection

import networkx as nx
import numpy as np

import time
import os
import csv

here = os.path.dirname(__file__)
database_path = here + "/data/gt/"
gt_common_prefix = 'graph'
gt_stat_suffix = '.csv'
gt_graph_suffix = '.g6'
DEBUG = False
clock_time = 60

# print(database_path)
class GraphProcessor:

    def __init__(self):
        self.ana_tool = DataCollection()

    def find_same_stat_graph(self, vertex_num, limit, vary_stat):
        limit_list, limit_vec = self.process_limit(limit)
        new_limit = ""
        for (stat, ran) in zip(limit_list, limit_vec):
            if stat != vary_stat:
                new_limit += str(stat)+":"+str(ran[0])+"~"+str(ran[1])+" "

        ready_graph_list = []
        is_asso = 0
        if vary_stat == 4:
            is_asso = 1
        for step in range(0-is_asso*10, 10, 1+is_asso):
            vary_stat_string = str(vary_stat)+":"+str(step/10)+"~"+str(step/10+0.1)
            fix_stat_graph = self.find_graph(vertex_num, new_limit+vary_stat_string, 0)
            if len(fix_stat_graph) > 0:
                ready_graph_list.append(fix_stat_graph[0])
            else:
                ready_graph_list.append(nx.empty_graph())
        return ready_graph_list

    def find_graph(self, vertex_num, limit,graph_num):
        if vertex_num < 11:
            return self.search_ground_truth(vertex_num,limit,graph_num)
        else:
            return self.generating_graph(vertex_num,limit,graph_num)


    def search_ground_truth(self, vertex_num,limit, graph_num):
        limit_list, limit_vec = self.process_limit(limit)
        # print(limit_list)
        # print(limit_vec)
        ready_graphs = []
        stat_file_name = database_path + gt_common_prefix + str(vertex_num) + gt_stat_suffix
        graph_file_name = database_path + gt_common_prefix + str(vertex_num) + gt_graph_suffix
        with open(stat_file_name, "r") as stat_set, open(graph_file_name, "rb") as graph_set:
            datareader = csv.reader(stat_set)
            for graph_stat in datareader:
                graph = graph_set.readline()
                graph_stat = [float(i) for i in graph_stat]
                row = [graph_stat[i] for i in limit_list]
                save_graph = 1
                for (stat, stat_range) in zip(row, limit_vec):
                    if not(stat_range[0] <= stat <= stat_range[1]):
                        save_graph = 0
                if save_graph == 1:
                    graph = nx.from_graph6_bytes(graph.rstrip())
                    ready_graphs.append(graph)
                    if DEBUG:
                        print(graph_stat)
                        # nx.write_graphml(graph,"Gc_=_0.graphml")
                        # nx.draw(graph)
                        # plt.show()
                    if len(ready_graphs) > graph_num:
                        break
        return ready_graphs


    def generating_graph(self, vertex_num, limit,graph_num):
        ready_graphs = []
        limit_list, limit_vec = self.process_limit(limit)
        start_time = time.time()
        while True:
            graph = self.ana_tool.get_graph_by_gen("ER", "U", vertex_num)
            graph_stat = self.ana_tool.standardized_data_analysis(graph, vertex_num)

            row = [graph_stat[i] for i in limit_list]
            save_graph = True
            for (stat, stat_range) in zip(row, limit_vec):
                if not (stat_range[0] <= stat <= stat_range[1]):
                    save_graph = False
            if save_graph:
                not_iso = True
                for r_g in ready_graphs:
                    if nx.is_isomorphic(graph, r_g):
                        not_iso = False
                if not_iso:
                    ready_graphs.append(graph)

            global clock_time
            if time.time() - start_time > clock_time:
                break
            if len(ready_graphs) > graph_num:
                break
        return ready_graphs


    ## limit have following structure: "0:0.3~0.5 1:0.4~0.9 6:0.2~1"
    def process_limit(self, lim):
        lim_stat_list = []
        lim_vec_list = []
        lim_list = lim.split()
        for stat in lim_list:
            pair = stat.split(':')
            lim_stat_list.append(int(pair[0]))
            lim_range = pair[1].split('~')
            lim_range = sorted([float(num) for num in lim_range])
            lim_vec_list.append(lim_range)
        return lim_stat_list, lim_vec_list

def find_same_stat_diff_graphs_gt(vertex_num):
    stat_file_name = database_path + gt_common_prefix + str(vertex_num) + gt_stat_suffix
    # print(stat_file_name)
    # to_write = open(here + "/data/repetition_" + str(vertex_num) + ".txt", 'w')
    rep_dic = {}
    with open(stat_file_name, "r") as stat_set:
        datareader = csv.reader(stat_set)
        index = 0
        for stat in datareader:
            stat_string = "".join(["{0:.5f} ".format(float(prop)) for prop in stat])
            if stat_string in rep_dic:
                rep_stat_list = rep_dic[stat_string]
                rep_stat_list.append(str(index))
                rep_dic[stat_string] = rep_stat_list
            else:
                rep_dic[stat_string] = [str(index)]
            index += 1
            if index%120000 == 1:
                print("\rgraphs finished: {0}".format(index),end=" ")
        print()
        to_write = open(here + "/data/repetition_real_" + str(vertex_num) + ".txt", 'w')
        for key, value in rep_dic.items():
            if len(value) > 1:
                to_write.write(" ".join(value)+"\n")
        to_write.close()
        check_repetition(vertex_num)

def check_repetition(vertex_num):
    repetition_list_name = here + "/data/repetition_real_" + str(vertex_num) + ".txt"
    graph_repete_set = {}
    with open(repetition_list_name, 'r')as rep_data_set:
        for line in rep_data_set.readlines():
            graph_index_list = line.rstrip("\n").split(' ')
            if len(graph_index_list) not in graph_repete_set:
                graph_repete_set[len(graph_index_list)] = 1
            else:
                graph_repete_set[len(graph_index_list)] += 1
    print(graph_repete_set)

# def check_repetition(vertex_num):
#     stat_file_name = database_path + gt_common_prefix + str(vertex_num) + gt_stat_suffix
#     repetition_list_name = here + "/data/repetition_real_" + str(vertex_num) + ".txt"
#     stat_list = np.loadtxt(stat_file_name, delimiter=",")
#     graph_repete_set = {}
#     with open(repetition_list_name, 'r')as rep_data_set:
#         for line in rep_data_set.readlines():
#             graph_index_list = line.rstrip("\n").split(' ')
#             if len(graph_index_list) not in graph_repete_set:
#                 graph_repete_set[len(graph_index_list)] = 1
#             else:
#                 graph_repete_set[len(graph_index_list)] += 1
#             graph_index_list = [int(ele) for ele in graph_index_list]
#             for i in range(0, len(graph_index_list)):
#                 for j in range(i + 1, len(graph_index_list)):
#                     if np.linalg.norm(stat_list[graph_index_list[i]] - stat_list[graph_index_list[i]]) > 0.00000000001:
#                         print("ERROR:"+line)
#
#     print(graph_repete_set)

if __name__ == '__main__':
    find_same_stat_diff_graphs_gt(9)
    # check_repetition(8)
    gp = GraphProcessor()
    # ana_tool = DataCollection()
    # num_vertex = 14
    # g_list = gp.find_graph(num_vertex, "0:0.2~0.5 1:0.2~0.5 2:0.2~0.5 3:0.3~0.6")
    # g_list = gp.find_graph(10, "1:0.2~0.5 2:0.2~0.5 3:0.2~0.5 8:0.3~0.6")
    # g_list = gp.find_graph(9, "0:0~0 1:0~0 2:0~0 3:0.63~0.64 4:-0.47~-0.48 5:0.5~0.5 6:0.27~0.28 7:0~0 8:0.12~0.13 9:0.12~0.13",9)
    g_list = gp.find_same_stat_graph(9,"0:0~0 1:0~0 2:0~0 3:0.63~0.64 4:-0.47~-0.48 5:0.5~0.5 6:0.27~0.28 7:0~0 8:0.12~0.13 9:0.12~0.13",4)

