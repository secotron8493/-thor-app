name: Build THOR APK

on:
  push:
    branches: [ main ]
  workflow_dispatch:

jobs:
  build-apk:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Setup Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'

    - name: Install system dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y \
          openjdk-17-jdk \
          build-essential \
          git \
          zip \
          unzip \
          autoconf \
          libtool \
          pkg-config \
          zlib1g-dev \
          libncurses5-dev \
          libncursesw5-dev

    - name: Create Android SDK directory
      run: mkdir -p /home/runner/android-sdk

    - name: Install Android SDK + API 30
      run: |
        wget https://dl.google.com/android/repository/commandlinetools-linux-9477386_latest.zip -O sdk.zip
        unzip sdk.zip -d /home/runner/android-sdk/
        yes | /home/runner/android-sdk/cmdline-tools/bin/sdkmanager --sdk_root=/home/runner/android-sdk "platforms;android-30" "build-tools;30.0.3"

    - name: Setup environment paths
      run: |
        echo "ANDROIDSDK=/home/runner/android-sdk" >> $GITHUB_ENV
        echo "ANDROIDSDK_HOME=/home/runner/android-sdk" >> $GITHUB_ENV
        echo "/home/runner/android-sdk/platform-tools" >> $GITHUB_PATH

    - name: Install Buildozer
      run: |
        pip install buildozer cython==0.29.36

    - name: Build APK
      run: |
        buildozer android debug

    - name: Upload APK
      uses: actions/upload-artifact@v4
      with:
        name: thor-apk
        path: bin/*.apk
        retention-days: 30

