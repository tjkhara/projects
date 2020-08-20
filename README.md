# Projects

Repo for projects starting Aug 2020

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
