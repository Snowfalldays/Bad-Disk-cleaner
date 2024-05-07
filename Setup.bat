@Echo off
:: check if pip and python are installed if not exit!
python3 --version 3>NUL
if errorlevel 1 goto errorNoPython

pip3 --version 3>NUL
if errorlevel 1 goto errorNoPip


Echo "Aight bet"
Echo "Installing pip modules needed for this scirpt!"
:: Install all needed python modules!
pip3 install humanize
pip3 install pathlib

python %cd%\main.py


:errorNoPip
Echo "Please do make sure that pip3 is indeed installed before running this program!"
Echo "Exitting!"


:errorNoPython
Echo "You do not have python3 installed!"
Echo "Please do install python3 before using this program!"
Echo "Exitting"
