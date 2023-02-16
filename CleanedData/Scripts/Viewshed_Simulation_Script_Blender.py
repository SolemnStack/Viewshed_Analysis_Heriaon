# This code is using the Blender Python API (bpy) to move a light object in the scene along the x and y axis, and set its height using the ray_cast method. 

# It then renders the scene from multiple perspectives and saves the images with a specific naming convention. 
# The script starts by prompting the user to input starting and ending x and y values for the light, 
# then it moves the light to the starting point, and sets the height of the light by finding the closest 
# point on a specific object in the scene using the ray_cast method. It then enters a while loop that 
# increments the x value of the light, while the y value stays constant until it reaches the ending x value, 
# then it decrements the y value and resets the x value to the starting point. Within the while loop, 
# the script renders the scene from multiple perspectives and saves the images with a specific naming convention using the current iteration count.

import bpy
import mathutils
import os

path_dir = bpy.context.scene.render.filepath #save for restore

def move_x_axis():
    # Move light on x axis by 1
    bpy.data.objects['Point'].location = bpy.data.objects['Point'].location + mathutils.Vector((1,0,0))

def move_y_axis():
    # Move light on y axis by 1
    bpy.data.objects['Point'].location = bpy.data.objects['Point'].location + mathutils.Vector((1,0,0))

def set_z_height_light():
    # Use the ray_cast() method to find the closest point on the mesh
    # to the light. This method returns a tuple containing the coordinates
    # of the closest point on the mesh, as well as the normal vector at
    # that point.
    hit_location = bpy.data.objects['Laufniveau'].ray_cast(bpy.data.objects['Point'].location, mathutils.Vector((0, 0, -1)))[1]

    # Move the light to the hit location plus an offset of 1.6 meters
    # in the positive z direction
    bpy.data.objects['Point'].location = hit_location + mathutils.Vector((0, 0, 1.6))

####

# User-Input Starting x,y Location for Point Light
# Currently only supports rectangle grid

start_cell_x = float(input("start cell x value"))
start_cell_y = float(input("start cell y value"))

# Moves Point-Light to start position
bpy.data.objects['Point'].location = (start_cell_x, start_cell_y, 10)

# User-Input Ending x,y Location for Point Light
end_cell_x = float(input("end cell x value"))
end_cell_y = float(input("end cell y value"))

set_z_height_light()

# Switches to first scene, renders camera, saves render
for scene in bpy.data.scenes.values():
    bpy.context.window.scene = bpy.data.scenes.get(scene.name)        
    cam = bpy.context.scene.camera
    bpy.context.scene.render.filepath = os.path.join(path_dir, cam.name + '_' + '1')
    bpy.ops.render.render(write_still=True)
    bpy.context.scene.render.filepath = path_dir

i = 1

while (not(bpy.data.objects['Point'].location[0] == end_cell_x and bpy.data.objects['Point'].location[1] == end_cell_y)):
    i += 1

    # prints current loop iteration, just for user feedback
    if i == 100:
        print(i)
    if i % 10000 == 0:
        print(i)
    
    # Moves Point-Light by 1 along x-axis
    bpy.data.objects['Point'].location[0] += 1
    set_z_height_light()
    
    # Switches to first scene, renders camera, saves render
    for scene in bpy.data.scenes.values():
        print(scene.name)
        bpy.context.window.scene = bpy.data.scenes.get(scene.name)        
        cam = bpy.context.scene.camera
        bpy.context.scene.render.filepath = os.path.join(path_dir, cam.name + '_' + str(i))
        bpy.ops.render.render(write_still=True)
        bpy.context.scene.render.filepath = path_dir

    # Moves point light to next location if end of row is reached
    if bpy.data.objects['Point'].location[0] == end_cell_x + 1:
        bpy.data.objects['Point'].location[1] -= 1
        bpy.data.objects['Point'].location[0] = start_cell_x
        