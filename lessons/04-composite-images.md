Lesson 4: Compositing Images
===

Summary
---
Draw an employee's image onto a the badge Image using Image.paste(), and 
place it correctly

Notes
---
At this point, we already have everything we need to complete this project.
We're able to:
  - load the badge template into a Image object
  - load employee data from a JSON file
  - load employee images into Image objects
  - save Image objects from PNGs to a directory as JPGs

All this with only 14 lines of code!

Now we can focus on processing the images to build the badges.

In this lesson, we're going to composite employee images onto the badge image using Image.copy() and Image.paste()

We'll get a glimpse of the Pillow cooridante system, as we'll place the employee
photo in the correct place on the badge.

We'll save the images as PNGs, which are high-quality, using good filenames.

Build Note: I noticed that the photo images are about 2 pixels too tall for the square
in the badge template. I could either resize all the images, or change the
badge. Either way, I need to take a few minutes to make changes to 00 and merge
that change through to the lesson 4 branches.
