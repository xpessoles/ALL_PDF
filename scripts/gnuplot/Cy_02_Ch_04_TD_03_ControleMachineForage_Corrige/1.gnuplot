set table "gnuplot/Cy_02_Ch_04_TD_03_ControleMachineForage_Corrige/1.table"; set format "%.5f"
set samples 150.0; set parametric; plot [t=-3:1] [] [] log10(10**t),-(t < log10(1./10) ? 20*log10(1) : 20*log10(0.1*10.0*1/(10))-20*log10(10**t))+20*log10(abs(1/(10**t)))+20*log10(abs(0.1))
