## Assumptions Made

- The brief does not explicitly state the expected behaviour of the ThrottleCmd when in the STDBY and DISABLE states.

  We assume that the ThrottleCmd should reflect the Accel when in the STDBY or DISABLE state as this is what we would expect to happen in a real car.

- The brief states that the cruise speed shall be set to the current speed when the On button is pressed initially.
  We assume this includes every time the cruise controller is turned OFF and back ON again. IE Every transition from OFF to ON will set the cruise speed to the current speed.

- There were no pre-defined representation of the cruise state (OFF, ON, STDBY, DISABLE).  
  We have used the following mapping.  
  OFF = 0  
  ON = 1  
  STDBY = 2  
  DISABLE = 3

- The brief states that "The cruise control shall go on when the on button (On) is pressed. The output CruiseState should be set to ON." however, also states that "The cruise control shall be immediately interrupted and should enter the standby state, when the brake (Brake) is pressed. The output CruiseState shall be set to STDBY."  
  We assume that the first statement takes priority, therefore if the cruise controller is turned on with the brake pressed. The cruise state will go to ON and then to STDBY on the next tick.

# Setting Up The Files

1. Create a folder for the source files to be located.  
   The path to this folder will be referred to as <path/to/project>

2. Place the root of the project (submission) in <path/to/project>

# Prerequisites

- Esterel (tested using Esterel V5.91)
- A terminal
- Python3 (only required for running tests)

Note: This has only been tested on Ubuntu 18.04 and the UoA Flex.it linux machine.

# Building and Running the Project

1. Open a terminal

2. Navigate to <path/to/project>/submission directory.

3. Run the command `./build.sh` to build and start the program.  
   Note: This will create a new folder at <path/to/project>/submission/Build

4. Enter various inputs via the Esterel GUI.

# Running the tests

The original automated testing script was written by Feneel Sanghavi, and has been modified to match our implementation. We do not claim ownership of this script, which has been used purely for testing post-development.

This test suite will use the inputs from <path/to/project>/submission/Test/vectors.in and compare the results to <path/to/project>/submission/Test/vectors.out.

1. Open a terminal

2. Navigate to <path/to/project>/submission directory.

3. Run the command `./test.sh` to build and start the test suite.  
   Note: This will create a new folder at <path/to/project>/submission/Build_For_Tests

4. Select a test option (1 for individual tests, 2 for all tests)

# Common Issues

Sometimes when moving the project between Windows and Ubuntu, some files might have incorrect line endings (CRLF) causing the bash scripts to fail.
If encountered, replace line endings from within VS Code (or your favourite text editor) to be just LF.
