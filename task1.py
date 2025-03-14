import dask.dataframe as dd

# Load large CSV file (Lazy loading, efficient for big data)
df = dd.read_csv(r"C:\Users\vaish\Documents\large_file.csv")

# Example processing: Filter rows where 'column1' > 100
filtered_df = df[df["column1"] > 100]

# Perform an aggregation: Group by 'category' and get the mean of 'value'
agg_df = filtered_df.groupby("category")["value"].mean()

# Compute and save the processed data
agg_df.compute().to_csv(r"C:\Users\vaish\Documents\processed_output.csv", index=True)

print(r"Processing completed! Output saved in 'C:\Users\vaish\Documents\processed_output.csv'.")
