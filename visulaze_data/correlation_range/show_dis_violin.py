import numpy as np
import matplotlib.pyplot as plt


# gt = ['gt_v='+str(x)+'_prop_connected' for x in range(4,8)]
# generated_filename = [8,9] + list(range(10,85,5))
# generated_filename = ['graphs_ER_'+str(x) for x in generated_filename]
# gt.extend(generated_filename)

generated_filename = list(range(4,10)) + list(range(10,85,5))
generated_filename = ['graphs_ER_'+str(x) for x in generated_filename]
files_list = generated_filename

stats_label = ["GCC", "SCC", "APL", "r", "diam", "den", "Ce",
			"Cd", "Cc", "Cb", "Cei", "e_g_resist", "s_rad"]



def draw_violin(title, label, data):
	plt.violinplot(data, range(len(label)), points=400, 
		# widths=0.3,
			showmeans=True, showextrema=True, showmedians=False)
	plt.xticks(range(len(label)), [str(x) for x in label], color='black')
	if title == "r":
		plt.ylim(-1,1)
	else:
		plt.ylim(0,1)
	plt.title(title, fontsize=20)
	# plt.show()
	plt.savefig("./image/"+title+".png")
	plt.gcf().clear()

def get_data(pos):
	data = []
	for filename in files_list:
		filesdata = np.loadtxt(filename+".csv", delimiter=",")
		# print(len(filesdata))
		# print(len(filesdata[0]))
		filesdata = np.transpose(filesdata)
		data.append(filesdata[pos])
	return data

def main():

	x_label = list(range(4,10)) + list(range(10,85,5))
	for i in range(len(stats_label)):
		draw_violin(stats_label[i], x_label, get_data(i))

main()