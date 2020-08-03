# export PYTHONPATH=/usr/local/bin/python3 # python3 as default python version DOESNT WORK
export PATH=$PATH:$HOME/Library/Python/3.8/bin # add python 3.8 to path
export GPG_TTY=$(tty) # Add GPG stuff for git commit signing to work
export PATH=$PATH:$GPG_TTY} # GPG

# Path to your oh-my-zsh installation.
export ZSH="$HOME/.oh-my-zsh"

ZSH_CUSTOM=$HOME/Documents/Github/custom-linux-config/zsh-custom
ZSH_THEME="avit-custom"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Which plugins would you like to load?
# Standard plugins can be found in ~/.oh-my-zsh/plugins/*
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git)

source $ZSH/oh-my-zsh.sh

# Display welcome screen ------------------------------------------------------------------------
figlet -w `tput cols` `date '+%b %d %Y'`
neofetch

# Preferred editor for local and remote sessions
if [[ -n $SSH_CONNECTION ]]; then
  export EDITOR='nano'
else
  export EDITOR='subl'
fi
local pathtome="$(dirname $(readlink ~/.zshrc))"
source $pathtome/functions.sh # Load custom functions (follow ~/.zshrc symlink to wherever this file is)

# Uncomment the following line to display red dots whilst waiting for completion.
COMPLETION_WAITING_DOTS="true"

# Custom Aliases ------------------------------------------------------------------------
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"
alias hg="history | grep"
alias gf="grep -B 1 -A 5 --color=auto" # Grep files. Highlight match, show 1 precending and 5 succeeding lines surrounding match
alias comgen="python3 ~/Documents/Programming_Personal/PrettyComments/comgen.py" # My pretty-comment generator
alias ls="ll -Fpl"
# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# export MANPATH="/usr/local/man:$MANPATH"


test -e "${HOME}/.iterm2_shell_integration.zsh" && source "${HOME}/.iterm2_shell_integration.zsh"

