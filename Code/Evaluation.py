import json
import numpy as np


metric_list=[]
global a
a=0
#update location
# Dataset='/home/szs0239/Feature_Mining/Dataset/'
# Results_Directory='/home/szs0239/Feature_Mining/Results/Privacy Policy/Topic Embedding/'
#must be the locations where you saved EM word and sentence files
Directory="/Users/souvika/Library/CloudStorage/OneDrive-AuburnUniversity/Spring 2023/BanglaNLP/venv/Results/LASER/A3P2/"
# Results_Directory_Word='/home/szs0239/NewsConceptMining/Sentence Embedding/P2A2/'
# Results_Directory_Sentence='/home/szs0239/Feature_Mining/Results/Privacy Policy/Topic Embedding/Sentence/'
Dataset='/Users/souvika/Library/CloudStorage/OneDrive-AuburnUniversity/Spring 2023/BanglaNLP/venv/dataset/'
#Results_Directory='/Users/souvikasarkar/Documents/OneDrive - Auburn University/FeatureMining/Results/Covid/BERT/'
#Results_Directory_Word='/Users/souvikasarkar/Documents/OneDrive - Auburn University/FeatureMining/Results/News/Temp/Word/'


def Count_TP_FP_FN():
    # theta1=[]
    # precision1=[]
    # recall1=[]
    # f_measure1=[]
    # theta2=[]
    # precision2=[]
    # recall2=[]
    # f_measure2=[]
    #
    # with open(Results_Directory+"Evaluation_Medical_Hybrid_Sentence.json", "r") as f:
    #     key = json.loads(f.read())
    # with open(Results_Directory+"Evaluation_Medical_Hybrid_Word.json", "r") as f:
    #     key1 = json.loads(f.read())
    #
    # for j in range(len(key)):
    #     print(j)
    #     theta1.append(key[j]['Color Probability'])
    #     precision1.append(key[j]['Precision'])
    #     recall1.append(key[j]['Recall'])
    #     f_measure1.append(key[j]['F-Measure'])
    #     theta2.append(key1[j]['Color Probability'])
    #     precision2.append(key1[j]['Precision'])
    #     recall2.append(key1[j]['Recall'])
    #     f_measure2.append(key1[j]['F-Measure'])
    #
    # # ax = plt.subplots()
    #
    # Presicion = plt.figure()
    # plt.ylim(0, 1)
    # plt.xlim(0, 1)
    # plt.plot(theta1, precision1,label='EM_Word')
    # plt.plot(theta2, precision2,label='EM_Sentence')
    # plt.xlabel('Theta')
    # plt.ylabel('Precision')
    # plt.legend()
    # plt.show()
    # Presicion.savefig(Results_Directory+"Presicion.pdf", bbox_inches='tight')
    # Recall = plt.figure()
    # plt.ylim(0, 1)
    # plt.xlim(0, 1)
    # plt.plot(theta1, recall1,label='EM_Word')
    # plt.plot(theta2, recall2,label='EM_Sentence')
    # plt.xlabel('Theta')
    # plt.ylabel('Recall')
    # plt.legend()
    # plt.show()
    # Recall.savefig(Results_Directory+"Recall.pdf", bbox_inches='tight')
    # F_measure = plt.figure()
    # plt.ylim(0, 1)
    # plt.xlim(0, 1)
    # plt.plot(theta1, f_measure1,label='EM_Word')
    # plt.plot(theta2, f_measure2,label='EM_Sentence')
    # plt.xlabel('Theta')
    # plt.ylabel('F1 Measure')
    # plt.legend()
    # plt.show()
    # F_measure.savefig(Results_Directory+"F1 Measure.pdf", bbox_inches='tight')
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
    # with open(Directory+"Evaluation_News_EMR_Sentence_7.json", "r") as f:
    #     key3 = json.loads(f.read())
    # with open(Directory+"Evaluation_PrivacyPolicy_TR_Word.json", "r") as f:
    #     key4 = json.loads(f.read())
    # with open(Directory+"Evaluation_PrivacyPolicy_Hybrid_Sentence.json", "r") as f:
    #     key5 = json.loads(f.read())
    # with open(Directory+"Evaluation_PrivacyPolicy_Hybrid_Word.json", "r") as f:
    #     key6 = json.loads(f.read())
    # with open("Covid_Euclidean_Evaluation_Sentence_hybrid.json", "r") as f:
    #     key5 = json.loads(f.read())
    # with open("Covid_Cosine_Evaluation_Sentence_hybrid.json", "r") as f:
    #     key6 = json.loads(f.read())

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
        # theta3.append(key3[j]['Color Probability'])
        # precision3.append(key3[j]['Precision'])
        # recall3.append(key3[j]['Recall'])
        # f_measure3.append(key3[j]['F-Measure'])
        # theta4.append(key4[j]['Color Probability'])
        # precision4.append(key4[j]['Precision'])
        # recall4.append(key4[j]['Recall'])
        # f_measure4.append(key4[j]['F-Measure'])
        # theta5.append(key5[j]['Color Probability'])
        # precision5.append(key5[j]['Precision'])
        # recall5.append(key5[j]['Recall'])
        # f_measure5.append(key5[j]['F-Measure'])
        # theta6.append(key6[j]['Color Probability'])
        # precision6.append(key6[j]['Precision'])
        # recall6.append(key6[j]['Recall'])
        # f_measure6.append(key6[j]['F-Measure'])

    # ax = plt.subplots()

    Presicion = plt.figure()
    plt.ylim(0, 1)
    plt.xlim(0, 1)
    plt.plot(theta1, precision1, label='EM_Sentence')
    plt.plot(theta2, precision2, label='EM_Word')
    # plt.plot(theta3, precision3, label='EM-Sentence_7Concept')
    # plt.plot(theta3, precision4, label='TR_Word')
    # plt.plot(theta5, precision5,label='Hybrid_Sentence - Cosine')
    # plt.plot(theta6, precision6,label='Hybrid_Word - Cosine')
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
    # plt.plot(theta3, recall3, label='EM_Sentence_7Concept')
    # plt.plot(theta3, recall4, label='TR_Word')
    # plt.plot(theta5, recall5,label='Hybrid_Sentence - Cosine')
    # plt.plot(theta6, recall6,label='HHybrid_Word - Cosine')
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
    # plt.plot(theta3, f_measure3, label='EM_Sentence_7Concept')
    # plt.plot(theta3, f_measure4, label='TR_Word')
    # plt.plot(theta5, f_measure5,label='Hybrid_Sentence - Cosine')
    # plt.plot(theta6, f_measure6,label='Hybrid_Word - Cosine')
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
        # precision = 0
        # recall = 0
        # F_Measure = 0
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
        # print(metric_list[a]['Color Probability'])
        # a +=
  # Update json file name here to save the result      
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






