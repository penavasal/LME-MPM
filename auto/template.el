(TeX-add-style-hook
 "template"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("svjour3" "smallextended")))
   (TeX-run-style-hooks
    "latex2e"
    "fix-cm"
    "svjour3"
    "svjour310"
    "graphicx"
    "mathptmx"
    "amsmath")
   (TeX-add-symbols
    '("Deriv" ["argument"] 2)
    '("Integral" 2)
    '("MatOp" 1)
    '("TensF" 1)
    '("TensT" 1)
    '("Tensor" 2)
    '("Vect" 1)
    '("Lapla" 1)
    '("Grad" 1)
    '("Div" 1))
   (LaTeX-add-labels
    "intro"
    "sec:global-max-ent"
    "eq:Convex_hull_X"
    "eq:Approximation_nodes"
    "eq:LME_constrains_I"
    "eq:LME_constrains_II"
    "eq:LME_constrains_III"
    "eq:Width_Shape_Fun"
    "eq:Total_Width_Shape_Fun"
    "eq:Entropy_def"
    "eq:Total_Entropy_def"
    "sec:anisotropic-lme")
   (LaTeX-add-bibliographies
    "../../../Biblio/BIBLIOGRAFIA_PHD.bib"))
 :latex)

