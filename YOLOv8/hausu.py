import cv2
import numpy as np
import glob
import os


pr_filepath ="./pr"
gt_filepath ="./gt"

files=glob.glob(gt_filepath+"/*.png")

for file in files:
    min_dis = []
    distance = []
    number = []
    basename = os.path.basename(file)
    basename_without_ext = os.path.splitext(basename)[0]

    if os.path.exists(os.path.join(pr_filepath, basename)) and os.path.exists(os.path.join(gt_filepath, basename)):
      
        pr_img = cv2.imread(pr_filepath + "/"+basename, cv2.IMREAD_GRAYSCALE)
        gt_img = cv2.imread(gt_filepath + "/"+basename, cv2.IMREAD_GRAYSCALE)
        # cv2.imshow("j",pr_img)
        # cv2.waitKey(0)
        # print(pr_img)


        pr_contours, _ = cv2.findContours(pr_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        gt_contours, _ = cv2.findContours(gt_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

        # print(pr_contours)

      


        # print(pr_contours[1])
        for i in range (len(pr_contours)):
            num = len(pr_contours[i])
            # print(num)
            number.append(num)
            max_num = max(number)
            # print(max_num)
            max_con_num = number.index(max_num)
            # print(max_con_num)





        for i in range(len(pr_contours[0])):
            pr_x = pr_contours[max_con_num][i][0][0]
            pr_y = pr_contours[max_con_num][i][0][1]

            for j in range(len(gt_contours[0])):
                gt_x = gt_contours[0][j][0][0]
                gt_y = gt_contours[0][j][0][1]
                pr_xy = np.array([pr_x,pr_y])
                gt_xy = np.array([gt_x,gt_y])
                dis=np.linalg.norm(gt_xy-pr_xy)
                # print(dis)
                # print(dis)
                # print(gt_xy)
                distance.append(dis)

            min_dis.append(min(distance))
            distance.clear()
            # print(min_dis) seikai``

       
        hausdorff_distance = max(min_dis)
        print(hausdorff_distance)












