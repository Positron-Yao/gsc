full_command_line := DllCall("GetCommandLine", "str")
if not (A_IsAdmin or RegExMatch(full_command_line, " /restart(?!\S)"))
{
    try ; leads to having the script re-launching itself as administrator
    {
        if A_IsCompiled
            Run *RunAs "%A_ScriptFullPath%" /restart
        else
            Run *RunAs "%A_AhkPath%" /restart "%A_ScriptFullPath%"
    }
    ExitApp
}
I_Icon = Neuvillette.ico
IfExist, %I_Icon%
Menu, Tray, Icon, %I_Icon%

#IfWinActive ahk_exe Yuanshen.exe

#NoEnv
#Warn
SendMode Input
SetWorkingDir %A_ScriptDir%

; Main
Capslock::
Send a
Sleep 375.0
Send a
Sleep 375.0
Send a
Sleep 375.0
Send a
Sleep 375.0
Sleep 375.0
return