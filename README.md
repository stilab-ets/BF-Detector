# General info
GP-CI-BUILD is a powerful tool written in Java that can detect Travis CI failed builds based on the history of the project.
For a detailed description of the tool and its associated research work, you can refer to the following research papers *GP-CI-Build: A Tool for CI build Failures Detection* and *Predicting Continuous Integration Build Failures Using Evolutionary Search*
# How to use it ?
This tool needs a Github project that uses Travis CI to work. We recommend to launch it with Java 10. 
1. the Graphviz visualization tool should be downloaded from https://graphviz.org/download/#windows and saved under *C:/Program Files/*
2. To launch the analysis of a project, you have to define:
	1. the project URL: it can be the Github URL or a the local directory to the GIT project.
	2. the commit(s) to be analysed
	3. TRUE/FALSE: Decision to work with cross-project option i.e. using existing rules generated from our database
2. The tool displays the prediction in the command line console.
3. To get more details, the user can have a look at the explanation (a PDF file)
# Example of usage
Then you can use this tool based on a cross-project prediction, for example :
```
java -jar gp-ci-build.jar https://github.com/mitchellh/vagrant d95dad9a79af220d11de7c91c61b456b819b8f27 T
```
