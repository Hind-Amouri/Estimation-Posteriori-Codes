
#### 2. Les **équations** utilisées

Dans tes notebooks ou tes scripts Python, tu devras expliquer les équations utilisées dans cette séance. Tu as probablement une équation aux dérivées partielles (EDP) à résoudre, par exemple :

L'équation de Poisson :

\[
-\Delta u = f \quad \text{dans } \Omega
\]

Avec \( \Delta \) représentant le laplacien et \( u \) la fonction inconnue. Nous cherchons à résoudre cette équation dans un domaine donné \( \Omega \).

Le **résidu a posteriori** pourrait être défini par :

\[
r_h(u_h) = f + \Delta u_h
\]

Le but de l'approximation a posteriori est d'estimer l'erreur dans la solution numérique \( u_h \) à travers l'analyse du résidu \( r_h \).

#### 3. Le code Python pour résoudre l'EDP

Dans ton dossier `src/`, crée un fichier `main.py` où tu vas coder la résolution de cette équation. Un exemple simple serait :

```python
import numpy as np
import matplotlib.pyplot as plt

# Paramètres de discrétisation
N = 100
x = np.linspace(0, 1, N)
h = x[1] - x[0]

# Initialisation de la solution
u = np.zeros(N)

# Source terme
f = np.ones(N)

# Boucle de calcul pour résoudre l'EDP
for i in range(1, N-1):
    u[i] = (f[i] + u[i-1] + u[i+1]) / 2

# Tracé de la solution
plt.plot(x, u)
plt.title('Solution Approximée de l\'EDP')
plt.xlabel('x')
plt.ylabel('u')
plt.savefig('figures/solution_EDP.png')
plt.show()
