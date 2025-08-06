Simple example :
```
$ cat /etc/passwd | column --table --separator ':' --table-columns name,pwd,uid,gid,comment,home,shell
```

JSON output :
```
$ cat /etc/passwd | column --table --separator ':' --table-columns name,pwd,uid,gid,comment,home,shell --json
```

Interesting example : _sed will return a new line after semicolon_
```
$ echo "A,B,C;a1,b1,c1;a2,b2,c2;" | sed 's/;/\n/g' | column -t -s ',' -o ', '
A , B , C
a1, b1, c1
a2, b2, c2
```

Keep semicolon :
```
$ echo "A,B,C;a1,b1,c1;a2,b2,c2;" | sed 's/;[^$]/;\n/g' | column -t -s ',' -o ', '
A, B , C;
1, b1, c1;
2, b2, c2;
```

More complex custom example :
```
$ echo "A,B,C;a1,b1,c1;a2,b2,c2;" | sed 's/;[^$]/; (END LINE)\n(START LINE)/g' | column -t -s ',' -o ',..'
A            ,..B ,..C; (END LINE)
(START LINE)1,..b1,..c1; (END LINE)
(START LINE)2,..b2,..c2;
```

Help :
```
$ column --version
column de util-linux 2.38.1

$ column --help

Utilisation :
column [options] [<fichier>...]

Formater des listes en plusieurs colonnes.

Options :
-t, --table                      créer un tableau
-n, --table-name <nom>           nom de table pour la sortie JSON
-O, --table-order <colonnes>     spécifier l'ordre des colonnes de sortie
-N, --table-columns <noms>       noms de colonnes séparés par des virgules
-l, --table-columns-limit <nombre> nombre maximal de colonnes d'entrée
-E, --table-noextreme <colonnes> ne pas compter les textes longs des colonnes dans la largeur des colonnes
-d, --table noheadings           ne pas affiche l'en-tête
-e, --table-header-repeat        répéter l'en-tête sur chaque page
-H, --table-hide <colonnes>      ne pas afficher les colonne
-R, --table-right <colonnes>     aligner le texte à droite dans ces colonnes
-T, --table-truncate <colonnes>  tronquer le texte dans les colonnes si nécessaire
-W, --table-wrap <colonnes>      imposer un retour à la ligne dans les colonnes si nécessaire
-L, --keep-empty-lines           ne pas ignorer les lignes vides
-J, --json                       utiliser le format de sortie JSON pour la table

-r, --tree <colonne>             colonne pour utiliser une sortie arborescente pour la table
-i, --tree-id <colonne>          ID de ligne pour spécifier la relation enfant/parent
-p, --tree-parent <colonne>      parent pour spécifier la relation enfant/parent

-c, --output-width <largeur>     largeur de la sortie en nombre de caractères
-o, --output-separator <chaîne>  séparateur de colonnes pour la sortie table (deux espaces par défaut)
-s, --separator <chaîne>         délimiteurs de tableau possibles
-x, --fillrows                   remplir les lignes avant les colonnes

-h, --help                       afficher cette aide
-V, --version                    afficher la version

Consultez column(1) pour obtenir des précisions complémentaires.
```