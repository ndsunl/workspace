import cv2
import numpy as np

mode = 'rectangle'
drawing = False
start = (0,0)
end = (0,0)
img = np.zeros((512, 512, 3), np.uint8)


def mouse_event(event, x, y, flags, param):
    global mode, drawing, start, img, end

    # 鼠标按下，开始画图：记录下起点
    if event == cv2.EVENT_LBUTTONDOWN and drawing == False:
        drawing = True
        start = (x,y)
    # 实时移动的位置作为矩形终点
    elif event == cv2.EVENT_MOUSEMOVE and drawing == True:
        end = (x,y)
    # 鼠标释放后，停止绘图，并画出最终结果
    elif event == cv2.EVENT_LBUTTONUP and drawing == True:
        drawing = False

        # 只需要完成松手时画图出来就行了
        if mode == 'rectangle':
            cv2.rectangle(img, start, (x, y), (0, 255, 0), 3)
        elif mode == 'circle':
            radius = int(((start[0] - x)**2 + (start[1] - y)**2 )**0.5)
            cv2.circle(img, start, radius, (0, 0, 255), 3)

        start = end = (0, 0)

def main():
    global img, mode, start, end
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', mouse_event)

    while(True):
        # 下面这句话很关键，拷贝出原图，这样才可以实时画图形
        temp = np.copy(img)

        if drawing == True and mode == 'rectangle':
            cv2.rectangle(temp, start, end, (0, 255, 0), 3)
        elif drawing == True and mode == 'circle':
            radius = int(((start[0] - end[0])**2 + (start[1] - end[1])**2 )**0.5)
            cv2.circle(temp, start, radius, (0, 0, 255), 3)

        cv2.imshow('image', temp)

        # 等待功能键的输入
        key = cv2.waitKey(70)

        if key == ord('q'):
            cv2.destroyAllWindows()
            break
        elif key == ord('m') and mode == 'rectangle':
            mode = 'circle'
            continue
        elif key == ord('m') and mode == 'circle' :
            mode = 'rectangle'
            continue
        elif key == ord('c'):
            img = np.zeros((512, 512, 3), np.uint8)
            continue

if __name__ == "__main__":
    main()