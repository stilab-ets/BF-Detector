import os
import pandas as pd
from sklearn.naive_bayes import GaussianNB 
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import recall_score
from sklearn.metrics import roc_auc_score
from imblearn.over_sampling import SMOTE
import math
from sklearn.preprocessing import StandardScaler

initialized_models = {#"decision_tree" : DecisionTreeClassifier(max_depth=10)}
                     # "random_forest" : RandomForestClassifier(n_estimators=200, max_depth=5),
                     "naive_bayes" : GaussianNB()} 
#defining dataframe
#it will be used to save results
results = pd.DataFrame(columns = ["proj"]+ ["algo"]+["iter"]+["exp"]+["F1"]+["precision"]+["recall"]+["tnr"]+["fnr"]+["accuracy"]
                       +["G"]+["auc"]+["Gmean"]+["balance"])
target_column = "build_failed"
for file_name in os.listdir("."): 
  if "train"  in file_name  :
    #reading train and test data
    train_df = pd.read_csv(file_name)
    test_df  = pd.read_csv(file_name.replace("train","test"))
    X_train = train_df.drop(columns=[target_column])
    X_train = X_train.iloc[:, :].values
    y_train = train_df[target_column]
    
    X_test = test_df.drop(columns=[target_column])
    X_test = X_test.iloc[:, :].values
    y_test = test_df[target_column]
     #Try preprocess
    sc = StandardScaler()
    X_train[:, 2:20] = sc.fit_transform(X_train[:, 2:20] )
    X_test[:, 2:20]  = sc.transform(X_test[:, 2:20] )
     #Try oversampling
    X_train, y_train = SMOTE().fit_resample(X_train, y_train)

    #intilizing models for training 
    models = initialized_models
    for i in range (0,31):
        for model_name in models : 
          #print("training model "+model_name+" for project "+  file_name.replace("train","").replace(".csv",""))
          models[model_name].fit(X_train,y_train)
          #y_train_pred = models[model_name].predict(X_train)
          y_test_pred = models[model_name].predict(X_test)
          # Compute confusion matrix
          tn, fp, fn, tp  = confusion_matrix(y_test,y_test_pred).ravel()
          entry = {}
          entry["algo"] = model_name
          entry["iter"] = i
		  entry["fpr"] = fp/ (fp+tn)
          entry["exp"] = (file_name.replace("train","").replace(".csv",""))[-6:-1]
          entry["proj"] = (file_name.replace("train","").replace(".csv",""))[:-6]
          entry["auc"] = roc_auc_score(y_test,y_test_pred)
		  entry["recall"] = recall_score(y_test,y_test_pred)
          entry["balance"] = 1.0 - math.sqrt(math.pow(entry["fpr"], 2) + math.pow(1 - entry["recall"],2)) / math.sqrt(2);
          results = results.append(entry,ignore_index=True)
    print(file_name,"-----------------------------")
results.to_excel("results_ML.xlsx")