# AutoCompiler
## Instructions for modifying program to work with any sheet of a similar format
  1. Change the directories listed on line 31 to match the location of the image file of the sheet.  
  ```    straighten.deskew("./directory/" + file_name, "./newdirectory/deskewed_sheet.jpg")```
  2. Retrieve size of each box, and replace the values of h and w, line 41 and 42 in images.py to the size of the box, in pixels. Then, retrieve the coordinates (in pixels) of the top left of the box and using this template, change the values of the coordinates, as well as the directory & file you would like to save the new cropped image to.  
If you have boxes close together, change the `gap` variable based on the distance from the first box, and include the 3rd line from this code snippet. 
``` 
    gap = value_in_pixels
    x, y = enter_x_coordinate, enter_x_coordinate
    cv2.imwrite("./directory/filename1.jpg", sheet[y:y+h, x:x+w])
    cv2.imwrite("./directory/filename2.jpg", sheet[y:y+h, x+gap:x+gap+w])
```  
If no gap required then omit the first and last lines and repeat the contents of the second and third lines.
