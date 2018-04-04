def movingAverage(myarray, window):
    #Length of the array
    sizeOfArray = len(myarray)
    print ("Length of the array is ",  str(sizeOfArray))
    #Calculating the number of sequences for the moving average
    numberOfSequences = sizeOfArray - int(window) + 1
    print ("For the given array of length, " + str(sizeOfArray) + " and a window of " + str(window) + ", there would be " + str(numberOfSequences) + " number of sequences")
    sum = 0
    Averages=[]
    m = 0
    n = window
    for i in range(len(myarray)):    
        
        for j in range(m,n):
            if(n <= len(myarray)):
                sum += myarray[j]
                if (j == n-1):
                    Average = (sum/window)
                    Averages.append(Average)
                    m+=1
                    n+=1
                    sum=0
                
    print(Averages)
arr = [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]
#print (len(arr))
movingAverage(arr,3)