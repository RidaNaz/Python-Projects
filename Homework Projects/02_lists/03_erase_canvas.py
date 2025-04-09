""" This program implements an 'eraser' on a canvas.

The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. 
We then create an eraser rectangle which, when dragged around the canvas, sets all of the 
rectangles it is in contact with to white. """

from graphics import Canvas
import time

# Constants for canvas and object sizes
CANVAS_WIDTH: int = 400
CANVAS_HEIGHT: int = 400
CELL_SIZE: int = 40
ERASER_SIZE: int = 20

def erase_objects(canvas, eraser):
    """Erase objects in contact with the eraser."""
    mouse_x = canvas.get_mouse_x()
    mouse_y = canvas.get_mouse_y()
    
    # Define the eraser's bounding box
    left_x = mouse_x
    top_y = mouse_y
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE
    
    # Find all shapes the eraser overlaps with
    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)
    
    # Change color of all overlapping shapes to white (except the eraser itself)
    for obj in overlapping_objects:
        if obj != eraser:
            canvas.set_color(obj, 'white')

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Calculate grid dimensions
    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE
    
    # Draw the grid of blue cells
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE
            canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'blue')
    
    canvas.wait_for_click()
    
    # Get initial position to place the eraser
    start_x, start_y = canvas.get_last_click()
    
    # Create the pink eraser
    eraser = canvas.create_rectangle(
        start_x, 
        start_y, 
        start_x + ERASER_SIZE, 
        start_y + ERASER_SIZE, 
        'pink'
    )
    
    # Continuously move the eraser with the mouse and erase touched cells
    while True:
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        canvas.moveto(eraser, mouse_x, mouse_y)
        
        erase_objects(canvas, eraser)
        
        time.sleep(0.05)

# Required boilerplate
if __name__ == '__main__':
    main()