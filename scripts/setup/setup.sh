#
# WIP - NOT FULLY FUNCTIONAL OR TESTED
#

# On Mac - install Pyenv and openssl3
if [[ "$OSTYPE" == "darwin"* ]]; then
  echo "Mac detected"

  brew install openssl@3

  export LDFLAGS="-L$(brew --prefix openssl@3)/lib"
  export CPPFLAGS="-I$(brew --prefix openssl@3)/include"
  export PKG_CONFIG_PATH="$(brew --prefix openssl@3)/lib/pkgconfig"

  brew install pyenv

# On Linux - install GH CLI
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
  echo "Linux/WSL detected"

  # Install pyenv and openssl on Windows
  sudo apt update
  sudo apt upgrade

  # Install dependencies for pyenv and openssl
  sudo apt install -y make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
    libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev \
    liblzma-dev python3-openssl

  # Install pyenv
  curl https://pyenv.run | bash

  # Add pyenv to bash so that it loads every time you open a terminal
  grep -qxF 'export PYENV_ROOT="$HOME/.pyenv"' ~/.bashrc || echo ''
  grep -qxF 'export PYENV_ROOT="$HOME/.pyenv"' ~/.bashrc || echo '# Set up pyenv'
  grep -qxF 'export PYENV_ROOT="$HOME/.pyenv"' ~/.bashrc || echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
  grep -qxF 'export PATH="$PYENV_ROOT/bin:$PATH"' ~/.bashrc || echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
  grep -qxF 'eval "$(pyenv init --path)"' ~/.bashrc || echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
  grep -qxF 'eval "$(pyenv init -)"' ~/.bashrc || echo 'eval "$(pyenv init -)"' >> ~/.bashrc

  # Run the commands to add pyenv to the current shell
  export PYENV_ROOT="$HOME/.pyenv"
  export PATH="$PYENV_ROOT/bin:$PATH"
  eval "$(pyenv init --path)"
  eval "$(pyenv init -)"
fi

# Install Python 3.13.1 with Pyenv, and initialize it
pyenv install 3.13.1
eval "$(pyenv init --path)"

# Create a virtual environment in ospf project, and activate it
python -m venv venv
source ./venv/bin/activate

# Install python dependencies
pip3 install -r requirements.txt
