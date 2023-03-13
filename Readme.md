# Helium CSV Processing Script

This script processes CSV files in a specified folder to check if certain conditions are met. 
It is designed to be run from the command line, with the folder name as an argument.

### Requirements
- Python 3.x
- csv module
- os module
- sys module

### Usage
```python helium.py data/[folder name]```

### Functionality
- Reads and processes CSV files in the specified folder.
- Filters rows based on review count and revenue values.
- Calculates total revenue for each brand and checks if it exceeds a % of the total revenue.
- Calculates revenue for the top 3 products and checks if it exceeds a % of the total revenue.
- Outputs SUCCESS or FAILURE for each file processed.

### Variables
BRAND_PERCENTAGE - represents the maximum percentage of total revenue that can come from a single brand.
TOP_THREE_PERCENTAGE - represents the maximum percentage of total revenue that can come from the top 3 products.
