# FloraFlow

FloraFlow is a minimal-maintenance plant-watering system that can automatically water plants following three different schedules. The system is designed to not require refilling for weeks or months at a time, while also retaining and recyling nutrients through a semi-closed-loop water cycle.

The system is currently under development and is designed to hang on the eastern window railing of the MakerHub.

The system can water up to 6 plants in 3.5" x 3.5" pots arranged in a 2x3 grid. Each watering channel can take care of 2 pots. The system allows people to put their own plants here for some time of display and care. 

The goal of this project is to give people opportunities to learn about various tools around the MakerHub and to provide MakerHub with a fun installation that not only engages visitors but also inspires students to learn to use tools to build their own projects as well.

# On-boarding

To familiarize yourself with the build, go to the [design section below](https://github.com/GeorgetownMakerHubOrg/floraflow#floraflow-design) to learn about the design.

To contribute to this repository with design specifications, files, and resources, clone this repo, request edit access, and add specs to this document and files to the appropriate folder. (Consider calling `source update-version-and-push.sh` to also update the semantic versioning of this system after adding / updating any non-README file. This script does semantic version update, git pull, git add, git commit, and git push for you.)

# FloraFlow Design

Design specs last updated April 19, 2023.

To be further fleshed out.

## Resources

For resources, see [resources page](https://github.com/GeorgetownMakerHubOrg/floraflow/tree/main/resources)

## Materials Overview

The externals and internals below are all relative to the plastic Sterilite container that acts as the sump.

No special names here...

- Externals
	- Outer (probably) wooden box
	- Metal hanging contraption
- Internals
	- Waterfall pump
	- Acrylic fingered boxes
		- Waterfall reservoir
		- Inner tri-lane container
	- 3D printed parts
		- Stream diverter
		- Pot lifters (6x)
	- Microcontrollers
		- A: for waterfall pump
		- B: for stream diverter
		- B/C: for reporting to Adafruit dashboard, for reading instructions over wifi

## Design Specifications

These correspond to the main pieces.

### 1 - Outer box
- 3/4" x 4' x 4' plywood (Pascal)
- door or magnetically shut opening facing the indoor that lets you see the inside
- metal hook 2x

### 2 - FloraFalls: Waterfall reservoir + pump + controller
#### Waterfall reservoir
- Boxes.py Fewer fingers
- Boxes.py -> Adobe Illustrator adjustments -> Laser Cutting (David) -> Assembly & Gluing

#### Waterfall pump + controller
- Sonoff3 (connected to Anker hub); communicates with the ESP controller for the FloraStream via HTTP

### 3 - FloraLanes: Inner tri-lane container + pot raisers
#### Watering chambers (FloraLanes / BloomBrooks)
- boxes.py "TypeTray" specs
- don't know yet what to use to lift the container. currently, we're just using the pots themselves.

#### FlowLifts: Pot lifters
- designed in Fusion360 by Q
- see 3d obj / stl files at [FlowLift design](https://github.com/GeorgetownMakerHubOrg/floraflow/tree/main/3-FloraLanes/FlowLifts)

### 4 - FloraStream: Waterfall stream-diverter + contraption + controller
#### Stream diverter (Hydrospout) x1 (PETG)
- designed in Fusion360 by David
- see 3d obj / stl files at [Hydrospout design](https://github.com/GeorgetownMakerHubOrg/floraflow/tree/main/4-FloraStream/Hydrospout)

##### (subcomponent) belt contraption
- designed in Fusion360 by David
- see 3d obj / stl files at Hydrospout design (same as for Hydrospout)
- belt clamp x1 (PETG)

#### servo + controller
- TMC2208 (see folder for pin usage suggestion)
- 12volt power for the stepper motor: 
	- Adafruit protoboard, female connector 
	- power jack plug adapter

# Timeline
|date|component(s) to design / build OR goal for next time|skills involved OR task delegation|
|---|---|---|
|2023-04-19|improve Hydrospout design & design belt holder|Fusion360|
|2023-04-19|set up initial stepper motor control via ESP|circuitry, ESP micropython REPL|
|2023-04-19|prioritize completing physical prototype and leave software for later, prepare for protoboard integration for stepper motor control, prepare for waterfall reservoir + hydrospout integration|practice running stepper motor script, practice acrylic gluing, finalize hydrospout design, learn MQTT and HTTP and how to run them on ESP|
|2023-04-26|construct exterior box (excluding front-facing wall)|woodworking: track saw, pocket hole drilling|
|2023-04-26|understand how to operate Micropython REPL and files|Micropython REPL|
|2023-04-27|print pot raisers|Fusion360, 3D printer|
|2023-04-27|figure out Micropython web server and posting to Sonoff|learning Python modules: network, socket, urequests, etc.; learning how to read Micropython manual|
