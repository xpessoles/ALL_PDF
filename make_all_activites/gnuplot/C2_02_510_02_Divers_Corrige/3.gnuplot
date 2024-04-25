set table "gnuplot/C2_02_510_02_Divers_Corrige/3.table"; set format "%.5f"
set samples 101.0; set parametric; plot [t=-3:3] [] [] log10(10**t),(t<log10(1./(10))? 0:-90) + (t<log10(1./(0.1))? 0:-90)
