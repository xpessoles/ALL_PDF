set table "gnuplot/Cy_02_Ch_04_TD_01_RobotCables_Corrige/2.table"; set format "%.5f"
set samples 150.0; set parametric; plot [t=1:5] [] [] log10(10**t),20*log10(abs(1773/sqrt(1+(0.000794*10**t)**2)))+20*log10(abs(1/(10**t)))
