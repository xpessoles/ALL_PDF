set table "gnuplot/C2_02_510_01_Divers_Corrige/6.table"; set format "%.5f"
set samples 50.0; set parametric; plot [t=-2:2] [] [] log10(10**t),(t < log10(1./0.3) ? 20*log10(6) : 20*log10(0.1*10.0*6/(0.3))-20*log10(10**t))
