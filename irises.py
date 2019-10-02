'Goal:  Perform supervised machined learning for the famous Iris classification problem'
 
# CREATE TABLE Irises (species text, sep_len real, sep_wid real, pet_len real, pet_wid);
from k_nearest_neighbors import predict
from pprint import pp
import sqlite3
 
def load_flower_data(db_name='data/irises.db', table_name='Irises'):
    ''' Load flower species data from a database.
 
        The *table_name* should have schema with flower species as
        the first field and various measurements are the remaining fields.
    '''
    points = []
    labels = []
    conn = sqlite3.connect(db_name)
    for species, *measurements in conn.execute(f'SELECT * FROM {table_name}'):
        points.append(tuple(measurements))
        labels.append(species)
    conn.close()
    return points, labels
 
if __name__ == '__main__':
    iris_measurements, iris_labels = load_flower_data()
    unknown_flower = (5.0, 4.0, 5.0, 3.5)
    print(predict(unknown_flower, iris_measurements, iris_labels))
