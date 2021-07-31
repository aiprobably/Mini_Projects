We have imported three libraries, pygame, tkinter, and os, to make our GUI-based music player.
We use mixer from pygame to load and play our songs, while the tkinter module helps us make the graphical user interface, and we use the module to interact with the operating system.
First, we create a primary GUI window using tkinter (tk()) and set the title and size of the window using .title and .geometry.
We then start our mixer using init() and declare variables track and status.
Now we start declaring our functions that play, pause, stop and resume our songs from our playlist.
First, in the play function, we get our playlist into the current variable and display it on the screen, after which we load our current playlist into the mixer and play it, then we set the values of both our status and track variables.
Similarly, we define the function pause using the mixer and then set its status.
Then we define our stop function and set its status.
Finally, we define our resume function using the mixer. Unpause the method and set its status to playing again.
Next, after defining all the functions and completing the backend, we move on to styling our music players.
First, we start by styling the track frame for song labels, track, and status labels by providing all the necessary alignments and beautification.
After which, we move on to styling our buttons for the GUI. The play button, the pause button, the stop button, and the resume button.
Our final step is to style our playlist and set its alignment.
We use the playlist. Pack to fill any extra space allocated to it by the packer, and here we fill both horizontally and vertically.
Next, we use the OS module to change the directory and read the songs from the folder that contains all the songs.
Note: Mention the folder in your respective PCs that contains the songs inside the quotation marks.
Next, in the songs variable, we store the list of all the files and directories in the specified directory.
And then, we insert the songs into the playlist.
Then we call mainloop() to run the application.
