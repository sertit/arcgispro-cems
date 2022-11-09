@echo on
SET anaconda_powershell=%windir%\System32\WindowsPowerShell\v1.0\powershell.exe
SET conda_hook=%userprofile%\Anaconda3\shell\condabin\conda-hook.ps1

IF NOT EXIST %conda_hook% (
    SET conda_hook=%userprofile%\AppData\Local\Continuum\anaconda3\shell\condabin\conda-hook.ps1
)

SET tools_arcgis_pro=".."

SET cli="%conda_hook% ;"^
 "conda activate arcgispro-cems;"^
 "pytest CI\test.py --capture=tee-sys --disable-warnings;"^
 "pytest %tools_arcgis_pro%\water-depth-dem --capture=tee-sys --disable-warnings;"

%anaconda_powershell% -NoProfile -ExecutionPolicy Bypass -Command^
 "& {Start-Process %anaconda_powershell% -ArgumentList '-ExecutionPolicy ByPass -NoExit -Command %cli%'};