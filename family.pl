
parent(john, mary).
parent(john, ann).
parent(mary, jim).
parent(jim, lisa).
male(john).
male(jim).
female(mary).
female(ann).
female(lisa).

father(X, Y) :- 
	parent(X, Y), 
	male(X).
mother(X, Y) :- 
	parent(X, Y), 
	female(X).
child(X, Y) :- 
	parent(Y, X).
son(X, Y) :- 
	child(X, Y), 
	male(X).
daughter(X, Y) :- 
	child(X, Y), 
	female(X).