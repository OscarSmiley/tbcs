# Mission Control Overview

This is a description and brief guide to a control module being developed for AUVIC. This control module is intended to run as a node in the ROS environment, where it will combine sensor information and make navigation decisions for an autonomous underwater vehicle

### Programming Decisions
This module is primarily written in python. The decision to use python in this module was based on several factors:

* The python interpreter and rospy should give us acceptable performance for this task.

* Although python is not staticly typed it is strongly typed. Variable types are not declared on initialization, like in C++ or Java, but are restricted in their intermingling by the interpreter. The lack of static typing can be overcome with proper development practices.

* As we currently have limited access to our hardware, and are working with members that are not living in Victoria, using the interpreter as an added layer of abstraction and for memory management will hopefully ease testing and debugging.

* Finally, Python is taught to more students earlier at the University of Victoria than C++, and is simply easier for new programmers to work with.

Additionally, ROS allows mixed python scripts and C++ compiled binaries in ROS nodes. So using python now doesn't exclude us from writing C++ code in the future.

This module is created around a finite state machine (fsm) using an in-processor to convert sensor information to a standard input language and an out-processor to generate navigation instructions.

### FSM
The 'finite state machine' is similar to the classic deterministic finite state machine algorithms used for tasks like pattern matching. However, the state shifting criteria are expanded to include a large set of parameters, and a record of previous inputs in a "history" object. In this module the fsm functions more as an overseer of its state objects. The state objects are left to do the hard work generating output.

Although not strictly part of a finite state machine, the history object allows the fsm to store finer-detail information on how it arrived at it's current state. In addition to having moved through a possible combination of other states, current state methods can account for the physical parameters that cased the fsm to follow a sequence of states.


### States
States are used to represent the mode of the control module, and compute the the output. The fsm starts an iteration by passing a current set of parameters to the current state, expecting it to return the next state. After which the current state uses internal methods to determine the next state and returns the next state object. The next state may be the current state. The fsm replaces the current state with the next state, and asks the new current state to generate output. Finally, the current state uses internal methods on the parameters passed earlier to generate output from the fsm.

### In/Out processors
These objects act as a layer of abstraction between the fsm and ROS messages. The in-processor converts ROS messages from nodes such as computer vision to a standard input language for the fsm. Likewise the out-processor will convert the output language of the fsm to a navigation request.

### Testing Scripts
There are several testing scrips and test data files that can be used to test the module. These are usually located in a test directory. As of now the fsmControler can run without a test script using is the filePreProcessor that has been added to the src folder. This pre-processor reads values line by line from a file. Files are passed to the fsmControler as command line arguments. Each ';' delimited line of the file represents a set of input parameters.  
