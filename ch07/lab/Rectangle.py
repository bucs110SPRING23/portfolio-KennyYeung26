class Rectangle:
    def __init__(self, x, y, h, w):
        self.x = abs(x)
        self.y = abs(y)
        self.height = abs(h)
        self.width = abs(w)
            
    def __str__(self):
        """
        This function returns a string containing the x, y, width, and height of the rectangle
        args: Self
        return: a string in the form "(x : #, y: #) width: #, height: #
        """
        return "(x: " + self.x + ", y: " + self.y + ") width: " + self.width + ", height: " + self.height
    