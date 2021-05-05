# The CI metrics used in GP-CI-BUILD
 The table bellow lists the build metrics used to generate our prediction rules.
 
|Metric|Description|
|:---------:|--------|
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
