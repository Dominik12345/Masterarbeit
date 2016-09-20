BeginPackage["Stability`"]
Get["Documents/QCDxdQCD/Mathematica/Packages/Beta'.m"]
Get["Documents/QCDxdQCD/Mathematica/Packages/Fixedpoint'.m"]


tranddet::usage="Computes trace and determinant of the stability 
				matrix at the nontrivial fixedpoint.
				Parameters:x1,y1,z1,x2,y2,z2"

aftranddet::usage="Computes trace and determinant of the stability 
				matrix at the nontrivial fixedpoint in the 
				all-fundamental representation.
				Parameters:norm1,norm2,Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj
								=(norm,model)"
a4::usage="Returns the nontrivial fixed point a4.
			Parameters:x1,y1,z1,x2,y2,z2=c"


Begin["`Private`"]

tranddet[x1_,y1_,z1_,x2_,y2_,z2_]:=(Module[{tr,
	a=a4@@{x1,y1,z1,x2,y2,z2},det,coeff={x1,y1,z1,x2,y2,z2}},
		
		tr=Simplify[d1b1@@Join[a,coeff] + d2b2@@Join[a,coeff]];
		det=Simplify[d1b1@@Join[a,coeff] * d2b2@@Join[a,coeff]-
			  d1b2@@Join[a,coeff] * d2b1@@Join[a,coeff]];
		Return[{tr,det}]
		]
	);

aftranddet[norm1_,norm2_,Nc_,Nd_,nfc_,nsc_,nfd_,nsd_,nfj_,nsj_]:=(
	Module[{afcoeff=c@@{norm1,norm2,Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj} },
			Return[Simplify[ tranddet@@afcoeff ]]
		]
	);

End[]
EndPackage[]