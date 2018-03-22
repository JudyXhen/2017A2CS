/*Judith Chen*/

/* bunny ears */
bunnyEars(0,0).
bunnyEars(B, E) :-
	X is B - 1,
	bunnyEars(X, Y),
	E is Y + 2.

/* fibonacci */
fibonacci(0, 0).
fibonacci(1, 1).
fibonacci(S, E) :-
	X is S - 1,
	Y is S - 2,
	fibonacci(X, Z),
	fibonacci(Y, A),
	E is A + Z.





	

/* triangle */
triangle(0, 0).
triangle(1, 1).
triangle(R, B) :-
	X is R - 1,
	triangle(X, Y),
	B is R + Y.

/* sum digits */
sumDigits(0, 0).
sumDigits(D, S) :-
	X is D div 10,
	sumDigits(X, Y),
	Z is Y mod 10,
	S is X + Z. 

