#!/bin/bash

echo "Please provide the following information:"

read -p "> Your name: " _author_
read -p "> Your email address: " _email_
read -p "> The current year [2019]: " _year_
read -p "> Your package name: " _package_name_
read -p "> Your package GitHub address: " _url_

_year_=${_year_:-"2019"}

echo

echo "'configure_package_name' will be updated to '$_package_name_' in the following files and directories:"

echo ./package_name
grep -rl "configure_package_name" . --exclude=*.pyc --exclude=*.git* --exclude=configure.sh

echo

echo "And the package will be updated with the following details:"
echo " - Your name: $_author_"
echo " - Your email_address: $_email_"
echo " - The current year: $_year_"
echo " - Your package GitHub address: $_url_"

echo

echo "Are you sure you want to make these changes?"

read -p "> [y/N]: " _response_

echo

_response_=${_response_:-"n"}

if [ "$_response_" != "Y"  ] && [ "$_response_" != "y"  ]; then
  echo "Looks like you are not happy with that. Better start over!"
  exit 1
fi

update_template() {
  grep -rl $1 . --exclude=*.pyc --exclude=*.git* --exclude=configure.sh| xargs sed -i '' -e "s,$1,$2,g"
}

export LC_ALL=C
mv ./package_name ./$_package_name_
update_template "configure_package_name" "$_package_name_"
update_template "configure_author" "$_author_"
update_template "configure_email" "$_email_"
update_template "configure_year" "$_year_"
update_template "configure_url" "$_url_"
