import cv2
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html

def demo1():
    # 而opencv默认通道是bgr的
    flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
    print("显示所有的转换模式：", flags)

    img = cv2.imread('../imagelib/lenna.jpg')
    # 转换为灰度图
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.cvtColor()用来进行颜色模型转换，参数1是要转换的图片，参数2是转换模式， COLOR_BGR2GRAY表示BGR→Gray
    cv2.imshow('img', img)
    cv2.imshow('gray', img_gray)
    cv2.waitKey(0)


"""
HSV是一个常用于颜色识别的模型，相比BGR更易区分颜色，转换模式用COLOR_BGR2HSV表示。

经验之谈：OpenCV中色调H范围为[0,179]，饱和度S是[0,255]，明度V是[0,255]。
虽然H的理论数值是0°~360°，但8位图像像素点的最大值是255，所以OpenCV中除以了2，某些软件可能使用不同的尺度表示，所以同其他软件混用时，记得归一化。
"""
# 只保留蓝色部分
def demo2():
    import numpy as np
    capture = cv2.VideoCapture(r"E:\bigdata\ai\video\1.mp4")
    # 蓝色的范围，不同光照条件下不一样，可灵活调整
    lower_blue = np.array([100, 110, 110])
    upper_blue = np.array([130, 255, 255])

    while (True):
        # 1.捕获视频中的一帧
        ret, frame = capture.read()

        # 2.从BGR转换到HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # 3.提取蓝色范围的物体 inRange()：介于lower/upper之间的为白色，其余黑色
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        # 4.只保留原图中的蓝色部分
        res = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('res', res)

        if cv2.waitKey(1) == ord('q'):
            break

"""
HSV介绍
HSV分别代表，色调（H：hue），饱和度（S：saturation），亮度（V：value），由A. R. Smith在1978年创建的一种颜色空间, 也称六角锥体模型(Hexcone Model)；

色调（H：hue）：用角度度量，取值范围为0°～360°，从红色开始按逆时针方向计算，红色为0°，绿色为120°,蓝色为240°。它们的补色是：黄色为60°，青色为180°，品红为300°；（OpenCV中H的取值范围为0~180，8bit存储时）；

饱和度（S：saturation）：取值范围为0~255，值越大，颜色越饱和；

亮度（V：value）：取值范围为0(黑色)～255(白色)；

实现思路

使用PS取的小猪佩奇颜色的HSB值，相当于OpenCV的HSV，不过PS的HSV（HSB）取值是：0360、01、01，而OpenCV的HSV是：0180、0255、0255，所以要对ps的hsv进行处理，H/2、SV*255；
使用OpenCV位“与运算”提取HSV的颜色部分画面；
使用高斯模糊优化图片；
图片展示；
"""

# 对象提取2 https://www.cnblogs.com/vipstone/p/9127383.html
def demo3():
    # HSV转换（颜色提取）

    import cv2
    import numpy as np

    cap = cv2.VideoCapture(r"E:\bigdata\ai\video\1.mp4")

    while (1):
        _, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # 在PS里用取色器的HSV
        psHSV = [112, 89, 52]
        diff = 40  # 上下浮动值
        # 因为PS的HSV（HSB）取值是：0~360、0~1、0~1，而OpenCV的HSV是：0~180、0~255、0~255，所以要对ps的hsv进行处理，H/2、SV*255
        lowerHSV = [(psHSV[0] - diff) / 2, (psHSV[1] - diff) * 255 / 100,
                    (psHSV[2] - diff) * 255 / 100]
        upperHSV = [(psHSV[0] + diff) / 2, (psHSV[1] + diff) * 255 / 100,
                    (psHSV[2] + diff) * 255 / 100]

        mask = cv2.inRange(hsv, np.array(lowerHSV), np.array(upperHSV))

        # 使用位“与运算”提取颜色部分
        res = cv2.bitwise_and(frame, frame, mask=mask)
        # 使用高斯模式优化图片
        res = cv2.GaussianBlur(res, (5, 5), 1)

        cv2.imshow('frame', frame)
        # cv2.imshow('mask', mask)
        cv2.imshow('res', res)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

demo3()