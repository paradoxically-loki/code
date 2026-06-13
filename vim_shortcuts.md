# Vim Key Bindings Reference

---

## Motion / Navigation

| Key | Action |
|-----|--------|
| `h` `j` `k` `l` | Left, down, up, right |
| `w` / `W` | Next word (word / WORD) |
| `b` / `B` | Previous word (word / WORD) |
| `e` / `E` | End of word (word / WORD) |
| `0` | Start of line |
| `^` | First non-blank character of line |
| `$` | End of line |
| `gg` | First line of file |
| `G` | Last line of file |
| `{number}G` | Go to line number |
| `{` / `}` | Previous / next empty line (paragraph) |
| `%` | Jump to matching bracket |
| `H` / `M` / `L` | Top / middle / bottom of screen |
| `Ctrl+d` / `Ctrl+u` | Scroll half-page down / up |
| `Ctrl+f` / `Ctrl+b` | Scroll full page down / up |
| `zz` | Center screen on cursor |
| `zt` / `zb` | Scroll screen so cursor is at top / bottom |

---

## Modes

| Key | Action |
|-----|--------|
| `i` | Insert before cursor |
| `I` | Insert at beginning of line |
| `a` | Append after cursor |
| `A` | Append at end of line |
| `o` | Open new line below |
| `O` | Open new line above |
| `v` | Visual (character) mode |
| `V` | Visual line mode |
| `Ctrl+v` | Visual block mode |
| `R` | Replace mode |
| `Esc` / `Ctrl+[` | Return to Normal mode |

---

## Editing

| Key | Action |
|-----|--------|
| `x` | Delete character under cursor |
| `X` | Delete character before cursor |
| `dd` | Delete (cut) line |
| `D` | Delete to end of line |
| `cc` | Change (replace) entire line |
| `C` | Change to end of line |
| `yy` / `Y` | Yank (copy) line |
| `p` / `P` | Paste after / before cursor |
| `u` | Undo |
| `Ctrl+r` | Redo |
| `.` | Repeat last change |
| `~` | Toggle case of character |
| `gU{motion}` | Uppercase over motion |
| `gu{motion}` | Lowercase over motion |
| `>>` / `<<` | Indent / unindent line |
| `={motion}` | Auto-indent |
| `J` | Join line below to current |

---

## Operators + Motions (the Vim "language")

Operators combine with motions: `{operator}{motion}`

| Operator | Meaning |
|----------|---------|
| `d` | Delete |
| `c` | Change |
| `y` | Yank |
| `>` / `<` | Indent / unindent |
| `g~` / `gU` / `gu` | Toggle / upper / lower case |

**Examples:**

| Example | Action |
|---------|--------|
| `dw` | Delete to next word |
| `d$` | Delete to end of line |
| `ci"` | Change inside quotes |
| `da(` | Delete around parentheses |
| `yiw` | Yank inner word |
| `>ap` | Indent a paragraph |

---

## Text Objects

Used after operators: `{operator}i{object}` (inner) or `{operator}a{object}` (around)

| Object | Meaning |
|--------|---------|
| `w` | Word |
| `s` | Sentence |
| `p` | Paragraph |
| `"` `'` `` ` `` | Quoted string |
| `(` `)` `b` | Parentheses |
| `[` `]` | Brackets |
| `{` `}` `B` | Braces |
| `<` `>` | Angle brackets |
| `t` | HTML/XML tag |

---

## Search & Replace

| Key | Action |
|-----|--------|
| `/pattern` | Search forward |
| `?pattern` | Search backward |
| `n` / `N` | Next / previous match |
| `*` / `#` | Search for word under cursor (forward / backward) |
| `:%s/old/new/g` | Replace all in file |
| `:%s/old/new/gc` | Replace all with confirmation |
| `:s/old/new/g` | Replace all on current line |
| `f{char}` | Jump to next occurrence of char on line |
| `F{char}` | Jump to previous occurrence of char on line |
| `t{char}` / `T{char}` | Jump to just before / after char |
| `;` / `,` | Repeat `f`/`t` forward / backward |

---

## Marks & Jumps

| Key | Action |
|-----|--------|
| `m{a-z}` | Set mark |
| `` `{a-z} `` | Jump to mark (exact position) |
| `'{a-z}` | Jump to mark's line |
| `Ctrl+o` | Jump to previous location |
| `Ctrl+i` | Jump to next location |
| `''` | Jump back to last jump position |

---

## Registers

| Key | Action |
|-----|--------|
| `"{register}y` | Yank into register |
| `"{register}p` | Paste from register |
| `"0p` | Paste last yanked text |
| `"+y` / `"+p` | Yank / paste with system clipboard |
| `:reg` | Show all registers |

---

## Macros

| Key | Action |
|-----|--------|
| `q{a-z}` | Start recording macro into register |
| `q` | Stop recording |
| `@{a-z}` | Play macro |
| `@@` | Repeat last macro |
| `{n}@{a-z}` | Run macro n times |

---

## Windows & Tabs

| Key | Action |
|-----|--------|
| `:sp` / `:vsp` | Horizontal / vertical split |
| `Ctrl+w w` | Cycle through windows |
| `Ctrl+w h/j/k/l` | Move between windows |
| `Ctrl+w =` | Equalize window sizes |
| `Ctrl+w q` | Close window |
| `:tabnew` | New tab |
| `gt` / `gT` | Next / previous tab |
| `:tabc` | Close tab |

---

## File & Ex Commands

| Key | Action |
|-----|--------|
| `:w` | Save |
| `:q` | Quit |
| `:wq` / `ZZ` | Save and quit |
| `:q!` / `ZQ` | Quit without saving |
| `:e {file}` | Open file |
| `:bn` / `:bp` | Next / previous buffer |
| `:ls` | List buffers |
| `:!{cmd}` | Run shell command |
| `Ctrl+g` | Show file info / position |
| `:set nu` | Show line numbers |
| `:set rnu` | Relative line numbers |