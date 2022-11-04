# :cloud: Introduction
This package has been created because complex vertical merging or rowspan is limited in docxtpl.  
<br>   

# :round_pushpin: Select one to install
* download docxtpl_dynamic_vertical_merging.zip && `pip3 install docxtpl_dynamic_vertical_merging.zip`
* `pip3 install git+https://github.com/tsy19900929/docxtpl_dynamic_vertical_merging.git`
<br>

# :zap:Usage
Following code merges given column: **row1-3** into a group,  **row4-6** into a group,  **row7-9** into a group.  
`from docxtpldvm import DVM`  
`context = {`  
  `'t':range(1,10),`    
  `'B':DVM([(1,3),(4,6),(7,9)])`  
 `}` 

# :tv: Examples
:arrow_forward: test1  
<img src="https://github.com/tsy19900929/docxtpl_dynamic_vertical_merging/blob/main/test1.jpg" height="200" />   
:arrow_forward: test2  
<img src="https://github.com/tsy19900929/docxtpl_dynamic_vertical_merging/blob/main/test2.jpg" height="108" />
