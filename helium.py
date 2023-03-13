import sys
import os
import csv

from constants import BRAND_PERCENTAGE, TOP_THREE_PERCENTAGE


def process_csv_file(csv_filename):

    # Open the CSV file with utf-8-sig encoding to remove the BOM from the header row
    with open(csv_filename, encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)

        # Create a dictionary to store the total revenue for each brand
        brand_revenue = {}

        # Create a list to store the filtered and sorted data
        products = []

        # Loop through each row in the CSV file
        for row in reader:
            # If the product details start with "($)", skip the row
            product_details = row['Product Details']
            if product_details.startswith('($)'):
                continue

            # If the review count is less than or equal to 800 and the revenue value is not "n/a", add the row to the products list and update the brand revenue
            review_count = int(row['Review Count'].replace(',', ''))
            revenue = row['Revenue'].replace(',', '')
            brand = row['Brand']
            if review_count <= 800 and revenue != 'n/a':
                row['Revenue'] = float(revenue)
                products.append(row)
                brand_revenue[brand] = brand_revenue.get(brand, 0) + float(revenue)

        # Sort the products list by revenue in descending order
        sorted_products = sorted(products, key=lambda k: k['Revenue'], reverse=True)

        # Check if the sum of the revenue for the first three products does not exceed 30% of the total revenue and if the revenue for each brand does not exceed 30% of the total revenue
        total_revenue = sum(product['Revenue'] for product in products)
        top3_revenue = sum(product['Revenue'] for product in sorted_products[:3])
        for brand, revenue in brand_revenue.items():
            if revenue > total_revenue * BRAND_PERCENTAGE:
                return f'FAILURE: {brand} revenue exceeds {BRAND_PERCENTAGE*100}% of total revenue'
        if top3_revenue > total_revenue * TOP_THREE_PERCENTAGE:
            return f'FAILURE: top 3 products revenue exceeds {TOP_THREE_PERCENTAGE*100}% of total revenue'
        else:
            return 'SUCCESS'

if __name__ == '__main__':
    # Get the folder name from the command line arguments
    if len(sys.argv) < 2:
        print('Usage: python helium.py [folder name]')
        sys.exit()
    folder_name = sys.argv[1]

    # Loop through each CSV file in the folder and check if the conditions are met
    for filename in os.listdir(folder_name):
        if filename.endswith('.csv'):
            keyword = os.path.splitext(filename)[0]
            csv_filename = os.path.join(folder_name, filename)
            result = process_csv_file(csv_filename)
            print(f"Keyword {keyword}: {result}")

