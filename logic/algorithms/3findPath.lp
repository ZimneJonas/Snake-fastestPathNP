#const length=10 -1. 
#const hight=20 -1.

vertex((0..length, 0..hight)).
direction((X,Y)) :- X=-1..1, Y=-1..1, |X+Y|=1.
edge((X1,Y1),(X1+X,Y1+Y)) :- vertex((X1,Y1)), direction((X,Y)), vertex((X1+X,Y1+Y)).

{in(X,Y)} :- edge(X,Y).

:- 2 {in(V1,V2) : edge(V1,V2)}, vertex(V1).
:- 2 {in(V1,V2) : edge(V1,V2)}, vertex(V2).

r(V2) :- in((3,3),V2), vertex(V2).
r(V2) :- r(V1), in(V1,V2), edge(V1,V2).

:- not r(V), vertex(V).