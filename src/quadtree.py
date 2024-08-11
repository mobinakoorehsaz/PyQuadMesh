import numpy as np
import matplotlib.pyplot as plt


class Node:
    """
        A node in the quadtree.

        Attributes:
            x (float): The x-coordinate of the node's top-left corner.
            y (float): The y-coordinate of the node's top-left corner.
            width (float): The width of the node.
            height (float): The height of the node.
            point (object): The point contained in the node (if any).
            divided (bool): Whether the node has been subdivided.
            nodes (list): A list of child nodes.
        """

    # node: هر گره دارای مختصات، اندازه، وضعیت تقسیم شدن، لیستی از اشیاء و لیستی از زیرگره‌ها است.
    def __init__(self, x, y, width, height, point=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.point = point
        self.divided = False
        self.nodes = []

    # متدهای subdivide, insert و query عملیات اصلی روی گره را انجام می‌دهند
    def subdivide(self):
        """Subdivides the node into four quadrants."""
        # ... (implementation will be added later)
        # تقسیم کردن گره به چهار زیر گروه
        pass

    def insert(self, object):
        """Inserts a point into the node or its descendants."""
        # ... (implementation will be added later)
        # ... (اضافه کردن یک شیء به گره یا یکی از زیرگره‌ها)
        pass

    def query(self, range):
        """Queries the node for points within a given range."""
        # ... (implementation will be added later)

        # ... (جستجوی اشیاء در یک محدوده مشخص)
        pass


class Quadtree:
    """
       A quadtree data structure.

       Attributes:
           root (Node): The root node of the tree.
           capacity (int): The maximum number of points a node can hold before subdividing.
       """

    # کلاس اصلی یک ریشه دارد که یک Node است. متدهای insert و query عملیات اصلی روی درخت را انجام می‌دهند
    def __init__(self, boundary, capacity=1):
        self.root = Node(boundary[0], boundary[1], boundary[2], boundary[3], capacity)

    def insert(self, point):
        """Inserts a point into the quadtree."""
        self.root.insert(point)

    def query(self, range):
        """Queries the quadtree for points within a given range."""
        return self.root.query(range)


def generate_points_around_circle(center, radius, num_points):
    angles = np.linspace(0, 2 * np.pi, num_points)
    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)
    return np.column_stack((x, y))


# # مثال استفاده:
# ایجاد یک دایره
radius = 2
center = (5, 5)

# ایجاد نقاط اطراف دایره
num_points = 20
points = generate_points_around_circle(center, radius, num_points)

# ایجاد Quadtree
boundary = (0, 0, 10, 10)  # مرز اولیه Quadtree
qt = Quadtree(boundary)

# درج نقاط در Quadtree
for point in points:
    qt.insert(point)

# رسم دایره و نقاط
plt.plot(center[0], center[1], 'ro', label='Center')
plt.plot(points[:, 0], points[:, 1], 'bo', label='Points')
plt.axis('equal')
plt.legend()
plt.show()
