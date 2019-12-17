# Scanner for Arthur Morgan's journal

### Here's an example screenshot
<img src="https://github.com/charlieeWang/RDR2_Scanner_for_Arthur_Morgan-s_journal/blob/master/examples/20191213162042_1.jpg" height="500" />

I chose different coordinates on two pages, then do a simple perspective transform using OpenCV.
The output image size is been roughly resized.

#### Example transform of the left page
<img src="https://github.com/charlieeWang/RDR2_Scanner_for_Arthur_Morgan-s_journal/blob/master/examples/Scanned_left.jpg" height="400" />

#### Example transform of the right page
<img src="https://github.com/charlieeWang/RDR2_Scanner_for_Arthur_Morgan-s_journal/blob/master/examples/Scanned_right.jpg" height="400" />

#### Combine
<img src="https://github.com/charlieeWang/RDR2_Scanner_for_Arthur_Morgan-s_journal/blob/master/examples/concatenate.png" height="400" />

#### post-processing
I use the method from this [link](https://stackoverflow.com/questions/44752240/how-to-remove-shadow-from-scanned-images-using-opencv). But the shadow removing result doesn't seem so well.

- shadow remove
<img src="https://github.com/charlieeWang/RDR2_Scanner_for_Arthur_Morgan-s_journal/blob/master/examples/shadows_out.png" height="400" />

- norm & fix brightness and contrast

<img src="https://github.com/charlieeWang/RDR2_Scanner_for_Arthur_Morgan-s_journal/blob/master/examples/shadows_out_norm.jpg" height="400" />

- another example that skip the shadow part (a bit awkward), which is the current version. I think this is more suitable to print separately.
<img src="https://github.com/charlieeWang/RDR2_Scanner_for_Arthur_Morgan-s_journal/blob/master/output/20191213162042_1.jpg" height="400" />

### Use
Directly run `python Scanner.py`, it will scan all the screenshots in `test` folder, and output to `output` folder.
