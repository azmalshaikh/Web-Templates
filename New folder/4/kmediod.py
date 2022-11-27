import numpy as np
import pandas as pd 

blobs = pd.read_csv('mediod.csv')
colnames = list(blobs.columns[1:-1])

def initiate_centroids(k, dset):
    centroids = dset.sample(k)     
    return centroids

np.random.seed(42)
inputK=int(input('Enter k:'))
df = blobs[['x','y']]    
centroids = initiate_centroids(inputK, df)

def euclidean(a,b):
    return np.sqrt(np.sum(np.square(a-b)))

def centroid_assignation(dset, centroids):

    k = centroids.shape[0]      
    n = dset.shape[0]           
    assignation = []
    assign_errors = []

    for obs in range(n):    
        all_errors = np.array([])
        for centroid in range(k):
            err = euclidean(centroids.iloc[centroid, :], dset.iloc[obs,:])
            all_errors = np.append(all_errors, err)

        nearest_centroid =  np.where(all_errors==np.amin(all_errors))[0].tolist()[0]
        nearest_centroid_error = np.amin(all_errors)

        assignation.append(nearest_centroid)      
        assign_errors.append(nearest_centroid_error)

    return assignation, assign_errors
df['centroid'], df['distance'] = centroid_assignation(df, centroids)

def totalCost(errors):
    cost=0
    for i in errors:
        cost+=i
    return cost

tc=totalCost(df['distance'])
print(tc)
print(centroids)
print(df)
print()

def kMedoids(dset, centroids, k=2, iter=100):
    global tc
    n=dset.shape[0]
    # m=dset.shape[1]
    count=0
    while True:
        swap=False
        for i in range(n):
                for j in range(k):
                    temp_centroids=centroids.copy()
                    temp_centroids.iloc[[j],[0]]=dset.iloc[[i],[0]]
                    temp_centroids.iloc[[j],[1]]=dset.iloc[[i],[1]]
                    c,e=centroid_assignation(df, temp_centroids)
                    error=totalCost(e)
                    if error<tc:
                        centroids=temp_centroids
                        tc=error
                        print(tc)
                        swap=True
                        df['centroid'], df['distance']=c,e
                        print(centroids)
                        print(df)
                        print()
        count+=1
        if(count>iter or not swap):
            break
    return centroids
            
centroids=kMedoids(df[['x','y']], centroids, inputK)