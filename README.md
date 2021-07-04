# nvim-jieba

使用结巴中文分词提供 Vim 的动作~~和文本对象~~。

本来想支持重复次数、xmap、iw、aw，结果大失败。

初始化和单次分词都很慢。

除此之外还有一些奇怪的 bug。

## 安装

### jieba

```sh
python3 -m pip install jieba
```

or

```sh
sudo pacman -S python-jieba
```

### vim-plug

```vim
Plug 'ouuan/nvim-jieba', { 'do': ':UpdateRemotePlugins' }
```

### UpdateRemotePlugins

插件安装、更新时需要运行：

```vim
:UpdateRemotePlugins
```

需要注意的是，不要在本插件未加载时（例如，使用了 vim-plug 的 lazy load）运行这条命令。

## 选项

`g:jieba_default_maps`: 使用默认键映射。

默认键映射如下：

```vim
nnoremap <silent> w :JiebaWordForward<cr>
onoremap <silent> w :JiebaWordForward<cr>
nnoremap <silent> b :JiebaWordBackward<cr>
onoremap <silent> b :JiebaWordBackward<cr>
nnoremap <silent> e :JiebaEndForward<cr>
onoremap <silent> e :JiebaEndForward<cr>
nnoremap <silent> ge :JiebaEndBackward<cr>
onoremap <silent> ge :JiebaEndBackward<cr>
```

## 命令

`JiebaEnable/Disable/Toggle`: 启动/禁用/切换

`JiebaWord/EndForward/Backward`: 移动
