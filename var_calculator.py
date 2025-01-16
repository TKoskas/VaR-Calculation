import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Génération de données de rendements simulés (scénario réel)
np.random.seed(42)  # Reproductibilité des résultats
# Rendements simulés : moyenne = 0.0005 (0.05%/jour, approximativement 12%/an), écart-type = 1%
portfolio_returns = np.random.normal(0.0005, 0.01, 1000)

# Niveau de confiance pour la VaR
confidence_level = 0.95

# Calcul de la VaR paramétrique
var = np.percentile(portfolio_returns, (1 - confidence_level) * 100)

# Affichage de la VaR
print(f"VaR à {confidence_level*100}% de niveau de confiance : {var:.4f}")

# Visualisation
plt.hist(portfolio_returns, bins=50, edgecolor='black', alpha=0.7)
plt.axvline(x=var, color='r', linestyle='--', label=f'VaR {confidence_level*100}%')
plt.title('Distribution des rendements simulés (scénario réel)')
plt.xlabel('Rendements')
plt.ylabel('Fréquence')
plt.legend()
plt.show()