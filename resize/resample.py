import numpy as np
from .interpolation import interpolation

class resample:
    def resize(self, image, fx=None, fy=None, interpolation=None):
        """calls the appropriate funciton to resample an image based on the interpolation method
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        interpolation: method used for interpolation ('either bilinear or nearest_neighbor)
        returns a resized image based on the interpolation method
        """
        if interpolation == 'bilinear':
            return self.bilinear_interpolation(image, float(fx), float(fy))

        elif interpolation == 'nearest_neighbor':
            return self.nearest_neighbor(image, float(fx), float(fy))

    def nearest_neighbor(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the nearest neighbor interpolation method
        """

        # Write your code for nearest neighbor interpolation here
        [w, h] = np.shape(image)
        # print("w,h",w,h)
        # print("size of given image: ", np.shape(image))
        [w_dash, h_dash] = [int(np.ceil(w * fy)), int(np.ceil(h * fx))]
        dash_image = np.zeros((w_dash, h_dash), dtype=int)
        # print("size of dash image: ", np.shape(dash_image))
        [rows, columns] = np.shape(dash_image)
        # print("rows, columns ", rows, columns)
        # print("len(range(rows)),len(range(columns))", len(range(rows)),len(range(columns)))
        for i in range(rows):
            for j in range(columns):
                nx = int(np.floor(i / fy))
                ny = int(np.floor(j / fx))
                # print("i,j,nx,ny,image[nx, ny]",i,j,nx,ny,image[nx, ny])
                dash_image[i, j] = image[nx, ny]

        return dash_image

    def bilinear_interpolation(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the bilinear interpolation method
        """
        object = interpolation()
        # Write your code for bilinear interpolation here
        [w, h] = np.shape(image)
        # print("size of given image: ", np.shape(image))
        [w_dash, h_dash] = [int(np.ceil(w * fy)), int(np.ceil(h * fx))]
        dash_image = np.zeros((w_dash, h_dash), dtype=int)
        # print("size of dash image: ", np.shape(dash_image))
        [rows, columns] = np.shape(dash_image)
        # print("rows, columns ", rows, columns)
        # print("len(range(rows)),len(range(columns))", len(range(rows)),len(range(columns)))
        for i in range(rows):
            for j in range(columns):
                [nx, ny] = [(i / fy), (j / fx)]

                x1 = int(np.floor(nx))
                x2 = int(np.ceil(nx))

                y1 = int(np.floor(ny))
                y2 = int(np.ceil(ny))

                if x1 > w-1:
                    x1 = w-1
                if y1 > h-1:
                    y1 = h-1
                if x2 > w-1:
                    x2 = w-1
                if y2 > h-1:
                    y2 = h-1
                # print("x1,y1,x2,y2", x1, y1, x2, y2)
                q11 = image[x1, y1]
                q12 = image[x1, y2]
                q21 = image[x2, y1]
                q22 = image[x2, y2]
                dash_image[i, j] = object.bilinear_interpolation([x1, y1, q11], [x1, y2, q12], [x2, y1, q21], [x2, y2, q22], [nx, ny])
                # print("i,j,nx,ny,dash_image[i, j]", i, j, nx, ny, dash_image[i, j])

        return dash_image
