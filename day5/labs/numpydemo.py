import numpy as np

# Define a structured array with different field types
dtype = [('name', 'S10'), ('age', 'i4'), ('height', 'f4')]
values = [('Alice', 30, 5.5), ('Bob', 25, 6.0)]

structured_array = np.array(values, dtype=dtype)
print(structured_array)
# Output:
