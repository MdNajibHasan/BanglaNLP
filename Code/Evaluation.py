import json
import numpy as np


metric_list=[]
global a
a=0

Directory="/Users/souvika/Library/CloudStorage/OneDrive-AuburnUniversity/Spring 2023/BanglaNLP/venv/Results/LASER/A3P2/"
Dataset='/Users/souvika/Library/CloudStorage/OneDrive-AuburnUniversity/Spring 2023/BanglaNLP/venv/dataset/'



def Count_TP_FP_FN():
    theta1 = []
    precision1 = []
    recall1 = []
    f_measure1 = []
    theta2 = []
    precision2 = []
    recall2 = []
    f_measure2 = []
    theta3 = []
    precision3 = []
    recall3 = []
    f_measure3 = []
    theta4 = []
    precision4 = []
    recall4 = []
    f_measure4 = []
    theta5 = []
    precision5 = []
    recall5 = []
    f_measure5 = []
    theta6 = []
    precision6 = []
    recall6 = []
    f_measure6 = []

    with open(Directory+"Evaluation_Covid_EM_Sentence.json", "r") as f:
        key1 = json.loads(f.read())
    with open(Directory+"Evaluation_Covid_EM_Word.json", "r") as f:
        key2 = json.loads(f.read())

    for j in range(len(key1)):
        print(j)
        theta1.append(key1[j]['Color Probability'])
        precision1.append(key1[j]['Precision'])
        recall1.append(key1[j]['Recall'])
        f_measure1.append(key1[j]['F-Measure'])
        theta2.append(key2[j]['Color Probability'])
        precision2.append(key2[j]['Precision'])
        recall2.append(key2[j]['Recall'])
        f_measure2.append(key2[j]['F-Measure'])
        

    Presicion = plt.figure()
    plt.ylim(0, 1)
    plt.xlim(0, 1)
    plt.plot(theta1, precision1, label='EM_Sentence')
    plt.plot(theta2, precision2, label='EM_Word')
    plt.xlabel('Theta')
    plt.ylabel('Precision')
    plt.legend()
    plt.show()
    Presicion.savefig(Directory+"Presicion_Covid.pdf", bbox_inches='tight')
    Recall = plt.figure()
    plt.ylim(0, 1)
    plt.xlim(0, 1)
    plt.plot(theta1, recall1, label='EM_Sentence')
    plt.plot(theta2, recall2, label='EM_Word')
    plt.xlabel('Theta')
    plt.ylabel('Recall')
    plt.legend()
    plt.show()
    Recall.savefig(Directory+"Recall_Covid.pdf", bbox_inches='tight')
    F_measure = plt.figure()
    plt.ylim(0, 1)
    plt.xlim(0, 1)
    plt.plot(theta1, f_measure1, label='EM_Sentence')
    plt.plot(theta2, f_measure2, label='EM_Word')
    plt.xlabel('Theta')
    plt.ylabel('F1 Measure')
    plt.legend()
    plt.show()
    F_measure.savefig(Directory+"F1 Measure_Covid.pdf", bbox_inches='tight')



def Evaluate_Inferred_Concepts():


  with open(Dataset+"NewsBlog_ProthomAlo_FinalDataset.json", "r") as f:
    data = json.loads(f.read())
  print("inside evaluation")
  for i in np.arange(0.0, 1.0, 0.05):
        filename= str(i)+'_BanglaNews Data-set_annotated_A3P2.json'
        # filename1=str(i)+'_Evaluation.json'
        print(filename)
        TP = 0.0
        FP = 0.0
        FN = 0.0
        for j in range(len(data)):
            print("Article Number::", j, "Threshold::", i)
            with open(Directory+filename, "r") as f:
                key = json.loads(f.read())
            metric_dict = {}
            ActualConcept = set([])
            ActualConcept.update(data[j]['Article Topics'])
            InferredImplicitFeatureSet = set([])
            InferredImplicitFeatureSet.update(key[j]['Inferred Article Topic'])
            TP += len(InferredImplicitFeatureSet.intersection(ActualConcept))
            FP += len(InferredImplicitFeatureSet - ActualConcept)
            FN += len(ActualConcept - InferredImplicitFeatureSet)
        try:
                precision = (TP / (TP + FP))
        except:
                precision = 0
        try:
                recall = (TP / (TP + FN))
        except:
                recall = 0
        try:
                F_Measure = (2 * (precision * recall) / (precision + recall))
        except:
                F_Measure = 0
        metric_dict['Color Probability'] = i
        print(i)
        metric_dict['True Positive Count'] = TP
        print(TP)
        metric_dict['False Positive Count'] = FP
        print(FP)
        metric_dict['False Negative Count'] = FN
        print(FN)
        metric_dict['Precision'] = precision
        metric_dict['Recall'] = recall
        metric_dict['F-Measure'] = F_Measure
        metric_list.append(metric_dict)     
  with open(Directory+"Bengali_Laser_Zero-shot_A3P2_Evaluation.json", 'w+') as f:
       print("writing json")
       json.dump(metric_list, f, indent=4, separators=(',', ':'))

  with open(Directory + 'Bengali_Laser_Zero-shot_A3P2_Evaluation_Summary.csv', 'w') as Summaryfile:
      Summaryfile.write('Color Probability,True Positive Count,False Positive Count,False Negative Count,Precision,Recall,F_measure\n')
      for x in range(0, len(metric_list)):
          Summaryfile.write(str(metric_list[x]['Color Probability']) + ',' + str(metric_list[x]['True Positive Count']) + ',' + str(metric_list[x]['False Positive Count']) + ',' + str(
              metric_list[x]['False Negative Count']) + ',' + str(metric_list[x]['Precision']) + ',' + str(metric_list[x]['Recall'])+ ',' + str(metric_list[x]['F-Measure'])+'\n')



Evaluate_Inferred_Concepts()
# Count_TP_FP_FN()






