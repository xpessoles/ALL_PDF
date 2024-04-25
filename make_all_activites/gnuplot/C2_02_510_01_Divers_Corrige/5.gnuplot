set table "gnuplot/C2_02_510_01_Divers_Corrige/5.table"; set format "%.5f"
set samples 50.0; set parametric; plot [t=-3:1] [] [] log10(10**t),-180/3.1415957*atan(10*10**t)
