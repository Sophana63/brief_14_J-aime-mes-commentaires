Fichiers utilisés par le formulaire
===================================


.. automodule:: files
   :members:
   :undoc-members:
   :show-inheritance:

Enregistrement en csv
---------------------

Tableau avec tous les employés enregistrés à partir du formulaire réalisé en Python

.. csv-filter:: Liste des employés
   :header: Prénom,Nom,Date d'embauche,Poste
   :file: csv/liste_employes.csv
   :exclude: {3: '(?i)Y\w*'}