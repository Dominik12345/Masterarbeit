BeginPackage[ "Beta`" ]

a1::usage="1of3 coefficient of g1^3. Parameters:d,TR1,dR2";
a2::usage="2of3 coefficient of g1^3. Parameters:TS1,dS2";
a3::usage="3of3 coefficient of g1^3. Parameters:C2G1";
b1::usage="1of3 coefficient of g1^5. Parameters:d,C2G1,C2R1,TR1,dR2";
b2::usage="2of3 coefficient of g1^5. Parameters:C2G1,C2S1,TS1,dS2";
b3::usage="3of3 coefficient of g1^5. Parameters:C2G1";
c1::usage="1of2 coefficient of g1^3g2^2. Parameters:d,C2R2,dR2,TR1";
c2::usage="2of2 coefficient of g1^3g2^2. Parameters:C2S2,dS2,TS1";

X1m::usage="g1^3 coefficient of the beta function in a general representation.
			Parameters:d,TR1,TR2,TS1,TS2,dR1,dR2,dS1,dS2,C2G1,C2G2,C2R1,C2R2,C2S1,C2S2";
Y1m::usage="g1^5 coefficient of the beta function in a general representation.
			Parameters:d,TR1,TR2,TS1,TS2,dR1,dR2,dS1,dS2,C2G1,C2G2,C2R1,C2R2,C2S1,C2S2";
Z1m::usage="g1^3g2^2 coefficient of the beta function in a general representation.
			Parameters:d,TR1,TR2,TS1,TS2,dR1,dR2,dS1,dS2,C2G1,C2G2,C2R1,C2R2,C2S1,C2S2";

X2m::usage="g2^3 coefficient of the beta function in a general representation.
			Parameters:d,TR1,TR2,TS1,TS2,dR1,dR2,dS1,dS2,C2G1,C2G2,C2R1,C2R2,C2S1,C2S2";
Y2m::usage="g2^5 coefficient of the beta function in a general representation.
			Parameters:d,TR1,TR2,TS1,TS2,dR1,dR2,dS1,dS2,C2G1,C2G2,C2R1,C2R2,C2S1,C2S2";
Z2m::usage="g2^3g1^2 coefficient of the beta function in a general representation.
			Parameters:d,TR1,TR2,TS1,TS2,dR1,dR2,dS1,dS2,C2G1,C2G2,C2R1,C2R2,C2S1,C2S2";

generalx::usage="Returns the coefficients of the beta-functions as {X1,Y1,Z1,X2,Y2,Z2}.
			Parameters:d,TR1,TR2,TS1,TS2,dR1,dR2,dS1,dS2,C2G1,C2G2,C2R1,C2R2,C2S1,C2S2";
setxfundamental::usage="Returns the arguments of 'generalx':{d,TR1,TR2,TS1,TS2,dR1,
			dR2,dS1,dS2,C2G1,C2G2,C2R1,C2R2,C2S1,C2S2} for the all-fundamental 
			representations. i.e. x[model]=generalx@@(setfundamental@@model) is the coefficients 
			of the betafunction";


beta1::usage="The beta1(g)-function. Parameters:{g,x}={g1,g2,X1,Y1,Z1,X2,Y2,Z2} ";
beta2::usage="The beta2(g)-function. Parameters:{g,x}={g1,g2,X1,Y1,Z1,X2,Y2,Z2} ";

c::usage="coefficients of the beta(alpha)-functions in all-fundamental representation.
			Parameters:{n1,n2,Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj}={norm,model}";

b1::usage="The beta1(alpha)-function. Parameters: {a,c}={a1,a2,X1,Y1,Z1,X2,Y2,Z2}";			
b2::usage="The beta2(alpha)-function. Parameters: {a,c}={a1,a2,X1,Y1,Z1,X2,Y2,Z2}";


d1b1::usage="Pre-derivated beta(alpha) function. Thus it is not 
			nessecary to derivate each time 'isuvfixedpoint' is called.
			Parameters: a1,a2,X1,Y1,Z1,X2,Y2,Z2"
d2b1::usage="Pre-derivated beta(alpha) function. Thus it is not 
			nessecary to derivate each time 'isuvfixedpoint' is called.
			Parameters: a1,a2,X1,Y1,Z1,X2,Y2,Z2"
d1b2::usage="Pre-derivated beta(alpha) function. Thus it is not 
			nessecary to derivate each time 'isuvfixedpoint' is called.
			Parameters: a1,a2,X1,Y1,Z1,X2,Y2,Z2"
d2b2::usage="Pre-derivated beta(alpha) function. Thus it is not 
			nessecary to derivate each time 'isuvfixedpoint' is called.
			Parameters: a1,a2,X1,Y1,Z1,X2,Y2,Z2"


afX1::usage="Coefficients of the beta(g1,g2) functions.
			Parameters: Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj=model"
afY1::usage="Coefficients of the beta(g1,g2) functions.
			Parameters: Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj=model"
afZ1::usage="Coefficients of the beta(g1,g2) functions.
			Parameters: Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj=model"			
afX2::usage="Coefficients of the beta(g1,g2) functions.
			Parameters: Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj=model"
afY2::usage="Coefficients of the beta(g1,g2) functions.
			Parameters: Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj=model"
afZ2::usage="Coefficients of the beta(g1,g2) functions.
			Parameters: Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj=model"

afix1a::usage="returns the 1. fixed point. Parameters:X1,...,Z2"
afix2a::usage="returns the 2. fixed point. Parameters:X1,...,Z2"
afix3a::usage="returns the 3. fixed point. Parameters:X1,...,Z2"
afix4a::usage="returns the 4. fixed point. Parameters:X1,...,Z2"

Begin["`Private`"]


(* Define the general coefficients *)

dirac[d_]:=If[d==1,2,1]; (*d==1=>diracfermions, else chiral fermions*)

a1[d_,TR1_,dR2_]:=2/3*TR1*dirac[d]*dR2;
a2[TS1_,dS2_]:=1/3*TS1*dS2;
a3[C2G1_]:=-11/3*C2G1;

b1[d_,C2G1_, C2R1_,TR1_,dR2_]:=(10/3*C2G1+2*C2R1)*TR1*dirac[d]*dR2;
b2[C2G1_,C2S1_,TS1_,dS2_]:=(2/3*C2G1+4*C2S1)*TS1*dS2;
b3[C2G1_]:=-34/3*C2G1^2;

c1[d_,C2R2_,dR2_,TR1_]:=2*C2R2*dirac[d]*dR2*TR1;
c2[C2S2_,dS2_,TS1_]:=4*C2S2*dS2*TS1;


X1m[d_,TR1_,TR2_,TS1_,TS2_,dR1_,dR2_,dS1_,dS2_,C2G1_,C2G2_,C2R1_,C2R2_,C2S1_,C2S2_]:=(
		( a1@@{d,TR1,dR2} + a2@@{TS1,dS2} + a3@@{C2G1} )/(16*Pi^2));
Y1m[d_,TR1_,TR2_,TS1_,TS2_,dR1_,dR2_,dS1_,dS2_,C2G1_,C2G2_,C2R1_,C2R2_,C2S1_,C2S2_]:=(
		( b1@@{d,C2G1,C2R1,TR1,dR2} + b2@@{C2G1,C2S1,TS1,dS2} + b3@@{C2G1} )/((16*Pi^2)^2));
Z1m[d_,TR1_,TR2_,TS1_,TS2_,dR1_,dR2_,dS1_,dS2_,C2G1_,C2G2_,C2R1_,C2R2_,C2S1_,C2S2_]:=(
		( c1@@{d,C2R2,dR2,TR1} + c2@@{C2S2,dS2,TS1})/((16*Pi^2)^2));

X2m[d_,TR1_,TR2_,TS1_,TS2_,dR1_,dR2_,dS1_,dS2_,C2G1_,C2G2_,C2R1_,C2R2_,C2S1_,C2S2_]:=(
		( a1@@{d,TR2,dR1} + a2@@{TS2,dS1} + a3@@{C2G2} )/(16*Pi^2));
Y2m[d_,TR1_,TR2_,TS1_,TS2_,dR1_,dR2_,dS1_,dS2_,C2G1_,C2G2_,C2R1_,C2R2_,C2S1_,C2S2_]:=(
		( b1@@{d,C2G2,C2R2,TR2,dR1} + b2@@{C2G2,C2S2,TS2,dS1} + b3@@{C2G2} )/((16*Pi^2)^2));
Z2m[d_,TR1_,TR2_,TS1_,TS2_,dR1_,dR2_,dS1_,dS2_,C2G1_,C2G2_,C2R1_,C2R2_,C2S1_,C2S2_]:=(
		( c1@@{d,C2R1,dR1,TR2} + c2@@{C2S1,dS1,TS2})/((16*Pi^2)^2));


generalx[d_,TR1_,TR2_,TS1_,TS2_,dR1_,dR2_,dS1_,dS2_,C2G1_,C2G2_,C2R1_,C2R2_,C2S1_,C2S2_]:=(
		Module[{arguments={d,TR1,TR2,TS1,TS2,dR1,dR2,dS1,dS2,C2G1,C2G2,C2R1,C2R2,C2S1,C2S2}},
				
				Return[List[X1m@@arguments,Y1m@@arguments,Z1m@@arguments,X2m@@arguments,Y2m@@arguments,Z2m@@arguments]] 
			];
		);




(*setxinadifferentrepresentation[Nc_,Nd_,nfc_,nsc_,nfd_,nsd_,nfj_,nsj_]...*)





(* The fundamental representation in the sense of "the scale of dark qcd" *)
afX1[Nc_,Nd_,nfc_,nsc_,nfd_,nsd_,nfj_,nsj_]:=( (2*2/3*1/2*(nfc+Nd*nfj)
												+1/3*1/2*(nsc+Nd*nsj)
												-11/3*Nc)/(16*Pi^2) );
afY1[Nc_,Nd_,nfc_,nsc_,nfd_,nsd_,nfj_,nsj_]:=( ( (2*10/3*Nc+2*2*(Nc^2-1)/(2*Nc) )*1/2*(nfc+Nd*nfj)
											+(2/3*Nc+4*(Nc^2-1)/(2*Nc))*1/2*(nsc+Nd*nsj)
											-34/3*Nc^2 )/((16*Pi^2)^2) );
afZ1[Nc_,Nd_,nfc_,nsc_,nfd_,nsd_,nfj_,nsj_]:=( (2*2*(Nd^2-1)/(2*Nd)*1/2*(Nd*nfj) 
											+4*(Nd^2-1)/(2*Nd)*1/2*Nd*nsj)/((16*Pi^2)^2));

afX2[Nc_,Nd_,nfc_,nsc_,nfd_,nsd_,nfj_,nsj_]:=afX1[Nd,Nc,nfd,nsd,nfc,nsc,nfj,nsj];
afY2[Nc_,Nd_,nfc_,nsc_,nfd_,nsd_,nfj_,nsj_]:=afY1[Nd,Nc,nfd,nsd,nfc,nsc,nfj,nsj];
afZ2[Nc_,Nd_,nfc_,nsc_,nfd_,nsd_,nfj_,nsj_]:=afZ1[Nd,Nc,nfd,nsd,nfc,nsc,nfj,nsj];



setxfundamental[Nc_,Nd_,nfc_,nsc_,nfd_,nsd_,nfj_,nsj_]:=(Module[{model=List[Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj]},
		Return[List[afX1@@model,afY1@@model,afZ1@@model,afX2@@model,afY2@@model,afZ2@@model]]
	]);







(* Define the beta(g) functions *)

beta1[g1_,g2_,X1_,Y1_,Z1_,X2_,Y2_,Z2_]:=X1*g1^3+Y1*g1^5+Z1*g1^3*g2^2;
beta2[g1_,g2_,X1_,Y1_,Z1_,X2_,Y2_,Z2_]:=X2*g2^3+Y2*g2^5+Z2*g2^3*g1^2;




(* Define the coefficients for the beta(alpha)-functions *)

c[n1_,n2_,Nc_,Nd_,nfc_,nsc_,nfd_,nsd_,nfj_,nsj_]:=(
		Module[{x=setxfundamental@@{Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj} },
		
			x[[1]]=2*x[[1]]/(n1);   (* Potenzen von n1/n2 richtig? Faktor 2 in den Nenner? *)
			x[[2]]=2*x[[2]]/(n1^2);
			x[[3]]=2*x[[3]]/(n1*n2);
			x[[4]]=2*x[[4]]/(n2);
			x[[5]]=2*x[[5]]/(n2^2);
			x[[6]]=2*x[[6]]/(n2*n1);

			Return[x]

			]
		);

(*cinadifferentrepresentation[n1_,n2_,Nc_,Nd_,nfc_,nsc_,nfd_,nsd_,nfj_,nsj_]:=...*)


(* Define beta alpha functions *)

b1[a1_,a2_,X1_,Y1_,Z1_,X2_,Y2_,Z2_]:=X1*a1^2+Y1*a1^3+Z1*a1^2*a2;
b2[a1_,a2_,X1_,Y1_,Z1_,X2_,Y2_,Z2_]:=X2*a2^2+Y2*a2^3+Z2*a2^2*a1;


(* derivatives of the beta-functions (stability matrix) *)

d1b1[a1_,a2_,X1_,Y1_,Z1_,X2_,Y2_,Z2_]:=2*X1*a1+3*Y1*a1^2+2*Z1*a1*a2;
d2b1[a1_,a2_,X1_,Y1_,Z1_,X2_,Y2_,Z2_]:=Z1*a1^2;
d1b2[a1_,a2_,X1_,Y1_,Z1_,X2_,Y2_,Z2_]:=Z2*a2^2;
d2b2[a1_,a2_,X1_,Y1_,Z1_,X2_,Y2_,Z2_]:=2*X2*a2+3*Y2*a2^2+2*Z2*a1*a2;


(* fixed points *)

afix1a[X1_,Y1_,Z1_,X2_,Y2_,Z2_]:=Simplify[{0,0}];
afix2a[X1_,Y1_,Z1_,X2_,Y2_,Z2_]:=Simplify[{0,-X2/Y2}];
afix3a[X1_,Y1_,Z1_,X2_,Y2_,Z2_]:=Simplify[{-X1/Y1, 0}];
afix4a[X1_,Y1_,Z1_,X2_,Y2_,Z2_]:=Simplify[{	(Z1*X2-X1*Y2)/(Y1*Y2-Z1*Z2),
				 							(Z2*X1-X2*Y1)/(Y1*Y2-Z1*Z2)}];

End[]
EndPackage[]