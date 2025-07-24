import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))
plt.scatter([0,10,0], [0,0,10], s=1000, marker="s") # Triangle outline
plt.text(5,8,"Joe-Pye Weed", ha='center', style='italic')
plt.savefig('garden.png')
