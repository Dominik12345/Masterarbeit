BeginPackage[ "Extrapolation`" ]

Get["Documents/QCDxdQCD/Mathematica/Packages/Beta'.m"]
Get["Documents/QCDxdQCD/Mathematica/Packages/Fixedpoint'.m"]


stabilitymatrix::usage="Returns the stabilitymatrix at (a1,a2) with
					coefficients X1,...,Z2"
saddlepointextrapolation::usage="extrapolates the separatrix emanating 
					from a saddlepoint, returns aextra (extrapolated 
					fixed point).
					Parameters:a1,a2,X1,...,Z2,amz={afix,coeff,alpha_QCD at
					mass_Z"

testsaddlepointextrapolation::usage="tests the deviation of the extrapolated 
					amz from
					the fixedpoint"




testfunction::usage="checks wether a point (xi1,xi2) in the (alpha1 x alpha2) 
					plane flows into the gaussian or infinity.
					Parameters:xi1,xi2,coeff(=X1,...,Z2)"


Begin["`Private`"]


stabilitymatrix[a1_,a2_,x1_,y1_,z1_,x2_,y2_,z2_]:=(
	Return[{{d1b1@@{a1,a2,x1,y1,z1,x2,y2,z2},
			d2b1@@{a1,a2,x1,y1,z1,x2,y2,z2}},
			{d1b2@@{a1,a2,x1,y1,z1,x2,y2,z2},
			d2b2@@{a1,a2,x1,y1,z1,x2,y2,z2}}}];
);

saddlepointextrapolation[a1_,a2_,X1_,Y1_,Z1_,X2_,Y2_,Z2_,amz_]:=
	Catch[( 

		Module[{afix={a1,a2},aextra ,tau,tauextra,
				var={a1,a2,X1,Y1,Z1,X2,Y2,Z2},eigen,direction},
			

			If[!isfixedpoint@@var,
				 Throw["not a fixed point"];
			];

			eigen = Eigensystem[stabilitymatrix@@var]; 
			Which[
				(eigen[[1,1]]>0 && eigen[[1,2]]>0)||(eigen[[1,1]]<0 && 
					eigen[[1,2]]<0), Throw["not a saddlepoint (at O(db/da)"],
				eigen[[1,1]]<0||eigen[[1,2]]>0, direction=eigen[[2,1]],
				eigen[[1,2]]<0||eigen[[1,1]]>0, direction=eigen[[2,2]]
			];
			tauextra = Simplify[(tau/.Solve[
				Rationalize[(afix+tau*direction)[[1]]==amz],
				tau,Reals])[[1]] ];
			aextra =Simplify[ afix+ tauextra*direction ];
			If[aextra[[1]]>=0 && aextra[[2]]>=0,
				Throw[aextra];,
				Throw["nicht physikalisch"];
			];
		];
	)];


testsaddlepointextrapolation[a1_,a2_,X1_,Y1_,Z1_,X2_,Y2_,Z2_,amz_]:=(
	Module[{afix={a1,a2},aextra, coeff={X1,Y1,Z1,X2,Y2,Z2},tau, tautest },
		aextra = saddlepointextrapolation@@Join[afix,coeff,{amz}];
	tautest=(tau/.Solve[Rationalize[(aextra+tau*{b1@@Join[aextra,coeff],
		b2@@Join[aextra,coeff]})[[2]]==a2],
		tau,Reals])[[1]];


		Return[Simplify[afix-(aextra+tautest*{b1@@Join[aextra,coeff],
			b2@@Join[aextra,coeff]})]]; 
	];
);
	



(* ---> Separatrix ---> *)
Clear[testfunction];

testfunction[xi1_,xi2_,x1_,y1_,z1_,x2_,y2_,z2_]:=(
	solution = {c1,c2}/.NDSolve[
			{c1'[t]  == b1@@Join[{c1[t],c2[t]},coeff ],
			 c2'[t]  == b2@@Join[{c1[t],c2[t]},coeff ],
			 c1[0] == xi1,
			 c2[0] == xi2 },
		
			{c1,c2},
			
	 		{t, 0, 10}
	  	];
	Return[solution[[1]] ];
);








(* <--- Separatrix <--- *)







End[]
EndPackage[]