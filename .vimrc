set nocompatible              " be iMproved, required
"{{{ Vundle
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'
" Vim airline plugin
Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'
Plugin 'vim-syntastic/syntastic'
Plugin 'koalaman/shellcheck'
"Plugin 'Valloric/YouCompleteMe'
Plugin 'scrooloose/nerdtree'
Plugin 'vim-scripts/Wombat'

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line
" }}} /Vundle
set encoding=utf-8
set autoindent
set hlsearch
set incsearch
set path+=**
set showmatch
set laststatus=2
" FileType specific settings {{{
augroup filetype_sh
    autocmd!
    autocmd FileType sh setlocal foldmethod=marker
augroup filetype_vim
    autocmd!
    autocmd FileType vim setlocal foldmethod=marker
augroup END
augroup filetype_python
    autocmd!
    autocmd FileType python setlocal foldmethod=marker
augroup END
"}}}

" Airline {{{
let g:airline_left_sep=''
let g:airline_right_sep=''
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#left_sep = ''
let g:airline#extensions#tabline#right_sep = ''
let g:airline_theme = 'serene'
"}}}

set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*
    " Put on the Right site a little satusline widget
" Syntastic {{{
let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
"let g:syntastic_check_on_open = 1
"let g:syntastic_check_on_wq = 0
let g:syntastic_python_checkers = ["pylint"]
let g:syntastic_sh_checkers = ["shellcheck"]
"let g:syntastic_error_symbol = 'â'
"let g:syntastic_style_error_symbol = 'â¢'
"let g:syntastic_warning_symbol = 'â '
"let g:syntastic_style_warning_symbol = 'â'
let g:syntastic_loc_list_height = 5
"}}}
" NERDTree {{{
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
let g:NERDTreeDirArrowExpandable = '▸'
let g:NERDTreeDirArrowCollapsible = '▾'
" }}}
" {{{Netrw
let g:netrw_banner = 0
let g:netrw_browse_split = 1
let g:netrw_winsize = 25
let g:netrw_altv = 1
" Per default, netrw leaves unmodified buffers open. This autocommand
" deletes netrw's buffer once it's hidden (using ':q', for example)
autocmd FileType netrw setl bufhidden=delete
"}}}

" Tabs {{{
set expandtab
set smarttab
set shiftwidth=4
set tabstop=4
" }}}

syntax enable
" Numbering {{{
set number
set relativenumber
autocmd FocusLost * set norelativenumber
autocmd FocusGained * set relativenumber
autocmd InsertEnter * set norelativenumber
autocmd InsertLeave * set relativenumber
autocmd WinLeave * set norelativenumber
autocmd WinEnter * set relativenumber
autocmd BufWinEnter * set relativenumber
autocmd BufWinLeave * set norelativenumber
autocmd VimEnter * set relativenumber
"}}}
set guioptions -=r
set guioptions -=T
set guioptions -=L
set t_Co=256
set background=dark
color wombat
set guifont=hack
set mouse=a
set listchars=eol:¶,tab:\|\ ,trail:·
set list
hi CursorLine cterm=None ctermbg=234
set cursorline
set backspace=indent,eol,start
set magic
set splitright
set wildmenu

" Key Mappings {{{
" Nope arrows
nnoremap <up> <nop>
nnoremap <down> <nop>
nnoremap <left> <nop>
nnoremap <right> <nop>
inoremap <up> <nop>
inoremap <down> <nop>
inoremap <left> <nop>
inoremap <right> <nop>

"noremap <F5> :NERDTreeToggle<cr>
noremap <F5> :Lexplore<cr>
noremap <F9> :cd %:p:h<cr>:pwd<cr>
noremap <F10> :vsplit $MYVIMRC<cr>
noremap <F11> :source $MYVIMRC<cr>
"}}}
