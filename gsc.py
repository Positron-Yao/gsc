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
    mode, min_interval = content[0].split(" ")
    score_code = content[1:]
    min_interval = eval(min_interval)

    # sequenced 序列模式，每个音的时长相同，只描述音符序列
    if mode == "sequenced":
        notes = re.sub(r"/\*.*?\*/", "", re.sub(r"#.*?\n", "", "".join(score_code)).replace("\n", "")).split("/")
        
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
        print("Done.")

    # timed 计时模式，在最小时长间隔的单位上再描述时长
    elif mode == "timed":
        class Notes:
            time = 0
            members = []
            count = 0
            output = ahk_ys_init
            def __init__(self, name, starttime, duration):
                # content = (name, duration)
                self.name = name
                self.starttime = starttime
                self.duration = duration
                self.life = 0
                self.alive = False
                # 加到总列表中
                Notes.count += 1
                Notes.members.append(self)

            def update(self):
                if Notes.time == self.starttime:
                    self.alive = True
                    Notes.output += f"Send {{{keys[self.name]} down}}\n"
                if self.alive:
                    self.life += 1
                if self.life >= self.duration+1:
                    self.alive = False
                    Notes.output += f"Send {{{keys[self.name]} up}}\n"
                    return True
                return False
                
            
            def step():
                # 使所有音符的生命前进一个单位
                i = 0
                while i < Notes.count:
                    if Notes.members[i].update():
                        # 似了
                        # print(Notes.members[i].name, "似了")
                        del Notes.members[i]
                        Notes.count -= 1
                        i -= 1
                    i += 1

            def read(notes):
                # 起始读带
                Notes.time = 0
                for note in notes:
                    if (note != "") and ("0" not in note):
                        i = note.split(" ")
                        for j in i:
                            Notes(j[:2], Notes.time, int(j[2:]))
                    Notes.time += 1

            def run():
                # 整体运行
                Notes.time = 0
                while Notes.count != 0:
                    Notes.step()
                    Notes.output += f"Sleep {min_interval}\n"
                    Notes.time += 1

            def get_output():
                return Notes.output + "return\n"


        notes = re.sub(r"/\*.*?\*/", "", re.sub(r"#.*?\n", "", "".join(score_code)).replace("\n", "")).split("/")
        Notes.read(notes)
        Notes.run()
        with open(fp + ".ahk", "w") as f:
            f.write(Notes.get_output())
        print("Done.")
        

def main():
    read_score(sys.argv[1])

if __name__ == "__main__":
    main()