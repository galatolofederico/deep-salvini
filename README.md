# DeepSalvini

[DeepSalvini](https://deepsalvini.club/) è un modello linguistico generativo basato su intelligenza artificiale addestrato sul corpus di tweets di Matteo Salvini

DeepSalvini utilizza come pretrain un istanza di [GPT-2](https://openai.com/blog/better-language-models/) addestrata su testo italiano chiamata [GePpeTto](https://github.com/LoreDema/GePpeTto).

DeepSalvini è disponibile [qui](https://deepsalvini.club/)

## Struttura del repository 

### ai

Codice necessario ad aggiornare il database di tweets, generare il dataset ed addestrare `GPT-2`

Creare un `virtualenv` ed installare le dipendenze:

```
cd ai/
virtualenv --python=python3.6 env
. ./env/bin/activate
pip install -r requirements.txt
```

Per aggiornare il database di tweets:

```
./update-tweets.sh
```

Per generare il dataset:

```
python build-dataset.py --input ./tweets/salvini.txt --output ./datasets/salvini.txt
```

Per addestrare `GPT-2`:

```
./train.sh
```

### backend

Codice del backend implementato con `flask` 


### frontend

Codice del frontend basato su `Boostrap 4.0`


## Deploy

Clona il repository

```
git clone https://github.com/galatolofederico/deep-salvini.git
cd deep-salvini
```

Scarica l'ultima versione addestrata del modello

```
wget https://github.com/galatolofederico/deep-salvini/releases/download/23012021/model.tar.gz
```

Estrai

```
tar -xzvf model.tar.gz
```

Avvia docker compose

```
docker-compose up
```

DeepSalvini sarà disponibile su `http://localhost`


## Ridistribuire/Contribuire

La ridistribuzione del codice, integro o parziale, originale o modificato, è permessa nei limiti della licenza GNU/GPL Versione 3.

Ogni tipo di aiuto sotto qualsiasi forma è ovviamente ben accetto.

DeepSalvini non è monetizzato e mai lo sarà: se vuoi aiutare a coprire i costi dei server puoi farlo [qui](paypal.me/federicogalatolo)