# Recommend Products

Algorithm used to identify recommended products for customers using past order history and product affinity

Getting Started yourself:

1. Create two CSV files. 1 is named orders_export.csv, the other is result.csv
2. name the rows userId,ItemId for orders_export.csv and the result.csv item1,item2,score
3. pip install panda
4. python scripts.py
5. python getResults.py (edit code to check for the product you want to know the affinity for)