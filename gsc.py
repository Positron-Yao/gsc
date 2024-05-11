import sys
import re

coords = [
    "q", "w", "e", "r", "t", "y", "u", 
    "a", "s", "d", "f", "g", "h", "j", 
    "z", "x", "c", "v", "b", "n", "m"
]

keys = {
    "c5": coords[0],
    "d5": coords[1],
    "e5": coords[2],
    "f5": coords[3],
    "g5": coords[4],
    "a5": coords[5],
    "b5": coords[6],
    "c4": coords[7],
    "d4": coords[8],
    "e4": coords[9],
    "f4": coords[10],
    "g4": coords[11],
    "a4": coords[12],
    "b4": coords[13],
    "c3": coords[14],
    "d3": coords[15],
    "e3": coords[16],
    "f3": coords[17],
    "g3": coords[18],
    "a3": coords[19],
    "b3": coords[20]
}

ahk_ys_init = '''full_command_line := DllCall("GetCommandLine", "str")
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
'''

# 接下来写个读谱解释器(?)
# min_interval 即 乐谱中的最小节奏间隔(毫秒)，也即一个0代表的停顿时间，写在乐谱文件的第一行
# 乐谱本体结构示例:
# c4/c4/g4/g4/a4/a4/g4/0
# f4 a4 c5/g4 b5 d5/a4 c5 e5/00000
def read_score(fp):
    with open(fp) as f:
        content = f.readlines()
    min_interval, score_code = eval(content[0]), content[1:]
    notes = re.sub(r"/\*.*?\*/", "", "".join(score_code).replace("\n", "")).split("/")
    
    output_string = ahk_ys_init
    for note in notes:
        if note == "":
            output_string += f"Sleep {min_interval}\n"
        elif "0" not in note:
            i = note.strip().split(" ")
            for j in i:
                output_string += f"Send {keys[j]}\n"
            output_string += f"Sleep {min_interval}\n"
        else:
            output_string += f"Sleep {min_interval*note.count('0')}\n"
    
    output_string += "return"
    with open(fp + ".ahk", "w") as f:
        f.write(output_string)


def main():
    read_score(sys.argv[1])

if __name__ == "__main__":
    main()