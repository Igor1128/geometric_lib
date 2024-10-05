
# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

# General description of the solution
This project provides a simple geometric calculator for calculating perimeters and areas of basic shapes: circles, squares, triangles.

## Overview

The Geometric Calculator is a Python program designed to help users quickly and easily calculate the perimeter and area of circles, squares, triangles. It utilizes separate modules for each shape (`circle` and `square` and `triangle`) to encapsulate shape-specific logic.

The calculator's functionality is built on the following principles:

* **Modularity:**  The code is divided into distinct modules for each shape, making it easier to maintain and extend.
* **User-Friendly Interface:** The program prompts the user for input and provides clear output, making it intuitive to use.
* **Simplicity:**  The focus is on providing basic geometric calculations in a straightforward manner.

# Description of each function with call examples
## `circle` Module

This module provides functions for calculating the perimeter and area of a circle.

### Functions

#### `perimeter(radius)`

Calculates the perimeter of a circle.

**Arguments:**

- `radius` (float): The radius of the circle.

**Returns:**

- `float`: The perimeter of the circle.

**Example:**

```python
import circle

radius = 5
perimeter = circle.perimeter(radius)
print(f"Perimeter of a circle with radius {radius} is {perimeter}")  Output: Perimeter of a circle with radius 5 is 31.41592653589793
```

#### `area(radius)`

Calculates the area of a circle.

**Arguments:**

- `radius` (float): The radius of the circle.

**Returns:**

- `float`: The area of the circle.

**Example:**
```python
import circle

radius = 5
area = circle.area(radius)
print(f"Area of a circle with radius {radius} is {area}")  # Output: Area of a circle with radius 5 is 78.53981633974483
```

## `square` Module

This module provides functions for calculating the perimeter and area of a square.

### Functions

#### `perimeter(side)`

Calculates the perimeter of a square.

**Arguments:**

- `side` (float): The side length of the square.

**Returns:**

- `float`: The perimeter of the square.

**Example:**

```python
import square

side = 5
perimeter = square.perimeter(side)
print(f"Perimeter of a square with side {side} is {perimeter}")  # Output: Perimeter of a square with side 5 is 20
```

#### `area(side)`
Calculates the area of a square.

**Arguments:**

- `side` (float): The side length of the square.

**Returns:**

- `float`: The area of the square.

**Example:**
```python
import square

side = 5
area = square.area(side)
print(f"Area of a square with side {side} is {area}")  # Output: Area of a square with side 5 is 25
```

## `triangle` Module

This module provides functions for calculating the perimeter and area of a triangle.

### Functions

#### `perimeter(sides)`

Calculates the perimeter of a triangle.

**Arguments:**

- `sides` (float): The sides length of the triangle.

**Returns:**

- `float`: The perimeter of the triangle.

**Example:**

```python
import triangle

sides = 5,4,3
perimeter = triangle.perimeter(sides)
print(f"Perimeter of a triangle with sides {sides} is {perimeter}")  # Output: Perimeter of a triangle with side 5,4,3 is 12
```

#### `area(sides)`
Calculates the area of a triangle.

**Arguments:**

- `sides` (float): The sides length of the triangle.

**Returns:**

- `float`: The area of the triangle.

**Example:**
```python
import triangle

sides = 3,4,5
area = triangle.area(sides)
print(f"Area of a triqngle with sides {sides} is {area}")  # Output: Area of a triangle with sides 3,4,5 is 6
```
## Usage

To use the calculator:

1. **Import the modules:**
   ```python
   import circle
   import square
   import triangle
   ```
2. **Choose a figure and function:**
```python
    fig = 'circle'  # Or 'square', 'triangle'
    func = 'perimeter'  # Or 'area'
```

3. **Input sizes:**

For a circle, provide the radius.
For a square, provide the side length.
For a triangle, provide the sides length.

4. **Calculate and print the result:**
```python
result = calculate(fig, func, [size])
print(f'{func} of {fig} is {result}')
```
# Project modification history with commit hashes (except the last entry)

<f507ab9b6fac8e88740eb72bcf63e6c7fdbb8690> Comments have been added
<3c181ebba413eaa8952eece557e49d379738c9f0> Comments have been added
<4fa8d5a0466a5347e65a23b01ed1866bda26ae26> The formula for calculating the area of a triangle has been fixed, comments have been added
<b5b0fae727ca72c317c383b39c0af73d6adcd81c> (origin/develop, develop) L-04: Update docs for calculate.py
<d76db2ac7f69cc920ae2e6f669fb0671a7fa7d71> L-04: Add calculate.py
<51c40ebfd0e0b65f52fe5e54740cbb038e492db3> L-04: Doc updated for triangle
<d080c7888b81955bad2ed78d58ad910526b5132a> L-04: Triangle added
<d078c8d9ee6155f3cb0e577d28d337b791de28e2> (origin/main, origin/HEAD, main) L-03: Docs added
<8ba9aeb3cea847b63a91ac378a2a6db758682460> L-03: Circle and square added