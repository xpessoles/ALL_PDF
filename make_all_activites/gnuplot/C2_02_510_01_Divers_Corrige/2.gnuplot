set table "gnuplot/C2_02_510_01_Divers_Corrige/2.table"; set format "%.5f"
set samples 50.0; set parametric; plot [t=-3:1] [] [] log10(10**t),20*log10(abs(15/sqrt(1+(10*10**t)**2)))
