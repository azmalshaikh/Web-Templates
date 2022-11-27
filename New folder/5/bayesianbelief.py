class Node:
    name=''
    cpt=[]
    pt=[]
    parent=[]
    def __init__(self,name,cpt,pt,parent):
        self.name=name
        self.cpt=cpt
        self.pt=pt
        self.parent=parent
    def printNode(self):
        print(self.name)
        print('=================================')
        print("Conditional Probability=>",self.cpt)
        print("Probability=>",self.pt)
        print("Parents=>",self.parent)
        print('=================================')

graph=[]
atmos_pres=Node('Atmospheric Pressure',[],[0.4,0.6],[])
graph.append(atmos_pres)
season=Node('Season',[],[0.3,0.7],[])
graph.append(season)
rain=Node('Rain',[[0.1,0.2],[0.1,0.6]],[],[1,0])
graph.append(rain)
allergy=Node('Allergy',[[0.02,0.08],[0.2,0.7]],[],[2,1])
graph.append(allergy)
crop_fail=Node('Crop Failure',[[0.3,0.7]],[],[2])
graph.append(crop_fail)

for node in graph:
    node.printNode()

def fillProbT(node):
    if len(node.pt) != 0:
        return node.pt
    parent_pts=[]
    for i in node.parent:
        parent_pts.append(fillProbT(graph[i]))
    #print(node.name,parent_pts)
    probab=0
    i=0
    for row in node.cpt:
        for elem in row:
            probab+=elem*getProb(parent_pts,0,i)
            i+=1
    node.pt.append(1-probab)
    node.pt.append(probab)
    #node.printNode()
    return node.pt

def getProb(parent_pts,pt,i):
    if pt==len(parent_pts):
        return 1
    idx=0
    if (1<<pt)&i != 0:
        idx=1
    return parent_pts[pt][idx]*getProb(parent_pts,pt+1,i)

for node in graph:
    fillProbT(node)

for node in graph:
    node.printNode()

#P(allergy^rain^season)=P(allergy|rain,season)*P(rain)*P(season)
probab_allergy_rain_season=graph[3].cpt[1][1]*graph[2].pt[1]*graph[1].pt[1]
print("Probability of allergy due to rain and change of season=>",probab_allergy_rain_season)