set table "gnuplot/C2_02_510_03_Divers_Corrige/3.table"; set format "%.5f"
set samples 200.0; set parametric; plot [t=-4:-1] [] [] log10(10**t),(t<log10(1./(300.))? 0:-90)+-90
