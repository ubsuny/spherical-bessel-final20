# ReadMe for Eigenfrequencies of a Spherical Electromagnetic Cavity

## Physics Background
The physics background information, including the derivation of the problem, as well as research on various computational techniques can be found in the "Report/Wiki" pdf file. This pdf was rendered using Latex as opposed to markdown due to the amount of Latex used within the document. Since github markdown does not have Latex support, this file stands in place of the github wiki. The pdf should be complete with hyperlinks so as to make your reading as easy as possible.
### Informaiton on Compiling
Personally I choose to use [Overleaf](www.overleaf.com) as a free web client to compile my latex documents. Uploading the latex source files found in the "Latex Source" folder to overleaf should immediately produce a copy of the compiled pdf without any needs to adjust settings. In the event that the user would prefer a local latex compiler, there are many solutions avaiable. The document should not include any _exotic_ packages that would not be present in the standard distributions of Latex. 

The structure of the document is as follows:
* Main.tex is the primary latex file that should be compiled.
* Structure.tex holds most of the preamble for the latex document. It contains all of the packages used, document settings, custom sections, custom headers and footers, and custom mathematics commands.
* Sources.bib is a bibtek file for all of the sources used.
* Content.tex is the _meat and potatoes_ of the document. It contains all of the material that is rendered with non of the formatting.

## Personal Implementation
The Implementation folder contains my implementation of computing the zeros of Spherical Bessel functions, which were shown to be the Eigenfrequencies of these Spherical conducting cavities. The jupyter notebook calls upon various libraries as well as the python files in the implementation folder. Otherwise this is a self contained document and does not need any input files. The user can adjust the parameters in the "visualizing" section to change the norder of Bessel functions displayed.

Finally the true highlight of this implementation is the "Higher Order Roots" section in which the parameters can be adjusted to find the nth root of a lth order Bessel.
