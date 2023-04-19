# interactive semver helper
semver() {
	if [ $# -ne 0 ]; then
		echo "usage: semver"
		return 1
	fi

	if ! [ -f semver ]; then
		echo "semver not found here"
		echo "usage: semver"
		return 1
	fi

	local version="$(cat semver)"

	local selection valid_sel=0
	while [ "$valid_sel" -eq 0 ]; do
		echo "[Ctrl-c] to quit"
		echo "The previous version was $version"
		echo "Update major (M), minor (m), or patch (p)?"
		read -p ": " selection
		case "$selection" in
		M)
			local major="$( echo "$version" | pcregrep -o '(?<=v)[0-9]+' )"
			((major++))
			echo "$version" | sed "s|v[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*|v${major}\.0\.0|" > semver
			valid_sel=1
			;;
		m)
			local minor="$( echo "$version" | pcregrep -o '(?<=\.)[0-9]+(?=\.)' )"
			((minor++))
			echo "$version" | sed "s|\(v[0-9][0-9]*\)\.[0-9][0-9]*\.[0-9][0-9]*|\1\.${minor}\.0|" > semver
			valid_sel=1
			;;
		p)
			local patch="$( echo "$version" | pcregrep -o '(?<=\.)[0-9]+$' )"
			((patch++))
			echo "$version" | sed "s|\.[0-9][0-9]*$|\.${patch}|" > semver
			valid_sel=1
			;;
		*)  echo "invalid selection '${selection}'" ;;
		esac
	done

	echo "semver upgraded to $(cat semver)"
}


# git add all, commit, and push
gtac() {

	# help menu
	if [ "$1" = "-h" ] || [ "$1" = "--help" ]
	then
		>&2 echo "Please provide either 0 or 1 arguments. If 1 argument, please input the commit message in double quotes."
		return 0
	fi

	# check if git repo
	if ! git status > /dev/null 2>&1; then
		>&2 echo -e "The current folder is not a git repo."
		return 1
	fi

	# optional pull
	if ! [ "$(git status -v | sed -n "2p;" | cut -d " " -f4)" = "ahead" ]; then
		git pull
	fi
	if [ $? -ne 0 ]; then >&2 echo "git pull failed."; return 1; fi

	# add all
	git add .
	if [ $? -ne 0 ]; then >&2 echo "git add . failed."; return 1; fi

	# commit
	if [ $# -eq 0 ]; then
		git commit

	# commit with messages
	else
		local commit_flags=()
		local each_line
		for each_line in "${@}"; do
			commit_flags+=("-m")
			commit_flags+=("$each_line")
		done
		git commit "${commit_flags[@]}"
	fi
	if [ $? -ne 0 ]; then >&2 echo "git commit failed."; return 1; fi

	git diff --cached
	if [ $? -ne 0 ]; then >&2 echo "git diff --cached failed."; return 1; fi

	read -p "Would you like to push all currently staged changes? (y/n): " push_confirm
	if [ "$push_confirm" = "y" ]; then
		git push
		echo -e "All changes in this folder have been committed and pushed to the remote."
	else
		echo -e "All changes in this folder have been committed, but have not been pushed."
	fi

}

# increment semver and update with a nice message
gtver() {
	semver || return 1

	local version="$(cat semver)"
	local invalid_summary=1
	local summary
	while [ "$invalid_summary" -eq 1 ]; do
		echo "provide summary for $version"
		read -p ": " summary
		if ! [ -z "$summary" ]; then
			invalid_summary=0
		fi
	done

	local invalid_desc=1
	local desc
	while [ "$invalid_desc" -eq 1 ]; do
		echo "provide description for $version"
		read -p ": " desc
		if ! [ -z "$desc" ]; then
			invalid_desc=0
		fi
	done

	gtac "$version - $summary" "$desc"
}

gtver "$@"
