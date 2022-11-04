class Rectangle:

    def __init__(self, width : int, height : int) -> None:
        self.width = width
        self.height = height


    def set_width(self, new_width : int) -> None:
        self.width = new_width


    def set_height(self, new_height : int) -> None:
        self.height = new_height


    def get_area(self) -> int:
        return self.width * self.height


    def get_perimeter(self) -> int:
        return (2 * self.width + 2 * self.height)


    def get_diagonal(self) -> float:
        return ((self.width ** 2 + self.height ** 2) ** .5)


    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return ("*" * self.width + '\n') * self.height


    def get_amount_inside(self, shape) -> int:
        return self.get_area() // shape.get_area()


    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"



class Square(Rectangle):


    def __init__(self, side: int) -> None:
        self.width = side
        self.height = side


    def set_height(self, new_height: int) -> None:
        self.width, self.height = new_height, new_height


    def set_width(self, new_width: int) -> None:
        return self.set_height(new_width)


    def set_side(self, new_side: int) -> None:
        self.width, self.height = new_side, new_side


    def __repr__(self) -> str:
        return f"Square(side={self.width})"
