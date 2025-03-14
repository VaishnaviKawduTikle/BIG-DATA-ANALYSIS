import pandas as pd
import numpy as np

# Generate sample data
num_rows = 1000000  # Change this for a larger dataset
data = {
    "id": range(1, num_rows + 1),
    "column1": np.random.randint(50, 200, size=num_rows),
    "value": np.random.uniform(10, 100, size=num_rows),
    "category": np.random.choice(["A", "B", "C"], size=num_rows),
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save as CSV
df.to_csv("large_file.csv", index=False)

print("CSV file generated successfully!")
