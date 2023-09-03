bird(hen,'not_fly').
bird(ostriche,'not_fly').
bird(peacock,'not_fly').
bird(eagle,'fly').
bird(dove,'fly').
birdcan(Name,FlyOrNot):-
	bird(Name,FlyOrNot).