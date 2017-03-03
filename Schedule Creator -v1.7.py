######################################
########0)Set up permutations#########
######################################


import itertools
import math
import random
import sys

permutations=[]
sublist=[]


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

##################################
###Set up togetherness array######
expectingTogether=[]
waitingTogether=[]
partneredTogether=[]
##################################

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
 #       for i in range(0,len(self.subjects)):
 #           print(self.subjects[i].getTeacher())
 #       for j in range(0,len(self.subjects)):           
 #           if self.subjects[j].together!=[]:
 #               ##@@Clear subject position here@@##
 #               if self.subjects[j] in expectingTogether:
 #                   expectingTogether.remove(self.subjects[j])
 #               waitingTogether.append(self.subjects[j])    ##########Expected problem here##########
 #                   partneredTogether.remove(self.subjects[j])
        
    #def periodRestriction(self, period):     #Restricts teacher from teaching at a particular period
    #    self.restrictions.append(period)
    def getName(self):                      #Returns name
        return self.name
    def getSubjects(self):                  #Returns subjects
        return self.subjects
    def getSubject(self, index):           #Returns particular subject
        self.arrangeSubjects()
        return self.subjects[index]
    def setIteration(self,i):                 #Returns iterations
        self.iteration=i
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
        if self.iteration==720:
            return True
        else:
            return False
        
    def lackingTogetherness(self):      #Check no problem with other periods that this class should be with
        for j in range(0,len(self.subjects)):           
            if self.subjects[j].together!=[]:
                if self.subjects[j].partnerProblem()==True:
                    return True
        return False


        

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
#        if self.name==teachers[0].getName(): #Aside for restrictions, no conflict for first teacher
#            return False

        
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
                    if periodTally[assignedPeriod-1]>1: #Conflict if more than 100percent of grade assigned same problem
                        return True

                
            
        return False
    def arrangeSubjects(self):
        numberOfSubjects=len(self.subjects)
        for i in range(0,numberOfSubjects):
            iterationIndex=int(permutations[5][self.iteration][i])
            self.subjects[i].setPeriod(iterationIndex)

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
                break
        if self.together!=[]:
            waitingTogether.append(self)    #This subject is waiting for a partner
            print(str(self.name) + " with " + str(self.together))
    def getName(self):                      #Returns name
        return self.name
    def getSubjectTitle(self):              #Returns title
        return self.subjectTitle
    def getRoster(self):                     #Returns roster
        return self.roster
    def getGrade(self):                     #Returns grade
        return self.grade
    def getTeacher(self):                     #Returns teacher name
        return data[teacherIndex][0]
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
    def partnerProblem(self):
        if self in expectingTogether:
            expectingTogether.remove(self)
        if self not in waitingTogether:
            waitingTogether.append(self)   
        expectingNames=[]
        waitingNames=[]
        for j in range(0,len(expectingTogether)):       #Compile names of expecting
            expectingNames.append(expectingTogether[j].getName())
        for j in range(0,len(waitingTogether)):         #Compile names of waiting
            waitingNames.append(waitingTogether[j].getName())
        if len(waitingNames)==1: #And odd number in a period
            #Iterate through periods, counting self.name and self.together
            #Number per period should match
            periods=[0,0,0,0,0,0]
            for j in range(0,len(allSubjects)):
                if self.together==allSubjects[j].getName():
                    periods[allSubjects[j].getPeriod()-1]+=1
                if self.name==allSubjects[j].getName():
                    periods[allSubjects[j].getPeriod()-1]-=1
            #print(periods)
            for j in range(0,len(periods)):
                if periods[j]!=0: #Mismatched classes in a period
                    return True
                   
        if self.together in waitingNames:    #If partner is waiting, no problem
            expectingTogether.append(self) #Class is now expecting, not waiting
            waitingTogether.remove(self)#2
            return False 
           #If waiting is empty except for this class, match must be in expecting           
        else:
            for i in range(0,len(expectingTogether)):
                if self.together==expectingTogether[i].getName():
                    if self.period==expectingTogether[i].getPeriod():
                        waitingTogether.remove(self)#2
                        return False

                      

        return True
                
 #Unknown difficulty in code above, does not recognize when waiting names is empty   



######Overarching loop######
running=True
corrections=[]
savedIterations=[]
while running==True:
    
    
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
    allClassAssignments=[[],[],[],[],[],[]]
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


    #####Modify order of teachers if corrections are required####
    tempTeachers=[]
    for i in range(0,len(corrections)):
        tempTeachers.append(teachers[corrections[i]])
    for i in range(0,len(tempTeachers)):
        teachers.remove(tempTeachers[i])
    for i in range(0,len(tempTeachers)):
        tempTeachers[i].setIteration(savedIterations[i])
        teachers.insert(0,tempTeachers[i])



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
        
    for i in range(0,len(allClassAssignments)):
        tempSum=0
        for j in range(0,len(allClassAssignments[i])):
            tempSum+=1/float(allClassAssignments[i][j].getName()[-1])
            if tempSum>6:
                print("\n\n"+str(i+7)+"th grade is overloaded with a load of " + str(tempSum)+"\n\n\n")
                sys.exit()
                
    loops=0
    i=0
    print("Searching")
    while i<numberOfTeachers:
        loops+=1
        if loops>40000:
            print("...")
            loops=loops-40000
    #    print("\n****Loop: "+str(i))
        if i<0:
            print("\n\n\n*****\n\nNo Schedule Found\n\n****")
            sys.exit()
        elif teachers[i].finalIteration():#Final iteration
            teachers[i].clearIterations()    #Clear current teacher's iterations
            #print("Iterations cleared for teacher: "+str(i))
            i=i-1                           #Step back once
            teachers[i].iterate()           #Increment new teacher's iterations
        elif teachers[i].conflict():    #Conflict
            #print("Conflict for teacher: "+str(i))
            teachers[i].iterate()           #Try next iteration
        else:                           #No overlap so schedule found
            i=i+1                           #Move to next teacher
        #if i==numberOfTeachers and len(expecting)>0:
     #       i=i-1
     #       print("Cheat")
    #    for i in range(0,len(partneredTogether)):
    #        print(partneredTogether[i].getName())    
    #print("Schedule found")
    #print("\n*Expecting*")
    #for j in range(0,len(expectingTogether)):
#        
#        #print(j)
#        print(expectingTogether[j].getName())
#        print(expectingTogether[j].getPeriod())
#    print("\n*Waiting*")
#    for j in range(0,len(waitingTogether)):
#       
#       print(j)
#       print(waitingTogether[j].getName())
#       print(waitingTogether[j].getPeriod())


    ###################################
    #####5) Write new schedule#########
    ###################################
    newFile=open('newClasses.txt','w')      #Open new file
    numerOfTeachers=len(teachers)
    for i in range(0,numberOfTeachers):     #Iterate through all the teachers
        numberOfSubjects=len(data[i])-1
        print("Teacher #" + str(i+1))
        print(teachers[i].getName())
        print(teachers[i].getSubjectsString())
        newFile.write("\n*********************\n%s" % teachers[i].getName())
        newFile.write("%s" % teachers[i].getSubjectsString()) #Write subjects
        #newFile.write("Iteration: "+str(teachers[i].getSubjectOrder())+"\n\n")

    newFile.close()                         #Close new file
    print("File Closed")

    ###################################
    #####6) Ask for modification#########
    ###################################
    print("\n\nWould you like to modify the schedule? Y/N")
    wouldLikeToModify=input()
#    corrections=[]
#    savedIterations=[]
    if wouldLikeToModify=="y" or wouldLikeToModify=="Y":
        completed=False
        while completed==False:
            print("Which teacher's schedule would you like to hold constant?")
            teacherIndex=int(input())-1
            corrections.append(teacherIndex)
            savedIterations.append(teachers[teacherIndex].getIteration())
            print("Would you like to add another?")
            modifyFurther=input()
            if modifyFurther=="n" or modifyFurther=="N":
                completed=True
    else:
        running=False

    
