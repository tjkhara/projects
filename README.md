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
