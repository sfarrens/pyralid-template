#!/bin/bash

# Divider line
line="########################################################################"
version="0.0.2"

echo
echo $line
echo "Python Package Set Up Script"
echo
echo "Author: Samuel Farrens"
echo "Year: 2020"
echo "Version:" $version
echo
echo "See https://github.com/sfarrens/python_package_template for help."
echo
echo $line
echo
echo "Please provide the following information:"

read -p "> Your name: " _author_
read -p "> Your email address: " _email_
read -p "> The current year [2020]: " _year_
read -p "> Your package name: " _package_name_
read -p "> Your package GitHub address: " _url_
read -p "> A short description of your package: " _describe_
read -p "> A list of packages your code requires (e.g. numpy,scipy,matplotlib): " _requires_


_year_=${_year_:-"2020"}

echo

echo "The following files and directories will be updated with the package name '$_package_name_':"

echo ./package_name
grep -rl "configure_package_name" . --exclude=*.pyc --exclude=*.git* --exclude=configure.sh

echo

echo "and the package will be updated with the following details:"
echo " - Your name: $_author_"
echo " - Your email_address: $_email_"
echo " - The current year: $_year_"
echo " - Your package GitHub address: $_url_"
echo " - A short description of your package: $_describe_"
echo " - A list of packages your code requires: $_requires_"

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
  if [[ "$OSTYPE" == "darwin"* ]]; then
    grep -rl $1 . --exclude=*.pyc --exclude=*.git* --exclude=configure.sh| xargs sed -i '' -e "s,$1,$2,g"
  else
    grep -rl $1 . --exclude=*.pyc --exclude=*.git* --exclude=configure.sh| xargs sed -i -e "s,$1,$2,g"
  fi
}

update_requirements() {
  for package in $(echo $_requires_ | sed "s/,/ /g")
  do
    echo $package >> requirements.txt
  done
}

export LC_ALL=C
mv ./package_name ./$_package_name_
update_template "configure_package_name" "$_package_name_"
update_template "configure_author" "$_author_"
update_template "configure_email" "$_email_"
update_template "configure_year" "$_year_"
update_template "configure_url" "$_url_"
update_template "configure_description" "$_describe_"
update_requirements

finish() {
  echo "All done!"
  exit 1
}

echo "Do you want the script to execute git commands for you?"
read -p "> [y/N]: " _response2_

echo

_response2_=${_response2_:-"n"}

if [ "$_response2_" != "Y"  ] && [ "$_response2_" != "y"  ]; then
  finish
fi

echo "Commiting changes to template."

git add .
git commit -m "updated template"
git push

echo "Creating gh-pages branch for API documentation."

git checkout --orphan gh-pages
git rm -rf .
git push --set-upstream origin gh-pages
git commit -m "cleaning gh-pages"
git push
git checkout master
git branch -d gh-pages

finish
