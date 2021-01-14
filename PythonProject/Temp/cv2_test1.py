import cv2

def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    img = cv2.imread('fw658.jpeg')
    cv_show('image', img)

if __name__ == "__main__":
    main()