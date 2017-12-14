# Prompt

These are directly taken from the Launch Academy curriculum. I put `Circle` and `Square` in their own files, but test them together in `geometry_test`.

## Circle

The Circle initialize method should take the radius as a required argument, and optional x and y coordinates, which represent the center of the circle. The x and y coordinates should default to the origin point (0, 0) if not provided.

Methods

- radius - Returns the radius of the circle
- x - Returns the x coordinate of the circle
- y - Returns the y coordinate of the circle
- diameter - Returns the calculated diameter of the circle
- area - Returns the calculated area of the circle
- perimeter - Returns the calculated perimeter, or circumference of the circle

## Square

The Square class has many of the same methods as the Circle class. The Square initialize method should take the length of one side as a required argument, and optional x and y coordinates, which represent the center point of the square. The x and y coordinates should default to the origin point (0, 0) if not provided.

Methods

- x - Returns the x coordinate of the square
- y - Returns the y coordinate of the square
- length - Returns the length of the square
- width - Returns the width of the square
- diameter - Returns the calculated diameter, or diagonal of the square
- area - Returns the calculated area of the square
- perimeter - Returns the calculated perimeter of the square
- contains_point?(x, y) - Returns true if the provided coordinates fall within or on the boundaries of the square. Returns false, otherwise.