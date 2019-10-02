from math import dist
from functools import partial
from heapq import nsmallest
from statistics import mode
 
def predict(unlabeled_point, known_points, labels,  k=5):
    ''' Predict the label for an *unlabeled_point* using the
        the supervised machine learning algorithm called
        "k nearest neighbors" where the core model assumes
        only that "people who are like you are like you".
 
        Starting with the *known_points* that have known *labels*,
        located the *k* nearest points closest to the unlabeled point,
        and then vote on the most popular label among those neighbors.
    '''
    knn = set(nsmallest(k, known_points, key=partial(dist, unlabeled_point)))
    lnn = [label for label, location in zip(labels, known_points) if location in knn]
    return mode(lnn)
 
if __name__ == '__main__':
    gas_station_locations = [(103, 82), (101, 85), (92, 91), (96, 108), (114, 105), (98, 104)]
    expense_labels        = ['exp',       'exp',    'cheap',    'med',   'cheap',    'med']
    print(predict((97, 101), gas_station_locations, expense_labels, k=3))
