# Customer Feedback and Sales Data Analysis
# Made by Lakshit Pandey

import pandas as pd
import numpy as np
import re
from collections import Counter

sales_df = pd.read_csv("sales_data.csv")

print("===== SALES DATA PREVIEW =====")
print(sales_df.head())

# Basic Sales Insights
total_revenue = np.sum(sales_df["UnitsSold"] * sales_df["Price"])
avg_rating = np.mean(sales_df["Rating"])
top_product = sales_df.loc[sales_df["UnitsSold"].idxmax(), "ProductName"]

print("\n===== SALES ANALYSIS =====")
print(f"Total Revenue: ₹{total_revenue}")
print(f"Average Rating: {round(avg_rating, 2)}")
print(f"Top Selling Product: {top_product}")

with open("customer_feedback.txt", "r") as file:
    feedback_text = file.read().lower()

# Clean text 
feedback_text = re.sub(r'[^a-z\s]', '', feedback_text)

# Tokenize words
words = feedback_text.split()

# Define simple positive and negative word lists
positive_words = ["good", "great", "amazing", "smooth", "bright", "comfortable", "excellent", "sharp"]
negative_words = ["bad", "poor", "noisy", "slow", "average", "expensive"]

# Count occurrences
pos_count = sum(word in positive_words for word in words)
neg_count = sum(word in negative_words for word in words)

word_freq = Counter(words).most_common(10)

print("\n===== FEEDBACK ANALYSIS =====")
print(f"Total Positive Words: {pos_count}")
print(f"Total Negative Words: {neg_count}")
print("\nTop 10 Most Common Words:")
for word, count in word_freq:
    print(f"{word}: {count}")


#  Merge Text & CSV Insights

# Find if feedback mentions top product
if top_product.lower() in feedback_text:
    print(f"\nTop product '{top_product}' is mentioned in feedback!")
else:
    print(f"\nTop product '{top_product}' not mentioned in feedback.")

#  Generate Report (Text File)

report = f"""
=============================
CUSTOMER FEEDBACK & SALES REPORT
=============================

💰 TOTAL SALES REVENUE: ₹{total_revenue}
⭐ AVERAGE PRODUCT RATING: {round(avg_rating, 2)}
🏆 TOP SELLING PRODUCT: {top_product}

Total Positive Words: {pos_count}
Total Negative Words: {neg_count}

Most Common Words:
{', '.join([f'{w}({c})' for w, c in word_freq])}

-----------------------------
🔗 INSIGHTS
-----------------------------
- Feedback mentions top product: {"Yes" if top_product.lower() in feedback_text else "No"}
- Products with rating below 4: {', '.join(sales_df[sales_df["Rating"] < 4]["ProductName"].tolist())}

Made by: Lakshit Pandey
"""

with open("analysis_report.txt", "w") as f:
    f.write(report)

print("\n✅ Report saved as 'analysis_report.txt'")
#Success!!