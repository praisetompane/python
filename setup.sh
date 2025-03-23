VERSION="3.13.2"
echo "Adding asdf python plugin"
    asdf plugin add python
echo "Done"

ostype="$(uname -s)"
if [ "$ostype" = "Linux" ]; then
    echo "Install openssl dependency"
    sudo apt install libedit2
    echo "Done"
fi

echo "Installing python"
    asdf install python $VERSION
echo "Done"

echo "Set python version"
    asdf set python $VERSION
echo "Done"

echo "Install pipenv"
    pip install pipenv --user
echo "Done"

echo "Adding user binaries to system path"
    echo 'export PATH="$PATH:~/.local/bin"' >> ~/.zshrc
echo "Done"