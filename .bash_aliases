# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

alias rebash="source ~/.bashrc"
alias python='printf "\033[00;36m" && python -ttB'
alias python3='printf "\033[00;32m" && python3 -ttB'

cd () {
	builtin cd "$@" && ls
}

cleanhome () {
    find ~ -type f -name "*~" -delete
    find ~ -type f -name "*.pyc" -delete
}
