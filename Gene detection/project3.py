#CSCI-2202-project3

#HUI_YANG_B00758346

def preprocess():
    '''
    This function preprocess the  data file

    It will do:
    
    1.read NC_003997.fnd
    2.write NC_003997.clean.fna

    3.read NC_003997.clean.fna
    4.write NC_003997.clean.GLIMMER3

    '''
    with open('NC_003997.fna') as f:
        s=f.readline()
        k=s[-1]
        DNA_sequence_with_blackflash=f.read()

        result=DNA_sequence_with_blackflash.replace(k,'')


    f1=open('NC_003997.clean.fna','w')


    f1.write(result)
    f1.close()

    with open('NC_003997.GLIMMER3') as f:
        next(f)
        result1=''
        for line in f:
            if line[28]=='+':
                result1=result1+line
    f2=open('NC_003997.clean.GLIMMER3','w')
    f2.write(result1)
    f2.close()


def extract_glimmaer3():
    '''
    This function will extract start and end index of gene from NC_003997.clean.GLIMMER3
    '''
    START=[]
    STOP=[]

    with open ('NC_003997.clean.GLIMMER3') as f:
        for line in f:
            output=line.split()
            START.append(output[1])
            STOP.append(output[2])


    return START,STOP        


def gene_detection(START,STOP):

    '''
    This function will detect gene in DNA sequence

    1.This function first read  NC_003997.clean.fna
    2.Then it will use a for loop to find the start codons in the DNA sequence.
    3 If it find the start codons, it starts to loop rest of the DNA sequence to find the stop codons
    START: hold the start codons .
    STOP:  hold stop codons.

    '''
    with open ('NC_003997.clean.fna') as f:
        nucleotides=f.read()                #nucleotides represents the who sequence of genes.
        size=len(nucleotides)

    start1=''
    start2=''
    start3=''
    

    start_codon=START                     #start_codon will hold START, which is a list holding start codons. ['ATG'] OR ['ATG','TTG']
    stop_codon=STOP                       #stop_codon will hold STOP, which is a list holding 3 stop codons ['TAA','TAG','TGA']


    # This two lists hold  index of start and stop condons in genome.


    testSTART=[]
    testSTOP=[]

    i=0
    while i in range(size-2):

        # Each time, we check three nucleotides.

        # And we name it as start1,start2,start3. for example, start1='A',start2='T',start3='G'

        start1=nucleotides[i]
        start2=nucleotides[i+1]
        start3=nucleotides[i+2]
    
        # concatenate start1+start2+start3 as test_start_codon
        test_start_codon=start1+start2+start3
        #print('test_start_codon: '+test_start_codon)

        # we check if test_start_codon is in start_codon

        if test_start_codon in start_codon:
            #print(i)
           
            # if it is , we set start_index=i
            start_index=i

            # For stop codon, each time, we check three nucleotides, which are end1, end2, end3.

            end1=i+3
            end2=i+4
            end3=i+5
            
            #concatenate end1+end2+end3 as test_stop_codon

            test_stop_codon=nucleotides[end1]+nucleotides[end2]+nucleotides[end3]
           
            
            # loop the rest of genome  to find the stop_codon
            find=True

            while test_stop_codon not in stop_codon: 
                end1+=3
                end2+=3
                end3+=3
                if end3>size-1:
                    find=False
                    i+=1    
                    break
                else:
                    test_stop_codon=nucleotides[end1]+nucleotides[end2]+nucleotides[end3]
            
            
            if find==True:
                stop_index=end3
                length=stop_index-start_index+1

            # if the length of this DNA sequence is more than 300. we say it is a gene and record the start_index and stop_index.    
                if length>=300:    

                    testSTART.append(str(start_index+1))

                    testSTOP.append(str(stop_index+1))

                    i=stop_index+1
                else:
                    i+=1
    
        else:
            i+=1
    return  testSTART,testSTOP


def pairwise_gene(sta,sto):
    '''
    This function will pair two list: sta and sto
    '''
    length1=len(sta)
    length2=len(sto)

    if length1!=length2:
        return 'gene detection wrong, number of start codons does not equal to number of stop codons'

    pairwise_gene=[]
    for i in range(length1):
        
        tup=(sta[i],sto[i])
        pairwise_gene.append(tup)

    return pairwise_gene



def sensitivity(TP,FN):
    '''
    calculate the sensitivey 
    '''

    return TP/(TP+FN)

def specificity(TP,FP):
    '''
    calculate the specificity
    '''

    return TP/(TP+FP)

def F_score(recall,precision):
    '''
    calculate the F_score
    '''
    return (2*recall*precision)/(recall+precision)

def project_calculation(tst,rfl,x):
    '''
    This function calculate TP,FN,FP,Sensitivity, Specificity, and F_score

    This function will also print sensitivity, specificity, and F_score
    '''
    TP=len(tst&rfl)
    FN=len(rfl-tst)
    FP=len(tst-rfl)
    recall=sensitivity(TP,FN)
    precision=specificity(TP,FP)
    f_score=F_score(recall,precision)
    print(x)
    print('TP is:'+str(TP))
    print('FN is:'+str(FN))
    print('FP is:'+str(FP))
    print('recall is: '+str(recall))
    print('Precision is: '+str(precision))
    print('F_score is: '+str(f_score))
        

def main():

    # refSTART,refSTOP represents the start and stop index of a gene part recored in glimmaer3 documents

    preprocess()#preprocess the data. see function description for detail of this function 

    refSTART,refSTOP=extract_glimmaer3() # extract the start and end index of genes in NC_003997.clean.GLIMMER3
    
    # testSTART, testSTOP are two lists each corresponding element of these two list are start and stop index of a gene.

    testSTART1,testSTOP1=gene_detection(['ATG'],['TAA','TAG','TGA']) # detect_gene method will detect all genes we find in NC_003997.clean.fna.
    testSTART2,testSTOP2=gene_detection(['ATG','TTG'],['TAA','TAG','TGA']) # see function description for more detail


    #tL and rl will be pairwise of gene 
    tL=pairwise_gene(testSTART1,testSTOP1)
    tL2=pairwise_gene(testSTART2,testSTOP2)
    rL=pairwise_gene(refSTART,refSTOP) 
   
  
    tst1=set(tL)
    tst2=set(tL2)
    rfl=set(rL)
    #project_calculation will calculate and print out the result the project mentioned.
    project_calculation(tst1,rfl,'For start codons:ATG')
    print()
    print()
    project_calculation(tst2,rfl,'For start codons:XTG')


    

if __name__=='__main__':

    main()
    


    
            

        

            
            
            





            
