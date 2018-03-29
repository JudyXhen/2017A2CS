/*Judith Chen s3c5-opt3*/

len([],0).
len([_|T],L):-
         len(T,X),
         L is X +1.

myMember(I,[I|_]).
myMember(I,[_|T]):-
        mymember(I, T).

myAppend([a,b],[c,d], [a,b,c,d]).
myAppend([],X, X).
myAppend([H|T],  L,[H|R]):-
       myappend(T,L,R).

myLast([b],b).
myLast([_|T],L):-
      myLast(T,L).


add1([],[]).
add1([A|B],[C|D]):-
        add1(B,D),
        C is A+1.

lastButone([A,_],A).
lastButone([_|B],R):-
       lastButone(B,R).

elementAt(A,[A|_],1).
elementAt(A,[A],1).
elementAt(A,[_|T],K):-
       R is K-1,
       elementAt(A,T,R).

reverse([a,b,c],[c,b,a]).
reverse([a],[a]).
reverse([],[]).
reverse([A|B],L):-
       reverse(B,R),
       myAppend(A,R,L).

palindrome(A):-
    reverse(A,B),
    A==B.

same(X,Y):-
   X==Y.