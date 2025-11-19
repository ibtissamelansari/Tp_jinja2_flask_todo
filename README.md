#  Flask Todo App

Une petite application **Todo** développée avec **Flask**, **Jinja2** et **HTML/CSS**.  
Elle permet d’ajouter, afficher, compléter et supprimer des tâches via une interface simple et agréable.

---

## Fonctionnalités

- **Ajouter** une nouvelle tâche  
- **Afficher** la liste des tâches  
- **Marquer** une tâche comme terminée  
- **Supprimer** une tâche  
- **Interface simple**, propre et responsive

---

## Installation & Démarrage

### 1 Cloner le dépôt

```bash
git clone https://github.com/ibtissamelansari/Tp_jinja2_flask_todo.git
cd Tp_jinja2_flask_todo
```

---

### 2 Créer un environnement virtuel (recommandé)

```bash
python3 -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows
```

---

### 3 Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## Structure du projet

```
todo-flask/
│
├── app.py
├── requirements.txt
├── README.md
│
├── static/
│   └── style.css
│
└── templates/
    ├── base.html
    └── index.html
```

---

## Lancer l’application

```bash
python app.py
```

L’application sera accessible à l’adresse :  
http://127.0.0.1:5000/