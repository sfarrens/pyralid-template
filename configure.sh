#!/bin/bash

echo "Please specify your package name:"

read -p "> " _package_name_

echo

echo "Are you sure you want to update the template to ?"

read -p "> [y/N]: " _response_

echo

_response_=${_response_:-"n"}

if [ "$_response_" != "Y"  ] && [ "$_response_" != "y"  ]; then
  echo "Better start over!"
  exit 1
fi

echo "Updating 'package_name' to '$_package_name_' in the following files:"

grep -rl "package_name" . --exclude=*.pyc --exclude=*.git* --exclude=configure.sh

echo

export LC_ALL=C
grep -rl "package_name" . --exclude=*.pyc --exclude=*.git* --exclude=configure.sh| xargs sed -i '' -e "s/package_name/$_package_name_/g"
