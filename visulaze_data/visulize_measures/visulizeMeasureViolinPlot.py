import numpy as np
import matplotlib.pyplot as plt

size_font = 30

def draw_data_as_violin_plot_per_vertex_rep(data, title_name):
    new_order = [1, 4, 0, 2, 3]
    corresponding_name = ["UN", "GE", "ER", "WS", "BA"]
    colors = ["#e41a1c", "#377eb8", "#ff7f00", "#984ea3", "#4daf4a"]
    measure_list = ['Kullback-Leibler divergence', "Earth mover's distance"]

    stat_list = []
    for i in range(len(data)):
        stat = np.reshape(data[i], (-1, 10))
        stat = [np.asarray(stat[i]) for i in new_order]
        stat_list.append(stat)
    fig,axes = plt.subplots(ncols=len(data))

    plot_list = []
    for i in range(len(data)):
        plt.sca(axes[i])
        plt.xticks([1,2,3,4,5],corresponding_name)
        plt.tick_params(labelsize=28)
        plot = axes[i].violinplot(stat_list[i], points=100, widths=0.7, showmeans=True,
                          showextrema=True, showmedians=False, bw_method=0.5)
        plot_list.append(plot)
        axes[i].set_title(measure_list[i], fontsize=size_font)
    # axes[0].set_ylim(ymin=0,ymax=1.1)
    axes[1].set_ylim(ymin=0,ymax=1.1)
    for x in plot_list:
        for patch, color in zip(x['bodies'], colors):
            patch.set_facecolor(color)
            patch.set_edgecolor(color)
            # patch.set_edgecolor('black')
        x['cmeans'].set_color(colors)
        x['cmins'].set_color(colors)
        x['cmaxes'].set_color(colors)
        x['cbars'].set_color(colors)

    # fig.suptitle(title_name,,fontsize=size_font)
    plt.show()


def draw_data_as_violin_plot_per_vertex(data, title_name):
    new_order = [1, 4, 0, 2, 3]
    corresponding_name = ["UN", "GE", "ER", "WS", "BA"]
    colors = ["#e41a1c", "#377eb8", "#ff7f00", "#984ea3", "#4daf4a"]
    meausre_list = ['Bounding box', 'Split bounding box', 'Diameter', 'Robust ellipse']

    stat_list = []
    for i in range(len(data)):
        stat = np.reshape(data[i], (-1, 10))
        stat = [np.asarray(stat[i]) for i in new_order]
        stat_list.append(stat)
    fig,axes = plt.subplots(ncols=len(data))

    plot_list = []
    for i in range(len(data)):
        plt.sca(axes[i])
        plt.xticks([1,2,3,4,5],corresponding_name)
        plt.tick_params(labelsize=26)
        plot = axes[i].violinplot(stat_list[i], points=100, widths=0.7, showmeans=True,
                          showextrema=True, showmedians=False, bw_method=0.5)
        plot_list.append(plot)
        axes[i].set_title(meausre_list[i], fontsize=size_font)
    axes[0].set_ylim(ymin=0,ymax=1.1)
    axes[1].set_ylim(ymin=0,ymax=1.1)
    axes[2].set_ylim(ymin=0,ymax=1.15)
    if max([max(ele) for ele in stat_list[3]]) < 1:
        axes[3].set_ylim(ymax=1)
    for x in plot_list:
        for patch, color in zip(x['bodies'], colors):
            patch.set_facecolor(color)
            patch.set_edgecolor(color)
            # patch.set_edgecolor('black')
        x['cmeans'].set_color(colors)
        x['cmins'].set_color(colors)
        x['cmaxes'].set_color(colors)
        x['cbars'].set_color(colors)

    # fig.suptitle(title_name,fontsize=size_font)
    plt.show()

def draw_data_as_violin_plot_per_measure(measure, title_name, ymin=0, ymax=1.1):
    colors = ["#e41a1c", "#377eb8", "#ff7f00", "#984ea3", "#4daf4a"]

    corresponding_name = ["UN", "GE", "ER", "WS", "BA"]
    # corresponding_vertex = ['5','6','7','8','9']
    # corresponding_vertex = ['7', '8', '9']
    corresponding_vertex = ['6', '7', '8', '9']
    fig,axes = plt.subplots(ncols=5)

    plt.legend(corresponding_name)
    # plt.text(6,ymin,"Graph vertex numbers", fontsize=16)
    # plt.text("Ratio of sample and ground truth", fontsize=16, x=1.4, y=0.30)

    plot_list = []
    # print measure.shape
    for i in range(0, len(measure)):
        gen_data = measure[i]
        print(gen_data)
        gen_data = [ele for ele in gen_data]
        gen_names = corresponding_name[i]
        plt.sca(axes[i])
        plt.xticks([1, 2, 3, 4, 5], corresponding_vertex)
        plt.tick_params(labelsize=16)
        plot_list.append(axes[i].violinplot(gen_data, points=100, widths=0.7, showmeans=True,
                                    showextrema=True, showmedians=False, bw_method=0.5))
        axes[i].set_title(gen_names, fontsize=size_font)
        axes[i].set_ylim(ymin=ymin, ymax=ymax)

    i = 0
    for x in plot_list:
        for patch in (x['bodies']):
            patch.set_facecolor(colors[i])
            patch.set_edgecolor(colors[i])
            # patch.set_edgecolor('black')
        x['cmeans'].set_color(colors[i])
        x['cmeans'].set_color('black')
        x['cmins'].set_color(colors[i])
        x['cmaxes'].set_color(colors[i])
        x['cbars'].set_color(colors[i])
        i += 1
    # plt.legend(plot_list, corresponding_name)
    # plt.sca(axes)
    fig.suptitle(title_name,fontsize=size_font)
    plt.show()




def draw_data_as_violin_plot_per_measure_benchmark(measure, ground_truth ,title_name, ymin=-0.1, ymax=1.1):
    colors = ["#e41a1c", "#377eb8", "#ff7f00", "#984ea3", "#4daf4a"]

    corresponding_name = ["UN", "GE", "ER", "WS", "BA"]
    # corresponding_vertex = ['5','6','7','8','9']
    # corresponding_vertex = ['7', '8', '9']
    corresponding_vertex = ['1%', '2%', '5%', '10%']
    fig,axes = plt.subplots(ncols=5)

    plt.legend(corresponding_name)
    # plt.text(6,ymin,"Graph vertex numbers", fontsize=16)
    # plt.text("Ratio of sample and ground truth", fontsize=16, x=1.4, y=0.30)

    plot_list = []
    gtplot_list = []
    # print measure.shape
    for i in range(0, len(measure)):
        gen_data = measure[i]
        # print gen_data
        gen_data = [ele for ele in gen_data]
        gen_names = corresponding_name[i]
        plt.sca(axes[i])
        plt.xticks([1, 2, 3, 4, 5], corresponding_vertex)
        plt.tick_params(labelsize=16)
        plot_list.append(axes[i].violinplot(gen_data, points=100, widths=0.7, showmeans=True,
                                    showextrema=True, showmedians=False, bw_method=0.5))
        gt_data = [ele for ele in ground_truth[i]]
        gtplot_list.append(axes[i].violinplot(gt_data, points=100, widths=0.7, showmeans=True,
                                            showextrema=True, showmedians=False, bw_method=0.5))
        axes[i].set_title(gen_names, fontsize=size_font)

        axes[i].set_ylim(ymin=ymin, ymax=ymax)

    i = 0

    for x in gtplot_list:
        for patch in (x['bodies']):
            patch.set_color('black')
            # patch.set_edgecolor('black')
        x['cmeans'].set_color('black')
        # x['cmeans'].set_color('black')
        x['cmins'].set_color('black')
        x['cmaxes'].set_color('black')
        x['cbars'].set_color('black')
        i += 1

    i = 0
    for x in plot_list:
        for patch in (x['bodies']):
            patch.set_facecolor(colors[i])
            patch.set_edgecolor(colors[i])
            # patch.set_edgecolor('black')
        x['cmeans'].set_color(colors[i])
        # x['cmeans'].set_color('black')
        x['cmins'].set_color(colors[i])
        x['cmaxes'].set_color(colors[i])
        x['cbars'].set_color(colors[i])
        i += 1
    # plt.legend(plot_list, corresponding_name)
    # plt.sca(axes)
    fig.suptitle(title_name,fontsize=size_font)
    plt.show()



def prepare_data(p_file):
    data = []
    for line in p_file.readlines():
        small_list = line.rstrip('\n').split(',')
        data.append(small_list[1:])
    data = np.transpose(data).astype(np.float)
    return data


# filelist: list of str which indicate name of files
def read_data_per_measure(filelist):
    new_gen_order = [1, 4, 0, 2, 3]
    # gen_num = len(new_gen_order)

    all_data = []
    for name in filelist:
        data_file = open(name, 'r')
        data = prepare_data(data_file)
        stat_lists = []
        for i in range(0, len(data)):
            stats = np.reshape(data[i], (-1, 10))
            stats = ([np.asarray(stats[j]) for j in new_gen_order])
            stat_lists.append(stats)
        # 5 vertex --> 4 measure --> 5 gens --> 10 runs
        all_data.append(stat_lists)
    # print all_data
    # 4 measure --> 5 gens -->5 vertex --> 10 runs
    new_data = [[[[0]*10]*len(all_data)]*len(all_data[0][0])]*len(all_data[0])
    new_data = np.asarray(new_data).astype(np.float)

    for j in range(0,len(all_data[i])):
        for k in range(0,len(all_data[i][j])):
            for i in range(0, len(all_data)):
                new_data[j][k][i] = all_data[i][j][k]
    # print new_data[0][0]
    # print new_data[3]
    return new_data



def coverage(filelist):
    index = 5
    # for name in filelist:
    #     data_file = open(name, 'r')
    #     data = prepare_data(data_file)
    #     draw_data_as_violin_plot_per_vertex(data, "|V| = " + str(index))
    #     index += 1
    data = read_data_per_measure(filelist)
    name_text = ['Bounding box', 'Split bounding box', 'Diameter', 'Robust ellipse']
    i = 0
    for name in name_text:
        if i == 0:
            draw_data_as_violin_plot_per_measure(data[i], name)
        elif i == 1:
            draw_data_as_violin_plot_per_measure(data[i], name)
        elif i == 2:
            draw_data_as_violin_plot_per_measure(data[i], name, -0.1, 1.19)
        else:  # ellipse
            draw_data_as_violin_plot_per_measure(data[i], name, -0.1, 45)
        i += 1


def representation(filelist):
    index = 5
    # for name in filelist:
    #     data_file = open(name, 'r')
    #     data = prepare_data(data_file)
    #     draw_data_as_violin_plot_per_vertex_rep(data, "|V| = " + str(index))
    #     index += 1
    data = read_data_per_measure(filelist)
    name_text = ['Kullback-Leibler divergence', "Earth mover's distance"]
    i = 0
    for name in name_text:
        if i == 0:
            draw_data_as_violin_plot_per_measure(data[i], name,-1, 760)
        else:  # Wasserstein distance
            draw_data_as_violin_plot_per_measure(data[i], name,0)
        i += 1


def benchmark(filelist, gt_file_list):
    data = read_data_per_measure(filelist)
    gt_data = read_data_per_measure(gt_file_list)
    name_text = ['Kullback-Leibler divergence', "Earth mover's distance"]
    # name_text = ['Bounding box', 'Split bounding box', 'Diameter', 'Robust ellipse']
    i = 0
    for name in name_text:
        if i == 0:
            draw_data_as_violin_plot_per_measure_benchmark(data[i], gt_data[i], name, -0.1, 760)
        else:  # Wasserstein distance
            draw_data_as_violin_plot_per_measure_benchmark(data[i], gt_data[i], name, 0, 1)
        i += 1
    #
    # for name in name_text:
    #     if i == 0:
    #         draw_data_as_violin_plot_per_measure_benchmark(data[i], gt_data[i], name)
    #     elif i == 1:
    #         draw_data_as_violin_plot_per_measure_benchmark(data[i], gt_data[i], name)
    #     elif i == 2:
    #         draw_data_as_violin_plot_per_measure_benchmark(data[i], gt_data[i], name, -0.1, 1.19)
    #     else:  # ellipse
    #         draw_data_as_violin_plot_per_measure_benchmark(data[i], gt_data[i], name, -0.1, 2000)
    #     i += 1


def main():
    filelist = ["v5.txt", "v6.txt", "v7.txt", "v8.txt", "v9.txt"]
    #coverage(filelist)

    representation(["v6''.txt", "v7''.txt"])
    # representation(["v7'.txt", "v8'.txt", "v9'.txt"])

    # benchmark(["1%.txt","2%.txt","5%.txt","10%.txt"],["1%'.txt","2%'.txt","5%'.txt","10%'.txt"] )
    # benchmark(["1%_cor.txt", "2%_cor.txt", "5%_cor.txt", "10%_cor.txt"], ["gt_corr.txt"]*4)
if __name__ == '__main__':
    main()



