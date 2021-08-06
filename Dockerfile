FROM quamotion/appium-docker-ios

# Create app directory
WORKDIR /usr/src/app

COPY . .

RUN sudo apt-get install -y usbmuxd libimobiledevice-utils
