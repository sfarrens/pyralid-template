#!/bin/bash

echo "Please specify your package name:"

read -p "> " _package_name_

echo

echo "'package_name' will be updated to '$_package_name_' in the following files:"

ls ./package_name
grep -rl "package_name" . --exclude=*.pyc --exclude=*.git* --exclude=configure.sh

echo

echo "Are you sure you want to update these files to $_package_name_?"

read -p "> [y/N]: " _response_

echo

_response_=${_response_:-"n"}

if [ "$_response_" != "Y"  ] && [ "$_response_" != "y"  ]; then
  echo "Better start over!"
  exit 1
fi

export LC_ALL=C
mv ./package_name ./$_package_name_
grep -rl "package_name" . --exclude=*.pyc --exclude=*.git* --exclude=configure.sh| xargs sed -i '' -e "s/package_name/$_package_name_/g"
