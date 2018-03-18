/* Judith Chen - S3C5 - Option 3 */

married(guang, qian).
ancestor(juntang, meiqin).

parent(meiqin, qian).
parent(meiqin, yun).
parent(meiqin, qiao).

parent(juntang, qian).
parent(juntang, yun).
parent(juntang, qiao).

parent(guang, judith).
parent(qian, judith).
parent(qian, yuan).
parent(guang, yuan).

female(qian).
female(yun).
female(judith).
 
male(qiao).
male(juntang).
male(guang).
male(yuan). 

brother(A, B) :- 
	parent(P, A),
	parent(P, B),
	male(A).

sister(A, B) :-
	parent(P, A),
	parent(P, B),
	female(A),
	not(A=B).

son(A, B) :-
	parent(B, A),
	male(A).

daughter(A, B) :-
	parent(B, A),
	female(A). 











