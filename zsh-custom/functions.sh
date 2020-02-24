#!/bin/bash
# This is a general-purpose function to ask Yes/No questions in Bash, either
# with or without a default answer. It keeps repeating the question until it
# gets a valid answer.

ask() {
    # https://djm.me/ask
    local prompt default reply

    if [ "${2:-}" = "Y" ]; then
        prompt="Y/n"
        default=Y
    elif [ "${2:-}" = "N" ]; then
        prompt="y/N"
        default=N
    else
        prompt="y/n"
        default=
    fi

    while true; do

        # Ask the question (not using "read -p" as it uses stderr not stdout)
        echo -n "$1 [$prompt] "

        # Read the answer (use /dev/tty in case stdin is redirected from somewhere else)
        read reply </dev/tty

        # Default?
        if [ -z "$reply" ]; then
            reply=$default
        fi

        # Check if the reply is valid
        case "$reply" in
            Y*|y*) return 0 ;;
            N*|n*) return 1 ;;
        esac

    done
}

function loading_spinner(){
    # Gets pid of last call, starts spinning until that process ends
    # Requires suppression of command output
    pid=$1 # Process Id of the previous running command
    spin='-\|/'
    i=0

    while kill -0 $pid 2>/dev/null
    do
      i=$(( (i+1) %4 ))
      printf "${spin:$i:1}" 
      sleep .1
      printf "\033[1D" # Move cursor back 1
    done
}

function start_spinner(){
    # Does not require suppression of output
    spin="-\|/"
    i=0
    while :
    do
      i=$(( (i+1) %4 ))
      printf "${spin:$i:1}" 
      sleep .1
      printf "\033[1D" # Move cursor back 1
    done
}
function cd() { # Automatically ls after cd
    new_directory="$*";
    if [ $# -eq 0 ]; then 
        new_directory=${HOME}; # If no path for cd, defaults to ~ (home dir)
    fi;
    builtin cd "${new_directory}" && ls
}
function sflag() { # Search man entry for flag
    LESS=+/^[[:blank:]]+"-$2" man "$1" ;
}

# Update homebrew package index, then upgrade all packages and apps (cask)
function update(){
    printf "Updating Homebrew package index...\n"
    # read<<( brew update & echo $! )
    # loading_spinner $REPLY # Spinner with output suppression
    echo `brew update`

    printf "Querying upgradable packages...\n"
    echo `brew outdated && brew cask outdated`

    if ask "Continue with upgrades?"; then
    echo `brew upgrade && brew cask upgrade`
    else
        echo "No"
    fi
}