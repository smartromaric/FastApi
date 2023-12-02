# ALGO GENETIQUE

base sur la theorie de l'evolution de CHARLES DARWIN //

population de depard , constitue d'individus , chaque individu pris seule va avoir une certain representation .
applique sur la population des operateur , la selection et le croisement

1-le croisement 
2-mutation 
3-selection
peut etre applique a tout type de probleme ( le probleme est de savoir comment representer represente solution en sachant kl doivent comprendre des gêne)

# # Rapprochement au probleme des 8 Reines

-ens des solution
-on divise par deux chaque elts et on les croise deux par deux (les sous morceau)
donc a chaque croissement on aura deux enfant (2 solution initiale)
-on choisie au reandon une solution et on choisie au hasard une valeur faire muter
- on prend ensuite les n meilleur solution et on reprend jusqu'a la fin des iterations 

si random  > 0.6 pas mutez (pour chaque element)
sinon mutez 

300 iteration (sa varie ) on s'arret on prend la meilleur solution  de la dernier solution 

// la 1er version du voyageur du commence "peut etre à l'examen" 