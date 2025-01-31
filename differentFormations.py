import matplotlib.pyplot as plt
from mplsoccer import Pitch
from mplsoccer import VerticalPitch
from pprint import pprint

pitch = Pitch()
#print(pitch.formations)
formation = pitch.get_formation('442')
pprint(formation)

fig, axs = plt.subplots(nrows=2, figsize=(6, 11))
# use uefa pitch type so don't need to list positions
pitch = VerticalPitch(pitch_type='uefa', goal_type='box')
#fig, ax = pitch.draw(figsize=(6, 8.72))
pitch.draw(axs[0])



positionst = [
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
#ax_scatter = pitch.formation('442', positions=positionst, kind='scatter', ax=ax)
ax_scatter = pitch.formation('442', kind='scatter', ax=ax)
ax_text = pitch.formation('442', positions=positionst, kind='text', text=positionst, va='center', ha='center', fontsize=10, xoffset=-4, ax=ax)
ax_text = pitch.formation('442', positions=positionst, kind='text', text=positionst, va='center', ha='center', fontsize=10, xoffset=-8, ax=ax)

# Add title
plt.title('4-4-2 Formation', pad=20)

# Show the plot
plt.show()

''' 
Either do 11 players any formation, validation of 15  players, and wants them to be put in a given formation

Create 2D array containing names, cost, club, position
order array from gk, def, mid, att

count n.o players in each position  
merge formation into a string
get list of positions required for formation and put them in a list

Then create 3 lists, names, cost, club
Do scatter, names above, club abbr (in position dot/circle), cost below



'''
#
'''
import matplotlib.pyplot as plt
import numpy as np
from mplsoccer import Pitch
from mplsoccer import VerticalPitch
from pprint import pprint

# Create figure with two subplots, one for pitch and one for bench
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 11), 
                              gridspec_kw={'height_ratios': [4, 1]})  # 4:1 ratio between pitch and bench

# Create and draw the main pitch
pitch = VerticalPitch(pitch_type='uefa', goal_type='box')
pitch.draw(ax=ax1)

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
ax_scatter = pitch.formation('442', kind='scatter', ax=ax1)
ax_text = pitch.formation('442', positions=positions, kind='text', 
                         text=positions, va='center', ha='center', 
                         fontsize=10, xoffset=-4, ax=ax1)

# Setup the bench area
bench_players = ["SUB1", "SUB2", "SUB3", "SUB4"]
ax2.set_xlim(-1, 1)
ax2.set_ylim(-1, 1)

# Calculate positions for bench players
num_subs = len(bench_players)
x_positions = np.linspace(-0.6, 0.6, num_subs)
y_positions = [0] * num_subs  # All at same y-level

# Plot bench players
ax2.scatter(x_positions, y_positions, c='red', zorder=2)
for i, (x, y, text) in enumerate(zip(x_positions, y_positions, bench_players)):
    ax2.text(x, y-0.2, text, ha='center', va='center', fontsize=10)

# Customize bench area
ax2.set_title('Bench', pad=10)
ax2.set_xticks([])
ax2.set_yticks([])
ax2.add_patch(plt.Rectangle((-0.8, -0.5), 1.6, 1, 
                          facecolor='none', 
                          edgecolor='black', 
                          linestyle='-'))

# Add main title
fig.suptitle('4-4-2 Formation with Bench', y=0.95)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
'''

#from mplsoccer import Pitch

# Create a Pitch object
#pitch = Pitch()

# Get the list of valid formations
#formations_list = pitch.formations
#print("List of valid mplsoccer formations:")
#print(formations_list)

# Alternatively, get detailed information in a DataFrame format
#formations_df = pitch.formations_dataframe()
#print("\nDetailed formations DataFrame:")
#print(formations_df)


#from mplsoccer.pitch import Pitch
#pitch = Pitch(pitch_color='grass', line_color='white', stripe=True)
#fig, ax = pitch.draw()


#from formations import Formation

# Initialize the formation
#formation = Formation()

# Access specific formations
#formation_442 = formation.formations['442']  # Get 4-4-2 formation
#formation_433 = formation.formations['433']  # Get 4-3-3 formation

# Print to check positions
#for player in formation_442:
 #   print(f"{player.name}: Position - ({player.x}, {player.y})")


#from mplsoccer import Pitch
#import matplotlib.pyplot as plt
#pitch = Pitch(pitch_color='grass', line_color='white', stripe=True)
#print(pitch.formations)
#fig, ax = pitch.draw()
#plt.show()




#from mplsoccer import VerticalPitch
#pitch = VerticalPitch()
#fig, ax = pitch.draw(figsize=(6.875, 10))
#position_text = pitch.formation('442',
#                                positions=[1, 2, 3, 5, 6, 9, 11, 12, 16, 22, 24],
#                                text=['GK', 'RB', 'RCB', 'LCB', 'LB', 'RDM', 'LDM',
#                                'RM', 'LM', 'RCF', 'LCF'],
#                                ax=ax,
#                                kind='text')
