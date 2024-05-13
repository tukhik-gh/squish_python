# squish_python
Squish automation test for qt android application in python.

## Prerequisites
Before you begin, ensure you have met the following requirements:

* Python3 installed on your system.
* Android Studio installed 
* JDK installed
* Qt installed and has a certificate
* Squish installed and has a certoficate

## Installation for Ubuntu
#### Step 1 : Install Java in your system.

```sh
  sudo apt update
  ```
```sh
  sudo apt install openjdk-11-jdk
  ```
```sh
  sudo apt install openjdk-11-jdk
  ```
```sh
  java -version
  ```
#### Step 2: – Install Android Studio in your system.apt update
  * Open the “ubuntu software” application in your system.
  * Search “Android Studio”.
  ![image](https://github.com/tukhik-gh/appium-python/assets/135021391/511074b8-abbc-4b43-858a-7c5fae946a42)
  * Select the first one and click on the “Install” button.
  * Follow the instructions described in the settings <a href="https://aurigait.com/blog/how-to-setup-appium-in-ubuntu/">link</a>.

#### Step 3 :- Installing QT 
 * Download QT from  <a href="https://www.qt.io/download">here</a>
   - [ ] Click "Download QT for Ubuntu"
   - [ ] Fill out the form
         An example you can see in the photo ![image](https://github.com/tukhik-gh/squish_python/assets/135021391/509a1f9b-ef55-4ac9-966f-7a2ea0abf69c)
         
    - [ ] Click the "Download unverified file"  ![image](https://github.com/tukhik-gh/squish_python/assets/135021391/fce37b80-a3c1-4b38-acef-459d9ca20c0a)
    - [ ] Make downloaded file executable
    - [ ] In “Downloads”, find the downloaded file and install.

   
#### Step 4 :- Installing Squish.
 * Download Squish
 * Install
 * Get Licensed

## Usage
* Run Android Studio 
    - [ ]  Create device
          ![image](https://github.com/tukhik-gh/appium-python/assets/135021391/ca159520-495b-49d5-881f-bd9b069fe8eb)
* OR connect android device

* Open Squish
    - [ ] File --> create test suit
    - [ ] Cuis Android --> python --> select apk file, select divice
    - [ ] Create the new suit
    - [ ] Run recording
 
  * Notes:
     Sometimes we get this error when we want to start recording: ![image](https://github.com/tukhik-gh/squish_python/assets/135021391/5092b947-6923-4c16-9321-b609df6ceb72).
    
      There may be several reasons.
    - First: the CT and Sushi versions must match, as shown in this graph.![image](https://github.com/tukhik-gh/squish_python/assets/135021391/abe8b8f4-9ea3-4ec9-997d-02b5ccec867a)
    - Second: After installing the Squish, sometimes a small window opens, showing a problem with the installation. We have to be careful and not ignore it

  




