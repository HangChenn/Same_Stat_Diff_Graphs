import numpy as np
import matplotlib.pyplot as plt

stats_label = ["GCC", "SCC", "APL", "r", "diam", "den","Ce",
                            "Cd", "Cc", "Cb", "Cei", "e_g_resist", "s_rad"]


def draw_one(color, x_label):

    corr_list = np.loadtxt("correlation.csv", delimiter=",")
    stat_num = len(stats_label)

    index = 0
    for i in range(stat_num):
        for j in range(stat_num):
            if i > j:
                continue
            axes = plt.subplot(stat_num, stat_num, j + i * stat_num + 1)
            if i == j:
                plt.xlabel(stats_label[j], fontsize=20)
                plt.ylabel(stats_label[i], fontsize=20)
            y_axies = corr_list[index]
            plt.scatter(range(len(y_axies)), y_axies, color=color)
            plt.ylim(-1,1)
            # if index == 4:
            #     print(y_axies)
            plt.xticks(range(len(y_axies)), [str(x) for x in x_label], color='black')
            index+=1

    mng = plt.get_current_fig_manager()
    mng.full_screen_toggle()
    plt.subplots_adjust(left=0.03, bottom=0.07, right=0.98, top=0.98,hspace=0.5,wspace=0.47)
    plt.show()


if __name__ == '__main__':

    x_label = list(range(4,10)) + list(range(10,85,5))
    draw_one('b', x_label)