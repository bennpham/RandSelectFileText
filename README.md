RandSelectFileText
===================

Introduction
------------
I needed a program to pick a random file or word from a list in cases where I want to play a few games that I will host for some friends. I mainly made this program for when I play Insurgency and wonder which theater file or map to play with in the beginning. I might as well ask a program to choose for me. I wanted the option to pick a random map from a list of map or a random theater file from a directory of files, but at the same time, have an option to create a list of item to exclude from the selection. I can look for the many random selection programs out there, but it won’t have the features I specifically want so I’ll create my own.
I decided to create this program with a few goals:
•	A really simple interface
•	The ability to exclude choices you don’t want
•	The ability to save presets of what file/directory you want to randomly select or exclude words from
Installation
Unzip the archive to anywhere on your computer.

How to Run
-----------
Click on RandSelectFileText.exe
 
Tool: Main Window
------------------ 
A window should pop up that looks like the one above. If you do not have a file called default.txt inside your RandSelectFileText folder, it will automatically be created for you. If you have this file inside your RandSelectFileText folder already, the program will read this document and will make its values (if it contains valid values) as its default launch parameters. 
 
Tool: List to Randomly Select
------------------------------
The List to Randomly Select box is where you type in the location of the directory with the filename or directory of the items you want to add to the list of randomly selected items (words for text files or names of files if directory). You can get the name/location in 3 ways.
-	Type in the directory of the file with the name of the file at the end or the name of the path
-	Click the file button and browse for the file to add
-	Click the folder button and browse for the path to add
Note:	You can just type in the name of the file if it is in the same folder as RandSelectFileText.exe 

Tool: List to Exclude
----------------------
The List to Exclude is where you type in the location of the directory with the filename or directory of the items you want to exclude from the list of randomly selected items (words for text files or names of files if directory). You can get the name/location the same way as List to Randomly Exclude. See above on page 4. 
Basically how List to Randomly Select and List to Exclude works is if List to Randomly Select contains “a, b, c, d, e” and List to Exclude contains “c, d, e”, only “a” and “b” will be selected on a randomly chosen list. 
The same thing works if List to Randomly Select contains “a.txt, a.dll, b.txt, b.exe, c.bat” and List to Exclude contains “a.rar”. Since filenames are stripped of their extension, the result chosen will not contain the extension and will only print out “b” or “c” (taking into account that “a” has been excluded from list to exclude. 
Note: There are no advantages of a single name reappearing multiple times to be selected more often.

Tool: Run & Result
------------------ 
The Run button executes the results of List to Randomly Select and List to Exclude then outputs the randomly selected word into the grey box. 
Note: If you enter rubbish into the text box that points to nothing and click RUN, nothing will happen.
Note: If you select an unreadable file, you will receive an error like the one below. (Example of unreadable files would be gif files, jpeg files, exe files, etc).
 
Tool: Make Default
------------------- 
This button saves your current settings (anything in your List to Randomly Select and List to Exclude) to your default.txt file.
Because the program reads from default.txt before it starts, the program will start with the same settings you previously had since the last time you click MAKE DEFAULT.
Note: You can change your default.txt file manually to change startup parameters. I would only recommend this to advance users only. If you put invalid parameters, the program will start up with any valid parameters it can find.

Tool: Load Set & Save Set
-------------------------- 
Besides MAKE DEFAULT, you can also use SAVE SET to save your current settings to a separate text file in the same format as default.txt file.
LOAD SET allows you to load parameters from another text file into the program and it will change each setting for each valid parameters.
Note: 
-	You can load a text file with random texts but it will still load as long as there is a valid parameter inside.
-	Nothing will happen if you load an invalid text file

Editing Default.txt & Making Your Own Sets Manually
--------------------------------------------------- 
This is the standard layout of the default.txt file. You can manually edit it if you want. You can add in any spam text (slowing the program down) as long as it still contains the following parameters, it will load. The parameters can appear in any order. It is best that you don’t add thousands of lines of spam texts or else you will slow the program down as it tries to read all of the lines although this haven’t been tested nor would it be too significant. 
You can also create your own text files to load via LOAD SET based on these parameters. LOAD SET and starting the program for default.txt will take any values for the following:
-	TARGET DESTINATION
-	EXCLUDE DESTINATION

Unknown Errors
--------------- 
If for any reason you receive this error from any task, please report them to me.
