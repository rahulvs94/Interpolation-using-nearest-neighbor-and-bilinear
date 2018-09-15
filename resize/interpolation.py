import numpy as np

class interpolation:

    def linear_interpolation(self, pt1, pt2, unknown):
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown"""

        # Write your code for linear interpolation here
        x1 = pt1[0]
        y1 = pt1[1]
        i1 = pt1[2]
        x2 = pt2[0]
        y2 = pt2[1]
        i2 = pt2[2]
        x = unknown[0]
        y = unknown[1]
        # print("x,y,x1,y1,x2,y2", x,y,x1,y1,x2,y2)
        if y2 == y1 and x2 == x1:
            # print("intensity if both same", np.uint8(i2))
            return np.uint8(i2)
        if y1 == y2:
            if x2 == x1:
                a = 0.000001
                i = (i1 * (x2 - x) / a) + (i2 * (x - x1) / a)
                # print("intensity11", np.uint8(i))
            else:
                i = (i1 * (x2 - x) / (x2 - x1)) + (i2 * (x - x1) / (x2 - x1))
                # print("intensity12", np.uint8(i))
        else:
            if y2 == y1:
                b = 0.000001
                i = (i1 * (y2 - y) / b) + (i2 * (y - y1) / b)
                # print("intensity21", np.uint8(i))
            else:
                i = (i1 * (y2 - y) / (y2 - y1)) + (i2 * (y - y1) / (y2 - y1))
                # print("intensity22", i, np.uint8(i))
        return np.uint8(i)

    def bilinear_interpolation(self, pt1, pt2, pt3, pt4, unknown):
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        pt1: known point pt3 and f(pt3) or intensity value
        pt2: known point pt4 and f(pt4) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown"""

        # Write your code for bilinear interpolation here
        # May be you can reuse or call linear interpolation method to compute this task

        value1 = self.linear_interpolation(pt1, pt3, [unknown[0], pt3[1]])
        value2 = self.linear_interpolation(pt2, pt4, [unknown[0], pt4[1]])
        i = self.linear_interpolation([unknown[0], pt3[1], value1], [unknown[0], pt4[1], value2], unknown)

        return i

