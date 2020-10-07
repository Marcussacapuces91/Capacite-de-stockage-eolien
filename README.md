# Capacité de stockage Éolien

Application Python permettant d'évaluer la capacité de stockage a associer à une éolienne pour lisser sa production.

## Introduction

Suite à une discussion commencée sur Twitter ([https://twitter.com/Fair_finance/status/1313763267932807170](https://twitter.com/Fair_finance/status/1313763267932807170)), j'ai voulu me lancer dans l'écriture d'une calculatrice permettant d'évaluer l'intérêt économique d'un système de stockage chimique (batterie) associé à une éolienne permettant d'assurer une production continue d'électricité.

## Documentation / Bibliographie

### Éolienne 
Il apparaît qu'une éolienne n'est pas un système linéaire mais répond à des règles techniques (incontournables) qui font que ces convertisseurs n'ont pas un rendement parfait et dépendent donc de leur propres caractéristiques mais aussi du vent.

1. [https://eolienne.ooreka.fr/astuce/voir/352953/puissance-eolienne](Ooreka.fr - Puissance d'une éolienne) ;
2. [http://www.xn--drmstrre-64ad.dk/wp-content/wind/miller/windpower%20web/fr/tour/wres/pwr.htm](http://www.xn--drmstrre-64ad.dk/wp-content/wind/miller/windpower%20web/fr/tour/wres/pwr.htm).

Trois variables seront à préciser :

* la vitesse du vent au démarrage du générateur (Vmin) ;
* la vitesse du vent au plateau (saturation) à la production maximale (Vsat) ;
* la vitesse de vent maximale avant extinction du générateur pour mise en sécurité (Vmax) ;
* la puissance maximale installée (Pmax).

Elles permettront de modéliser la fonction de production d'énergie en fonction de la vitesse du vent.

### Modélisation du vent
Il est important de modéliser le vent, ce qui va être un élément fondamental de la discussion qui va suivre puisqu'il faudra bien justifier les capacités de stockage en regard de ces variations.




A priori, je pars sur une distribution selon la loi de Weiball




