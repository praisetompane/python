echo "Adding asdf python plugin"
    asdf plugin add python
echo "Done"

ostype="$(uname -s)"
if [ "$ostype" = "Linux" ]; then
    echo "install openssl dependency"
    sudo apt install libedit-dev
    echo "Done"
fi

echo "Installing python"
    asdf install python latest
echo "Done"

echo "Set latest version to system wide version"
    asdf global python latest
echo "Done"

echo "Installing pipenv"
    brew install pipenv
echo "Done"

echo "installing system level Black in python"
    pip3 install black
echo "Done"
