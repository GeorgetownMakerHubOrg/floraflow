# FloraFlow

FloraFlow is a minimal-maintenance plant-watering system that can automatically water plants following three different schedules. The system is designed to not require refilling for weeks or months at a time, while also retaining and recyling nutrients through a semi-closed-loop water cycle.

The system is currently under development and is designed to hang on the eastern window railing of the MakerHub.

The system can water up to 6 plants in 3.5" x 3.5" pots arranged in a 2x3 grid. Each watering channel can take care of 2 pots. The system allows people to put their own plants here for some time of display and care. 

The goal of this project is to give people opportunities to learn about various tools around the MakerHub and to provide MakerHub with a fun installation that not only engages visitors but also inspires students to learn to use tools to build their own projects as well.

# On-boarding

At our first meeting, we will first introduce the project and its motivations, then go over each component and the skills and tools that it teaches, so people know what they want to learn. We'll also present a (pretty packed) timeline for building the project, step by step. You can sign up (please sign up!) then show up during that build session and come to learn how that step is done and/or to participate in the build itself.

To familiarize yourself with the build, go to the [design section below](https://github.com/GeorgetownMakerHubOrg/floraflow#floraflow-design) to first learn about the design, then go to the [timeline](https://github.com/GeorgetownMakerHubOrg/floraflow#timeline) to see which build sessions you are interested in attending to learn and/or participate in the build. 

A note on team organization: I made the deliberate choice not to divide the build effort into smaller teams. For one, this project is on a tight timeline to finish before the semester ends, so we want more action, less hierarchy. Second, I think the MVP scope is small enough not to require people to spend a lot of time focusing on one thing. Third, I don't want people to be arbitrarily siloed, but would love for anyone who wishes so to be able to learn multiple engineering tools through this project.

# FloraFlow Design

Design specs last updated April 10, 2023.

## Resources

- Box generator: [Boxes.py](https://festi.info/boxes.py/)

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

These roughly correspond to the build teams.

### 1 - Outer box
- 3/4" x 4' x 4' plywood (Pascal)

### 2 - FloraFalls: Waterfall reservoir + pump + controller
#### Waterfall reservoir

#### Waterfall pump + controller

### 3 - FloraLanes: Inner tri-lane container + pot raisers
#### Watering chambers (FloraLanes / BloomBrooks)
- boxes.py "TypeTray" specs (David)

#### FlowLifts: Pot lifters
- see 3d STL files at [FlowLift design]
- see Fusion360 shared file [here (inactive)]()

### 4 - FloraStream: Waterfall stream-diverter + contraption + controller
#### Stream diverter (HydroSpout) x1 (PETG)

#### servo + controller
- TMC2208 (see folder for pin usage suggestion)
- 12volt power for the stepper motor: 
	- Adafruit protoboard, female connector 
	- power jack plug adapter

#### belt contraption
- belt clamp x1 (PETG)
- Gear system options:
	- [OpenSCAD gear](https://github.com/dpellegr/PolyGear)
	- [English version of the above](https://github.com/chrisspen/gears)

# Timeline
|date|build session number|component to build|skills involved|
|---|---|---|---|
|2023-04-19|1|component|skills|
