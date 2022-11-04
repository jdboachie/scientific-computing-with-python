class Rectangle:

    def __init__(self, width : int, height : int) -> None:
        """Initializes a Rectangle object

        Args:
            width (int): The rectangle's width
            height (int): The rectangle's length
        """
    
        self.width = width
        self.height = height


    def set_width(self, new_width : int) -> None:
        """Sets the width of the Rectangle object to new_width

        Args:
            new_width (int): The new_width of the Rectangle object
        """

        self.width = new_width


    def set_height(self, new_height : int) -> None:
        """Sets the height of the Rectangle object to new_height

        Args:
            new_height (int): The new_height of the Rectangle object
        """

        self.height = new_height


    def get_area(self) -> int:
        """Returns the area of the Rectangle object

        Returns:
            int: the area of the Rectangle object
        """

        return self.width * self.height


    def get_perimeter(self) -> int:
        """Returns the perimeter of the Rectangle object

        Returns:
            int: the perimeter of the Rectangle object
        """

        return (2 * self.width + 2 * self.height)


    def get_diagonal(self) -> float:
        """Returns the length of the diagonal of the Rectangle object

        Returns:
            float: the length of the diagonal
        """

        return ((self.width ** 2 + self.height ** 2) ** .5)


    def get_picture(self) -> str:
        """Prints a picture of the Rectangle object

        Returns:
            str: a "*" string representation of the Rectangle object
        """

        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return ("*" * self.width + '\n') * self.height


    def get_amount_inside(self, shape) -> int:
        """Returns the number of "shape" that will fit within the Rectangle object

        Args:
            shape (Square or Rectangle): a given shape, square or rectangle

        Returns:
            int: amount inside the rectangle
        """

        return self.get_area() // shape.get_area()


    def __repr__(self) -> str:
        """A string representation of the Rectangle object

        Returns:
            str: A string stating the width and height of the Rectangle object
        """

        return f"Rectangle(width={self.width}, height={self.height})"



class Square(Rectangle):


    def __init__(self, side: int) -> None:
        """Initializes a square object

        Args:
            side (int): the length of the side of the Square
        """

        self.width = side
        self.height = side


    def set_height(self, new_height: int) -> None:
        """Sets the side of the Square to new_height

        Args:
            new_height (int): the new side length
        """

        self.width, self.height = new_height, new_height


    def set_width(self, new_width: int) -> None:
        """Set's the side of the Square to new_width

        Args:
            new_width (int): the new side length of the square

        Returns:
            _type_: a reference to the set_height function
        """

        return self.set_height(new_width)


    def set_side(self, new_side: int) -> None:
        """Sets the side of the Square to new_side

        Args:
            new_side (int): the new length of the side of the square
        """

        self.width, self.height = new_side, new_side


    def __repr__(self) -> str:
        """Called when the print function is called on a Square object

        Returns:
            str: A string representation of the Square object
        """

        return f"Square(side={self.width})"
