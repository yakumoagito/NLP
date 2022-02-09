import cv2
import glob




# #加载背景图片
# bk_img = cv2.imread("pig.png")
# cv2.imshow("show",bk_img)
# cv2.waitKey()
# print(bk_img.shape)
# i=str(input('input:'))
# #在图片上添加文字信息
# cv2.putText(bk_img,i, (100,100), cv2.FONT_HERSHEY_SIMPLEX, 
# 0.7,(255,255,255), 1, cv2.LINE_AA)
# #显示图片
# cv2.imshow("add_text",bk_img)
# cv2.waitKey()
# #保存图片
# cv2.imwrite("add_text.jpg",bk_img)

for jpgfile in glob.glob('*.jpg'):
    img = cv2.imread(jpgfile)
    # img2 = img.copy()
    print(jpgfile)
    cv2.imshow("show",img)
    cv2.waitKey()
    print(img.shape)
    i=str(input('input:'))
    #在图片上添加文字信息
    cv2.putText(img,i, (100,100), cv2.FONT_HERSHEY_SIMPLEX, 
    1.4,(111,234,57), 2, cv2.LINE_AA)
    #显示图片
    cv2.imshow("add_text",img)
    cv2.waitKey()
    cv2.imwrite('D:/test/'+i+jpgfile, img)
    