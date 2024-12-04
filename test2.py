import cv2

# 打开图像
img = cv2.imread('1.jpg', 1)

# 创建一个可调整大小的窗口
#cv2.namedWindow('result', cv2.WINDOW_NORMAL)

# 设置窗口大小
#cv2.resizeWindow('result', 800, 600)


# 显示图像
cv2.imshow('Image', img)


cv2.imwrite('11.jpg', img)

cv2.waitKey(0)

cv2.destroyAllWindows()
# 保存图像







