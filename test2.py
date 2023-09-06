import cv2

# 读取两个图像
image1 = cv2.imread('screenshot.png')
image2 = cv2.imread('Snipaste.png')

# 比较两个图像
difference = cv2.subtract(image1, image2)

# 计算差异图像的总和
sum_of_differences = difference.sum()

# 设置阈值，用于判断两个图像是否不同
threshold = 1000  # 根据需要调整阈值

# 如果总差异超过阈值，则认为图像不同（正确），否则认为图像相同（不正确）
if sum_of_differences > threshold:
    print("图像不同（正确）")
else:
    print("图像相同（不正确）")
import sys
sys.path.append(r'C:\Users\CUSTOMIZEPC-24\PycharmProjects\ui\Common')


