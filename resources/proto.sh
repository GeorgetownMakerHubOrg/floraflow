# source this file to load a few useful ESP interface helper functions grouped under the function name 'ei' (change 'ei' to something else if it collides with an existing command. You can check whether it collides by typing `type ei` and seeing if you get anything.)

ei() {
	_ei_usage() {
		cat <<EOF

  ei: ESP board interface helper. 
    automatically detects the tty device to the ESP board and connects via this port.

  usage: ei <option>

  <option>s:
    h | help               - help menu
    cs                     - ESP interface cheatsheet (such as how to use screen)
    s | screen | go        - connect to ESP board via screen
    a | ampy <cmd> <args>  - connect to ESP board via ampy

  <cmd>s: all the ampy commands. add <args> as appropriate.
    get    Retrieve a file from the board.
    ls     List contents of a directory on the board.
    mkdir  Create a directory on the board.
    put    Put a file or folder and its contents on the board.
    reset  Perform soft reset/reboot of the board.
    rm     Remove a file from the board.
    rmdir  Forcefully remove a folder and all its children from the board.
    run    Run a script and print its output.

EOF
	}

	_ei_cheatsheet() {
		cat <<EOF
  cheat sheet for screen to ESP:

    to see help         help()
    to navigate         import os; 
                        os.listdir(); 
                        os.chdir('dirname');
    to paste some script to run directly via command line
                        <Ctrl-e>, <Ctrl-v> & other things as necessary, <Ctrl-e>
    to run an existing path/to/script.py script file
                        import path/to/script
    to quit screen      <Ctrl-a>, k, y


EOF
	}

	_ei_err() {
		>&2 printf "${FUNCNAME[1]}():"
		local each_arg
		for each_arg in "$@"; do
			>&2 echo -e "    $each_arg"
		done
	}

	_ei_detect_port() {
		local esp_port="$(ls /dev/tty* | grep 'usb')"
		local confirmation
		>&2 echo "going to port '${esp_port}'"
		read -p "confirm? y/n: " confirmation
		case "$confirmation" in
		y|yes) echo "$esp_port" ;;
		*) return 1 ;;
		esac
	}

	local port
	case "$1" in
	""|h|help) _ei_usage ;;
	cs) _ei_cheatsheet ;;
	a|ampy)
		if [ -z "$2" ]; then _ei_err "Missing ampy command."; _ei_usage; return 1; fi
		port="$(_ei_detect_port)"
		if [ $? -ne 0 ]; then _ei_err "Quit."; return 1; fi
		if [ -z "$port" ]; then _ei_err "No usb port found."; return 1; fi
		ampy -p "$port" "${@:2}"
		;;
	s|screen|go)
		port="$(_ei_detect_port)"
		if [ $? -ne 0 ]; then _ei_err "Quit."; return 1; fi
		if [ -z "$port" ]; then _ei_err "No usb port found."; return 1; fi
		screen "$port" 115200
		;;
	*) _ei_err "The option ${1} is unknown."; _ei_usage; return 1 ;;
	esac
}

