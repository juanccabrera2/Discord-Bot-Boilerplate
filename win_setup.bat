:: Check if virtual environment is set up for this project ::
if exist ".\venv\" (
    :: Virtual environment is present ::
    echo "Virtual environment detected."
) else (
    :: Virtual environment is not present ::
    echo "Creating virtual environment."
    call virtualenv venv
)
echo "Activating environment."
call .\venv\Scripts\activate
echo "Upgrading environment package manager."
call python -m pip install --upgrade pip
echo "Installing dependencies."
if exist ".\requirements.txt" (
	:: Requirements file is present ::
	call pip install -r requirements.txt
	set /p="Setup finished. Press ENTER key to exit..."
) else (
	:: Requirements file is not present ::
	echo "ERROR: Could not locate requirements.txt file to install dependencies."
	set /p="Press ENTER key to exit..."
)