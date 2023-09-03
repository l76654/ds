student(mohan,192211622).
student(varun,192211790).
student(vijay,192211504).
student(narayana,192224110).
teacher(judy,t101).
teacher(deepa,t102).
subject(csa11,'ooad').
subject(csa13,'compiler design').
teaches(t101,csa11).
teaches(t102,csa13).
enrolled(192211622,csa11).
enrolled(192211790,csa11).
enrolled(192211504,csa11).
enrolled(192224110,csa13).
teaching(Teacher,Subject):-
	student(Name,Reg),
	teacher(Teacher,Id),
	subject(Subcode,Sub_Name),
	teaches(Id,Subcode),
	enrolled(Reg,Subcode).
	