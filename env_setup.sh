#!/bin/bash

if [ -d tweet ]
then
	printf "Environment exists!\nEntering Python virtualenv and creating ENV_VARIABLES\n"
	source tweet/bin/activate
	pip3 install -r requirements.txt
	export AT='YOUR ACCESS TOKEN'
	export AT_S='YOUR ACCESS TOKEN SECRET'
	export CON='YOUR CONSUMER KEY'
	export CON_S='YOUR CONSUMER KEY SECRET'
else
	printf "Environment doesn't exist. Creating Python virtualenv tweet and ENV_VARIABLES\n"
	virtualenv -p python3 tweet
	source tweet/bin/activate
	pip3 install -r requirements.txt
	export AT='YOUR ACCESS TOKEN'
	export AT_S='YOUR ACCESS TOKEN SECRET'
	export CON='YOUR CONSUMER KEY'
	export CON_S='YOUR CONSUMER KEY SECRET'
fi