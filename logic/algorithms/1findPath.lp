%want 60 * 40 fast
#const length=4. 
#const hight=6.
%grid((1..length,1..hight)). %snake grid
%time(0..hight*length).

%start  
head((3,2),0).

apple((1,1)).


direction((X,Y)) :- X=-1..1, Y=-1..1, |X+Y|=1.
%nextto((X,Y),(XX,YY),(X+XX,Y+YY)) :- grid((X,Y)), direction((XX,YY)), grid((X+XX,Y+YY)).

%Choose a step
%1{head((X+X',Y+Y'),T):direction((X',Y')),Y+Y'>0,Y+Y'<=hight,X+X'>0,X+X'<=length}1:- head((X,Y),T-1), T < (hight*length).

%to compare
{head((X+X',Y+Y'),T):direction((X',Y')),Y+Y'>0,Y+Y'<=hight,X+X'>0,X+X'<=length}1:- head((X,Y),T-1), T < (hight*length).


%head to tail
%1{head((X+X',Y+Y'),hight*length-1): direction((X',Y'))}1:- head((X,Y),0).
:- not head((X+X',Y+Y'),hight*length-1): direction((X',Y')), head((X,Y),0).

%limit search space:
:-head((X,Y),T), head((X,Y),TT), T!=TT. 
%:-{head((X+X',Y+Y'),T):direction((X',Y'))}>1,head((X,Y),T-1).

food(T):-apple((X,Y)),head((X,Y),T).
:-not 1{food(T)}1. %Suprisingly fast

#minimize{T:food(T)}.



#show.
#show ((X,Y),T) : head((X,Y),T).
#show food(T):food(T).