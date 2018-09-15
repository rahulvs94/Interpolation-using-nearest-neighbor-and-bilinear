# Digital Image Processing 

1. Resampling using nearest neighbor and bilinear:
    
  - resize/resample.py: This file is use to edit the functions "nearest_neighbor" and "bilinear"
  - resize/interpolation.py: This file is use to write code for linear and bilinear interpolation in there respective function definitions which could be use while performing bilinear method 
  - Usage: 
		./dip_hw1_resize.py -i image-name -fx scalex -fy scaley -m method  
		
		- image-name: name of the image
		- scalex, scaley: scale to resize the image (eg. fx 0.5, fy 0.5 to make it half the original size)
		- method: "nearest_neightbor" or "bilinear" 
	   
  - Example: 
		- ./dip_hw1_resize.py -i cell2.jpg -fx 0.75 -fy 0.75 -m nearest_neighbor
        or 
        - python dip_hw1_resize.py -i cell2.jpg -fx 0.75 -fy 0.75 -m nearest_neighbor

