# By: Brendan Luke
# Date: February 9, 2022
# Purpose: Convert PDS .img files to .txt files

Read-Host -Prompt "Press any key to continue"
# Create Input & Output filepaths
#$inFile = $PSScriptRoot + '\ldem_4.img'
#$outFile = $PSScriptRoot + '\testLDEM_4.txt'
$inFile = $PSScriptRoot + '\' + $Args[0]
$outFile = $PSScriptRoot + '\' + $Args[1]

format-hex $inFile > $outFile
Read-Host -Prompt "Press any key to continue"