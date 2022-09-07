(TeX-add-style-hook
 "README"
 (lambda ()
   (add-to-list 'LaTeX-verbatim-environments-local "lstlisting")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "href")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "lstinline")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "lstinline")
   (TeX-run-style-hooks
    "latex2e"
    "caption-xetex-bidi"
    "article"
    "art10"
    "hevea"
    "fontspec"
    "morefloats"
    "rcs"
    "makeidx"
    "supertabular"
    "lscape"
    "array"
    "framed"
    "listings"
    "color"
    "hyperref"
    "url"
    "fancyhdr"
    "caption"
    "xltxtra"
    "xunicode"
    "bidi")
   (LaTeX-add-environments
    "fa"
    "faPar")
   (LaTeX-add-color-definecolors
    "darkred"
    "darkgreen"
    "darkblue"))
 :latex)

