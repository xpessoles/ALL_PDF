set table "gnuplot/Cy_02_Ch_04_TD_03_ControleMachineForage_Corrige/4.table"; set format "%.5f"
set samples 190.0; set parametric; plot [t=-3:1] [] [] log10(10**t),--180/3.1415957*atan(10*10**t)+-90
