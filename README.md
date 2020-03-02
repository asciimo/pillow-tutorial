Module Summary
===

Target audience: Creatives and technology professionals who are often tasked
with processing large amounts of image data. Students should be familiar with various
image formats, filesystems, and have beginner to intermediate Python skills.

Project: Create and print employee identification badges

The general purpose of this module is to instruct the student how to batch process
a collection of image files using Python. Specifically, the student will use the
Pillow imaging library to output annotated composite images from several source images.

One might assume that an image processing library as powerful as Pillow might be
difficult to use. It's actually quite intuitive and concise.

The module is built upon a project in which the student will create printable
identification badges using a JSON file of employee data, a collection of employee
images, and an identification badge template. The student will use the Pillow imaging
library to copy each employee's photograph on a copy of the badge template, and
draw the employee's data as text onto the image.

The learning objectives for the student are:
  - Loading a JSON file into memory and using it to drive batch image processing
  - Manipulating image data as Pillow `Image` objects
  - Calculate two dimensional layout values using Pillow's drawing context and coordinate system
  - Draw text onto Image objects using Pillow's `ImageDraw` module 
  - Loading TrueType fonts to improve Pillow's typography
  - Composite images using `Image.paste()`
  - Output processed images suitable for printing

Module Lesson Sequence
===
1. **Setup**: Set up a working environment with Pillow and its dependencies
2. **Introduction to Pillow**: Load the badge template into a Pillow `Image` object
3. **Mapping Employee Records to Image Files**: Load and parse the employee data 
   from a JSON file, and load the employee's photo file into an Image object
4. **Compositing Images**: Draw an employee's image onto the badge Image using Image.paste(), and
   place it correctly
5. **Placing Text**: Draw the employee's name onto the image using Pillow's
   drawing context and coordinate system.
6. **TrueType Fonts**: Using Pillow's `ImageFont.truetype()` to draw good-looking fonts 
7. **Creating a PDF**: Use the same techniques above to create a printer-ready PDF
8. **Further Reading**: Where to go from here?

Navigating the Module
===
This module was developed in a series of Git branches, each branch building on
the previous. If you would like to see how the project is built following the
lesson sequence, you may check out the branch associated with the lesson.

**Only Lesson 5 ([05-placing-text](https://github.com/asciimo/pillow-tutorial/tree/05-placing-text))
has complete lesson material.** Other branches contain notes or lesson summaries
that illustrate the context of those lessons.

The lesson branches are:

1. Setup [01-source-assets](https://github.com/asciimo/pillow-tutorial/tree/01-source-assets)
2. Introduction to Pillow [02-load-badge](https://github.com/asciimo/pillow-tutorial/tree/02-load-badge)
3. Mapping Employee Records to Image Files [03-parse-employees](https://github.com/asciimo/pillow-tutorial/tree/03-parse-employees)
4. Compositing Images [04-composite-images](https://github.com/asciimo/pillow-tutorial/tree/04-composite-images)
5. Placing Text [05-placing-text](https://github.com/asciimo/pillow-tutorial/tree/05-placing-text)

Quick Start
===
You can get up and running with Lesson 5 by following these steps:

Clone this repository.
---

```bash
git clone git@github.com:asciimo/pillow-tutorial.git
```

Check out the Lesson 4 branch
---

This will start you with the project code at the end of Lesson 4. You can then
follow the lesson content for [Lesson 5 on GitHub](https://github.com/asciimo/pillow-tutorial/tree/05-placing-text/lessons/05-placing-text.md). 

```bash
git checkout 04-composite-images
```

Enter the working environment
---

```bash
cd environment
```

Build the Docker image
---

```bash
docker build . --build-arg uid=$UID -t asciimo/pillow-tutorial
```
Run the Docker container
---

```bash
docker run -v $(pwd):/pillow-tutorial --name pillow-tutorial -it asciimo/pillow-tutorial /bin/sh
```

This will drop you into the working environment shell, with the current host
directory (`environment/`) mounted. You can run `badges.py` from here. You can
browse and modify the project code and images on your host machine, and the
changes will be reflected in the container.

Attribution
===
Several free images have been modified for use in this project. They are:

| filename            | author                         | source                                                                                               |
| ---                 | ---                                  | ---                                                                                                  |
| greta_white.jpg     | Alexander Khokhlov, Veronica Ershova | [Creative Commons](https://ccsearch.creativecommons.org/photos/11f2758a-0084-4333-8581-a54914fa0de4) |
| paul_donaldson.jpg  | Alexander Khokhlov, Veronica Ershova | [Creative Commons](https://ccsearch.creativecommons.org/photos/cab91603-e825-4d8c-b6d8-3bdb29d0228e) |
| robert_jackson.jpg  |                                      | [Creative Commons](https://ccsearch.creativecommons.org/photos/3474484f-f75c-45bd-85f7-0efa8678bc1a) |
| stanley_odonnel.jpg |                                      | [Creative Commons](https://ccsearch.creativecommons.org/photos/78081f76-d2e8-492a-b37f-4a8f5a64eba8) |
| samantha_jones.jpg  | Stephen Calnan                       | That's my girl!                                                                                      |
| badge.png           | Template Archive                     | [Template Archive](https://templatearchive.com/id-badge-cards/)                                      |
