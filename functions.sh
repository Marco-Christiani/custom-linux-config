#!/bin/bash
CHECK_MARK="\033[0;32m\xE2\x9C\x94\033[0m"
CLR_RT='\033[0K' # Clear everything to right of cursor

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
    # printf  "\n\033[4mUpdating:\033[0m\n"
    printf "\nUpdating Homebrew package index\n"
    
    output=`brew update`

    printf "\\r${CLR_RT}${CHECK_MARK} Homebrew package index updated:\n"
    printf $output
    printf "\n"

    printf "\nQuerying upgradable packages"
    output=`brew outdated && brew cask outdated 2>&1`
    # output=`echo $output| sed 's/^/  /'` # Gets rid of version number, idky I did that lol
    printf "\\r${CHECK_MARK} Queried upgradable packages"
    
    printf "\nThe following packages can be upgraded:\n"
    printf "${output}" 
    printf "\n"

    if ask "Continue with upgrades?"; then
        printf "\n\033[32mUpgrading packages\033[39m\n\n"
        brew upgrade && brew cask upgrade
        printf "\n"
    else
        printf "Exiting without upgrading.\n"
    fi

}

