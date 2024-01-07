# zeroZ Python Package

## Description
The `zeroZ` package is a simple and flexible data structure for storing and retrieving values associated with `(x, y)` coordinates and a 'group'. It can be used as a basic form of a database.

## Installation
To install the `zeroZ` package, you can download it directly from the repository and import it into your Python script.

## Usage
Here's how to use the `zeroZ` package:

```python
import zeroZ

# Store a value with its position and group
zeroZ.list(1, 1, "value", "group")

# Retrieve a value based on its position
value, group = zeroZ.listvalue(1, 1)

# Print all stored values with their positions
zeroZ.listposall()

# Print values stored at positions within a range
zeroZ.listpos(x1, y1, x2, y2)
