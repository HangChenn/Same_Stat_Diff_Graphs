from scipy import stats
import numpy as np


# gt = ['gt_v='+str(x)+'_prop_connected' for x in range(4,8)]
# generated_filename = [8,9] + list(range(10,85,5))
# generated_filename = ['graphs_ER_'+str(x) for x in generated_filename]
# files_list = gt + generated_filename
# files_list = gt
# generated_filename = list(range(4,10)) + list(range(10,85,5))
generated_filename = list(range(4,8))
files_list = ['graphs_ER_'+str(x) for x in generated_filename]


num_prop = 13
correlation_list = [[0 for y in range(len(files_list))] for x in range(num_prop*(num_prop+1)/2)]

for times in range(len(files_list)):
	matrix = np.loadtxt(files_list[times]+".csv", delimiter=",")
	matrix = np.transpose(matrix)
	index = 0
	for i in range(len(matrix)):
		list1 = matrix[i]
		for j in range(len(matrix)):
			if j < i:
				continue
			list2 = matrix[j]
			corr, p = stats.pearsonr(list1, list2)
			correlation_list[index][times] = corr
			index += 1;

np.savetxt("correlation.csv", correlation_list, delimiter=",")