from sys import * 
from math import * 
pErEmEnNaYa_s_DlYa_SpiSka = [] 
for arg in argv: 
	pErEmEnNaYa_s_DlYa_SpiSka.append(arg) 
name,pErEmEnNaYa_a_DlYa_PeRvOgO_ArGuMeNtA,pErEmEnNaYa_b_DlYa_VtOrOgO_ArGuMeNtA,pErEmEnNaYa_c_DlYa_TrEtEgO_ArGuMeNtA=pErEmEnNaYa_s_DlYa_SpiSka [0],int (pErEmEnNaYa_s_DlYa_SpiSka [1]),int (pErEmEnNaYa_s_DlYa_SpiSka  [2]),int (pErEmEnNaYa_s_DlYa_SpiSka [3]) 
l=pErEmEnNaYa_b_DlYa_VtOrOgO_ArGuMeNtA**2-4*pErEmEnNaYa_a_DlYa_PeRvOgO_ArGuMeNtA*pErEmEnNaYa_c_DlYa_TrEtEgO_ArGuMeNtA 
if l < 0: 
	print ("No roots") 
else: 
	l=sqrt (l) 
	x1=((-1)*pErEmEnNaYa_b_DlYa_VtOrOgO_ArGuMeNtA+l)/(2*pErEmEnNaYa_a_DlYa_PeRvOgO_ArGuMeNtA);x2=((-1)*pErEmEnNaYa_b_DlYa_VtOrOgO_ArGuMeNtA-l)/(2*pErEmEnNaYa_a_DlYa_PeRvOgO_ArGuMeNtA) 
	if x1<0 and x2<0: 
		print ("No roots") 
	elif x2<0: 
		x=sqrt (x1); print (-x,x); 
	elif x1<0: 
		x=sqrt (x2) 
		print (-x, x) 
	else: 
		x1,x2=sqrt (x1), sqrt (x2) 
		print(-x1, -x2, x1, x2) 

