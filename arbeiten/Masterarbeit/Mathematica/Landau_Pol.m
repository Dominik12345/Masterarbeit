Get["Documents/QCDxdQCD/Mathematica/Packages/Beta'.m"]


Clear[mz,Lambda,LambdaQCD,alpha0, nfc, Nc,n1,n2,X1,Y1,
	betafunction,mu,c1,c2 ,coeff,A, kappa];

(* CONSTANTS *)


mz = 91187.6; (*in MeV*)
alpha0  = 0.1185;



(* ---SETUP---> *)


	model = {Nc ,Nd, nfc, nsc,nfd,nsc,nfj,nsj};
	norm	= {1/(4*Pi), 1/(4*Pi)};

	Nc 		= 3;
	Nd    	= 2;
	nfc     = 6;
	nsc		= 0;
	nfd		= 0;
	nsc		= 0;
	nfj		= 0;
	nsj		= 0;

	coeff = c@@Join[norm,model];


	(* define beta function--->*)

		X1 = coeff[[1]];
		Y1 = coeff[[2]];
		(*usw*)


		betafunction[alpha_]:=( X1 * alpha^2 + Y1 *alpha^3 ); 

	(*<--- define beta function*)


(* <---SETUP--- *) 




(* CALCULATION --->*)

	(*calculate the A --->*)
		
	A[alpha_]:= (Integrate[ 1/(betafunction[x]), x])/.{
					x->alpha};

	(*<---calculate the A*)


	(*calculate the scale--->*)

	tInf =Simplify[ Limit[A[x], x->Infinity] - A[alpha0] ];
	Lambda = mz; (*to have t0 = 0*)
	kappa = 1; (* Korrekturfaktor falls alpha(m^2) *)
	muInf = Simplify[Lambda * Exp[tInf/kappa] ];

	(*<---calculate the scale*)

(* <--- CALCULATION *)


 






	Print[StringJoin["beta = ", ToString[ betafunction[alpha] ] ] ];
	Print[StringJoin["A = ", ToString[ A[alpha] ] ] ];
	Print[StringJoin["X1 = ", ToString[ N[X1] ] ] ];
	Print[StringJoin["Y1 = ", ToString[ N[Y1] ] ] ];
	Print[StringJoin["LambdaQCD = ", 
		ToString[ N[muInf] ], "Mev" ] 
	];

