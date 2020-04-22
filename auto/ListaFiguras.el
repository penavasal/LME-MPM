(TeX-add-style-hook
 "ListaFiguras"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("subfig" "lofdepth" "lotdepth") ("units" "ugly")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "Figures/Dyka_bar"
    "Figures/Block"
    "article"
    "art10"
    "subfig"
    "mathptmx"
    "amssymb"
    "amsmath"
    "amsfonts"
    "epstopdf"
    "mathrsfs"
    "hyperref"
    "enumitem"
    "array"
    "tabularx"
    "supertabular"
    "fancyhdr"
    "multirow"
    "color"
    "makeidx"
    "xstring"
    "setspace"
    "epsfig"
    "pgf"
    "preview"
    "algorithm"
    "algorithmic"
    "stanli"
    "units")
   (LaTeX-add-labels
    "fig:MPM-discretization"
    "fig:MPM_algorithm"
    "fig:MPM_Shape_Fun"
    "fig:LME_17.3_Shape_Fun"
    "fig:GIMP_Shape_Fun"
    "fig:LME_10.0_Shape_Fun"
    "fig:LME_7.0_Shape_Fun"
    "fig:LME_5.0_Shape_Fun"
    "fig:LME_MPM"
    "fig:Dyka_Bar"
    "fig:Velocity-Dyka-PCE-FE"
    "fig:Stress-Dyka-PCE-FE"
    "fig:Velocity-Dyka-LME-gamma-comparative"
    "fig:Velocity-Dyka-MPM-vs-OTM"
    "fig:Velocity-Dyka-Q4-uGIMP-LME"
    "fig:block"
    "fig:vertical-displacement-block"
    "fig:Block-LME3-PCE-t0"
    "fig:Block-LME3-PCE-t025"
    "fig:Block-LME3-PCE-t1"
    "fig:Block-LME3"
    "fig:vel_analytics_dyka"
    "fig:stress_analytics_dyka"))
 :latex)

