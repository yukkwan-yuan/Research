#!/usr/bin/env python3
import cv2
import imutils
# 人脸识别分类器
faceCascade = cv2.CascadeClassifier('/home/ykyuan/OpenCV_xml/haarcascade_frontalface_default.xml')
# 识别眼睛的分类器
# eyeCascade = cv2.CascadeClassifier('/home/ykyuan/OpenCV_xml/haarcascade_eye.xml')
eyeCascade = cv2.CascadeClassifier('/home/ykyuan/OpenCV_xml/haarcascade_mcs_nose.xml')
# 开启摄像头
# cap = cv2.VideoCapture(0)
cap = cv2.imread('./1.jpg')
ok = True
nosej=["左鼻孔","右鼻孔"]
center=[";","\n"]
cv2.imshow("image", cap)
while ok:
    # 读取摄像头中的图像，ok为是否读取成功的判断参数
    #ok, img = cap.read()
    img = cap
    img2 = img

    cv2.rectangle(img, (309, 158), (342, 174), (255, 0, 0), 1)

    
    # 設定ROI區域，該區域由yolo得出，但爲了可視化，目前設固定
    image=img[160:172,309:342]
    #for (x, y, w, h) in img:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 40, 255, cv2.THRESH_BINARY_INV)[1]
    #cv2.imshow("thresh", thresh)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)  
    #cv2.drawContours(image,contours,-1,(0,0,255),3)
 


    m=1
    for c in contours:
        m+=1
        n=m%2
        M = cv2.moments(c)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

        cv2.drawContours(image, [c], -1, (0, 0, 255), 2)
        cv2.circle(image, (cX, cY), 1, (255, 255, 255), -1)
        # cv2.putText(image, "center", (cX , cY ),
        # cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        #cv2.imshow('video', image)
        cv2.imshow("image", img)

    #img3=thresh
    #cnts = cv2.findContours(img3, cv2.RETR_EXTERNAL,
    #                                  cv2.CHAIN_APPROX_SIMPLE)
    # cnts = imutils.grab_contours(cnts)

    # m=1
    # for c in cnts:
    #     m+=1
    #     n=m%2
    #     M = cv2.moments(c)
    #     cX = int(M["m10"] / M["m00"])
    #     cY = int(M["m01"] / M["m00"])
    # #             # 在图像上绘制形状的轮廓和中心
    #     cv2.drawContours(image2, [c], -1, (0, 255, 0), 2)
    #     cv2.circle(image2, (cX, cY), 7, (255, 255, 255), -1)
    #     cv2.putText(image2, "center", (cX - 20, cY - 20),
    #     cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    #             # 展示图片
    

    # cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
    #                                     cv2.CHAIN_APPROX_SIMPLE)
    # cnts = imutils.grab_contours(cnts)
    # try:
    # for (ex, ey, ew, eh) in result:
    #     cv2.rectangle(img, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)  # 鼻子
    #     img_eye_l = cv2.resize(img2[result[0][1]:result[0][1] + result[0][3], result[0][0]:result[0][0] + result[0][2]], (300, 300))
    #     img_eye_l = img_eye_l[60:240, 10:290]
    #     image = img_eye_l
    #     image = cv2.resize(image, (image.shape[1], image.shape[0]))
    #     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 灰度
    #     blurred = cv2.GaussianBlur(gray, (5, 5), 0)  # 5x5的内核的高斯平滑
    #         ##################################
    #     thresh = cv2.threshold(blurred, 40, 255, cv2.THRESH_BINARY_INV)[1]  # 阈值化，阈值化后形状被表示成黑色背景上的白色前景。
    #         #############################    ↑  (1,74)
    #     cv2.imshow("Image", thresh)
    #         # 在阈值图像中查找轮廓
    #         # 找到白色对应的边界点的集合
    #     cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
    #                                 cv2.CHAIN_APPROX_SIMPLE)
    #     cnts = imutils.grab_contours(cnts)
    #         # 计算轮廓中心
    #     m=1
    #     for c in cnts:
    #         m+=1
    #         n=m%2
    #         M = cv2.moments(c)
    #         cX = int(M["m10"] / M["m00"])
    #         cY = int(M["m01"] / M["m00"])
    #             # 在图像上绘制形状的轮廓和中心
    #         cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
    #         cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
    #         cv2.putText(image, "center", (cX - 20, cY - 20),
    #                         cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

                # 展示图片
            #cv2.imshow("Image", image)
                # with open(file_path, 'w') as w_obj:
                #     w_obj.write(str(cX) +' ' + str(cY)+ "\n")
            #cv2.waitKey(1)
                # print("左鼻孔:", cX, "右鼻孔:", cY)
            # print("相对于鼻子的坐标："f"{nosej[n]}:"f"({cX},{cY})",end=center[0])
            # print("相对于脸的坐标："f"{nosej[n]}:"f"({cX+x},{cY+y})",end=center[0])
            # print("相对于摄像头的坐标："f"{nosej[n]}:"f"({cX + ex},{cY + ey})", end=center[1])
    

    #cv2.imshow('video', img)

    k = cv2.waitKey(1)
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()

