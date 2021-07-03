" Copyright 2021 Yufan You
"
" Licensed under the Apache License, Version 2.0 (the "License");
" you may not use this file except in compliance with the License.
" You may obtain a copy of the License at
"
"     http://www.apache.org/licenses/LICENSE-2.0

if &cp || exists("g:jieba_loaded") || !has('python3')
    finish
endif

let g:jieba_loaded = 1

if exists("g:jieba_default_maps") && g:jieba_default_maps
    nnoremap <silent> w :JiebaWordForward<cr>
    onoremap <silent> w :JiebaWordForward<cr>
    nnoremap <silent> b :JiebaWordBackward<cr>
    onoremap <silent> b :JiebaWordBackward<cr>
    nnoremap <silent> e :JiebaEndForward<cr>
    onoremap <silent> e :JiebaEndForward<cr>
    nnoremap <silent> ge :JiebaEndBackward<cr>
    onoremap <silent> ge :JiebaEndBackward<cr>
endif
