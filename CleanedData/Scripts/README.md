Two Python scripts were written to help with the project. 
They were needed as parts of the project would not have been able to be completed just using manual labor.
These included:

### Read_Write_Report_to_asc.py
After processing the rendered viewsheds in QGIS, it saved a R-statistics file for every image containing the ammount of white to black pixels. 
These values then had to be extracted from these individual files and saved in a .asc file, so that it could then be opened by QGIS again and display the raster image
of the viewshed. The values had to be formated correctly into the .asc file.
This script handles the reading of the files, extracting the values, and inserting them in the correct format.

This code reads a set of HTML files and extracts a numeric value from them, then writing that value to an ASCII file in a specific format.

The code starts by defining two variables for the number of columns and files to be read, and using them to calculate the number of rows.
It then creates a header string containing information about the ASCII file format, and writes that header to an ASCII file using the with open statement and the 'w' mode.
Then, the script enters a while loop that iterates through each file, reading it and using a regular expression to extract a specific string ("Mean") and its value,
which is then converted to an int number. It then performs a mathematical operation on that value and writes the result to the ASCII file, with a specific format.
If the current file number is not a multiple of the number of columns, it writes the value followed by a space, otherwise it writes the value followed by a new line.


### Viewshed_Simulation_Script_Blender.py
As the project needed to calculate the viewshed from many positions, a script was written to be able to switch from position to position, 
render the image and then save it with a formatted name. Render time was also saved using this method, cutting off a couple seconds per image.

This code uses the Blender Python API (bpy) to move a light object in the scene along the x and y axis, set its height using the ray_cast method.
It then renders the scene from multiple perspectives and saves the images with a specific naming convention. 

The script starts by prompting the user to input starting and ending x and y values for the light, 
then it moves the light to the starting point, and sets the height of the light by finding the closest 
point on a specific object in the scene using the ray_cast method. It then enters a while loop that 
increments the x value of the light, while the y value stays constant until it reaches the ending x value, 
then it decrements the y value and resets the x value to the starting point. Within the while loop, 
the script renders the scene from multiple perspectives and saves the images with a specific naming convention using the current iteration count.
