set table "gnuplot/C2_02_510_03_Divers_Corrige/2.table"; set format "%.5f"
set samples 50.0; set parametric; plot [t=-4:-1] [] [] log10(10**t),20*log10(abs(40/sqrt(1+(300*10**t)**2)))+20*log10(abs(1/(10**t)))
