We have imported two Python libraries to make our very own YouTube video downloader, which is as follows,
Tkinter: It is a standard python library used to create Graphical User Interface (GUI) Applications. Tk is one of python’s own GUI toolkits, which we will use with the help of the Tkinter interface.
Pytube: It is yet another python library containing methods and functions to help us download YouTube videos effortlessly.
After importing the libraries, we are heading towards creating the GUI window. We’ll incorporate the desired title of our downloader, a textbox to get the URL from the user, and a cool download button to click on to start downloading.
First, we have created a widget of tk, which will inhibit all the functions. The geometry function sets up the default window size of our downloader. Next, we have a resizable method that allows us to specify if we want to resize the window or not. You can put up any value in terms of width x height. The title method allows us to give the title to our GUI window.
The Label method allows us to create GUI components in the window such as text and apply formats like font and background.
The Pack method sets the component’s placement in the window by taking x and y coordinates as parameters.
We must be able to take URL input in our downloader, for which we have created a link variable that will store the URL. We share this variable in the Entry method, which constructs an entry widget with the parent MASTER.
Our program is ready to run, but one last thing is still missing. The download button! The button method allows us to create a button with desired text, color on it. In the command property of the button, we’ll pass the name of our download function, which is in this program Video_Downloader, to call in the method to execute.
 The last line allows us to download another time once we have completed the Download
