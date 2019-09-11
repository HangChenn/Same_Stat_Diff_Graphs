package requirments

This small server mainly use "python 3".
please have "networkx", "numpy" and "Flask" installed

-----------
run instruction


python App.py
http://127.0.0.1:4000/
-----------
Usage instruction

In this website, you can choose some graph properties to fix, and vary one graph property. 
Noted vertex number is one graph proprity must fixed.

For example,
|V| = 9, vary GCC,
APL 	min: 0.41, 	max: 0.52
diam 	min: 0.375, max: 0.375
r 		min: -0.29, max: -0.22
Cv 		min: 0.25, 	max: 0.25
Ce 		min: 0.25, 	max: 0.25

and press submit, will give you GCC with 10 slots, from 0-0.1, 0.1-0.2 ... 0.9-1


You can also try a larger |V|, e.g. |V| = 50, 100.
But this tool will not guarantee to find one such set. And we don't know is it not exist or not lucky enough.
we set a 'clock_time' for each slot. you can modify it(In findGraph.py)

--

alternatively, you can also fix several graph properties without vary any graph property
this will return a set of graph with similar graph properties you fixed.

For example,
|V| = 9, 
GCC 	min: 0, 	max: 0
ACC 	min: 0, 	max: 0
SCC		min: 0, 	max: 0
APL		min: 0.63, 	max: 0.64
r 		min: -0.48,	max: -0.47
diam 	min: 0.5, 	max: 0.5
den 	min: 0.27, 	max: 0.28
Rt 		min: 0, 	max: 0
Cv 		min: 0.12, 	max: 0.13
Ce 		min: 0.12, 	max: 0.13


