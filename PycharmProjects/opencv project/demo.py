import cv2
import numpy as np
# image=cv2.imread('download.png',1)
# cv2.imshow('original',image)
cap=cv2.VideoCapture(0)
while(1):
    _,frame=cap.read()
    new_image=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow('image',new_image)

    low_bound=np.array([110,50,50])
    up_bound=np.array([130,252,252])
    mask=cv2.inRange(new_image,low_bound,up_bound,)
    cv2.imshow('mask',mask)

    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('res',res)

# print(image)
# cv2.imshow('image',image)
# cv2.waitKey(10000)
# cv2.imwrite('shirt.png',image)
# cv2.destroyAllWindows()
# cv2.line(image,(0,0),(400,400),(255,0,0),4)
# cv2.rectangle(image,(0,0),(400,400),(0,255,0),5)
# cv2.circle(image,(200,200),100,(0,0,255),-1)
# font=cv2.FONT_HERSHEY_TRIPLEX
# cv2.putText(image,'hai',(100,100),font,4,(255,255,255),cv2.LINE_AA)
# cv2.imshow('shapes',image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# def draw_cicle(event,x,y,flag,parameter):
#     if event == cv2.EVENT_LBUTTONDBLCLK:
#         cv2.circle(image,(x,y),100,(0,0,255),-1)
# cv2.namedWindow('image')
# cv2.setMouseCallback('image',draw_cicle)
#
# while(1):
#     cv2.imshow('image',image)
#     if cv2.waitKey(20) & 0xFF == 27:
#         break


# image=cv2.imread('gradient.jpg',0)
# ret,thresh=cv2.threshold(image,60,255,cv2.THRESH_BINARY)
# cv2.imshow('image',image)
# cv2.imshow('thresh',thresh)

# image=cv2.imread('shirt.jpg',1)
# matrix=np.ones((5,5),np.float32)/25
# new_image=cv2.filter2D(image,-1,matrix)
# blur=cv2.blur(image,(5,5))
# gaussian=cv2.GaussianBlur(image,(5,5),0)
# cv2.imshow('image',image)
# cv2.imshow('new_image',new_image)
# cv2.imshow('blur',blur)
# cv2.imshow('gaussian',gaussian)
    k= cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()