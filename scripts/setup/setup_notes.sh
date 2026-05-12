brew install openssl@3

export LDFLAGS="-L$(brew --prefix openssl@3)/lib"
export CPPFLAGS="-I$(brew --prefix openssl@3)/include"
export PKG_CONFIG_PATH="$(brew --prefix openssl@3)/lib/pkgconfig"

pyenv install 3.13.1

eval "$(pyenv init --path)"

python -m venv venv
source ./venv/bin/activate

pip3 install -r requirements.txt

#### WSL2 SETUP STEPS ####
wsl --set-default-version 2
wsl --install -d Ubuntu
wsl --setdefault Ubuntu
sudo apt update
sudo apt upgrade

# Check if git is installed. Run:
git --version

# It should work and not produce an error if it is. If not, run
sudo apt-get install git -y

# If it's present, install GH CLI. Run:
(type -p wget >/dev/null || (sudo apt update && sudo apt-get install wget -y)) \
	&& sudo mkdir -p -m 755 /etc/apt/keyrings \
  && out=$(mktemp) && wget -nv -O$out https://cli.github.com/packages/githubcli-archive-keyring.gpg \
  && cat $out | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null \
	&& sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
	&& echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
	&& sudo apt update \
	&& sudo apt install gh -y

# Create a projects folder for code:
mkdir ./projects

# Navigate to the projects folder:
cd ./projects

# Run this set of commands to grab the repo:
gh repo clone OpenSourcePharmaFoundation/ospf-ayurveda-kg

#### MORE SETUP STEPS ####
# Visit \\wsl$\Ubuntu\home\<insert-username-here> in windows explorer
# Bookmark this location in your file explorer for easy access in the future
#  - i.e. add to Quick Links by navigating back

# Make a note of this somewhere:
#  /mnt/c/Users/ (that's the Windows drive location from WSL)


#### TODOs ####
# - ! Set Ubuntu as the default Windows terminal environment
# - ! Pull the repo
# - ! Get VS Code
# - Get github set up

