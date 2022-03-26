@echo off
nuitka --windows-company-name=BrailleScreen --windows-product-name="Markovify Test" --windows-file-version=1.0 --windows-product-version=1.0 --windows-file-description="Markovify Testing" --standalone --python-flag=no_site --remove-output --onefile main.py
pause > nul
