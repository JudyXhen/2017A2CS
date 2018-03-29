/* Judith Chen - S3C5 - Option 3 */

/* Q1 */
capital (vienna) .
capital(london).
capital (santiago) .
capital (caracas).
capital(tokyo).


cityin (vienna, austria).
cityin(santiago, chile).
cityin(salzburg, austria).
cityin(maracaibo, venezuela).
/* a i */
cityin(london, uk).

continent (austria, europe).
continent (chile, southAmerica) .
continent(uk, europe) .
continent(argentina, southAmerica).

iVisited(vienna).
iVisited(tokyo).
/* a ii */
iVisited(Strasbourg).

capitalOf(City, Country) :-
	capital(City) AND cityin(City, Country). 

europeanCity (City) :-
	cityin(City, Country) AND continent(Country, europe).


/* 1 b */
/* 
Country = chile
Country = argentina
*/

/* 1 c */
countriesIVisited(Country) :-
	iVisited(CT),
	cityin(CT, Country).

/* 2 a */
age (fred, 19).
qualifiedDriver (X, V)
	IF allowedToDrive (X, V)
		AND passedTheoryTest (X)
		AND passedDrivingTest(X,V).

/* b */
Who = jack
false.
false.

/* c */
qualifiedDriver(Who, car).

passedTheoryTest(X), AND NOT(passedDrivingTest(X, car)), AND NOT(passedDrivingTest(X, truck))

/* don’t understand question B */

/*  */

