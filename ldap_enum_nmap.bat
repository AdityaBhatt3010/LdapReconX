@echo off

set /p ip=Enter Target IP: 
set /p dc1=Enter DC1 (e.g., example): 
set /p dc2=Enter DC2 (e.g., local): 

set /p user=Enter Username (leave blank for anonymous): 
set /p pass=Enter Password (leave blank for anonymous): 

if not "%user%"=="" if not "%pass%"=="" (
    echo [+] Running Credentialed LDAP Search...
    nmap -p 389 --script ldap-search --script-args "ldap.username=%user%@%dc1%.%dc2%,ldap.password=%pass%,ldap.base=dc=%dc1%,dc=%dc2%" %ip%
) else (
    echo [+] Running LDAP Brute (Anonymous Mode)...
    nmap -p 389 --script ldap-brute --script-args "ldap.base=dc=%dc1%,dc=%dc2%" %ip%
)

pause
