import cv2
image = cv2.imread('example.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
resized_image = cv2.resize(gray_image, (224, 224))
cv2.imshow('processd image',resized_image)
key = cv2.waitKey(0)
if key == ord('s'):
    cv2.imwrite('grayscale_resized_image.jpg', resized_image)
    print('image saved as grayscale_resized_image.jpg')
else:
    print('image not saved')
cv2.destroyAllWindows()
print(f"processed image dimensions: {resized_image.shape}")
