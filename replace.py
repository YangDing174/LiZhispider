from snownlp import SnowNLP
import xlrd
f = open('./LiZhi_news复工.txt','rb')
content = f.read().decode('utf-8')
s = SnowNLP(content)
words = s.words
f.close()

workBook = xlrd.open_workbook('./target.xlsx')
sheet1 = workBook.sheet_by_index(0)
dic = {}
for i in range(1, 27467):
    dic[sheet1.row(i)[0].value] = sheet1.row(i)[4].value


list_key = list(dic.keys())
for j in range(0,len(words)):
    if words[j] in list_key:
        words[j] = dic[words[j]]

feel_dic = {'PA':0,'PE':0,'PD':0,'PH':0,'PG':0,'PB':0,'PK':0,'NA':0,'NB':0,'NJ':0,'NH':0,'PF':0,'NI':0,'NC':0,'NG':0,'NE':0,'ND':0,'NN':0,'NK':0,'NL':0,'PC':0}
feel_key = list(feel_dic.keys())

t = open('LiZhi_news复工_替换后.txt','w',encoding='utf-8')
t.write("共有："+str(len(words))+'\n')
for key in feel_key:
    feel_dic[key]=words.count(key)
    t.write(key+":"+str(feel_dic[key])+'\n')
for item in words:
    t.write(item+'\n')
t.close()