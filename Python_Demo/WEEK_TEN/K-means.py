#K-means 聚类算法
import numpy as np
import matplotlib.pyplot as plt

def main():
    ##step 1: load dataSet
    print("Step 1: loading data...")
    dataSet = []
    dataSetFile = open('testSet.txt')
    for line in dataSetFile:
        lineArr = line.strip().split('\t')
        dataSet.append([float(lineArr[0]), float(lineArr[1])])
    dataSetFile.close()

    #step 2: clustering...
    print("step 2: clustering...")
    dataSet = np.mat(dataSet)

    k = 3
    centers_result, clusterAssignment_result = kmeans(dataSet, k, 100)

    ##step 3: show the result
    print("step 3: showing the result...")
    showCluster(dataSet, k, centers_result, clusterAssignment_result)

def initCenters(dataSet, k):
    numSamples, dim = dataSet.shape
    centers = np.zeros((k, dim))
    for i in range(k):
        index = int(np.random.uniform(0, numSamples)) #random get k centers
        centers[i, :] = dataSet[index, :]
    print(centers)
    return centers

def dist2Centers(sample, centers):
    k = centers.shape[0]
    dis2cents = np.zeros(k)
    for i in range(k):
        dis2cents[i] = np.sqrt(np.sum(np.power(sample - centers[i, :], 2)))
    return dis2cents

def kmeans(dataSet, k, iterNum):
    numSamples = dataSet.shape[0]
    iterCount = 0

    # clusterAssignment stores which cluster this sample belongs to.
    clusterAssignment = np.zeros(numSamples)
    clusterChanged = True

    ## step 1: initialize centers
    centers = initCenters(dataSet, k)
    while clusterChanged and iterCount < iterNum:
        clusterChanged = False
        iterCount = iterCount + 1
        ## for each sample
        for i in range(numSamples):
            dis2cent = dist2Centers(dataSet[i, :], centers)
            minIndex = np.argmin(dis2cent)
            ## step 3: update its belonged cluster
            if clusterAssignment[i] != minIndex:
                clusterChanged = True
                clusterAssignment[i] = minIndex

        ## step 4: update centers
        for j in range(k):
            pointsInCluster = dataSet[np.nonzero(clusterAssignment[:] == j)[0]]
            centers[j, :] = np.mean(pointsInCluster, axis = 0)
    print('Congratulations, Cluster Achieved!')
    return centers, clusterAssignment
            

def showCluster(dataSet, k, centers, clusterAssignment):
    numSamples, dim = dataSet.shape

    mark = ['or', 'ob', 'og', 'om']

    # draw all samples
    for i in range(numSamples):
        markIndex = int(clusterAssignment[i])
        plt.plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex])

    mark = ['Dr', 'Db', 'Dg', 'Dm']
    # draw the centroids
    for i in range(k):
        plt.plot(centers[i, 0], centers[i, 1], mark[i], markersize = 17)

    plt.show()

main()
    
