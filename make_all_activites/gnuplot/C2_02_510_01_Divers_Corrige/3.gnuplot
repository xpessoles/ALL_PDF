set table "gnuplot/C2_02_510_01_Divers_Corrige/3.table"; set format "%.5f"
set samples 100.0; set parametric; plot [t=-3:1] [] [] log10(10**t),(t < log10(1./1) ? 20*log10(15) : 20*log10(0.1*10.0*15/(1))-20*log10(10**t))
