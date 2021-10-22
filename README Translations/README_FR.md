<!-- Do not translate this -->
<details>
<summary>
<strong> Read this guide in other languages </strong>
</summary>
    <ul>
        <li><a href="https://github.com/Twiggecode/Integer-Sequences/blob/main/README.md"> English </a></li>
        <li><a href="https://github.com/Twiggecode/Integer-Sequences/blob/main/README%20Translations/README_IT.md"> Italian </a></li>
        <li><a href="https://github.com/Twiggecode/Integer-Sequences/blob/main/README%20Translations/README_HINDI.md"> Hindi </a></li>
        <li><a href="https://github.com/Twiggecode/Integer-Sequences/blob/main/README%20Translations/README_CN.md"> Chinese </a></li>
        <li><a href="https://github.com/Twiggecode/Integer-Sequences/blob/main/README%20Translations/README_FR.md"> French </a></li>
        <li><a href="https://github.com/Twiggecode/Integer-Sequences/blob/main/README%20Translations/README_ID.md"> Indonesian </a></li>
        <li><a href="https://github.com/Twiggecode/Integer-Sequences/blob/main/README%20Translations/README_KR.md"> Korean </a></li>
        <li><a href="https://github.com/Twiggecode/Integer-Sequences/blob/main/README%20Translations/README_PT.md"> Portuguese </a></li>
        <li><a href="https://github.com/Twiggecode/Integer-Sequences/blob/main/README%20Translations/README_RO.md"> Romanian </a></li>
        <li><a href="https://github.com/Twiggecode/Integer-Sequences/blob/main/README%20Translations/README_RU.md"> Russian </a></li>
        <li><a href="https://github.com/Twiggecode/Integer-Sequences/blob/main/README%20Translations/README_ES.md"> Spanish </a></li>
        <li><a href="https://github.com/Twiggecode/Integer-Sequences/blob/main/README%20Translations/README_AR.md"> Arabic </a></li>
        
</details>
<!-- Do not translate this -->

# Séquence d'entiers (Integer sequences)

## Introduction 

Il s'agit d'un projet open source relativement simple et adatpé pour les débutants, qui constitue un excellent choix de contribution pour ceux qui veulent faire leurs premières contributions open source. Tout le monde est libre de contribuer.

L'objectif de ce projet est de créer une base de données d'algorithmes en utilisant le langage de programmation de votre choix, où chaque algorithme retournera le Nième élément d'une des séquences d'entiers notables listées sur le lien wikipedia suivant : https://en.wikipedia.org/wiki/List_of_integer_sequences

Ce lien Wikipedia contient une liste de beaucoup de séquences d'entiers notables, tel que les nombres premiers, la séquence de Kolakoski, les nombres de Motzkin, les nombres de Lucas, etc.

'n' représente un nombre entier saisi par l'utilisateur. Par exemple, si l'utilisateur saisit le nombre entier '2', alors votre algorithme devrait renvoyer le troisième élément de la séquence (puisque l'indexation commence à 0, le premier élément de la séquence correspond à n=0, le deuxième élément à n=1, etc.)

Si quelqu'un a besoin d'implémenter l'une des séquences d'entiers les plus obscures listées sur la page wikipedia dans son propre programme, il est probable qu'il devra développer son propre algorithme à partir de zéro pour trouver le nième élément de la séquence, car aucun code pour générer ces séquences obscures n'existera sur Internet. 

Je veux compléter la base de données des algorithmes de ce projet afin que d'autres puissent simplement utiliser les algorithmes de ma base de données au lieu de perdre du temps à développer leurs propres algorithmes. Tout le monde est libre d'utiliser le code de ce projet dans son propre logiciel, il n'est pas nécessaire de demander la permission car ce projet utilise la "Unlicense".

## Comment contribuer

Jetez un coup d'œil sur le lien wikipedia : https://en.wikipedia.org/wiki/List_of_integer_sequences

Regardez la liste des séquences d'entiers notables et développez un algorithme dans n'importe quel langage de programmation pour retourner le nième élément de la séquence. L'indexation commence à 0, donc si l'utilisateur saisit n=0, cela renverra le premier élément de la séquence, n=1 renverra le deuxième élément, etc. Consultez le dépôt (repository) du projet pour vous assurer que le code de la séquence d'entiers de votre choix n'a pas déjà été ajouté au projet dans le langage de programmation de votre choix.

Par exemple, si quelqu'un a créé un algorithme Python pour les nombres de Bell et l'a ajouté au projet, vous pouvez toujours créer un algorithme pour les nombres de Bell dans tout autre langage, mais pas avec Python.

Si aucun code pour une séquence d'entiers spécifique n'existe dans le référentiel du projet, vous pouvez créer un code pour cette séquence d'entiers dans le langage de programmation de votre choix.

Regardez le code qui existe déjà dans le projet, utilisez-le pour vous guider et vous aider à développer votre propre algorithme.

Lorsque vous êtes satisfait du code que vous avez développé, soumettez une "pull request" en utilisant le modèle de pull request et mettez également à jour la liste de suivi. Si votre code produit des résultats corrects, il sera toujours ajouté au dépôt du projet, indépendamment des normes de codage/de la qualité du code, et indépendamment de la vitesse du code.

Vous pouvez également modifier et améliorer le code existant au sein du projet, en soumettant une demande de modification (pull request) et j'examinerai vos changements. Par exemple, vous pouvez améliorer la vitesse du code, ou améliorer les normes de codage en ajoutant des commentaires, des espaces, en changeant les noms de variables, etc.

## Comment faire une demande de Pull Request

Comme il s'agit d'un projet destiné aux débutants, je veux expliquer brièvement la manière la plus simple de soumettre une pull request pour ceux qui ne le savent pas.

Ouvrez mon dépôt et cliquez sur "Fork". Cela crée une copie (un fork) du dépôt.

Ajoutez votre code à votre copie.

Retournez sur mon dépôt et cliquez sur "submit pull request". Cliquez sur "compare across forks". Sélectionnez votre copie (fork) du référentiel comme "head" et mon référentiel comme "base".

Sinon, vous pouvez utiliser les commandes git suivantes :

1. Pour cloner le dépôt sur votre système local, utilisez la commande

```git clone lien-repo nom-du-dossier```

2. Pour ajouter le fichier que vous avez changé, utilisez la commande

```git add nom-du-fichier```

3. Dans le cas où vous avez changé plusieurs fichiers et que vous voulez les ajouter tous d'un coup

```git add .```

4. Pour "commit" ces changements, utilisez la commande

```git commit -m "Fixed Issue #issue_number"```

5. Pour envoyer (push) ces changements, utilisez la commande

```git push origin nom-de-la-Branche```
