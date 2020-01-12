# install oh-my-zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# install figlet and neofetch
sudo apt install figlet && sudo apt install neofetch

# Create symlink in home directory
ln -s /path/to/custom-linux-config/zsh-custom/.zshrc .zshrc

# If its not working, check ZSH and ZSH_CUSTOM env path in .zshrc
# * need to write an install script
# Need to add support for python venv, breaks bash prompt, aliases

# Add comment generator script
