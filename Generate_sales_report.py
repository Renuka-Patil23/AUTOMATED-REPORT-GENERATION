import pandas as pd
from fpdf import FPDF
import matplotlib.pyplot as plt

# Step 1: Load the data
data = pd.read_csv("sales_data.csv")

# Step 2: Calculate total revenue per item
data['Revenue'] = data['Quantity'] * data['Price']
total_revenue = data['Revenue'].sum()
top_product = data.groupby('Product')['Revenue'].sum().idxmax()
top_product_sales = data.groupby('Product')['Revenue'].sum().max()
category_wise = data.groupby('Category')['Revenue'].sum()

# Step 3: Generate a bar chart
plt.figure(figsize=(6,4))
category_wise.plot(kind='bar', color='skyblue')
plt.title("Revenue by Category")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("category_chart.png")
plt.close()

# Step 4: Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(200, 10, "Sales Report", ln=True, align="C")

pdf.set_font("Arial", size=12)
pdf.ln(10)
pdf.cell(200, 10, f"Total Revenue: Rs{total_revenue}", ln=True)
pdf.cell(200, 10, f"Top-Selling Product: {top_product} (Rs{top_product_sales})", ln=True)

pdf.ln(10)
pdf.cell(200, 10, "Category-wise Revenue:", ln=True)

for category, revenue in category_wise.items():
    pdf.cell(200, 10, f" - {category}: Rs{revenue}", ln=True)

# Step 5: Add chart to PDF
pdf.image("category_chart.png", x=10, y=None, w=180)

# Step 6: Save PDF
pdf.output("sales_report.pdf")

print(" Report generated successfully as 'sales_report.pdf'")
