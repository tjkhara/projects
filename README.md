# Projects

## Feb 2021

### HTML/CSS/Web Design

Omnifood website: https://cocky-elion-672a4e.netlify.app/

* Beautiful design
* Responsive
* Single page website for a food company

## January 2021

### Todo App

Live app link: direful-cap.surge.sh

This app:

* Has a simple CRUD application using browser local storage to manage todos
* Uses webpack and babel to make the app functional on older browsers with modern code
* Allows the user to complete todos, hide completed todos, and search todos

### Notes App

Live app link: https://tjnotes.netlify.app/

This app:

* Has a simple CRUD application using browser local storage to manage notes
* Uses webpack and babel to make the app functional on older browsers with modern code
* Allows the user to open multiple browser tabs and syncs state across all tabs

### Hangman Game

Live app link: https://tjhangman.netlify.app/

This app:

* Allows the user to play the hangman game in a browser
* Uses webpack and babel to make the app functional on older browsers with modern code
* Uses an external api to load new words for games

## Update for wrapping up 2020

[nodejs - socket.io real time chat app](https://github.com/tjkhara/socket.io-chatapp)

Live app link: https://tjkhara-chatapp.herokuapp.com/

This app:

* Uses the socket.io protocol to enable users to send messages from the client to the server and from server to the chat rooms
* Enables users to join different chat rooms and chat with other clients in those chat rooms
* Messages are not stored and are emitted and received in real time
* Users can share their locations as well

[nodejs - task manager api](https://github.com/tjkhara/task-manager-api)

Live api link: https://tjkhara-task-manager-api.herokuapp.com/

This app:

* Enables front end users to make requests for creating, reading, updating, and deleting tasks.
* Project tested with jest.
* Has email integration with sendgrid API.
* Is integrated with MongoDB.
* Handles image formatting and uploading pictures to the server.
* Supports filtering, pagination, and sorting of data.

[nodejs - weather app](https://github.com/tjkhara/weather-app)

Live app link: https://tjkhara-weather-app.herokuapp.com/

This app:

* Enables users to get the live wether for any location.
* Uses the geolocation api along with the weatherstack api.

Projects built post August 2020

[bash scripting project - adding local users](./bash_scripting/add-local-user.sh)

This script:

* Enforces that it be executed with superuser (root) privileges. If the script is not executed with
superuser privileges it will not attempt to create a user and returns an exit status of 1.
* Prompts the person who executed the script to enter the username (login), the name for
person who will be using the account, and the initial password for the account.
* Creates a new user on the local system with the input provided by the user.
* Informs the user if the account was not able to be created for some reason. If the account is
not created, the script is to return an exit status of 1.
* Displays the username, password, and host where the account was created. This way the
help desk staff can copy the output of the script in order to easily deliver the information to
the new account holder.

[bash scripting project - generating random passwords](./bash_scripting/generate-random-password.sh)

* Uses loops, random number generating, SHA256 hashing to automatically generate random passwords for users supplied as arguments on the command line along with the script.

[bash scipting project - adding local users via the command line with comments field and randomly generated passwords](./bash_scripting/add-new-local-user.sh)

* Add users to your local account by suppying command line arguments as opposed to an interactive session.
* Add username and the comments field for each user.
* A randomly generated password will be added for each added user.
* The password will need to be changed on the first login.
* The first argument provided is the username and any number of arguments after that are processed as the input for the comments field.

[python scripting project - encrypting text using the caesar cipher, decryption, and brute force decryption also available](https://github.com/tjkhara/projects/blob/master/python/caesar_cipher/caesar_cipher.py)

* Encrypt your text using the caesar cipher using a shift value
* Decrypt the encrypted text using the shift value
* Decrypt the encypted text using a brute force method

[Object Oriented Python Scripting Project](https://github.com/tjkhara/courses_repo/blob/master/python3_masterclass_jp/sandbox/FRE%20-%20test%203%20adding%20in%20random%20letter.ipynb)

* Added on to the caesar cipher
* Three step cipher
  * Added in a random letter at every other index position
  * Reversed the string
  * Used a randomly shuffled alphabet for a caesar cipher
* Contains decryption method as well

[Traversing Directories and Files Recursively To Search For a Pattern in the Text Files Using Regular Expressions](https://github.com/tjkhara/projects/tree/master/python/traversing_file_structure_and_using_regex)

* Used os.walk() to traverse through directory structure and examine the content of all the text files to look for a link regular expression pattern
* Used shutil to unzip downloaded zip file
* Explored directories and files using os neutral methods such as os.listdir()
* Read text of the files within numerous sub directories
* Then searched using the re module

[Encryption and Decryption scripts in python](https://github.com/tjkhara/projects/blob/master/python/encryption_decryption/encryption.py)

* Use this script to encrypt any sensitive data and get a key along with the encrypted message
* Use the key and the encrypted message in the decryption script to decrypt this data
* Potential use could be to store sensitive crendential information on the cloud or on a private git repo
* Still need to investigate the use of public private key encryption for the same purpose
* This is possibly insecure for this purpose but better than storing sensitive data in plain text
