######################################
########0)Set up permutations#########
######################################

#####UPDATE ALLCLASSASSIGNMENTS EVER LOOP

import itertools
import math
import random
import sys

permutations=[]
sublist=[]
allClassAssignments=[[],[],[],[],[],[]]

for x in itertools.permutations('1'):
    sublist.append(x)
permutations.append(sublist)
sublist=[]
for x in itertools.permutations('12'):
    sublist.append(x)
permutations.append(sublist)
sublist=[]
for x in itertools.permutations('123'):
    sublist.append(x)
permutations.append(sublist)
sublist=[]
for x in itertools.permutations('1234'):
    sublist.append(x)
permutations.append(sublist)
sublist=[]
for x in itertools.permutations('12345'):
    sublist.append(x)
permutations.append(sublist)
sublist=[]
for x in itertools.permutations('123456'):
    sublist.append(x)
permutations.append(sublist)
sublist=[]

##########################
########1) Objects###########
##########################

class Teacher(object):
    def __init__(self, name, subjects,teacherNumber,restrictions):     #Initalizes teacher
        self.name=name
        self.subjects=subjects
        self.iteration=0;
        self.newSubjects=subjects
        self.teacherNumber=teacherNumber
        self.restrictions=[]
        if restrictions:
            for i in range(1,len(restrictions)):
                self.restrictions.append(restrictions[i])
        
    #def periodRestriction(self, period):     #Restricts teacher from teaching at a particular period
    #    self.restrictions.append(period)
    def getName(self):                      #Returns name
        return self.name
    def getSubjects(self):                  #Returns subjects
        return self.subjects
    def getSubject(self, index):           #Returns particular subject
        self.arrangeSubjects()
        return self.subjects[index]
    def getIteration(self):                 #Returns iterations
        return self.iteration
    def iterate(self):                      #Increments iterations
        self.iteration=self.iteration+1
    def backTrack(self):                    #Decrements iterations
        self.iteration=self.iteration-1
    def clearIterations(self):              #Clears iterations
        self.iteration=0
        ##Clear subject period assignments
        for i in range(0,len(self.subjects)):
            self.subjects[i].setPeriod(-1)
    def finalIteration(self):               #Tests for final iteration

        #if self.iteration==math.factorial(len(self.subjects)):
            #print("Final iteration at: " + str(self.iteration))
            #numberOfSubjects=len(self.subjects)
            #print(permutations[numberOfSubjects-1][self.iteration])
        if self.iteration==720:
            return True
        else:
            return False
    def lackingTogetherness(self):      #Check no problem with other periods that this class should be with
        #Need to check for no previous classes scheduled
        togethernessCounter=0
        classesPreviouslyScheduled=0
        for j in range(0,len(self.subjects)):
            if self.subjects[j].together!=[]:   #Check if class must be with another class
                togethernessCounter+=1
                togetherPeriod=self.subjects[j].getPeriod()
                ##Check for one together class at same time
                for i in range(0,len(allSubjects)):
                    if self.subjects[j].together==allSubjects[i].getName():
                        if allSubjects[i].getPeriod()!=-1:
                            classesPreviouslyScheduled+=1
                        if togetherPeriod==allSubjects[i].getPeriod():
                            togethernessCounter-=1    #Together class schedule at this period          
        if togethernessCounter==0 or classesPreviouslyScheduled==0:      #No classes need to be scheduled together
            return False
        else:
            return True     #No schedule classes were found

        

    def conflict(self):                     #Tests for conflict
        self.arrangeSubjects()
        ##1) Check for required corresponding classes##
        if self.lackingTogetherness()==True:   #If togetherness conflict, return true
            return True
        numberOfSubjects=len(self.subjects)
        ##2) Test for restrictions##
        for i in range(0,numberOfSubjects): #Test for period restrictions
            if str(self.subjects[i].getPeriod()) in self.restrictions:
                return True

        ##3) Test for first teacher##    
        if self.name==teachers[0].getName(): #Aside for restrictions, no conflict for first teacher
            return False

        
        ##4) Check for too many classes at once per grade##
        #Get all core subjects and check for any period that has more than three grade and core classes
        #currentPeriodAssignments.checkForGradeOrCoreOverlaps()
        for grade in range(0,6):    #Iterate through grades
            periodTally=[0,0,0,0,0,0]
            for i in range(0,len(allClassAssignments[grade])):  #Iterate through particular classes
                assignedPeriod=allClassAssignments[grade][i].getPeriod()
                if assignedPeriod>0:
                    portionOfClassAssigned=1/float(allClassAssignments[grade][i].getSize())
                    periodTally[assignedPeriod-1]+=portionOfClassAssigned
                    #Conflict if 3 or more of same class in period:
                    if periodTally[assignedPeriod-1]>1: #Conflict if more than 100percent of grade assigned same problem
                        return True
                    #Conflict if 2 or more doubled classes
                    ##>>> ADD CODE HERE
                    

                
                
        
        ## Old method of checking##           
        #for i in range(0,self.teacherNumber):   #Check for conclicts with all other subjects
        #    otherNumberOfSubjects=len(teachers[i].getSubjects())
        #    for j in range(0,numberOfSubjects):
        #        for k in range(0,otherNumberOfSubjects):
        #            if teachers[i].getSubject(k).conflictsWith(self.subjects[j]):
        #                 return True
        ##
        return False
    def arrangeSubjects(self):
        numberOfSubjects=len(self.subjects)
        for i in range(0,numberOfSubjects):
            iterationIndex=int(permutations[5][self.iteration][i])
            self.subjects[i].setPeriod(iterationIndex)

 #       allClassAssignments=[[],[],[],[],[],[]]
       # for j in range(0,numberOfTeachers):
 #           for k in range(0,len(teachers[j].getSubjects())):
 #               allClassAssignments[int(teachers[j].getSubjects()[k].getGrade())-7].append(teachers[j].getSubjects()[k])


    def getSubjectOrder(self): #Broken
        return permutations[numberOfSubjects-1][self.iteration]
    def getSubjectsString(self):                #Returns subjects ordered according to iteration
        subjectsString=""
        self.arrangeSubjects()
        for period in range(1,7):
            subjectsString=subjectsString+"\nPeriod "+str(period)+": "
            for i in range(0,len(self.subjects)):
                if self.subjects[i].getPeriod()==period:
                    subjectGrade=self.subjects[i].getGrade()
                    subjectTitle=self.subjects[i].getSubjectTitle()
                    subjectsString=subjectsString+subjectGrade+"th " + subjectTitle
        subjectsString=subjectsString+"\n"
        return subjectsString
                       
        
    
    

class Subject(object):
    def __init__(self, name, teacherIndex): #Initalizes subject
        self.name=name;
        if name[0]=="1":    #If 10th, 11th, or 12th, take two numbers for grade
            self.grade=name[0:2]
            self.subjectTitle=name[2:len(name)-1]   #Find subject appropriately
        elif name[0]=="7" or name[0]=="8" or name[0]=="9":
            self.grade=name[0]
            self.subjectTitle=name[1:len(name)-1]
        self.teacherIndex=teacherIndex
        self.period=-1
        self.roster=[]
        self.together=[]
        self.size=name[-1]
        allClassAssignments[int(self.grade)-7].append(self)  #Update total class list
        for i in range(0,len(rosters)):
            if self.name==rosters[i][0]:
                self.roster=rosters[i][1:len(rosters[i])]
        if self.roster:
            print(self.name)
            print(self.roster)
        for i in range(0,len(together)):
            if self.name==together[i][0]:
                self.together=together[i][1]
        if self.together:
            print(str(self.name) + " with " + str(self.together))
    def getName(self):                      #Returns name
        return self.name
    def getSubjectTitle(self):              #Returns name
        return self.subjectTitle
    def getRoster(self):                     #Returns roster
        return self.roster
    def getGrade(self):                     #Returns grade
        return self.grade
    def getPeriod(self):                    #Returns period
        return self.period
    def getSize(self):                      #Returns size
        return self.size
    def setPeriod(self, period):            #Sets period
        self.period=period        
    def rosterConflictWith(self, otherSubject):  #Checks if two subjects have a roster conflict
        if self.roster==[]:
            return False            #Assume no conflict if no roster
        for i in range(0,len(self.roster)):
            if self.roster[i] in otherSubject.roster:
                return True
    def conflictsWith(self, otherSubject):  #Tests if two subjects conflict

                    
            #Ensure that this period matches with period of other class or class is not schedule
        if otherSubject.getGrade()==self.grade:
            if self.rosterConflictWith(otherSubject) or otherSubject.getSection()==self.section:
                if otherSubject.getPeriod()==self.period:                    
                        return True
                        
                        
        return False
    


##########################
#####2) Read file#########
##########################
originalFile=open('classes','r')
rawData=originalFile.readlines()
teachers=[]
data=[]
for line in rawData:
    data.append(line.split())

originalFile.close()


####################################################
#####3) Create Teacher and class objects############
####################################################
## Test for rosters
rosterIndex=0
teacherIndex=0
togetherIndex=0
i=0
rosters=[]
together=[]
allSubjects=[]

while teacherIndex==0 and i<len(data):  #Find end of teachers
    if data[i]==[]:
        teacherIndex=i
    i=i+1
i=0
while rosterIndex==0 and i<len(data):
    if data[i]==['Rosters']:
        rosterIndex=i+1
    i=i+1
i=0
while togetherIndex==0 and i<len(data):
    if data[i]==['Together']:
        togetherIndex=i+1
    i=i+1


for i in range(rosterIndex,togetherIndex-1):
    if data[i]!=[]:
        rosters.append(data[i])

for i in range(togetherIndex,len(data)):
    if data[i]!=[]:
        together.append(data[i])

#if otherIndex:
#    print("Other:")
#    print(other)
#
#if rosterIndex:
#    print("Roster:")
#    print(rosters)


## Test for combination classes

for i in range(0,teacherIndex):            ## Build Teacher list
    teacherName=data[i][0]
    teacherIndex=i
    restrictions=[]
    numberOfClasses=len(data[i])-1
    if data[i][-1][0]=="r": #Check for restrictions (if last word is restricted)
        numberOfClasses=numberOfClasses-1 #Last note is not a class
        restrictions=data[i][-1]
    individualClassList=[]
    for j in range(0,numberOfClasses):  #Create the class list
        newSubject=Subject(data[i][j+1],teacherIndex)
        allSubjects.append(newSubject)              #Form list of all subjects
        individualClassList.append(newSubject)
    newTeacher=Teacher(teacherName,individualClassList,i,restrictions) #Create new teacher with class list an name
    #newTeacher.setRestrictions(restrictions)
    teachers.append(newTeacher)
print("Teacher and class objects created")


#######################
#####4) Main Procedure######
#######################




numberOfTeachers=len(teachers)



#arrangeTeachersInOrderOfRestrictions

#Randomize Teacher order
#random.shuffle(teachers)
    ##for i in range(0,len(teachers)):
    ##    print(teachers[i].getName())



subjectNames=[]                       #Build list of class names
for i in range(0,len(allSubjects)):
    #if allSubjects[i].getName() in subjectNames:       #Test for repeated subjects
    #    print("Error #401: Repeated class name found.")
    #    print("  ->Repeat:"+allSubjects[i].getName())
    #    sys.exit()
    subjectNames.append(allSubjects[i].getName())

#Section conflict tally
period1ConflictTally=[0,0,0,0,0,0]
period2ConflictTally=[0,0,0,0,0,0]
period3ConflictTally=[0,0,0,0,0,0]

for i in range(0,len(allSubjects)):
    if subjectNames[i][-1]=="1" and subjectNames[i][0]=="7":
       period1ConflictTally[0]=period1ConflictTally[0]+1
    if subjectNames[i][-1]=="1" and subjectNames[i][0]=="8":
       period1ConflictTally[1]=period1ConflictTally[1]+1
    if subjectNames[i][-1]=="2" and subjectNames[i][0]=="7":
       period2ConflictTally[0]=period2ConflictTally[0]+1
    if subjectNames[i][-1]=="2" and subjectNames[i][0]=="8":
       period2ConflictTally[1]=period2ConflictTally[1]+1
    if subjectNames[i][-1]=="3" and subjectNames[i][0]=="7":
       period3ConflictTally[0]=period3ConflictTally[0]+1
    if subjectNames[i][-1]=="3" and subjectNames[i][0]=="8":
       period3ConflictTally[1]=period3ConflictTally[1]+1

#print("Section 1 Conflict Tally")
#print(period1ConflictTally)
#print("Section 2 Conflict Tally")
#print(period2ConflictTally)
#print("Section 3 Conflict Tally")
#print(period3ConflictTally)


#periodAssignments=[[],[],[],[],[],[]]

##Build Period assignments
#for i in range(0,len(teachers)):    #For each teacher
#    tempSubjects=teachers.getSubjects()
#    for i in range(0,len(tempSubjects)):  #For each of their subjects
        #Log period assignment
    
#for i in range(0,6):
#    for j in range(0,len(allClassAssignments[i])):
#        print(allClassAssignments[i][j].getName())
allClassAssignments1=allClassAssignments
allClassAssignments=[[],[],[],[],[],[]]
for j in range(0,numberOfTeachers):
    for k in range(0,len(teachers[j].getSubjects())):
        allClassAssignments[int(teachers[j].getSubjects()[k].getGrade())-7].append(teachers[j].getSubjects()[k])
if allClassAssignments1==allClassAssignments:
    print("Copied")

###    Main Loop    ###
i=0    

while i<numberOfTeachers:
    if i<0:
        print("Error #402: Seaching for teacher with negative index.")
        sys.exit()
    if teachers[i].finalIteration():#Final iteration
        teachers[i].clearIterations()    #Clear current teacher's iterations
        #print("Iterations cleared for teacher: "+str(i))
        i=i-1                           #Step back once
        teachers[i].iterate()           #Increment new teacher's iterations
    elif teachers[i].conflict():    #Conflict
        #print("Conflict for teacher: "+str(i))
        teachers[i].iterate()           #Try next iteration
    else:                           #No overlap so schedule found
        i=i+1                           #Move to next teacher
    
print("Schedule found")

###################################
#####5) Write new schedule#########
###################################
newFile=open('newClasses.txt','w')      #Open new file
numerOfTeachers=len(teachers)
for i in range(0,numberOfTeachers):     #Iterate through all the teachers
    numberOfSubjects=len(data[i])-1
    print(teachers[i].getName())
    print(teachers[i].getSubjectsString())
    newFile.write("\n*********************\n%s" % teachers[i].getName())
    newFile.write("%s" % teachers[i].getSubjectsString()) #Write subjects
    #newFile.write("Iteration: "+str(teachers[i].getSubjectOrder())+"\n\n")

newFile.close()                         #Close new file
print("File Closed")
