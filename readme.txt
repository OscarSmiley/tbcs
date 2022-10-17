How to start this thing:
	1) Start roscore in one terminal window
	2) Start various publisher nodes
	3) Start reviever nodes (not implemented yet)
	4) Run `$ rosrun fsm FsmController.py  <path to state scripts from control_system/> <path to io.txt from control_system/>` 
		ex: `$ rosrun fsm FsmController.py /src/fsm/scripts/stateScripts /src/fsm/io.txt`
	5) Profit
