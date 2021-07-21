pyinstaller -F -w start.py

copy .\dist
del /Q dist
rmdir /Q dist
del /Q build\start
rmdir /Q build\start
rmdir /Q build
del /Q start.spec
del /Q __pycache__
rmdir /Q __pycache__