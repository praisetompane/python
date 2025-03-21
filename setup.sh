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
    asdf install python latest
echo "Done"

echo "Set python version"
    asdf set python latest
echo "Done"