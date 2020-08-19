#!/bin/bash

# Enforces that it is executed with super user privileges
echo "Your UID is ${UID}"

UID_TO_TEST_FOR=0

if [[ "${UID}" -ne "${UID_TO_TEST_FOR}" ]]
then
	echo "You are not root"
	exit 1
fi

# Prompts the person who executed the script to enter the username (login), the name for
# person who will be using the account, and the initial password for the account.

# Ask for the username
read -p 'Enter the username to create: ' USER_NAME
# Ask for the real name
read -p 'Please enter your full name: ' COMMENT
# Get the password
read -p 'Enter the password: ' PASSWORD

# Creates a new user on the local system with the input provided by the user.
useradd -c "${COMMENT}" -m ${USER_NAME}

# Test if the command succeeded
if [[ "${?}" -ne 0 ]]
then
	echo "The user was not created successfully."
	exit 1
fi

# Set the password for the user
echo ${PASSWORD} | passwd --stdin ${USER_NAME}

# Test if the command succeeded
if [[ "${?}" -ne 0 ]]
then
	echo "The password was not created successfully."
	exit 1
fi

# Checking
echo "The username is ${USER_NAME} the password is ${PASSWORD} and the hostname is ${HOSTNAME}."

# Force the user to change their password the first time they log in
passwd -e ${USER_NAME}
