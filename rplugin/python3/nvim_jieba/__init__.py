"""
   Copyright 2021 Yufan You

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0
"""

import pynvim
import jieba

jieba.setLogLevel(20)

@pynvim.plugin
class Main():

    def __init__(self, nvim):
        self.nvim = nvim


    def jieba_get_word(self):
        return self.nvim.eval("expand('<cword>')")


    def jieba_get_pos_in_word(self):
        line = self.nvim.eval("getline('.')")
        if line == '':
            return None
        bytecol = int(self.nvim.eval("getpos('.')")[2]) - 1
        escaped_line = line.replace("\\", "\\\\").replace('"', '\\"')
        # In Vim we can use charcol(), but it's not available in nvim
        col = int(self.nvim.eval(f'charidx("{escaped_line}", {bytecol})'))
        word = self.jieba_get_word()
        if line[col] not in word:
            return None
        if self.nvim.eval(f'charidx("{word}", 1)') != 0:
            return None
        l = max(0, col - len(word) + 1)
        r = min(len(line), col + len(word))
        return col - l - line[l:r].find(word)


    def jieba_get_word_cut(self):
        return list(jieba.cut(self.jieba_get_word()))


    def jieba_get_index(self, pos, cut):
        total_len = 0
        for i in range(0, len(cut)):
            if pos < total_len + len(cut[i]):
                return (i, pos - total_len)
            total_len += len(cut[i])
        raise Exception("pos out of range")


    @pynvim.command('JiebaWordForward', nargs = 0, sync = True)
    def jieba_word_forward(self):
        pos = self.jieba_get_pos_in_word()
        if pos != None:
            cut = self.jieba_get_word_cut()
            index, p = self.jieba_get_index(pos, cut)
            if index < len(cut) - 1:
                self.nvim.command(f'normal! {len(cut[index]) - p}l')
                return
        self.nvim.command('normal! w')


    @pynvim.command('JiebaWordBackward', nargs = 0, sync = True)
    def jieba_word_backward(self):
        pos = self.jieba_get_pos_in_word()
        if pos != None:
            cut = self.jieba_get_word_cut()
            index, p = self.jieba_get_index(pos, cut)
            if index > 0:
                if p == 0:
                    self.nvim.command(f'normal! {len(cut[index - 1])}h')
                else:
                    self.nvim.command(f'normal! {p}h')
                return
        self.nvim.command('normal! b')


    @pynvim.command('JiebaEndForward', nargs = 0, sync = True)
    def jieba_end_forward(self):
        pos = self.jieba_get_pos_in_word()
        if pos != None:
            cut = self.jieba_get_word_cut()
            index, p = self.jieba_get_index(pos, cut)
            if index < len(cut) - 1:
                if p == len(cut[index]) - 1:
                    self.nvim.command(f'normal! {len(cut[index + 1])}l')
                else:
                    self.nvim.command(f'normal! {len(cut[index]) - 1 - p}l')
                return
        self.nvim.command('normal! e')


    @pynvim.command('JiebaEndBackward', nargs = 0, sync = True)
    def jieba_end_backward(self):
        pos = self.jieba_get_pos_in_word()
        if pos != None:
            cut = self.jieba_get_word_cut()
            index, p = self.jieba_get_index(pos, cut)
            if index > 0:
                self.nvim.command(f'normal! {p + 1}h')
                return
        self.nvim.command('normal! ge')
