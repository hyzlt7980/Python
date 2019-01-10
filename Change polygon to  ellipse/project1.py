#csci-2202-project1
#HUI_YANG_B00758346
import random
import stddraw
def td_Matrix(rows,columns,value=None):
    '''
    This Function will create and return an 2D matrix with the value initialize to
    paramater value.
    And it will return the 2D matrix
    '''
    a=[None]*rows
    for i in range(rows):
        a[i]=[value]*columns
    return a


def average_coordinates(array):
    '''
    This function will calculate the x or y coordiantes of new polygon.
    And return the new coordinates.

    '''
    l=len(array)                    # l is the number of coordinates  
    averageM=td_Matrix(l,l,0)       # Create a 2D array with all elements 0
    count=0
    # this for loop create the matrix for doing average of x and y coordinates
    for i in range(l):
        if i==l-1:
            averageM[i][count]=0.5
            averageM[i][0]=0.5    

        else:
            averageM[i][count]=0.5
            averageM[i][count+1]=0.5
            count+=1
        
    average_coordinates=[0]*l
    
    # this for loop multiple the array and matrix. and average_Coordinates will have the new coordinates
    # for x and y

    for i in range(l):
        for j in range(l):
            average_coordinates[i]+=averageM[i][j]*array[j]

    return average_coordinates

def average(x):
    '''
    This function calculate the average of numbers in an array and return it
    '''
    s=0
    for i in range(len(x)):
         s+=x[i]
         

    return s/len(x)
def generate_polygon(number):
    '''
    This function generate the random polygon


    '''
    x=[0]*number
    y=[0]*number

    for i in range(number):
        xP=random.uniform(-50,50)
        yP=random.uniform(-50,50)
        x[i]=xP
        y[i]=yP
    return x,y
def difference(x,y,x_bar,y_bar):
    '''
    This fucntion calculate the from x_bar,y_bar to all vertice and return true if all difference are smaller than 0.001
    
    '''
    state=True

    for i in range(len(x)):

        d=(x[i]-x_bar)**2+(y[i]-y_bar)**2

        if d<=(0.001)**2:
            state=True
        else:
            state=False
            break
    return state
def computation(number):    
    
    '''
    This function compute the steps which takes that for all distance from vertices of a polygon to its centroid are smaller than 0.001

    This function will also plot a new polygon 

    '''
    
    # x and y are arrays to hold x coordinates and y coordinates of a vertex
    
    x,y=generate_polygon(number)
     

    x_average=average(x)  # calculate x bar
    y_average=average(y)  # calculate y bar

    
    
    diff=difference(x,y,x_average,y_average)
    # if diff is true, means distance of (x_bar,y_bar) and all vertices of a polygon are smaller than 0.001
    k=0
    while not diff:
        k+=1
        stddraw.clear()
        stddraw.polygon(x,y)
        stddraw.show(20)
        x=average_coordinates(x) # calculate the new x coordinates
        y=average_coordinates(y) # calculate the new y coordinates   
        x_average=average(x)     # x_average is the x bar of this new polygon
        y_average=average(y)     # y_average is the y bar of this new polygon
        diff=difference(x,y,x_average,y_average)

    
    return k
def average_step(number):
    '''
    This function calculate the average_steps take to achieve that distance from (x_bar,y_bar) to all vertices are <=0.001

    '''
    stddraw.setXscale(-70,70)
    stddraw.setYscale(-70,70)
    stddraw.setPenRadius(0.001)
    k=[]
    for i in range(100):
        k.append(computation(number))

    stddraw.clear()
    step=average(k)
    return step

def remove_centroid(x,y):
    '''
    This function move the polygon to the middle of coorinates system

    '''
    x_bar=average(x)
    y_bar=average(y)

    x_new=[]
    y_new=[]

    for i in range(len(x)):
        x_new.append(x[i]-x_bar)
        y_new.append(y[i]-y_bar)
    
    return x_new,y_new

def magnitude(x):
    '''
    calculate the magnitude of a vector
    '''
    square_sum=0

    for i in range(len(x)):
        square_sum+=(x[i])**2

    return square_sum**(0.5)
        
def normalize(x,y):
    '''
    normalize the x and y vector
    '''
    x1=x
    y1=y
    
    mx=magnitude(x)
    my=magnitude(y)
    
    for i in range(len(x)):
        x1[i]=x1[i]/mx
        y1[i]=y1[i]/my

    return x1,y1
    
def crossing_edge(x,y):
    '''
    This function determine if there are crossing edge in a polygon

    '''
    size=len(x)
    
    for i in range(size-1):
        x1=x[i]
        y1=y[i]
        x2=x[i+1]
        y2=y[i+1]
        for j in range(1,size-1):
            ax=x[j]
            ay=y[j]
            bx=x[j+1]
            by=y[j+1]
            opposite=((y1-y2)*(ax-x1)+(x2-x1)*(ay-y1)) * ( (y1-y2)*(bx-x1)+(x2-x1)*(by-y1) ) 
            if opposite<0:
                return False

    return True
    
    
def uncross_step(number):      
    ''' 
    This function will calcuate and return the values k that after k steps, the polygon does not have corssing edges

    This function has a cross_edge() function inside, which will determine whether or not the current polygon has crossing edge

    '''
    stddraw.clear()

    stddraw.setXscale(-1,1)
    stddraw.setYscale(-1,1)
    stddraw.setPenRadius(0.001)
    stddraw.setPenColor(stddraw.BLACK)

    
    x,y=generate_polygon(number)
    stddraw.polygon(x,y)
    stddraw.show(20)

    # move the polygon to the middle 
    x,y=remove_centroid(x,y)
    stddraw.clear()
    # draw the new polygon
    stddraw.polygon(x,y)
    stddraw.show(20)

    # cross_edge() will determine whether or not this polygon has crossing edge
    cross=crossing_edge(x,y)

    k=0
    while cross==False: 
        stddraw.clear()
        stddraw.polygon(x,y)
        stddraw.show(20)
        x=average_coordinates(x) # calculate the new x coordinates
        y=average_coordinates(y) # calculate the new y coordinates
        x,y=normalize(x,y)
        k+=1
        cross=crossing_edge(x,y)
 
    stddraw.clear()
    stddraw.polygon(x,y)
    
    return k
    
    
        
    
        
def main():
    print('Please input the number of vertices of the polygon')
    number=int(input())

    
    #averageK=average_step(number) # averageK will hold value that isaverage step of computation of new polygon  untill δ<=0.001
    #print(averageK)

                        
    k=uncross_step(number)  # k hold the values that after k step, the polygon does not have crossing edge.
    print(k)

    
    
if __name__=='__main__':
    main()
