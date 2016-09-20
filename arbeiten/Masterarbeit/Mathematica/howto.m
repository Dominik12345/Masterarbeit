
(* Import Packages *)
	 
	Get["Documents/QCDxdQCD/Mathematica/Packages/Fixedpoint'.m"]
	Get["Documents/QCDxdQCD/Mathematica/Packages/Beta'.m"]


(* Always Clear variables *)

	Clear[afix,coeff,norm,model];


(* frequently used Lists *)

	norm={1,1}; (*alpha=norm g^2*)
	model={3,3,6,0,6,0,1,0}; (*={Nc,Nd,nfc,nsc,nfd,nsd,nfj,nsj}*)


(* coefficients of the beta (alpha)-functions*)

	coeff=c@@Join[norm,model];


(* findfixedpoints searches for roots of the beta(alpha)-functions 
	corresponding to given coefficients *)

	afix=findfixedpoints@@coeff


(* isfixedpoint and uvcheck check wether the fixedpoints are 
	uv or not. Computes the stability matrix and eigenvalues.
	Assumtion: eigenvalues both neg <=> uv-fixedpoint *)
	
	isfixedpoint@@Join[{alpha1,alpha2},coeff]
	uvcheck@@Join[{afix},coeff]]


(* truncations for the findmodels-function *)

	min={3,3,6,0,6,0,0,0}
	max={3,3,6,0,6,0,2,0}
	possiblemodels=findmodels[norm,min,max]