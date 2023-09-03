hanoi(1,Source,Target,_):-
	write('move disk 1 from'),
	write(Source),
	write('to'),
	write(Target),
	nl.
hanoi(N,Source,Target,Spare):-
	N>1,
	M is N-1,
	hanoi(M,Source,Spare,Target),
	hanoi(1,Source,Target,_),
	hanoi(M,Spare,Target,Source).