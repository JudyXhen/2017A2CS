/*Judith Chen*/

character(jim).
character(jenny).
character(habib).
character(hatter).
character(alice).

charater_type(jim, prince).
character_type(jenny, princess).
character_type(habib, explorer).
character_type(hatter, rebel).
character_type(alice, champion).

has_skill(jim, fly).
has_skill(jenny, invisiblility).
has_skill(habib, time_travel).
has_skill(hatter, futterwacken).
has_skill(alice, killJabberwocky).
has_skill(X, Y) :- 
	character(X), skill(Y).

has_pet(jim, horse).
has_pet(jenny, bird).
has_pet(habib, fish).
has_pet(hatter, marchHare).
has_pet(alice, bandersnatch).
has_pet(A, B) :-
	character(A), animal(B).

animal(horse).
animal(bird).
animal(fish).
animal(marchHare).
animal(bandersnatch).

skill(fly).
skill(invisibility).
skill(time_travel).
skill(futterwacken).
skill(killJabberwocky).



/* Task 3.4 */
/* true */
/* X = princess */
/* X = invisibility */
/* X = jim */



/* Task 3.5 */
/* has_pet(jim, X). */
/* has_skill(X, fly). */
/* skill(X). */
/* has_pet(X, Y), character_type(X, princess). */