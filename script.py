The script used in the analysis of the images 

# -*- coding: utf-8 -*-
"""
Bruno’s Research

@author: xenificity
"""
print("Red staining is divided into three levels\n\n","Please wait!\n\n\n")

#Importing libraries
import cv2
import numpy as np
import pandas as pd
import os
directory=os.chdir("C:/Users/Lenovo/Desktop/Assoted photos")
list_dir=os.listdir(directory)

def identify_stain():
    result = pd.DataFrame(columns=['Image','Total_pixels','High_red','medium_red','low_red','perc_high_red','perc_med_red','perc_low_red'])
    for i in list_dir:
    #importing image -representing your original image  
        image = cv2.imread(str(i))
        #cv2.imshow("image",image)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        
        #Converting image RGB into HSV -Gives more insights from your original image
        img_hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV) 
        #cv2.imshow("image",img_hsv)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        
        
        
        def red_intensity_high():
            lower_bound = np.array([170,50, 50]) 
            upper_bound = np.array([255,255, 255]) 
            msk = cv2.inRange(img_hsv, lower_bound, upper_bound) 
            #cv2.imshow("image",msk)
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()
            
            height, width = msk.shape[:2] 
            num_pixels = height * width
            count_white = cv2.countNonZero(msk) 
            percent_high_red_pixels = (count_white/num_pixels) * 100 
            percent_high_red_pixels = round(percent_high_red_pixels,2) 
            high_red_pixels=count_white
            
            return num_pixels,high_red_pixels,percent_high_red_pixels 
        
        
        def red_intensity_medium():
            lower_bound = np.array([85,50, 50]) 
            upper_bound = np.array([170,255, 255]) 
            msk = cv2.inRange(img_hsv, lower_bound, upper_bound) 
            #cv2.imshow("image",msk)
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()
            
            height, width = msk.shape[:2] 
            num_pixels = height * width
            count_white = cv2.countNonZero(msk) 
            percent_medium_red_pixels = (count_white/num_pixels) * 100 
            percent_medium_red_pixels = round(percent_medium_red_pixels,2) 
            medium_red_pixels = count_white
            
            return medium_red_pixels,percent_medium_red_pixels 
        
        
        def red_intensity_low():
            lower_bound = np.array([0,50, 50]) 
            upper_bound = np.array([85,255, 255]) 
            msk = cv2.inRange(img_hsv, lower_bound, upper_bound) 
            #cv2.imshow("image",msk)
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()
            
            height, width = msk.shape[:2] 
            num_pixels = height * width
            count_white = cv2.countNonZero(msk) 
            percent_low_red_pixels = (count_white/num_pixels) * 100 
            percent_low_red_pixels = round(percent_low_red_pixels,2) 
            low_red_pixels=count_white
            
            return low_red_pixels,percent_low_red_pixels 
          
        
        a,b,c=red_intensity_high()
        d,e=red_intensity_medium()
        f,g=red_intensity_low()
        data = [[str(i),int(a),int(b),int(c),int(d),int(e),int(f),int(g)]]
        data_new = pd.DataFrame(data,columns=['Image','Total_pixels','High_red','medium_red','low_red','perc_high_red','perc_med_red','perc_low_red'])
        result = pd.concat([result,data_new])
        print(result)
        
        #print(xyz)
        #print("Results are: High",result_1,"Medium",result_2,"low",result_3)
    
    return result
        
        #result.to_csv('C:/Users/Lenovo/Desktop/Assoted photos/results.csv')
output=identify_stain()
output.to_csv('D:/bruno.csv'
