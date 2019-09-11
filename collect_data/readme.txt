this part is pure python3, 
package requirments
"networkx"
-------------
This code part(generate_graph_code) provide a way to 
(1) generate 10D properties and graphs by given a generator name
(2) compute 10D proerties for the total set of non-isomorphic graphs for fixed vertex.

You can either call generateGraphSet.py from other code or directly run it(changing code in if __main__ part)
I provide examples for (1) and (2) in if __main__ part

-------------
the data part(generator_data) provide part of our experiments
we provide some of the generaotr_set in(graph_properties). 
It is recommanded to generate from code and store it 

-------------
Noted the ground-truth dataset is in find_find_same_stat_graph_set/data/gt

the reason seperate it out from data folder is because the web need to seft-contain, it won't run without the data
