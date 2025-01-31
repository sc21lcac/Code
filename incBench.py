import matplotlib.pyplot as plt
import numpy as np
from mplsoccer import Pitch
from mplsoccer import VerticalPitch
from pprint import pprint

# Create figure with two subplots
fig, axs = plt.subplots(2, 1, figsize=(6, 10), 
                       gridspec_kw={'height_ratios': [4, 1]})

# Create and draw the main pitch
pitch = VerticalPitch(pitch_type='uefa', goal_type='box')
pitch.draw(ax=axs[0])

# Starting XI positions
positions = [
    "GK", 
    "RB", 
    "RCB", 
    "LCB", 
    "LB", 
    "RM", 
    "RCM", 
    "LCM", 
    "LM", 
    "RCF", 
    "LCF"
]

# Draw the formation on the main pitch
ax_scatter = pitch.formation('442', kind='scatter', s=500, ax=axs[0])
ax_text = pitch.formation('442', positions=positions, kind='text', 
                         text=positions, va='center', ha='center', 
                         fontsize=10, xoffset=5, ax=axs[0])
ax_text = pitch.formation('442', positions=positions, kind='text', 
                         text=positions, va='center', ha='center', 
                         fontsize=8, xoffset=0, ax=axs[0])
ax_text = pitch.formation('442', positions=positions, kind='text', 
                         text=positions, va='center', ha='center', 
                         fontsize=10, xoffset=-5, ax=axs[0])

# Setup the bench area
bench_players = ["SUB1", "SUB2", "SUB3", "SUB4"]
axs[1].set_xlim(-1, 1)
axs[1].set_ylim(-1, 1)

# Hide the border of axs[1]
for spine in axs[1].spines.values():
    spine.set_visible(False)

# Calculate positions for bench players
num_subs = len(bench_players)
#x_positions = np.linspace(-0.45, 0.45, num_subs)
x_positions = [-0.45 + i * (0.9 / (num_subs - 1)) for i in range(num_subs)]
y_positions = [0] * num_subs  # All at same y-level

# Plot bench players
axs[1].scatter(x_positions, y_positions, s=500)
for i, (x, y, text) in enumerate(zip(x_positions, y_positions, bench_players)):
    axs[1].text(x, y-0.35, text, ha='center', va='center', fontsize=10)

# Removes axis labels from bench
axs[1].set_xticks([])
axs[1].set_yticks([])

# Create rectangle around bench as spine border (data area) to is too big and spacious
axs[1].add_patch(plt.Rectangle((-0.68, -0.5), 1.35, 1, 
                              facecolor='none', 
                              edgecolor='black', 
                              linestyle='-'))

axs[1].text(0, 0.6, 'Bench', ha='center', va='bottom', fontsize=10)



# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()