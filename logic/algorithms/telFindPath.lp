#const length=60. 
#const hight=4.



#program always.
direction((X,Y)) :- X=-1..1, Y=-1..1, |X+Y|=1.

#program initial.
head((3,2)).
apple((1,1)).

#program dynamic.
1{head((X+X',Y+Y')):direction((X',Y')),Y+Y'>0,Y+Y'<=hight,X+X'>0,X+X'<=length}1:- 'head((X,Y)).

#program final.
%:- &tel {<< head((X,Y))}, not head((X+X',Y+Y')),direction((X',Y')).


%:- not head((X+X',Y+Y'),hight*length-1): direction((X',Y')), head((X,Y),0).