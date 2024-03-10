echo "adding asdf python plugin"
asdf plugin add python
echo "done"

ostype="$(uname -s)"
if [ "$ostype" = "Linux" ]; then 
    echo "install openssl dependecy"
    sudo apt install libedit-dev
    echo "done"
fi

echo "installing python"
asdf install python latest
echo "done"

echo "set latest version to system wide version"
asdf global python latest
echo "done"

echo "installing pipenv"
brew install pipenv
echo "done"

echo "installing system level Black in python"
pip3 install black
echo "done"

echo "installig Tk interface"
brew install python-tk
echo "done"
