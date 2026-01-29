@echo off
echo ========================================
echo  HelpDesk Info - Demarrage
echo ========================================
echo.

REM Verification de Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERREUR: Python n'est pas installe ou n'est pas dans le PATH
    echo Telechargez Python depuis https://www.python.org/
    pause
    exit /b 1
)

echo [1/3] Verification de l'environnement...

REM Verification de l'environnement virtuel
if not exist "venv\" (
    echo [INFO] Creation de l'environnement virtuel...
    python -m venv venv
    if errorlevel 1 (
        echo ERREUR: Impossible de creer l'environnement virtuel
        pause
        exit /b 1
    )
)

echo [2/3] Activation de l'environnement virtuel...
call venv\Scripts\activate.bat

REM Installation des dependances
echo [3/3] Verification des dependances...
pip install -q -r requirements.txt
if errorlevel 1 (
    echo ERREUR: Impossible d'installer les dependances
    pause
    exit /b 1
)

echo.
echo ========================================
echo  Lancement de HelpDesk Info
echo ========================================
echo.
echo L'application va s'ouvrir dans votre navigateur...
echo Appuyez sur Ctrl+C pour arreter le serveur
echo.

REM Lancement de l'application
python main.py

pause
