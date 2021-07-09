First, we import three libraries: requests, os, and bs4. The requests module allows one to send HTTP requests using Python and the HTTP request returns a response object with all response data. The OS module is one of Python's standard utility modules that provides functionality for interacting with the operating system. We import the last module, the beautiful soup module or bs4 module that scrapes information from web pages, pulling data out of HTML and XML files.
We then set the Base URL of the web page that we are going to scrape. In this case, it is the xkcd comics page.
After which, we create an xkcd directory using the os module. This directory will store the scraped data from the xkcd website.    
We can download any number of pages as per our requirements; in this case, we use the for loop to download ten comic pages.  
The print statement in the loop starts printing the downloading URL of the xkcd page. This is where the entire page is downloaded.
After this, a GET request is sent to the URL, and the response object is stored in the res variable.
If there is an error, the res.raise_for_status() will throw an exception, and the code will stop; otherwise, the execution continues.
Next, we use the beautiful soup module to parse HTML data of the URL and store it in the soup variable.
Now we need to find the URL of the comic image, for which we select the comic URL from the soup variable that has all the parsed data. Now, if comic_elem comes up empty, that means the image could not be found, and we display it using a prompt.
Comic_elem stores a list of image sources, so in the next step, we always take the first element of the list and send a GET request for the source of the first element and store it in the comicUrl variable.
This is when the downloading of the comic images begins by sending a GET request and storing the response object in the res variable, and checking its status after it.
We then have to save the images in the xkcd folder that we made earlier. We store the comic images chunk by chunk using the res response object in the loop and then writing the images to the image_file.
This is when one single image is downloaded and stored in the xkcd directory. After which, we get the URL of the previous button and store it in the prev_link, and the URL is updated with a GET request for prev_link added to the original URL.
This process is then repeated to download the required number of comic images.
After the specified number of images are downloaded, we exit the loop, and Done is prompted to the user.
