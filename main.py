#!/usr/bin/env python3

"""
    Source:
    https://stanford.edu/~cpiech/cs221/handouts/kmeans.html

    Clusters: groups of data which are similar to one another

    Algorithm:

    1.
"""

from sklearn.datasets import load_breast_cancer as lbc
import numpy as np

def init_centroids(arr, k):
    _arr = arr.copy()
    np.random.shuffle(_arr)
    return centroids[k]

def adjust_centroids(centroids):
    pass

def kmeans(arr, k, max_iter=3000):
    featuresNum = arr.shape[0]
    centroids = init_centroids(arr, k)
    old_centroids = null

    i = 0
    while i < max_iter and old_centroids != centroids:
        i = i + 1
        old_centroids = centroids

        centroids = adjust_centroids(centroids)

    return arr

def main():
    data = lbc()
    X = data.data

    print(X)

if __name__ == '__main__':
    main()
