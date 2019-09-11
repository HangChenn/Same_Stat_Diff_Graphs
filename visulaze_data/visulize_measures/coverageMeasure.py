import numpy as np
import math

class coverMeasure:
    def box_volume(self, matrix, box_num=1):
        if len(matrix) != 10:
            matrix = np.transpose(matrix)
        step = 1 / float(box_num)

        box_list = [i / float(box_num) for i in range(0, box_num)]
        ass_list = [i * 2 / float(box_num) - 1 for i in range(0, box_num)]

        box_volume = 0
        log = 0

        temp_matrix = [matrix for i in range(10)]
        for i1 in box_list:
            temp_matrix[0] = self.fileting_matrix(matrix, 0, i1, i1 + step)
            for i2 in box_list:
                temp_matrix[1] = self.fileting_matrix(temp_matrix[0], 1, i2, i2 + step)
                for i3 in box_list:
                    temp_matrix[2] = self.fileting_matrix(temp_matrix[1], 2, i3, i3 + step)
                    for i4 in box_list:
                        temp_matrix[3] = self.fileting_matrix(temp_matrix[2], 3, i4, i4 + step)
                        for i5 in ass_list:
                            temp_matrix[4] = self.fileting_matrix(temp_matrix[3], 4, i5, i5 + step * 2)
                            for i6 in box_list:
                                temp_matrix[5] = self.fileting_matrix(temp_matrix[4], 5, i6, i6 + step)
                                for i7 in box_list:
                                    temp_matrix[6] = self.fileting_matrix(temp_matrix[5], 6, i7, i7 + step)
                                    for i8 in box_list:
                                        temp_matrix[7] = self.fileting_matrix(temp_matrix[6], 7, i8, i8 + step)
                                        for i9 in box_list:
                                            temp_matrix[8] = self.fileting_matrix(temp_matrix[7], 8, i9, i9 + step)
                                            for i10 in box_list:
                                                log = log + 1
                                                temp_matrix[9] = self.fileting_matrix(temp_matrix[8], 9, i10, i10 + step)
                                                # print(len(temp_matrix[9]))
                                                # print len(temp_matrix[9][0])
                                                # temp = temp_matrix[9]
                                                if len(temp_matrix[9]) != 0:
                                                    volume_box = 1
                                                    for small_list in temp_matrix[9]:
                                                        # print small_list
                                                        volume_box = volume_box * (
                                                                    max(small_list) - min(small_list))
                                                    box_volume = box_volume + volume_box
        return box_volume


    def diameter_measure(self, matrix):
        if len(matrix) == 10:
            matrix = np.transpose(matrix)
        max_dis = 0
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                dist = np.linalg.norm(matrix[i] - matrix[j])
                if dist > max_dis:
                    max_dis = dist
        return max_dis


    def elapse_measure(self, matrix):
        if len(matrix) != 10:
            matrix = np.transpose(matrix)
        mu = []
        # calculate average
        for ele in matrix:
            mu.append(np.average(ele))
        # xi = mu
        trans_m = np.transpose(matrix)
        new_temp = []
        for ele in trans_m:
            new_ele = ele - mu
            new_temp.append(new_ele)
            # print (ele - mu)
        sum_matrix = [[0] * 10] * 10
        for ele in trans_m:
            # print ele
            met = np.outer(ele, ele)
            # print met
            sum_matrix = sum_matrix + met
        sum_matrix = sum_matrix/len(matrix[0])
        u, s, vh = np.linalg.svd(sum_matrix)
        # print sum_matrix
        volume_elapse = np.prod(s)
        # print volume_elapse
        return volume_elapse


    #########################################################################################
    #     update index list and return preprocessor of max number inside a sorted list      #
    #########################################################################################
    def fileting_matrix(self, twod_list, dim, lower_bound, upper_bound):
        twod_list = np.transpose(twod_list)
        new_list = []
        for vec in twod_list:
            if vec[dim] >= lower_bound and vec[dim] <= upper_bound:
                new_list.append(vec)
        new_list = np.transpose(new_list)
        return new_list



class represetationMeasure:

    def KL_divergence(self, matrix, truth):
        if len(matrix) != 10:
            matrix = np.transpose(matrix)
        if len(truth) != 10:
            truth = np.transpose(truth)
        # print matrix
        # print len(truth[0])
        truth = np.asmatrix(truth)
        mu_s = []
        mu_t = []
        for ele in matrix:
            mu_s.append(np.average(ele))
        for ele in truth:
            mu_t.append(np.average(ele))
        # print np.cov(matrix)
        cov_s = np.cov(matrix)
        cov_t = np.cov(truth)
        mu_s = np.matrix(mu_s)
        mu_t = np.matrix(mu_t)
        # print cov_s
        # print cov_t
        # print (np.linalg.det(cov_t) / np.linalg.det(cov_s))
        # exit()
        KL_div = 0.5 * (np.trace(np.linalg.inv(cov_t) * cov_s) +
                        (np.subtract(mu_t,mu_s)) * np.linalg.inv(cov_t) * np.transpose(np.subtract(mu_t,mu_s)) - 10
                        + math.log(np.linalg.det(cov_t) / np.linalg.det(cov_s)) )
        # except:
        #     KL_div = None
        # print KL_div[0,0]
        return KL_div[0,0]

    def WS_distance(self, matrix, truth):
        if len(matrix) != 10:
            matrix = np.transpose(matrix)
        if len(truth) != 10:
            truth = np.transpose(truth)

        mu_s = []
        mu_t = []
        for ele in matrix:
            mu_s.append(np.average(ele))
        for ele in truth:
            mu_t.append(np.average(ele))
        cov_s = np.cov(matrix)
        cov_t = np.cov(truth)
        mu_s = np.matrix(mu_s)
        mu_t = np.matrix(mu_t)
        # print 2 * np.sqrt(np.sqrt(cov_t) * cov_s * np.sqrt(cov_t))
        em_d = np.linalg.norm(mu_s - mu_t) ** 2  + np.trace(cov_s + cov_t - 2 * np.sqrt(np.sqrt(cov_t) * cov_s * np.sqrt(cov_t)) )
        return em_d



def writing_coverage_data():
    folder = "./new_graph_set/"
    name_list = ["ER_T", "ER_U", "WS", "BA", "geo"]
    ana = coverMeasure()
    percentage = [1,2,5,10]
    # percentage = [100]
    to_write = open("data_cor_bench_ellipse.txt", "w")
    to_write2 = open("cor_gt_ignore.txt", "w")

    to_write.write("model name/index,")
    to_write.write("bounding box,")
    to_write.write("bounding box k = 2,")
    to_write.write("diameter,")
    to_write.write("robust elapse\n")

    to_write2.write("model name/index,")
    to_write2.write("bounding box,")
    to_write2.write("bounding box k = 2,")
    to_write2.write("diameter,")
    to_write2.write("robust elapse\n")
    for percent in percentage:
        truth_time = 0
        for index in range(9, 10):
            # Ground truth
            divider = []
            matrix = np.loadtxt(folder + "graph" + str(index) + ".csv", delimiter=",")
            truth = np.random.permutation(matrix)
            volume = ana.box_volume(matrix)
            divider.append(volume)
            volume = ana.box_volume(matrix, 2)
            divider.append(volume)

            sums = 0
            runtime = 10
            # if len(matrix) > 3000:
            #     matrix_temp = matrix[0:3000]
            #     for i in range(runtime):
            #         sums += ana.diameter_measure(matrix_temp)
            #     volume = float(sums) / runtime
            # else:
            #     volume = ana.diameter_measure(matrix)
            volume = 3.1622776601683795
            divider.append(volume)

            volume = ana.elapse_measure(matrix)
            divider.append(volume)

            # sample
            inner_folder = "v=" + str(index) + "/"
            # to_write.write(str(index) + "\n")
            # to_write2.write(str(index) + "\n")
            for name in name_list:
                for time in range(10):
                    truth = np.random.permutation(truth)
                    matrix = np.loadtxt(folder + inner_folder + name + "_" +
                                        str(index) + "_" + str(time) + ".csv", delimiter=",")
                    # matrix = np.transpose(matrix)
                    # matrix = matrix.astype(np.float)

                    # print matrix
                    num_graphs = int(float(percent * len(matrix)) / 100)
                    to_write.write(name + ",")
                    ### box ###
                    # print "bounding box: "
                    volume = ana.box_volume(matrix[0:num_graphs]) / divider[0]
                    to_write.write("{0:.8f},".format(volume))

                    ### k2 box ###
                    # print "bounding box k = 2: "
                    volume = ana.box_volume(matrix[0:num_graphs], 2) / divider[1]
                    to_write.write("{0:.8f},".format(volume))

                    ### diameter ###
                    print("diameter: ")
                    sums = 0
                    if len(matrix) > 3000:
                        matrix_temp = matrix[0:3000]
                        for i in range(runtime):
                            sums += ana.diameter_measure(matrix_temp) / divider[2]
                        volume = float(sums)/runtime
                    else:
                        volume = ana.diameter_measure(matrix) / divider[2]
                    volume = 1
                    to_write.write("{0:.8f},".format(volume))

                    ### elpase ###
                    print("robust elapse: ")
                    volume = ana.elapse_measure(matrix[0:num_graphs]) / divider[3]
                    to_write.write("{0:.8f}\n".format(volume))

                    if truth_time == 1:
                        continue
                    truth_time = 1
                    to_write2.write(name + ",")
                    ### box ###
                    print("bounding box: ")
                    volume = ana.box_volume(truth[0:num_graphs]) / divider[0]
                    to_write2.write("{0:.8f},".format(volume))

                    ### k2 box ###
                    print("bounding box k = 2: ")
                    volume = ana.box_volume(truth[0:num_graphs], 2) / divider[1]
                    to_write2.write("{0:.8f},".format(volume))

                    ### diameter ###
                    print("diameter: ")
                    sums = 0
                    if len(truth) > 3000:
                        matrix_temp = truth[0:3000]
                        for i in range(runtime):
                            sums += ana.diameter_measure(matrix_temp) / divider[2]
                        volume = float(sums)/runtime
                    else:
                        volume = ana.diameter_measure(truth[0:num_graphs]) / divider[2]
                    to_write2.write("{0:.8f},".format(volume))

                    ### elpase ###
                    print("robust elapse: ")
                    volume = ana.elapse_measure(truth[0:num_graphs]) / divider[3]
                    to_write2.write("{0:.8f}\n".format(volume))
            print(index)


def writing_representation_data():
    folder = "./new_graph_set/"
    # folder = "./"
    name_list = ["ER_T", "ER_U", "WS", "BA", "geo"]
    ana = coverMeasure()

    # percentage = [1,2,5,10]
    percentage = [100]
    to_write = open("data_rep_bench_3.txt", "w")
    to_write2 = open("rep_gt.txt_3", "w")

    to_write.write("model name/index,")
    to_write.write("KL,")
    to_write.write("WS\n")

    to_write2.write("model name/index,")
    to_write2.write("KL,")
    to_write2.write("WS\n")
    for percent in percentage:
        for index in range(4, 6):
            # Ground truth
            truth = np.loadtxt(folder + "Graph" + str(index) + ".csv", delimiter=",")
            np.random.shuffle(truth)
            inner_folder = "v=" + str(index) + "/"
            to_write.write(str(percent) + "%\n")
            to_write2.write(str(percent) + "%\n")
            for name in name_list:
                for time in range(10):
                    matrix = np.loadtxt(folder + inner_folder + name + "_" +
                                        str(index) + "_" + str(time) + ".csv", delimiter=",")

                    num_graphs = int(float(percent * len(truth))/100)
                    # num_graphs = len(matrix)
                    to_write.write(name + ",")
                    to_write2.write(name + ",")
                    # KL divergence
                    # print matrix[0:num_graphs]
                    num = ana.KL_divergence(matrix[0:num_graphs], truth)
                    if num is not None:
                        to_write.write("{0:.8f},".format(float(num)))

                    # WS distance
                    num = ana.WS_distance(matrix[0:num_graphs], truth)
                    if num is not None:
                        to_write.write("{0:.8f}\n".format(num))

                    truth = np.random.permutation(truth)
                    num = ana.KL_divergence(truth[0:num_graphs], truth)
                    if num is not None:
                        to_write2.write("{0:.8f},".format(float(num)))

                    # WS distance
                    num = ana.WS_distance(truth[0:num_graphs], truth)
                    if num is not None:
                        to_write2.write("{0:.8f}\n".format(num))
            print(index)


if __name__ == '__main__':
    # writing_coverage_data()
    writing_representation_data()
