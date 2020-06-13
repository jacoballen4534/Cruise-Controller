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

# Setting Up The Files

1. Create a folder for the source files to be located.  
   The path to this folder will be referred to as <path/to/project>

2. Place the root of the project (cs723-as2) in <path/to/project>

# Prerequisites

- Esterel (tested using Esterel V5)
- A terminal
- Python3 (only required for running tests)

Note: This has only been tested on Ubuntu 18.0 and the UoA Flex.it linux machine.

# Building and Running the Project

1. Open a terminal

2. Navigate to <path/to/project>/cs723-as2 directory.

3. Run the command `./build.sh` to build and start the program.  
   Note: This will create a new folder at <path/to/project>/cs723-as2/Build

4. Enter various inputs via the Esterel GUI.

# Running the tests

This test suite will use the inputs from <path/to/project>/cs723-as2/Test/vectors.in and compare the results to <path/to/project>/cs723-as2/Test/vectors.out.

1. Open a terminal

2. Navigate to <path/to/project>/cs723-as2 directory.

3. Run the command `./test.sh` to build and start the test suite.  
   Note: This will create a new folder at <path/to/project>/cs723-as2/Build_For_Tests

4. Select a test option (1 for individual tests, 2 for all tests)
