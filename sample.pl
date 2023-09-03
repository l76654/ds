planet(mercury, 57.9, 0).
planet(venus, 108.2, 0).
planet(earth, 149.6, 1).
planet(mars, 227.9, 2).
planet(jupiter, 778.3, 79).
planet(saturn, 1427.0, 83).
planet(uranus, 2870.0, 27).
planet(neptune, 4497.1, 14).

planet_info(Name, DistanceFromSun, Moons) :-
    planet(Name, DistanceFromSun, Moons).
