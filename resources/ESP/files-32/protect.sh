# protect ssid & passwords
protect_file() {
	local protectfile="$1"
	echo "protecting file '$protectfile'..."
	local tmpfile=$(mktemp)
	cat "$protectfile" |
	sed "s|^\(.*SSID[ ]*=[ ]*\).*$|\1'default_ssid'|" |
	sed "s|^\(.*PASSWORD[ ]*=[ ]*\).*$|\1'default_password'|" |
	sed "s|^\(.*USER[ ]*=[ ]*\).*$|\1'default_user'|" |
	sed "s|^\(.*IFTTT_KEY[ ]*=[ ]*\).*$|\1'default_ifttt_key'|" |
	cat > "$tmpfile"
	mv "$tmpfile" "$protectfile"
	echo "file protected: "
	cat "$protectfile"
}

protect_file config.py
