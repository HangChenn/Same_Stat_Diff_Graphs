import numpy as np
from sklearn.cluster import MiniBatchKMeans


def prepare_pcp_data(data, kmeans_cluster):
    if len(data) > kmeans_cluster:
        kmeans = MiniBatchKMeans(n_clusters=kmeans_cluster, init='random', ).fit(data)
        data = kmeans.cluster_centers_.tolist()
    return data

if __name__ == '__main__':
    vertex_num = 6
    file_name = 'graph'+str(vertex_num)+'.csv'
    kmeans_name = 'g'+str(vertex_num)
    data = np.loadtxt(file_name,delimiter=',')
    data = prepare_pcp_data(data, 2000)
    f = open(kmeans_name + ".csv", 'w')
    f.write("GCC,ACC,SCC,APL,assortativity,diameter,density,r_triangle,node_conn,edge_conn\n")
    for i in range(len(data)):
        for num in range(len(data[i])):
            number = data[i][num]
            if num == 0:
                f.write(str(number))
            else:
                f.write("," + str(number))
        f.write("\n")
    f.close()