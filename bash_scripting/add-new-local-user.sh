#!/bin/bash

# Enforces that it is executed with super user privileges
echo "Your UID is ${UID}"

UID_TO_TEST_FOR=0

if [[ "${UID}" -ne "${UID_TO_TEST_FOR}" ]]
then
	echo "You are not root"
	exit 1
fi

# Display what the user typed on the command line
echo "You executed this command: ${0}"

# Tell them how many arguments they passed in
NUMBER_OF_PARAMETERS="${#}"
echo "You supplied ${NUMBER_OF_PARAMETERS} argument(s) on the command line."

# Make sure atleast one user is supplied on the command line
if [[ "${NUMBER_OF_PARAMETERS}" -lt 1 ]]
then
	echo "Usage: ${0} USER_NAME [COMMENT]..."
	echo "Create an account on the local system with the name of USER_NAME and a comments field of COMMENT"
	exit 1
fi

# Old code start
# Prompts the person who executed the script to enter the username (login), the name for
# person who will be using the account, and the initial password for the account.

# Ask for the username
# read -p 'Enter the username to create: ' USER_NAME
# Ask for the real name
# read -p 'Please enter your full name: ' COMMENT
# Get the password
# read -p 'Enter the password: ' PASSWORD
# old code end

# Uses the first argument provided on the command line as the username for the account. Any
# remaining arguments on the command line will be treated as the comment
USER_NAME=${1}
echo "The first param you entered is ${1}"

# Write separate case for when number of parameters is exactly two
if [[ "${NUMBER_OF_PARAMETERS}" -eq 2 ]]
then
	COMMENT_STR="${2}"
else

	# If the number of parameters is greater than 2 we need to do this additional step
	while [[ "${#}" -ge 2 ]]
	do
		COMMENT_STR="${COMMENT_STR} ${2}"
		shift
	done
fi

# Creates a new user on the local system with the input provided by the user.
useradd -c "${COMMENT_STR}" -m ${USER_NAME}

# Test if the command succeeded
if [[ "${?}" -ne 0 ]]
then
	echo "The user was not created successfully."
	exit 1
fi

# Automatically generate a password for the new account
PASSWORD=$(date +%s%N | sha256sum | head -c10)
echo "The password generated for user: ${USER_NAME} is ${PASSWORD}"

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
