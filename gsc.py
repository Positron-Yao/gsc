import sys
import re

keys = {
    "c5": "q",
    "d5": "w",
    "e5": "e",
    "f5": "r",
    "g5": "t",
    "a5": "y",
    "b5": "u",
    "c4": "a",
    "d4": "s",
    "e4": "d",
    "f4": "f",
    "g4": "g",
    "a4": "h",
    "b4": "j",
    "c3": "z",
    "d3": "x",
    "e3": "c",
    "f3": "v",
    "g3": "b",
    "a3": "n",
    "b3": "m"
}

ahk_ys_init = '''#IfWinActive ahk_exe Yuanshen.exe

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
    if len(sys.argv) > 1:
        read_score(sys.argv[1])
    else:
        choice = input("Genshin Score Compiler\n [1] 输入曲谱文件\n [q] 退出\n>> ")
        if choice == "1" or choice == "":
            fp = input("文件位置: \n>> ")
            read_score(fp)
        else:
            return


if __name__ == "__main__":
    try:
        main()
    except BaseException:
        print("爆了，你看你小宝贝的输入的什么可爱东西，重开吧()")