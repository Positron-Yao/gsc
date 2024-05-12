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
Send {y down}
Sleep 375.0
Sleep 375.0
Sleep 375.0
Send {y up}
Send {t down}
Sleep 375.0
Sleep 375.0
Send {t up}
Send {r down}
Sleep 375.0
Send {r up}
Send {e down}
Sleep 375.0
Sleep 375.0
Sleep 375.0
Sleep 375.0
Send {e up}
Send {h down}
Sleep 375.0
Send {h up}
Send {j down}
Sleep 375.0
Send {j up}
Send {q down}
Sleep 375.0
Send {q up}
Send {w down}
Sleep 375.0
Send {w up}
Send {e down}
Sleep 375.0
Send {e up}
Send {w down}
Sleep 375.0
Send {w up}
Send {q down}
Sleep 375.0
Send {q up}
Send {h down}
Sleep 375.0
Send {h up}
Send {q down}
Sleep 375.0
Sleep 375.0
Sleep 375.0
Send {q up}
Send {j down}
Sleep 375.0
Sleep 375.0
Sleep 375.0
Send {j up}
Sleep 375.0
Send {y down}
Sleep 375.0
Sleep 375.0
Send {y up}
Send {t down}
Sleep 375.0
Sleep 375.0
Send {t up}
Send {r down}
Sleep 375.0
Send {r up}
Send {e down}
Sleep 375.0
Sleep 375.0
Sleep 375.0
Sleep 375.0
Send {e up}
Send {h down}
Sleep 375.0
Send {h up}
Send {j down}
Sleep 375.0
Send {j up}
Send {q down}
Sleep 375.0
Send {q up}
Send {w down}
Sleep 375.0
Send {w up}
Send {e down}
Sleep 375.0
Send {e up}
Send {w down}
Sleep 375.0
Send {w up}
Send {q down}
Sleep 375.0
Send {q up}
Send {j down}
Sleep 375.0
Send {j up}
Send {h down}
Sleep 375.0
Sleep 375.0
Sleep 375.0
Send {h up}
Sleep 375.0
Send {h down}
Sleep 375.0
Send {h up}
Send {j down}
Sleep 375.0
Send {j up}
Send {q down}
Sleep 375.0
Send {q up}
Send {j down}
Sleep 375.0
Send {j up}
Send {q down}
Sleep 375.0
Send {q up}
Send {w down}
Sleep 375.0
Sleep 375.0
Send {w up}
Send {t down}
Sleep 375.0
Send {t up}
Send {e down}
Sleep 375.0
Sleep 375.0
Sleep 375.0
Send {e up}
Sleep 375.0
Send {h down}
Sleep 375.0
Send {h up}
Send {j down}
Sleep 375.0
Send {j up}
Send {q down}
Sleep 375.0
Send {q up}
Send {j down}
Sleep 375.0
Send {j up}
Send {q down}
Sleep 375.0
Send {q up}
Send {w down}
Sleep 375.0
Sleep 375.0
Send {w up}
Send {u down}
Sleep 375.0
Send {u up}
Send {e down}
Sleep 375.0
Sleep 375.0
Sleep 375.0
Send {e up}
Sleep 375.0
Send {h down}
Sleep 375.0
Send {h up}
Send {j down}
Sleep 375.0
Send {j up}
Send {q down}
Sleep 375.0
Send {q up}
Send {j down}
Sleep 375.0
Send {j up}
Send {h down}
Sleep 375.0
Send {h up}
Send {j down}
Sleep 375.0
Sleep 375.0
Send {j up}
Send {e down}
Sleep 375.0
Send {e up}
Send {y down}
Sleep 375.0
Send {y up}
Send {t down}
Sleep 375.0
Send {t up}
Send {r down}
Sleep 375.0
Send {r up}
Send {t down}
Sleep 375.0
Sleep 375.0
Send {t up}
Send {q down}
Sleep 375.0
Send {q up}
Send {r down}
Sleep 375.0
Send {r up}
Send {e down}
Sleep 375.0
Send {e up}
Send {w down}
Sleep 375.0
Send {w up}
Send {q down}
Sleep 375.0
Sleep 375.0
Send {q up}
Send {j down}
Sleep 375.0
Send {j up}
Send {h down}
Sleep 375.0
Sleep 375.0
Sleep 375.0
Sleep 375.0
Sleep 375.0
Sleep 375.0
Send {h up}
Sleep 375.0
return
