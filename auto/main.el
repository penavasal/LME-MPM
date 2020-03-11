(TeX-add-style-hook
 "main"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("svjour3" "twocolumn")))
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
    "fix-cm"
    "svjour3"
    "svjour310"
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
   (TeX-add-symbols
    '("Deriv" ["argument"] 2)
    '("Integral" 2)
    '("GradT" 1)
    '("GradS" 1)
    '("Grad" 1)
    '("Div" 1)
    '("Vector" 1)
    '("Matrix" 1))
   (LaTeX-add-labels
    "intro"
    "sec:Notation"
    "tab:notation-table"
    "sec:derivation-mpm"
    "sec:governing-equations"
    "eq:Balance-momentum"
    "eq:Compatibility-equation"
    "eq:Constitutive-equation"
    "eq:Rho-material-derivative"
    "sec:variational-formulation"
    "eq:Hilbert-space"
    "eq:cauchy-secuence"
    "eq:BalanceMomentum_wf"
    "sec:Galerkin-procedure"
    "fig:MPM-discretization"
    "eq:particle_acceleration_forces"
    "eq:particle_internal_forces"
    "eq:particle_body_forces"
    "eq:particle_load_forces"
    "eq:Approx-velocity-mesh"
    "eq:Approx-gradvelocity-mesh"
    "eq:particle_balance_forces3"
    "eq:particle_nod_mass"
    "eq:nodal_internal_forces"
    "eq:nodal_external_forces"
    "eq:IncrStrainPoint"
    "eq:MassConservation"
    "eq:Updated_Lagrangian"
    "fig:MPM_algorithm"
    "eq:Sulsky-1994-UL-v"
    "eq:Sulsky-1994-UL-x"
    "eq:Zhang-2016-UL-x"
    "eq:Zhang-2016-UL-v"
    "eq:Tran-2019-GA-v"
    "eq:Tran-2019-GA-x"
    "eq:Tran-2019-GA-a"
    "sec:epc-algor-mpm"
    "eq:5"
    "eq:Predictor-velocity"
    "alg:PCE-algorithm"
    "sec:EPC-accuracy"
    "fig:Dyka_Bar"
    "eq:3"
    "fig:Dyka-PCE-FE"
    "sec:local-max-ent"
    "eq:Shannon-entropy"
    "eq:LME-p"
    "eq:LME-Z"
    "eq:LME-grad-p"
    "eq:LME-f"
    "eq26"
    "eq27"
    "eq28"
    "fig:MPM_Shape_Fun"
    "fig:LME_17.3_Shape_Fun"
    "fig:GIMP_Shape_Fun"
    "fig:LME_10.0_Shape_Fun"
    "fig:LME_7.0_Shape_Fun"
    "fig:LME_5.0_Shape_Fun"
    "fig:LME_MPM"
    "fig:block"
    "sec:study-error"
    "eq:RMS"
    "fig:Dyka-MPM-uGIMP-LME"
    "sec:mpm-versus-otm"
    "sec:conclusions"
    "app:analytical_sol"
    "eq:1D-balance-linear-momentum"
    "eq:1D-constitutive-equation"
    "eq:CompatibilityEquation_e"
    "eq:1D-balance-linear-momentum-II"
    "eq:1D-constitutive-equation-II"
    "eq:1D-wave-elastic"
    "eq:1D-elastic-wave-celerity"
    "eq:System-stress-velocity"
    "eq:System-stress-velocity-II"
    "eq:eq:System-stress-velocity-II"
    "eq:P-matrix"
    "eq:Lambda-matrix"
    "eq:Riemann-definition"
    "eq:Riemann-II"
    "eq:Riemann-III"
    "eq:System-stress-velocity-III"
    "eq:System-stress-velocity-IV"
    "eq:SystemEquations_sigma_v_VI"
    "eq:Riemann-I-1D-elastic-bar"
    "eq:Riemann-II-1D-elastic-bar"
    "eq:Riemann-stress-velocity"
    "fig:vel_analytics_dyka"
    "fig:stress_analytics_dyka")
   (LaTeX-add-bibliographies
    "Biblio.bib"))
 :latex)

