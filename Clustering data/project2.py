#CSCI-2202-project2
#HUI-YANG-B00758346

import stddraw

def mean(g,index):
    '''
    Args:
    g: a list of tuple
    index; specify which one we need to compute the mean. x or y.

    This function calculate the mean of a single element of a tuple in list g

    '''
    summ=0
    for i in range(len(g)):
     summ=summ+g[i][index]

    m=summ/len(g)
    return m


def standard_de(g,index,m):
    '''
    g is a list;
    index specify which coordinates we need to compute its standard deviation.
    
    '''
    summ=0
    for i in range(len(g)):
       summ+=(g[i][index]-m)**2

    variance=summ/len(g)

    return variance**(1/2)
    
def distance(x,y):
    '''
    calculate the distance from point x and y
    '''
    d=(x[0]-y[0])**2+(x[1]-y[1])**2
    d=d**(1/2)
    return d

def centroid(g):
    '''
    calculate the centroid of a group of points

    '''
    l=len(g)
    x=g[0][0]
    y=g[0][1]
    for i in range(1,l):
        x=x+g[i][0]
        y=y+g[i][1]

    centroid=(x/l,y/l)
    return centroid

def set_scale_read_data():
    '''
    this function set the stddraw scale and read data 
    
    '''
    data=[] # data is a list contains tuple of data point
    stddraw.setPenRadius(0.005)
    stddraw.setXscale(-2,2)
    stddraw.setYscale(-2,2)
    with open('data3.txt') as f:
        for line in f:
            l=line.replace(',',' ')
            data_point=l.split()
            data.append((float(data_point[0]),float(data_point[1])))
    return data

def regroup_data(d1,d2,d3,g1,g2,g3,data_point):
    '''
    This function regroup the data_point into group d1,d2 and d3


    '''
    d1=d1
    d2=d2
    d3=d3
    if d1<d2 and d1<d3:
        g1.append(data_point)
    
        stddraw.setPenColor(stddraw.RED)
        stddraw.point(data_point[0],data_point[1])
        
        stddraw.show(20)
            
    elif d2<d1 and d2<d3:
        g2.append(data_point)
 
        stddraw.setPenColor(stddraw.BLUE)
        stddraw.point(data_point[0],data_point[1])
        
        stddraw.show(20)
    else:
        g3.append(data_point)
       
        stddraw.setPenColor(stddraw.GREEN)
        stddraw.point(data_point[0],data_point[1])
        
        stddraw.show(20)
    return g1,g2,g3
def plot_centroid(stable,g1,g2,g3,centroid1,centroid2,centroid3):

    '''
    This function plot the centroid if centroid is changing

    Or do nothing will centroid is stailized.

    '''
    if stable==0:

        centroid1_new=centroid(g1)
        
        centroid2_new=centroid(g2)

        centroid3_new=centroid(g3)

        error=1e-3

        if distance(centroid1_new,centroid1)<error and distance(centroid2_new,centroid2)<error and distance(centroid3_new,centroid3)<error:
                                                          
            return 1,centroid1,centroid2,centroid3                                            
                                                        
        else:

            stddraw.setPenRadius(0.010)
            stddraw.setPenColor(stddraw.WHITE)
            stddraw.point(centroid1[0],centroid1[1])
            centroid1=centroid1_new
            stddraw.setPenColor(stddraw.RED)
            stddraw.point(centroid1[0],centroid1[1])
            stddraw.show(10)

            stddraw.setPenColor(stddraw.WHITE)
            stddraw.point(centroid2[0],centroid2[1])
            centroid2=centroid2_new
            stddraw.setPenColor(stddraw.BLUE)
            stddraw.point(centroid2[0],centroid2[1])
            stddraw.show(10)

            stddraw.setPenColor(stddraw.WHITE)
            stddraw.point(centroid3[0],centroid3[1])
            centroid3=centroid3_new
            stddraw.setPenColor(stddraw.GREEN)
            stddraw.point(centroid3[0],centroid3[1])
            stddraw.show(10)
            return 0,centroid1,centroid2,centroid3
    if stable==1:
        return 1,centroid1,centroid2,centroid3

def rss(g,centroid):
    '''
    calculate the rss of a group of data

    '''
    rss=0
    for i in range(len(g)):
        rss+=(distance(g[i],centroid))**2 
    return rss

def mean_sd(g1,g2,g3,centroid1,centroid2,centroid3):
    '''
    calculate the mean and standard deviation of x,y coordinates of group1,group2,group3

    '''
    g1_x_mean=mean(g1,0)
    g1_y_mean=mean(g1,1)

    g2_x_mean=mean(g2,0)
    g2_y_mean=mean(g2,1)

    g3_x_mean=mean(g3,0)
    g3_y_mean=mean(g3,1)

    g1_x_sd=standard_de(g1,0,g1_x_mean)
    g1_y_sd=standard_de(g1,1,g1_y_mean)

    g2_x_sd=standard_de(g2,0,g2_x_mean)
    g2_y_sd=standard_de(g2,1,g2_y_mean)


    g3_x_sd=standard_de(g3,0,g3_x_mean)
    g3_y_sd=standard_de(g3,1,g3_y_mean)

    print('Red group x mean:'+str(g1_x_mean))
    print('Red group y mean:'+str(g1_y_mean))
    print('Blue group x mean:'+str(g2_x_mean))
    print('Blue group y mean:'+str(g2_y_mean))
    print('Green group x mean:'+str(g3_x_mean))
    print('Green group y mean:'+str(g3_x_mean))
    print()
    print()
    print('Red group x standard deviation:'+str(g1_x_sd))
    print('Red group y standard deviation:'+str(g1_y_sd))
    print('Blue group x standard deviation:'+str(g2_x_sd))
    print('Blue group y standard deviation:'+str(g2_y_sd))
    print('Green group x standard deviation:'+str(g3_x_sd))
    print('Green group y standard deviation:'+str(g3_y_sd))
    

def plot_histograms(g):
    '''
    plot the histograms of g


    '''
    x=[]
    y=[]
    stddraw.setPenColor(stddraw.GREEN)
    for i in range(len(g)):
        x.append(g[i][0])
    for i in range(len(g)):
        y.append(g[i][1])
        
    x_count=[0]*6
    for i in range(len(x)):
        if x[i]>-1.5 and x[i]<-1:
            x_count[0]+=1
        elif x[i]>-1 and x[0]<-0.5:
            x_count[1]+=1

        elif x[i]>-0.5 and x[i]<0:
            x_count[2]+=1

        elif x[i]>0 and x[i]<0.5:
            x_count[3]+=1
        elif x[i]>0.5 and x[i]<1:
            x_count[4]+=1

        else:
            x_count[5]+=1
    k=0.5
    for i in range(6):
        stddraw.filledRectangle(k,0,0.5,x_count[i]/100)        
        k+=1
    stddraw.show(2000)

    

    y_count=[0]*6
    
    for i in range(len(y)):
        if y[i]>-1.5 and y[i]<-1:
            y_count[0]+=1
        elif y[i]>-1 and y[0]<-0.5:
            y_count[1]+=1

        elif y[i]>-0.5 and y[i]<0:
            y_count[2]+=1

        elif y[i]>0 and y[i]<0.5:
            y_count[3]+=1

        elif y[i]>0.5 and y[i]<1:
            y_count[4]+=1

        else:
            y_count[5]+=1
    k=0.5
    for i in range(6):
        stddraw.filledRectangle(k,0,0.5,y_count[i]/100)        
        k+=1
    stddraw.show(2000)


def main():

    #set_scale_read_data() will
    #set the drawing scale
    #read data from file
    #return a list contains all the data

    data=set_scale_read_data()

    # g1,g2,g3 represent the three group
    g1=[]
    g2=[]
    g3=[]

    # assign one of the data point to g1,g2,g3
    g1.append(data[10])
    g2.append(data[15])
    g3.append(data[20])

    
    # Frist, calculate and plot initial three point
    # centroid1, centroid2, centroid 3 represent the centroid of the three group
    centroid1=centroid(g1)

    stddraw.setPenColor(stddraw.RED)
    stddraw.point(centroid1[0],centroid1[1])
    stddraw.show(10)

    centroid2=centroid(g2)

    stddraw.setPenColor(stddraw.BLUE)
    stddraw.point(centroid2[0],centroid2[1])
    stddraw.show(10)

    centroid3=centroid(g3)

    stddraw.setPenColor(stddraw.GREEN)
    stddraw.point(centroid3[0],centroid3[1])
    stddraw.show(10)

    

    stable=0  # stable is 0 means that the centroid is changing.   stable is 1 means that the centroid is not changing


    # loop through the data[]
    # regroup each data point into g1,g2 or g3
    for i in range(len(data)):
        data_point=data[i]
        d1=distance(data_point,centroid1)
        d2=distance(data_point,centroid2)
        d3=distance(data_point,centroid3)
        
        stddraw.setPenRadius(0.005)
        g1,g2,g3=regroup_data(d1,d2,d3,g1,g2,g3,data_point)

        #plot the new centroid if stable=0
        #Or if stable=1,do nothing
        #For more detail,see function description of plot_centroid
        stable,centroid1,centroid2,centroid3=plot_centroid(stable,g1,g2,g3,centroid1,centroid2,centroid3)

    # calculate the rss1,rss2,rss3
    # sum them together
    rss1=rss(g1,centroid1)
    rss2=rss(g2,centroid2)
    rss3=rss(g3,centroid3)
    Rss=rss1+rss2+rss3
    stddraw.clear()
    print('RSSk is:'+str(Rss))

    # calculate the mean and standard devation or g1,g2,g3
    mean_sd(g1,g2,g3,centroid1,centroid2,centroid3)


    #set new drawing scale for drawing histogram  
    stddraw.setXscale(-1,6.5)
    stddraw.setYscale(-1,3)
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.line(0,0,6.5,0)
    stddraw.line(0,0,0,3)


    #plot the histogram of g1,g2,g3
    #the histrogram has 6 category
    # (-1.5,-1),(-1,-0.5),(-0.5,0),(0,0.5),(0.5,1),(1,1.5)
    plot_histograms(g1)
    plot_histograms(g2)
    plot_histograms(g3)
    stddraw.show()

    

if __name__=='__main__':
    main()

        

