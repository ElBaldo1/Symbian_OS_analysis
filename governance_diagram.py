import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Creazione del diagramma di governance con rettangoli più grandi per il testo
fig, ax = plt.subplots(figsize=(12, 8))

# Definizione delle posizioni dei box
positions = {
    'Board of Directors': (0.5, 0.9),
    'Project Management Office (PMO)': (0.5, 0.75),
    'Project Manager': (0.3, 0.6),
    'Functional Managers': (0.7, 0.6),
    'Project Team': (0.3, 0.4),
    'Technical Team': (0.7, 0.4),
    'Stakeholders': (0.5, 0.2)
}

# Dimensioni dei box
box_width = 0.3
box_height = 0.1

# Disegna i box con bordi più spessi
for role, (x, y) in positions.items():
    ax.add_patch(mpatches.Rectangle(
        (x - box_width / 2, y - box_height / 2),
        box_width, box_height,
        facecolor='lightblue', edgecolor='black', linewidth=2.5  # Bordi più spessi con linewidth
    ))
    ax.text(x, y, role, ha='center', va='center', fontsize=10, weight='bold', wrap=True)

# Disegna le frecce di connessione
connections = [
    ('Board of Directors', 'Project Management Office (PMO)'),
    ('Project Management Office (PMO)', 'Project Manager'),
    ('Project Management Office (PMO)', 'Functional Managers'),
    ('Project Manager', 'Project Team'),
    ('Functional Managers', 'Technical Team'),
    ('Project Team', 'Stakeholders'),
    ('Technical Team', 'Stakeholders')
]

for start, end in connections:
    x_start, y_start = positions[start]
    x_end, y_end = positions[end]
    ax.annotate('', xy=(x_end, y_end + box_height / 2), xytext=(x_start, y_start - box_height / 2),
                arrowprops=dict(facecolor='black', arrowstyle='->'))

# Rimuovi assi
ax.axis('off')

# Titolo del diagramma
plt.title('Symbian OS Project Governance Structure', fontsize=14, weight='bold')

# Mostra il diagramma
plt.tight_layout()
plt.show()
