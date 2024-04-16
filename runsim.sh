#!/bin/sh
# Set the environment variables

usage() {
    echo "Usage: $0 <platform> <device>"
    echo "\texample: $0 ios \"iPhone-8\""
    echo "\texample: $0 android \"emulator-5554\""
    echo "\trun 'xcrun simctl list devices' to see available devices (IOS)" 
  exit $1
}

if [ $# -ne 2 ]; then
    usage 1
fi

export BONSAI_PLATFORM=$1
export BONSAI_DEVICE=$2

cd ./app

if [ "$BONSAI_PLATFORM" = "ios" ]; then
    echo "Running on IOS"
    npx react-native run-ios --simulator="$BONSAI_DEVICE"
elif [ "$BONSAI_PLATFORM" = "android" ]; then
    echo "Running on Android"
    npx react-native run-android
else
    echo "Invalid platform"
    usage 1
fi

