set table "gnuplot/C2_02_510_03_Divers_Corrige/4.table"; set format "%.5f"
set samples 50.0; set parametric; plot [t=-4:-1] [] [] log10(10**t),-180/3.1415957*atan(300*10**t)+-90
