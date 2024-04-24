#!/bin/sh

# make sure yarn is installed

cd ./app


usage() {
    echo "Usage: $0 <platform>"
    echo "\texample: $0 ios"
    echo "\texample: $0 android"
  exit $1
}

if [ $# -ne 1 ]; then
    usage 1
fi


if ! command -v npx &> /dev/null
then
    echo "npx could not be found"
    cd ../
    exit
fi


if ! command -v yarn &> /dev/null
then
    echo "yarn could not be found"
    cd ../
    exit
fi

# install dependencies
yarn install

export BONSAI_PLATFORM=$1

if [ "$BONSAI_PLATFORM" = "ios" ];
then
    cd ./ios && pod install && cd ..
fi

cd ../

echo "Run \"./runsim.sh\" and follow the instructions to run the app" 