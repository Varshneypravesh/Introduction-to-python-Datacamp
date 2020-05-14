 1. --- PYTHON BASICS

 

--- the python interface
 print(5 / 8)
 print(7+10) # the sum of 7 and 10

--- when to use python
/// for which applications can you use python ?
 > you want to do some quick calculations.
 > for your new business, you want to develop a database-driven website.
 > your boss asks you to clean and analyze the results of the latest satisfaction survey.
above all three are the applications where you can use python.

--- Any comments
# Division
  print(5/8)
# Addition
  print(7+10)

--- Python as a calculator
# addition, subtraction
  print(5+5)
  print(5-5)
# multiplication, division, modulo, and exponentiation
  print(3*5)
  print(10/2)
  print(18%7)
  print(4**2)
# how much is your $100 worth after 7 years
  print(100*1.1**7)

--- Variable Assignment
 savings=100
 print(savings)
 
--- Calculations with variables
 savings=100
 growth_multiplier=1.1
 result=savings*growth_multiplier**7
 print(result)

--- Other variable types
 desc="compound interest"
 profitable=True

--- Guess the type
 a is of type float, b is of type str, c is of type bool

--- Operations with other types
 savings=100
 growth_multiplier=1.1
 desc="compound interest"
 year1=savings*growth_multiplier
 print(type(year1))
 doubledesc=desc+desc
 print(doubledesc)
 
--- Type conversion
 savings = 100
 result = 100 * 1.10 ** 7
 print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")
 pi_string = "3.1415926"
 pi_float=float(pi_string)

--- Can python handle everything ?
 "The correct answer to this multiple choice exercise is answer number " + 2



 2.  ---PYTHON LISTS
                                                          

  
--- Create a list
 hall = 11.25
 kit = 18.0
 liv = 20.0
 bed = 10.75
 bath = 9.50
 areas=[hall,kit,liv,bed,bath]
 print(areas)

--- Create list with different types
 hall = 11.25
 kit = 18.0
 liv = 20.0
 bed = 10.75
 bath = 9.50
 areas= ["hallway",hall,"kitchen",kit,"living room",liv,"bedroom",bed,"bathroom",bath]
 print(areas)

--- Select the valid list
 which ones of the following lines of python code are valid ways to build a list?
 A. [1,3,4,2]   B. [[1,2,3], [4,5,7]]  C. [1+2, "a" *5, 3]
 here, all A, B, C are valid ways to build a list.

--- List of lists
 hall = 11.25
 kit = 18.0
 liv = 20.0
 bed = 10.75
 bath = 9.50
 house = [["hallway", hall],["kitchen", kit],["living room, liv],["bedroom", bed],["bathroom", bath]]
 print(house)
 print(type(house))

--- Subset and conquer
 areas=["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
 print(areas[1])
 print(areas[-1])                              
 print(areas[5])                              

--- Subset and calculate
 areas=["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
 eat_sleep_area=(area[3]+area[7])
 print(eat_sleep_area)                                        
                                              
--- Slicing and dicing
 areas=["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]                                        
 downstairs=(areas[0:6])
 upstairs=(areas[6:11])
 print(downstairs)                                            
 print(upstairs)

--- Slicing and dicing(2)
 areas=["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
 downstairs=areas[:6]
 upstairs=areas[6:]

--- Subsetting list of list 
    What will house[-1][1] ?
 A float: the bathroom area                                          

--- Replace list elements
 areas=["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
 areas[-1]=10.5
 areas[4]="chill zone"

--- Extend a list
 areas=["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 10.50]
 areas_1=areas+["poolhouse", 24.5]
 areas_2=areas_1+["garage", 15.45]

--- Delete list elements
 Now after extending the areas list,
 areas=areas=["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 10.50, "poolhouse", 24.5, "garage", 15.45]                                           
 del(areas[-4:-2])

--- Inner working of lists 
 areas=[11.25, 18.0, 20.0, 10.75, 9.50]
 areas_copy = list(areas)
 print(areas)



3.  --- FUNCTIONS AND PACKAGES


                                                                                    
--- Familiar Functions                                            
 var1=[1,2,3,4]
 var2=True
 print(type(var1))
 print(len(var1))                                   
 out2=int(var2)

--- complex() takes two arguments: real and imag.
    real is a required argument, imag is an optional argument.                                         
    
--- Multiple arguments
 first = [11.25, 18.0, 20.0]
 second = [10.75, 9.50]
 full=first+second
 full_sorted=sorted(full,reverse = True)
 print(full_sorted)

--- String Methods                                              
 place = "poolhouse"
 place_up=place.upper()
 print(place)                                              
 print(place_up)
 print(place.count("o"))

--- List Methods
 areas=[11.25, 18.0, 20.0, 10.75, 9.50]
 print(areas.index(20.0))
 print(areas.count(9.50))

--- List Methods(2)
 areas=[11.25, 18.0, 20.0, 10.75, 9.50]
 areas.append(24.5)
 areas.append(15.45)
 print(areas)
 areas.reverse()
 print(areas)

--- Import package
 r = 0.43
 import math
 C=2*math.pi*r
 A=math.pi*r**2
 print("Circumference: " + str(C))
 print("Area: " + str(A))

--- Selective import
 r = 192500
 from math import radians
 dist=r*radians(12)
 print(dist)

--- Different ways of importing 
 Function inv(), which is in the linalg subpackage of the scipy package. 
 You want to be able to use this function as follows:
            my_inv([[1,2], [3,4]])                                  
 THEN
    from scipy.linalg import inv as my_inv
  above import statement you will need in order to run the above code without an error.                                       





(4) --- NumPy



--- Your First NumPy Array
 baseball = [180, 215, 210, 210, 188, 176, 209, 200]
 import numpy as np
 np_baseball=np.array(baseball)
 print(type(np_baseball))

--- Baseball player's height
 import numpy as np
 np_height_in=np.array(height_in)
 print(np-height_in)
 np_height_m=np_height_in*0.0254
 print(np_height_m)

--- Baseball player's BMI
 import numpy as np
 np_height_m = np.array(height_in) * 0.0254
 np_weight_kg = np.array(weight_lb) * 0.453592
 bmi=np_weight_kg/np_height_m**2
 print(bmi)

--- Lightweight baseball players
 import numpy as np
 np_height_m = np.array(height_in) * 0.0254
 np_weight_kg = np.array(weight_lb) * 0.453592
 bmi = np_weight_kg / np_height_m**2
 light=bmi<21
 print(light)
 print(bmi[light])

--- NumPy Side Effects
 numpy arrays cannot contain elements with different types. If you try to build such a list,
 some of the elements'types are changed to end up with a homogeneous list.
 This is known as type coercion.
                                              
 np.array([True, 1 2]) + np.array([3, 4, False])
 then
     np.array([4, 3, 0]) + np.array([0, 2, 2]) code from all the given options builds the exact 
 same python object.

--- Subsetting NumPy arrays
 import numpy as np 
 np_weight_lb = np.array(weight_lb)
 np_height_in = np.array(height_in)
 print(np_weight_lb[50])
 print(np_height_in[100:111])

--- Your First 2D NumPy Array
 baseball = ([180, 78.4]
             [215, 102.7]       
             [210, 98.5]       
             [188, 75.2])
 import numpy as np
 np_baseball=np.array(baseball)
 print(type(np_baseball))
 print(np_baseball.shape)
 
--- Baseball data in 2D form
 import numpy as np
 np_baseball=np.array(baseball)
 print(np_baseball.shape)

--- Subsetting 2D NumPy Arrays
 import numpy as np
 np_baseball=np.array(baseball)
 print(np_baseball[49:,])
 np_weight_lb=np_baseball[:,1])
 print(np_baseball[123:,0])

--- 2D Arithmetic 
 import numpy as np
 np_baseball=np.array(baseball)
 print(np_baseball+updated)
 conversion=np.array([0.0254,0.453592,1])
 print(np_baseball*conversion)
 
--- Average versus median
 import numpy as np
 np_baseball_in=np.array(np_baseball[:,0])
 print(np.mean(np_height_in)
 print(np.median(np_height_in))

--- Explore the baseball data
 import numpy as np
 avg = np.mean(np_baseball[:,0])
 print("Average: " + str(avg))
 med = np.median(np_baseball[:,0])
 print("Median: " + str(med))
 stddev = np.std(np_baseball[:,0])
 print("Standard Deviation: " + str(stddev))
 corr = np.corrcoef(np_baseball[:,0],np_baseball[:,1])
 print("Correlation: " + str(corr))
 
--- Blend it all together
 import numpy as np
 np_positions=np.array(positions)
 np_heights=np.array(heights)
 gk_heights=np_heights[np_positions=='Gk']
 other_heights=np_heights[np_positions!='Gk']
 print("Median height of goalkeepers: " + str(np.median(gk_heights)))
 print("Median height of other players: " + str(np.median(other_heights))) 



 



                                              
 


                                              
