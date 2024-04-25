set table "gnuplot/C2_02_510_02_Divers_Corrige/1.table"; set format "%.5f"
set samples 100.0; set parametric; plot [t=-3:3] [] [] log10(10**t),(t < log10(1./10) ? 20*log10(1) : 20*log10(0.1*10.0*1/(10))-20*log10(10**t)) + (t < log10(1./10) ? 20*log10(1) : 20*log10(0.1*10.0*1/(10))-20*log10(10**t))
