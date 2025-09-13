python setup.py sdist bdist_wheel
Write-Output "Setup/Build done"

Set-Location dist
pip install cli_chess-1.4.3-py3-none-any.whl
Write-Output "Installed cli-chess"

Set-Location ..
Write-Output "Run cli-chess to start"
