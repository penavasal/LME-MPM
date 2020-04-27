(TeX-add-style-hook
 "LME-MPM"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("elsarticle" "preprint" "12pt" "a4paper")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("units" "ugly") ("glossaries" "acronym")))
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
    "elsarticle"
    "elsarticle12"
    "lineno"
    "float"
    "subfig"
    "color"
    "soul"
    "cancel"
    "algorithm"
    "algorithmic"
    "subfigure"
    "amsmath"
    "amsthm"
    "amssymb"
    "xstring"
    "stanli"
    "units"
    "glossaries")
   (TeX-add-symbols
    '("Deriv" ["argument"] 2)
    '("MMP" 1)
    '("red" 1)
    '("Integral" 2)
    '("GradT" 1)
    '("GradS" 1)
    '("Grad" 1)
    '("Div" 1)
    '("Vector" 1)
    '("Matrix" 1)
    '("tens" 1)
    '("vect" 1))
   (LaTeX-add-labels
    "intro"
    "sec:meshfree-methodology"
    "sec:derivation-mpm"
    "fig:Continuum-solid"
    "eq:Compatibility-equation"
    "eq:Balance-momentum"
    "eq:Constitutive-equation"
    "eq:Rho-material-derivative"
    "eq:Hilbert-space"
    "eq:cauchy-secuence"
    "eq:BalanceMomentum_wf"
    "eq:particle_acceleration_forces"
    "eq:particle_internal_forces"
    "eq:particle_body_forces"
    "eq:particle_load_forces"
    "fig:MPM-discretization"
    "eq:particle_balance_forces3"
    "eq:particle_nod_mass"
    "eq:nodal_internal_forces"
    "eq:nodal_external_forces"
    "eq:IncrStrainPoint"
    "eq:MassConservation"
    "eq:Updated_Lagrangian"
    "sec:epc-algor-mpm"
    "fig:MPM_algorithm"
    "eq:Sulsky-1994-UL-v"
    "eq:Sulsky-1994-UL-x"
    "eq:Zhang-2016-UL-x"
    "eq:Zhang-2016-UL-v"
    "eq:Tran-2019-GA-v"
    "eq:Tran-2019-GA-x"
    "eq:Tran-2019-GA-a"
    "eq:Predictor-velocity-I"
    "eq:Variational-recovery"
    "eq:Predictor-velocity-II"
    "eq:Corrector-velocity"
    "eq:Update-lagrangian-pce"
    "algo:1"
    "sec:local-max-ent"
    "eq:Shannon-entropy"
    "eq:least-biased-approximation-scheme"
    "eq:RAJAN"
    "eq:LME-scheme-pareto-set"
    "eq:LME-p"
    "eq:LME-Z"
    "eq:LME-J"
    "eq:LME-r"
    "eq:LME-grad-p"
    "eq:LME-f"
    "eq26"
    "fig:Particle-discretization"
    "fig:LME_MPM"
    "sec:Application-linear-elasticity-dynamic-problems"
    "sec:dyka-bar"
    "fig:Dyka_Bar"
    "eq:Cel"
    "fig:Dyka-error-evol"
    "eq:RMS"
    "fig:Dyka-NPC-FE"
    "fig:Dyka-LME-gamma"
    "fig:Dyka-uGIMP-LME"
    "fig:Dyka-OTM-MPM"
    "sec:andersen-block"
    "fig:block"
    "eq:gravity-load-block"
    "fig:Block-LME3"
    "fig:vertical-displacement-block"
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
    "Biblio/Biblio"))
 :latex)

