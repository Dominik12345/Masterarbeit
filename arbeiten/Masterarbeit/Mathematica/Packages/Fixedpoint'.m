BeginPackage["Fixedpoint`"]
Get["Documents/QCDxdQCD/Mathematica/Packages/Beta'.m"]

findfixedpoints::usage="searches for fixedpoints of the RG-flow (i.e. roots of
			the beta(alpha)-functions.Parameters:X1,Y2,Z1,X2,Y2,Z2=c";


isuvfixedpoint::usage="checks eigenvalues of db/da at {a1,a2}.
			Returns: 'source', 'sink', 'saddle', 'indefinite', 
			'semi-source', 'semi-sink', 'zeroes' as a String. 
			Parameter:a1,a2,X1,Y1,Z1,X2,Y2,Z2={a,c}";
uvcheck::usage="checks for negative eigenvalues of the stabilitymatrix and 
			returns the fixedpoints which pass 'isuvfixedpoint'.
			Parameters:afix={{a1,a2},{b1,b2},...},{X1,Y1,Z1,X2,Y2,Z2}=c
			Bem:@@Join[{afix},coeff]";

findmodels::usage="searches for models with UV-fixedpoint within 
			a given truncation of models, min and max. Returns
			List of { {model,afix}, ...}.
			Parameters:norm, min, max;where min,max={Nc,Nd,...,nsj}"

isfixedpoint::usage="checks wether afix={alpha1^*,alpha2^*} is a 
			fixed point. 
			Parameters: alpha1,alpha2,X1,Y2,Z1,X2,Y2,Z2"


Begin["`Private`"]

isfixedpoint[a1_,a2_,x1_,y1_,z1_,x2_,y2_,z2_]:=(
			Simplify[b1[a1,a2,x1,y1,z1,x2,y2,z2]]==0 
		&&	Simplify[b2[a1,a2,x1,y1,z1,x2,y2,z2]]==0
	);

findfixedpoints[x1_,y1_,z1_,x2_,y2_,z2_]:=(
		Module[{solution,arguments,a1,a2,list=List[]},

			arguments={a1,a2,x1,y1,z1,x2,y2,z2};

			solution=Solve[b1@@arguments==0 &&
							b2@@arguments==0 &&
							a1>=0 && a2 >=0,
							{a1,a2}
						];
Print[solution]
			

			Do[list=Append[list,{a1,a2}/.solution[[i]]],
				{i,Length[solution]}
				];

			Return[list];

			];
	);





isuvfixedpoint[a1_,a2_,x1_,y1_,z1_,x2_,y2_,z2_]:=(
		Module[{stab},

				stab={	{	d1b1[a1,a2,x1,y1,z1,x2,y2,z2],
							d2b1[a1,a2,x1,y1,z1,x2,y2,z2]	},
				
						{	d1b2[a1,a2,x1,y1,z1,x2,y2,z2],
							d2b2[a1,a2,x1,y1,z1,x2,y2,z2]	}
					};
Print[stab]

				Return[
					Which[	
							Tr[stab] > 0 && Det[stab] > 0,"source",
							Tr[stab] < 0 && Det[stab] > 0,"sink",
											Det[stab] < 0,"saddle",
							Tr[stab] == 0 && Det[stab] > 0,"indefinite",
							Tr[stab] > 0 && Det[stab] == 0,"semi-source",						
							Tr[stab] < 0 && Det[stab] == 0,"semi-sink",
							Tr[stab] == 0 && Det[stab] == 0,"zeroes"							
						]

					]
				
			];
	);




uvcheck[afix_,x1_,y1_,z1_,x2_,y2_,z2_]:=(
	
	Module[{sinklist=List[], saddlelist=List[],coeff={x1,y1,z1,x2,y2,z2}},
		
		Do[
			If[	isuvfixedpoint@@Join[afix[[i]],coeff]=="sink"  ,
				sinklist=Append[sinklist,afix[[i]]]
				];
			If[	isuvfixedpoint@@Join[afix[[i]],coeff]=="saddle",
				saddlelist=Append[saddlelist,afix[[i]]]
				],
			{i,Length[afix]}
			];
		Return[{sinklist,saddlelist}]
		];
	);



findmodels[norm_,min_,max_]:=(
	Module[{sinkmodels=List[],saddlemodels=List[]},
		Do[
			Module[{model={i1,i2,i3,i4,i5,i6,i7,i8},afix,coeff},
						coeff=c@@Join[norm,model];
						afix=findfixedpoints@@coeff;
						afix=uvcheck@@Join[{afix},coeff];
						If[Length[afix[[1]]]>0,sinkmodels=Append[sinkmodels,{model,afix[[1]]}]];
						If[Length[afix[[2]]]>0,saddlemodels=Append[saddlemodels,{model,afix[[2]]}]]
					],
			{i1,min[[1]],max[[1]]},
			{i2,min[[2]],max[[2]]},
			{i3,min[[3]],max[[3]]},
			{i4,min[[4]],max[[4]]},
			{i5,min[[5]],max[[5]]},
			{i6,min[[6]],max[[6]]},
			{i7,min[[7]],max[[7]]},
			{i8,min[[8]],max[[8]]}
				];
		Return[{sinkmodels,saddlemodels}]
			];
	);









End[]
EndPackage[]