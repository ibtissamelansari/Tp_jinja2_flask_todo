# Flask Todo App

Une petite application Todo construite avec **Flask**, **Jinja2** et un peu de **HTML/CSS**.  
Elle permet d’ajouter des tâches, les marquer comme terminées et les supprimer.

---

## Fonctionnalités

- Afficher la liste des tâches  
- Ajouter une nouvelle tâche  
- Marquer une tâche comme terminée  
- Supprimer une tâche  
- Interface simple et stylée

---

## Installation

### 1. Cloner le projet

```bash
git clone https://github.com/ibtissamelansari/Tp_jinja2_flask_todo.git
cd Tp_jinja2_flask_todo 
```
--- 

### 2. Créer un environnement virtuel (optionnel mais recommandé)

python3 -m venv venv
source venv/bin/activate  # macOS / Linux
venv\Scripts\activate     # Windows

---

### 3. Installer les dépendances

pip install -r requirements.txt

---

## Structure du projet

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

---

### Lancer l'application

python app.py


