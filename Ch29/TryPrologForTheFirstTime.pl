cat(jack).

dog(erniu).

capitalCity(ottawa).
capitalCity(beijing).

cTinCntry(ottawa, canada).
cTinCntry(beijing, china).
cTinCntry(chongqing, china).
cTinCntry(nyc, us).

vegetable(celery).
vegetable(carrot).

meat(chicken).
meat(beef).
meat(lamb).

ingredient(chicken, soup, 250).
ingredient(carrot, soup, 100).


len([], 0).
len([_|T], L) :-
	len(T, X),
	L is X + 1. 

mymember(I, [I|_]).
mymember(I, [_|T]) :-
	mymember(I, T).

