/* Judith Chen S3C5 Option 3 */

/* 29.01 */
capitalCity(paris).
capitalCity(berlin).
capitalCity(cairo).

/* 29.02. Test see file 29.02_Test in folder */

/* 29.03 + 29.04 code see file Family.pl. Test see 29.03+04_Test. */

/* 29.05 Test see 29.05_Test*/
factorial(0, 1).
factorial(N, Result) :-
	M is N-1,
	factorial(M, PartResult),
	Result is PartResult * N.

/* 29.06 */
writeList([pan, zhang, chen]).
writeList([H|T]):- writeList(H), n1, writeList(T).