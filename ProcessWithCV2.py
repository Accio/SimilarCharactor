# coding=gbk
import cv2
import Character
from tqdm import tqdm

# ���ݻҶȱȽ�����ͼƬ��hash����
def dHash(img1,img2):
    img1 = cv2.resize(img1, (12,12), interpolation=cv2.INTER_CUBIC)
    img2 = cv2.resize(img2, (12,12), interpolation=cv2.INTER_CUBIC)
    gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    similarity = 0
    for i in range(12):
        for j in range(12):
            if gray1[i,j] == gray2[i,j]:
                similarity += 1
            else:
                pass
    return similarity/144

def main():
    file1 = open('D:/py/Shape_CV2.txt', 'w')

    word_pic_path = 'D:/py/chinese/'
    for index1,word1 in tqdm(enumerate(Character.Symbol_lst())):
        # print(index1,word1)
        # print(word_pic_path + str(index1) + '.png')
        word_pic1 = cv2.imread(word_pic_path + str(index1) + '.png')
        file1.write(word1 + ' ')
        for index2, word2 in enumerate(Character.Symbol_lst()):
            word_pic2 = cv2.imread(word_pic_path + str(index2) + '.png')
            if index1 == index2:
                continue
            else:
                # cv2.imshow('image1',word_pic1)
                # cv2.waitKey(0)
                # cv2.imshow('image2',word_pic2)
                # cv2.waitKey(0)
                similar_index = dHash(word_pic1,word_pic2)
                if similar_index > 0.85:
                    print(similar_index, word1, word2)
                    file1.write(word2)
    file1.close()



# 2018-02-05�²��������㱸��
# �ж�����ƥ��ȣ�������0.8����¼�룬��������֧��
# ���ֺ��ֽṹ����Ϊ���ҽṹ������ģʽ1�����Ҳ�ƥ��ȳ���0.9��������ƥ��ȳ���0.8����¼��
# ��Ϊ���½ṹ������ģʽ2�����²�ƥ��ȳ���0.9������ƥ��ȳ���0.8����¼��
# ��Ϊ�����ֽṹ������ģʽ3��������ƥ��ȳ���0.75����¼��

