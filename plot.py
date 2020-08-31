import cv2 
import numpy as np
import matplotlib.pyplot as plt

img_file1 = 'sample_pictures/1.jpg'
img_file2 = 'sample_pictures/2.jpg'
img_file3 = 'sample_pictures/3.jpg'
img_file4 = 'sample_pictures/4.jpg'
img_file5 = 'sample_pictures/5.jpg'
img_file6 = 'sample_pictures/6.jpg'
img_file7 = 'sample_pictures/7.jpg'
img_file8 = 'sample_pictures/8.jpg'
img_file9 = 'sample_pictures/9.jpg'
img_file10 = 'sample_pictures/10.jpg'
img_file11 = 'sample_pictures/11.jpg'
img_file12 = 'sample_pictures/12.jpg'
img_file13 = 'sample_pictures/13.jpg'
img_file14 = 'sample_pictures/14.jpg'
img_file15 = 'sample_pictures/15.jpg'
img_file16 = 'sample_pictures/16.jpg'
img_file17 = 'sample_pictures/17.jpg'
img_file18 = 'sample_pictures/18.jpg'
img_file19 = 'sample_pictures/19.jpg'
img_file20 = 'sample_pictures/20.jpg'
img_file21 = 'sample_pictures/21.jpg'
img_file22 = 'sample_pictures/22.jpg'
img_file23 = 'sample_pictures/23.jpg'
img_file24 = 'sample_pictures/24.jpg'
img_file25 = 'sample_pictures/25.jpg'
img_file26 = 'sample_pictures/26.jpg'
img_file27 = 'sample_pictures/27.jpg'
img_file28 = 'sample_pictures/28.jpg'
img_file29 = 'sample_pictures/29.jpg'
img_file30 = 'sample_pictures/30.jpg'
img_file31 = 'sample_pictures/31.jpg'
img_file32 = 'sample_pictures/32.jpg'
img_file33 = 'sample_pictures/33.jpg'
img_file34 = 'sample_pictures/34.jpg'
img_file35 = 'sample_pictures/35.jpg'
img_file36 = 'sample_pictures/36.jpg'
img_file37 = 'sample_pictures/37.jpg'
img_file38 = 'sample_pictures/38.jpg'
img_file39 = 'sample_pictures/39.jpg'
img_file40 = 'sample_pictures/40.jpg'
img_file41 = 'sample_pictures/41.jpg'
img_file42 = 'sample_pictures/42.jpg'
img_file43 = 'sample_pictures/43.jpg'
img_file44 = 'sample_pictures/44.jpg'
# img = cv2.imread(img_file, cv2.IMREAD_COLOR) #rgb
gray_img1 = cv2.imread(img_file1, cv2.IMREAD_GRAYSCALE) #grayscale
gray_img2 = cv2.imread(img_file2, cv2.IMREAD_GRAYSCALE)
gray_img3 = cv2.imread(img_file3, cv2.IMREAD_GRAYSCALE)
gray_img4 = cv2.imread(img_file4, cv2.IMREAD_GRAYSCALE)
gray_img5 = cv2.imread(img_file5, cv2.IMREAD_GRAYSCALE)
gray_img6 = cv2.imread(img_file6, cv2.IMREAD_GRAYSCALE)
gray_img7 = cv2.imread(img_file7, cv2.IMREAD_GRAYSCALE)
gray_img8 = cv2.imread(img_file8, cv2.IMREAD_GRAYSCALE)
gray_img9 = cv2.imread(img_file9, cv2.IMREAD_GRAYSCALE)
gray_img10 = cv2.imread(img_file10, cv2.IMREAD_GRAYSCALE)
gray_img11 = cv2.imread(img_file11, cv2.IMREAD_GRAYSCALE)
gray_img12 = cv2.imread(img_file12, cv2.IMREAD_GRAYSCALE)
gray_img13 = cv2.imread(img_file13, cv2.IMREAD_GRAYSCALE)
gray_img14 = cv2.imread(img_file14, cv2.IMREAD_GRAYSCALE)
gray_img15 = cv2.imread(img_file15, cv2.IMREAD_GRAYSCALE)
gray_img16 = cv2.imread(img_file16, cv2.IMREAD_GRAYSCALE)
gray_img17 = cv2.imread(img_file17, cv2.IMREAD_GRAYSCALE)
gray_img18 = cv2.imread(img_file18, cv2.IMREAD_GRAYSCALE)
gray_img19 = cv2.imread(img_file19, cv2.IMREAD_GRAYSCALE)
gray_img20 = cv2.imread(img_file20, cv2.IMREAD_GRAYSCALE)
gray_img21 = cv2.imread(img_file21, cv2.IMREAD_GRAYSCALE)
gray_img22 = cv2.imread(img_file22, cv2.IMREAD_GRAYSCALE)
gray_img23 = cv2.imread(img_file23, cv2.IMREAD_GRAYSCALE)
gray_img24 = cv2.imread(img_file24, cv2.IMREAD_GRAYSCALE)
gray_img25 = cv2.imread(img_file25, cv2.IMREAD_GRAYSCALE)
gray_img26 = cv2.imread(img_file26, cv2.IMREAD_GRAYSCALE)
gray_img27 = cv2.imread(img_file27, cv2.IMREAD_GRAYSCALE)
gray_img28 = cv2.imread(img_file28, cv2.IMREAD_GRAYSCALE)
gray_img29 = cv2.imread(img_file29, cv2.IMREAD_GRAYSCALE)
gray_img30 = cv2.imread(img_file30, cv2.IMREAD_GRAYSCALE)
gray_img31 = cv2.imread(img_file31, cv2.IMREAD_GRAYSCALE)
gray_img32 = cv2.imread(img_file32, cv2.IMREAD_GRAYSCALE)
gray_img33 = cv2.imread(img_file33, cv2.IMREAD_GRAYSCALE)
gray_img34 = cv2.imread(img_file34, cv2.IMREAD_GRAYSCALE)
gray_img35 = cv2.imread(img_file35, cv2.IMREAD_GRAYSCALE)
gray_img36 = cv2.imread(img_file36, cv2.IMREAD_GRAYSCALE)
gray_img37 = cv2.imread(img_file37, cv2.IMREAD_GRAYSCALE)
gray_img38 = cv2.imread(img_file38, cv2.IMREAD_GRAYSCALE)
gray_img39 = cv2.imread(img_file39, cv2.IMREAD_GRAYSCALE)
gray_img40 = cv2.imread(img_file40, cv2.IMREAD_GRAYSCALE)
gray_img41 = cv2.imread(img_file41, cv2.IMREAD_GRAYSCALE)
gray_img42 = cv2.imread(img_file42, cv2.IMREAD_GRAYSCALE)
gray_img43 = cv2.imread(img_file43, cv2.IMREAD_GRAYSCALE)
gray_img44 = cv2.imread(img_file44, cv2.IMREAD_GRAYSCALE)

# print ('Gray shape:', gray_img.shape)

#intensity of apple
intensity_of_apple = np.array([gray_img1[180, 310],gray_img2[180, 310],gray_img3[180, 310],gray_img4[180, 310],gray_img5[180, 310],
             gray_img6[180, 310],gray_img7[180, 310],gray_img8[180, 310],gray_img9[180, 310],gray_img10[180, 310],
             gray_img11[180, 310],gray_img12[180, 310],gray_img13[180, 310],gray_img14[180, 310],gray_img15[180, 310],
             gray_img16[180, 310],gray_img17[180, 310],gray_img18[180, 310],gray_img19[180, 310],gray_img20[180, 310],
             gray_img21[180, 310],gray_img22[180, 310],gray_img23[180, 310],gray_img24[180, 310],gray_img25[180, 310],
             gray_img26[180, 310],gray_img27[180, 310],gray_img28[180, 310],gray_img29[180, 310],gray_img30[180, 310],
             gray_img31[180, 310],gray_img32[180, 310],gray_img33[180, 310],gray_img34[180, 310],gray_img35[180, 310],
             gray_img36[180, 310],gray_img37[180, 310],gray_img38[180, 310],gray_img39[180, 310],gray_img40[180, 310],
             gray_img41[180, 310],gray_img42[180, 310],gray_img43[180, 310],gray_img44[180, 310]])

#intensity of paper
intensity_of_paper = np.array([gray_img1[20, 630],gray_img2[20, 630],gray_img3[20, 630],gray_img4[20, 630],gray_img5[20, 630],
             gray_img6[20, 630],gray_img7[20, 630],gray_img8[20, 630],gray_img9[20, 630],gray_img10[20, 630],
             gray_img11[20, 630],gray_img12[20, 630],gray_img13[20, 630],gray_img14[20, 630],gray_img15[20, 630],
             gray_img16[20, 630],gray_img17[20, 630],gray_img18[20, 630],gray_img19[20, 630],gray_img20[20, 630],
             gray_img21[20, 630],gray_img22[20, 630],gray_img23[20, 630],gray_img24[20, 630],gray_img25[20, 630],
             gray_img26[20, 630],gray_img27[20, 630],gray_img28[20, 630],gray_img29[20, 630],gray_img30[20, 630],
             gray_img31[20, 630],gray_img32[20, 630],gray_img33[20, 630],gray_img34[20, 630],gray_img35[20, 630],
             gray_img36[20, 630],gray_img37[20, 630],gray_img38[20, 630],gray_img39[20, 630],gray_img40[20, 630],
             gray_img41[20, 630],gray_img42[20, 630],gray_img43[20, 630],gray_img44[20, 630]])

plt.subplot(1,2,1)
plt.plot([400,405,410,415,420,430,436,442,450,455,\
          458,467,470,480,486,488,492,500,505,508,\
          510,515,520,532,535,540,546,550,568,580,\
          589,600,610,620,632,636,640,647,650,656,\
          671,676,690,694],intensity_of_apple[::-1])
plt.title("apple slice")
plt.xlabel("wavelength (nm)")
plt.ylabel("intensity (0-255)")

plt.subplot(1,2,2)
plt.plot([400,405,410,415,420,430,436,442,450,455,\
          458,467,470,480,486,488,492,500,505,508,\
          510,515,520,532,535,540,546,550,568,580,\
          589,600,610,620,632,636,640,647,650,656,\
          671,676,690,694],intensity_of_paper[::-1])
plt.title("white paper")
plt.xlabel("wavelength (nm)")
plt.ylabel("intensity (0-255)")

plt.suptitle("hyperspectral response")
plt.show()