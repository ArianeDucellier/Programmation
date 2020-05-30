#Buy It Again

#Given a CSV file in the following format:

#CustomerID, ProductID, Date of Purchase, Quantity
#1, 295872, 2020-01-02, 2
#1, 295872, 2020-02-03, 1
#1, 235984, 2019-01-06, 3
#2, 325982, 2018-05-05, 1
#...

# ... i.e. the CSV file contains multiple 
# `(customer ID, product ID, purchase date, quantity)`
# tuples, with each line representing a  purchase
# event by the given customer of the given product.

# Read file above, for each customer ID,
# recommend the top k ProductIDs that the customer
# is likely to purchase again, ideally in descending 
# order of likelihood of purchase.

# We'll assume the file fits in memory for this exercise.
# {1: [253852,235259,23582389], 2: [3528923,93258,23598], ...}
# ^ this means k = 3.

# ./example.py 3 /tmp/purchases.txt

import sys
import numpy as np
import pandas as pd

def recommend(k, filename):
    """
    Find the top k products that each customer has purchased
    Input:
        type k: integer
        k: number of top products
        type filename: string
        filename: name of the purchases file
    Output:
        type result: dictionary
        result: {customer ID: list of top products ID}
    """
    data = pd.read_csv(filename)
    data['CustomerID'] = data.CustomerID.astype('category')
    customers = data['CustomerID'].cat.categories.to_list()
    result = {}
    # Loop on customer IDs
    for customer in customers:
        subdata = data.loc[data['CustomerID'] == customer]
        purchases = subdata.groupby('ProductID')
        quantity = purchases['Quantity'].agg(np.sum)
        most_purchased = quantity.sort_values(ascending=False)
        top = most_purchased.index.tolist()
        result[customer] = top[0 : k]
    return result

if __name__ == "__main__":
    k = int(sys.argv[1])
    fn = sys.argv[2]
    print(recommend(k, fn))
