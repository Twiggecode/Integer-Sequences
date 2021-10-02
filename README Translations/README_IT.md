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
    
</details>
<!-- Do not translate this -->

# Integer Sequences

## Introduzione al Progetto

Questo è un progetto open source relativamente semplice e adatto ai principianti che risulta essere una scelta eccellente per coloro che vogliono dare i loro primi contributi open source. Tuttavia, chiunque è libero di contribuire.

Lo scopo di questo progetto è creare un database di algoritmi utilizzando un linguaggio di programmazione di tua scelta, in cui ogni algoritmo restituirà l'ennesimo elemento di una delle sequenze intere notevoli elencate nel seguente collegamento a wikipedia. https://en.wikipedia.org/wiki/List_of_integer_sequences

Questo collegamento a wikipedia contiene un elenco di molte sequenze intere degne di nota, come i numeri primi, la sequenza di Kolakoski, i numeri di Motzkin, i numeri di Lucas ecc...

'n' Rappresenta un numero intero immesso dall'utente. Ad esempio, se l'utente inserisce l'intero '2', il tuo algoritmo dovrebbe restituire il terzo elemento della sequenza (poiché l'indicizzazione inizia da 0, il primo elemento della sequenza è per n=0, il secondo elemento è per n =1, ecc.).

Se qualcuno intende implementare una delle sequenze intere più oscure elencate nella pagina di wikipedia all'interno del proprio programma, è probabile che dovrà sviluppare il proprio algoritmo per trovare l'ennesimo elemento della sequenza da zero, poiché il codice per generare queste sequenze oscure non è reperibile su Internet.

Voglio completare il database degli algoritmi all'interno di questo progetto in modo che altri possano semplicemente utilizzare gli algoritmi all'interno del mio database invece di perdere tempo a sviluppare i propri algoritmi. Chiunque è libero di utilizzare il codice all'interno di questo progetto nel proprio software, non c'è bisogno di chiedere il permesso perché questo progetto utilizza la Unlicense.

## Come Contribuire

Visita il link wikipedia https://en.wikipedia.org/wiki/List_of_integer_sequences

Guarda l'elenco delle sequenze intere degne di nota e sviluppa un algoritmo in qualsiasi linguaggio di programmazione per restituire l'ennesimo elemento della sequenza. L'indicizzazione inizia da 0, quindi se l'utente immette n=0, questo restituirà il primo elemento della sequenza, n=1 restituisce il secondo elemento ecc. Guarda la repository del progetto per assicurarti che il codice per la sequenza intera da te scelta non sia già stato aggiunto al progetto nel linguaggio di programmazione scelto.

Ad esempio, se qualcuno ha creato un algoritmo Python per i numeri di Bell e lo ha aggiunto al progetto, puoi comunque creare un algoritmo per i numeri di Bell in qualsiasi altro linguaggio, ma non con Python.

Se non esiste alcun codice per una sequenza intera specifica nella repository del progetto, è possibile creare codice per questa sequenza intera in qualsiasi linguaggio di programmazione desiderato.

Guarda il codice che esiste già all'interno della repository del progetto e usalo per guidarti e aiutarti a sviluppare il tuo algoritmo.

Quando sei soddisfatto del codice che hai sviluppato, invia una pull request utilizzando il modello a disposizione e aggiorna la tracking list. Esaminerò quindi il tuo codice per assicurarmi che funzioni come previsto, quindi lo aggiungerò alla repository del progetto. Se il tuo codice produce gli output corretti, verrà sempre aggiunto alla repository del progetto, indipendentemente dagli standard di codifica/qualità del codice e indipendentemente dalla velocità di esecuzione.

Puoi anche modificare e migliorare il codice esistente all'interno del progetto e inviare una pull request. Ad esempio, puoi migliorare la velocità di esecuzione del codice o migliorare gli standard di codifica aggiungendo commenti, spazi, modificando i nomi delle variabili, ecc.


## Come Effettuare una Pull Request

Visto che questo è un progetto rivolto ai principianti, voglio spiegare brevemente il modo più semplice per inviare una pull request per coloro che non lo sanno.

Dalla mia repository fai clic su "Fork". Questo crea una copia della repository.

Aggiungi il tuo codice nella tua copia.

Torna nella mia repository e fai clic su invia pull request. Fai clic su "Confronta tra i fork". Seleziona la tua copia del repository come "head" e il mio repository come "base".

Fai clic su Invia pull request e lascia un commento significativo che spieghi il codice che stai tentando di aggiungere al progetto.


In alternativa, puoi usare i seguenti comandi git:

1. Per clonare localmente la repository usa

```git clone repo-link nome_folder ```

2. Per aggiungere alla coda il file che hai modificato usa

```git add nome-file```
   
3. Nel caso tu abbia modificato più file e voglia aggiungerli alla coda tutti insieme usa

```git add .``` 

4. Per rendere effettivi i cambiamenti usa

```git commit -m "Risolta Issue #numero_issue"```

5. Per inviare le modifiche alla repository remota usa

```git push origin nome-branch```


