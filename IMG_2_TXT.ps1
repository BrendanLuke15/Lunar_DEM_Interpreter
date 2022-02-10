# By: Brendan Luke
# Date: February 9, 2022
# Purpose: Convert PDS .img files to .txt files

# Specify Input & Output files
$inFile = $PSScriptRoot + '\ldem_4.img'
$outFile = $PSScriptRoot + '\LDEM_4.txt'

format-hex $inFile > $outFile
Read-Host -Prompt "Press any key to continue"