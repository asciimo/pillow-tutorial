Lesson 3: Map Employee Records to Image Files
===

Summary 
---
Load and parse the employee data from a JSON file, and load the employee's photo file into an Image object

Notes
---
Now that we know PIL is good to go, we'll load the employee data from a JSON
file, and iterate over the records.  We'll print the employee name to the
console, and then load the employee photo into an Image object.  

This ensures that we can map the employee data to images in the filesystem.
At a higher leve, this illustrates a common pattern when batch-processing lots
of image files: iterate, load, process, save.

Along the way, we'll demonstrate how easy it is to transform a JPG image into a
PNG image, by saving the images as PNGs in the dist/ directory.
