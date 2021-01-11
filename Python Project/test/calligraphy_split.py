import numpy as np
import cv2
from matplotlib import pyplot as plt
import os


class PrCalligraph(object):

    filename = 0
    dirname = ""

    def cut_img(self, img, flag_pi):
        row, col = img.shape
        for i in range(row-1):
            if img[i, col/2] <= flag_pi:
                new_up_row = i
                break
        for i in range(col-1):
            if img[row/2, i] <= flag_pi:
                new_left_col = i
                break
        for i in range(row-1, 0, -1):
            if img[i, col/2] <= flag_pi:
                new_down_row = i
                break
        for i in range(col-1, 0, -1):
            if img[row/2, i] <= flag_pi:
                new_right_col = i
                break
        print(new_up_row, new_left_col, new_down_row, new_right_col)
        return new_up_row, new_left_col, new_down_row, new_right_col

    # deal the image with binaryzation
    def thresh_binary(self, img):
        blur = cv2.GaussianBlur(img, (9, 9), 0)
        # OTSU's binaryzation
        ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        kernel = np.ones((2, 2), np.uint8)
        opening = cv2.morphologyEx(th3, cv2.MORPH_OPEN, kernel)
        return opening

    # sum the black pixel numbers in each cols
    def hist_col(self, img):
        list=[]
        row, col = img.shape
        for i in xrange(col):
            list.append((img[:, i] < 200).sum())
        return list

    # find the each segmentatoin cols
    def cut_col(self, img, hist_list):
        minlist = []
        images = []
        row, col = img.shape
        np_list = np.array(hist_list)
        avg = col/8
        i = 0
        # print np_list
        while i < col-1:
            if i >= col-10:
                if np_list[i] < 40 and np_list[i] <= np_list[i+1: col].min():
                    minlist.append(i)
                    break
                if i == col-1:
                    minlist.append(i)
                    break
            else:
                if np_list[i] < 40 and np_list[i] < np_list[i+1: i+10].min():
                    minlist.append(i)
                    i += avg
            i += 1
        print(minlist)
        for j in xrange(len(minlist)-1):
            print(j)
            images.append(img[0:row, minlist[j]:minlist[j+1]])
        return images

    # sum the black pixel numbers in each rows
    def hist_row(self, img):
        list=[]
        row, col = img.shape
        for i in xrange(row):
            list.append((img[i, :] < 200).sum())
        return self.cut_row(img, list)

    # find each segmentation rows
    def cut_row(self, img, row_list):
        minlist = []
        single_images_with_rect = []
        row, col = img.shape
        np_list = np.array(row_list)
        avg = row/16
        i = 0
        while i <= row-1:
            if i >= row-10 and np_list[i] == 0:
                minlist.append(i)
                break
            elif np_list[i] == 0 and (np_list[i+1: i+10] < 200).sum() >= 5:
                minlist.append(i)
                i += avg
            i += 1
        print(minlist)
        for j in xrange(len(minlist)-1):
            single_img = img[minlist[j]:minlist[j+1], 0:col]
            single_img_with_rect = self.single_cut(single_img)
            if single_img_with_rect is not None:
                single_images_with_rect.append(single_img_with_rect)
        return single_images_with_rect

    # find the single word's contours and take off the redundant margin
    def single_cut(self, img):
        blur = cv2.GaussianBlur(img, (9, 9), 0)
        ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        contours, hierarchy = cv2.findContours(th3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        up, left = img.shape
        down, right = 0, 0
        for i in range(len(contours)):
            cnt = contours[i]
            x, y, w, h = cv2.boundingRect(cnt)
            if w < 6 and h < 6:
                continue
            if x < up:
                up = x
            if y < left:
                left = y
            if x+w > down:
                down = x+w
            if y+h > right:
                right = y+h
        if down-up >= 40 and right-left >= 40:
            word = img[left:right, up:down]
            cv2.imwrite(self.dirname+str(self.filename)+'.png', word)
            cv2.rectangle(img,(up, left), (down, right), (0, 255, 0), 2)
            self.filename += 1
            return img
        else:
            return None

if __name__ == '__main__':

    prcaligraphy = PrCalligraph()
    # read sys origin dir
    origin_images = os.listdir('./calligraphies/')
    # handle each picture
    for im in origin_images:
        # use for new single word filename
        prcaligraphy.filename = 0
        # take out the original picture's name
        outdir = os.path.splitext(im)[0]
        # mkdir  output dir name/path
        prcaligraphy.dirname = "./split/"+outdir+'/'
        os.makedirs(prcaligraphy.dirname, False)
        # use opencv read images
        img = cv2.imread('./calligraphies/'+im, cv2.IMREAD_GRAYSCALE)
        # preprocess original picture, cutout the redundant margin
        row, col = img.shape
        middle_pi = img[row/2, col/2]
        if middle_pi > 220:
            middle_pi = 220
        else:
            middle_pi += 10
        new_up_row, new_left_col, new_down_row, new_right_col = prcaligraphy.cut_img(img, middle_pi)
        cutedimg = img[new_up_row:new_down_row, new_left_col:new_right_col]
        # deal the image with binaryzation
        opening = prcaligraphy.thresh_binary(cutedimg)
        # split the image into pieces with cols
        hist_list = prcaligraphy.hist_col(opening)
        images = prcaligraphy.cut_col(opening, hist_list)
        # create two plt
        fig, axes = plt.subplots(1, len(images), sharex=True, sharey=True)
        fig2, axes2 = plt.subplots(len(images), 12, sharex=True, sharey=True)
        # split the pieces into single words by rows
        for i in range(len(images)):
            axes[i].imshow(images[i], 'gray')
            single_images_with_rect = prcaligraphy.hist_row(images[i])
            for j in range(len(single_images_with_rect)):
                axes2[i, j].imshow(single_images_with_rect[j], 'gray')
        fig.savefig(prcaligraphy.dirname+'cut_col.png')
        fig2.savefig(prcaligraphy.dirname+'single.png')
        plt.clf()
    # plt.show()

# cv2.imshow('image', imageee)
# cv2.waitKey(0)
# cv2.destroyAllWindows()