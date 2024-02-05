# General info
BF-Detector is a powerful tool written in Java that can detect Travis CI failed builds based on the history of the project.
For a detailed description of the tool and its associated research work, you can refer to the following research papers *On the Prediction of Continuous Integration Build FailuresUsing Search-Based Software Engineering* and *Predicting Continuous Integration Build Failures Using Evolutionary Search*

A demonstration video is available at: 

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/E9HPErvT3Sw/0.jpg)](https://www.youtube.com/watch?v=E9HPErvT3Sw&ab_channel=IslemSaidani)

# How to use it ?
First, you need to download the jar file from this link https://github.com/stilab-ets/BF-Detector/blob/main/BF-Detector.jar. Do NOT download it from ZIP (the code button above) because it will be corrupted and cannot be used.
 
This tool needs a Github project that uses Travis CI to work. We recommend to launch it with Java 10. 
1. the Graphviz visualization tool should be downloaded from https://graphviz.org/download/#windows and saved under *C:/Program Files/*
2. To launch the analysis of a project, you have to define:
	1. the project URL: it can be the Github URL or a the local directory to the GIT project.
	2. the commit(s) to be analysed
	3. TRUE/FALSE: Decision to work with cross-project option i.e. using existing rules generated from our database
2. The tool displays the prediction in the command line console.
3. To get more details, the user can have a look at the explanation (a PDF file)
# Example of usage
You can use this tool based on a cross-project prediction, for example :
```
java -jar BF-Detector.jar https://github.com/mitchellh/vagrant d95dad9a79af220d11de7c91c61b456b819b8f27 T
```

# The used CI metrics
 The table bellow lists the build metrics used to generate our prediction rules.
 
|Metric|Description|
|--------|--------|
|NC|# of commits contained in this single build|
|ND|# of changed directories|
|NS|# of changed systems|
|src_churn|# of lines of code changed in all built commits|
|test_churn|# of lines of test code changed in all built commits|
|ConfigF|# of configuration files|
|maintC|# of maintenance commits|
|fixC|# of fixing commits|
|srcF|# of source files|
|docF|# of documentation files|
|mergeC|# of merge files|
|otherF|# of other files|
|buildF|# of build files|
|FilesA|# of added files|
|FilesM|# of modified files|
|FilesD|# of deleted files|
|BMsg|Measures the importance of terms appearing in the commit message using TF-IDF|
|classif_build|Feature Addition (1), Corrective (2), Merge (3), Perfective (4), Preventative (5), Non-Functional (6), None (7)|
|entropy|Measures the distribution of the change across the different files|
|TFC|# of the changed files' types identified by their extension|
|NUC|# of unique last commits of the modified files|
|NDEV|# of unique committers|
|EXP|the average # of commits made by the committers before the current build|
|elapsed_days|Counts the days since last build|
|same_committer|Indicates whether the committer is the same as last build|
|proj_fail_rate_history|The fail rate of the all the project’s previous build|
|proj_fail_rate_recent|Similar to project fail history but using only last five builds|
|comm_fail_rate_history|The fail rate of the builds by the current committer in the past|
|comm_fail_rate_recent|Similar to committer history, but measuring only his last five builds |
|prev_build_result|Result of last build|
|day_week|Day of week of the first commit for the build|

# How to cite?

Please, use the following bibtex entries:

```tex
@inproceedings{saidani2021bf,
  title={BF-detector: an automated tool for CI build failure detection},
  author={Saidani, Islem and Ouni, Ali and Chouchen, Moataz and Mkaouer, Mohamed Wiem},
  booktitle={29th ACM Joint Meeting on European Software Engineering Conference and Symposium on the Foundations of Software Engineering},
  pages={1530--1534},
  year={2021}
}

@article{saidani2021predicting,
  title={Predicting Continuous Integration Build Failures Using Evolutionary Search},
  author={Saidani, Islem and Ouni, Ali and Chouchen, Moataz and Mkaouer, Mohamed Wiem},
  journal={Journal of Information and Software Technology},
  volume={128},
  year={2021},
  publisher={Elsevier}
}
```
