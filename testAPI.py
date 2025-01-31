import requests
import random
import matplotlib.pyplot as plt
from mplsoccer import VerticalPitch


# get data from FPL API endpoint
r = requests.get('https://fantasy.premierleague.com/api/bootstrap-static/').json()


GKS = ['Hein', 'Raya', 'Neto', 'Setford', 'Gauci', 'Marschall', 'Martinez', 'Olsen', 'Sinisalo', 'Zych', 'Paulsen', 'Travers', 'Arrizabalaga', 'Dennis', 'Flekken', 'Valdimarsson', 'Steele', 'Verbruggen', 'Rushworth', 'Cahill', 'Bergström', 'Bettinelli', 'Petrović', 'Sánchez', 'Jørgensen', 'Henderson', 'Matthews', 'Turner', 'J.Virginia', 'Pickford', 'Begovic', 'Benda', 'Leno', 'Slicker', 'Walton', 'Muric', 'Hermansen', 'Iversen', 'Stolarczyk', 'Ward', 'A.Becker', 'Kelleher', 'Jaros', 'Davies', 'Carson', 'Ederson M.', 'Ortega Moreno', 'Bayindir', 'Heaton', 'Onana', 'Dúbravka', 'Odysseas', 'Pope', 'Ruddy', 'C.Miguel', 'Sels', 'Ramsdale', 'Bazunu', 'Lis', 'Lumley', 'McCarthy', 'Austin', 'Forster', 'Vicario', 'Whiteman', 'Areola', 'Fabianski', 'Foderingham', 'Johnstone', 'Bentley', 'José Sá', 'King']        
DEF = ['Gabriel', 'J.Timber', 'Kiwior', 'Saliba', 'Tierney', 'Tomiyasu', 'White', 'Zinchenko', 'Calafiori', 'Kacurri', 'Heaven', 'Nichols', 'Cash', 'Diego Carlos', 'Digne', 'Hause', 'Kesler-Hayden', 'Konsa', 'Maatsen', 'Mings', 'Nedeljkovic', 'Pau', 'Sousa', 'Bogarde', 'Swinkels', 'Aarons', 'Hill', 'Kerkez', 'Mepham', 'Senesi', 'Smith', 'Zabarnyi', 'Huijsen', 'J.Araujo', 'Ajer', 'Collins', 'Henry', 'Hickey', 'Ji-soo', 'Mee', 'Pinnock', 'Roerslev', 'Zanka', 'Van den Berg', 'Meghoma', 'Barco', 'Dunk', 'Estupiñan', 'Igor', 'Lamptey', 'Offiah', 'Van Hecke', 'Veltman', 'Webster', 'F.Kadıoğlu', 'Samuels', 'B.Badiashile', 'Chilwell', 'Colwill', 'Cucurella', 'Disasi', 'Gilchrist', 'Gusto', 'James', 'M.Sarr', 'Tosin', 'W.Fofana', 'Wiley', 'Chalobah', 'C.Richards', 'Chadi Riad', 'Clyne', 'Guéhi', 'Holding', 'Mitchell', 'Muñoz', 'Ward', 'Lacroix', 'Kporha', 'Branthwaite', 'Coleman', 'Holgate', 'Keane', 'Mykolenko', 'Patterson', 'Tarkowski', 'Young', "O'Brien", 'Dixon', 'Andersen', 'Bassey', 'Castagne', 'Diop', 'Mbabu', 'Ream', 'Robinson', 'Tete', 'Sessegnon', 'J.Cuenca', 'Baggott', 'Burgess', 'H.Clarke', 'Davis', 'Edmundson', 'Greaves', 'Johnson', 'Ndaba', 'Tuanzebe', 'Woolfenden', 'Townsend', "O'Shea", 'Coady', 'Faes', 'Justin', 'Kristiansen', 'Okoli', 'Ricardo', 'Souttar', 'Thomas', 'Vestergaard', 'Nelson', 'Alexander-Arnold', 'Bradley', 'Gomez', 'Konaté', 'N.Phillips', 'Quansah', 'R.Williams', 'Robertson', 'Tsimikas', 'Virgil', 'Akanji', 'Aké', 'Gvardiol', 'João Cancelo', 'Lewis', 'Rúben', 'Stones', 'Walker', 'Kaboré', 'Simpson-Pusey', 'Wilson-Esbrand', 'Dalot', 'Evans', 'Lindelof', 'Maguire', 'Malacia', 'Martinez', 'Shaw', 'Yoro', 'De Ligt', 'Mazraoui', 'Amass', 'A.Murphy', 'Botman', 'Burn', 'Hall', 'Kelly', 'Krafth', 'Lascelles', 'Lewis', 'Livramento', 'Schär', 'Targett', 'Trippier', 'Pivas', 'Alex Moreno', 'Aina', 'Boly', 'Murillo', 'N.Williams', 'O.Richards', 'Omobamidele', 'Panzo', 'Toffolo', 'Worrall', 'Milenković', 'Morato', 'Bednarek', 'Bella-Kotchap', 'Bree', 'Edwards', 'Harwood-Bellis', 'Larios', 'Manning', 'Stephens', 'Sugawara', 'Taylor', 'Walker-Peters', 'Wood', 'A.Phillips', 'Davies', 'Dragusin', 'E.Royal', 'Pedro Porro', 'Reguilón', 'Romero', 'Spence', 'Udogie', 'Van de Ven', 'Wan-Bissaka', 'Coufal', 'Cresswell', 'Emerson', 'Kilman', 'Mavropanos', 'N.Aguerd', 'Zouma', 'Todibo', 'Casey', 'Scarles', 'Aït-Nouri', 'Dawson', 'Doherty', 'H.Bueno', 'Hoever', 'Mosquera', 'N.Semedo', 'Pedro Lima', 'S.Bueno', 'Toti', 'Meupiyou', 'Pond']
MID = ['Fábio Vieira', 'Jorginho', 'Martinelli', 'Nwaneri', 'Ødegaard', 'Rice', 'Saka', 'Thomas', 'Trossard', 'Sterling', 'Lewis-Skelly', 'Merino', "Oulad M'hand", 'Kabia', 'Bailey', 'Barkley', 'Barrenechea', 'Buendia', 'Dendoncker', 'Diaby', 'Dobbin', 'Iling Jr', 'Kamara', 'McGinn', 'Ramsey', 'Rogers', 'Tielemans', 'Onana', 'Jaden', 'Young', 'Adams', 'Anthony', 'Brooks', 'Christie', 'Cook', 'Faivre', 'H.Traorè', 'Kluivert', 'O.Dango', 'Philip', 'Scott', 'Semenyo', 'Sinisterra', 'Tavernier', 'Brierley', 'Damsgaard', 'Dasilva', 'Janelt', 'Jensen', 'Konak', 'Lewis-Potter', 'Mbeumo', 'Nørgaard', 'Onyeka', 'Peart-Harris', 'Schade', 'Yarmoliuk', 'Carvalho', 'Trevitt', 'G.Nunes', 'Yogane', 'Maghoma', 'Adingra', 'Baker-Boaitey', 'Baleba', 'Cozier-Duberry', 'Dahoud', 'Enciso', 'Gilmour', 'Gross', 'Hinshelwood', 'I.Osman', 'Kozlowski', 'March', 'Mazilu', 'Milner', 'Minteh', 'Mitoma', 'Moder', 'Peupion', 'Sarmiento', 'Wieffer', 'Gruda', 'Ayari', 'Moran', 'Georginio', "O'Riley", 'Andrey Santos', 'Ângelo', 'Caicedo', 'Casadei', 'Chukwuemeka', 'Dewsbury-Hall', 'Enzo', 'Gallagher', 'Kellyman', 'Lavia', 'Madueke', 'Mudryk', 'Nkunku', 'Palmer', 'Renato Veiga', 'Sancho', 'Neto', 'João Félix', 'Ahamada', 'C.Doucouré', 'Ebiowei', 'Eze', 'Hughes', 'Kamada', 'Lerma', 'M.França', 'Ozoh', 'Rak-Sakyi', 'Schlupp', 'Wharton', 'I.Sarr', 'Umeh-Chibueze', 'Devenny', 'Agbinone', 'Rodney', 'A.Doucoure', 'Gana', 'Garner', 'Harrison', 'Iroegbunam', 'McNeil', 'Lindstrøm', 'Armstrong', 'Metcalfe', 'Mangala', 'Bates', 'Nelson', 'Smith Rowe', 'Adama', 'Andreas', 'Cairney', 'Harris', 'Iwobi', 'Lukić', 'Reed', 'Wilson', 'King', 'Godo', 'Berge', 'Broadhead', 'Burns', 'Chaplin', 'Harness', 'Humphreys', 'Hutchinson', 'Luongo', 'Morsy', 'Taylor', 'Phillips', 'Szmodics', 'Cajuste', 'J.Clarke', 'Ogbene', 'Buonanotte', 'J.Ayew', 'B.Soumaré', 'Choudhury', 'De Cordova-Reid', 'Golding', 'Marcal', 'Mavididi', 'McAteer', 'Ndidi', 'Winks', 'Skipp', 'A.Fatawu', 'Alves', 'El Khannouss', 'Bajcetic', 'Clark', 'Diogo J.', 'Doak', 'Elliott', 'Endo', 'Gravenberch', 'Jones', 'Luis Díaz', 'M.Salah', 'Mac Allister', 'McConnell', 'Morton', 'Szoboszlai', 'Chiesa', 'Bernardo', 'Bobb', 'De Bruyne', 'Doku', 'Foden', 'Grealish', 'Kovačić', 'Matheus N.', 'McAtee', 'Rodrigo', 'Sávio', 'O’Reilly', 'Gündogan', 'Wright', 'Amad', 'Antony', 'B.Fernandes', 'Casemiro', 'Eriksen', 'Garnacho', 'Hannibal', 'Mainoo', 'McTominay', 'Mount', 'Pellistri', 'Rashford', 'Collyer', 'Ugarte', 'Fletcher', 'Fitzgerald', 'Almirón', 'Barnes', 'Bruno G.', 'Gordon', 'Hayden', 'J.Murphy', 'Joelinton', 'Kuol', 'Longstaff', 'Miley', 'Tonali', 'White', 'Willock', 'Anderson', 'Bowler', 'Da Silva Moreira', 'Danilo', 'Dominguez', 'Elanga', 'Gibbs-White', 'Hudson-Odoi', 'Mighten', "O'Brien", 'Sangaré', 'Yates', 'Ward-Prowse', 'Jota Silva', 'Sosa', 'Ugochukwu', 'Fraser', 'Alcaraz', 'Amo-Ameyaw', 'Aribo', 'Charles', 'Edozie', 'Kamaldeen', 'Lallana', 'Smallbone', 'Cornet', 'Downes', 'Brereton Díaz', 'Dibling', 'M.Fernandes', 'Bentancur', 'Bergvall', 'Bissouma', 'Bryan', 'Devine', 'Gray', 'Højbjerg', 'Johnson', 'Kulusevski', 'Lo Celso', 'Maddison', 'P.M.Sarr', 'Solomon', 'Son', 'Werner', 'Moore', 'Odobert', 'Álvarez', 'Bowen', 'Earthy', 'Kudus', 'L.Guilherme', 'L.Paquetá', 'Souček', 'Irving', 'Summerville', 'G.Rodríguez', 'C.Soler', 'B.Traore', 'Bellegarde', 'Chiquinho', 'Chirewa', 'Cundle', 'Doyle', 'Gonzalez', 'Guedes', 'Hee Chan', 'Hodge', 'J.Gomes', 'Mario Jr.', 'Podence', 'R.Gomes', 'Sarabia', 'André', 'Forbs']
FWD = ['G.Jesus', 'Havertz', 'Butler-Oyedeji', 'Duran', 'Watkins', 'Enes Ünal', 'Jebbison', 'Evanilson', 'Thiago', 'Toney', 'Wissa', 'Ferguson', 'João Pedro', 'O’Mahony', 'Undav', 'Welbeck', 'D.D.Fofana', 'Deivid', 'Lukaku', 'Marc Guiu', 'N.Jackson', 'Nketiah', 'Mateta', 'Marsh', 'Broja', 'Beto', 'Calvert-Lewin', 'Maupay', 'Ndiaye', 'Y. Chermiti', 'Muniz', 'Raúl', 'Stansfield', 'Vinicius', 'Al-Hamadi', 'Delap', 'Hirst', 'Ladapo', 'Edouard', 'Cannon', 'Daka', 'Vardy', 'Darwin', 'Gakpo', 'Haaland', 'J.Alvarez', 'Højlund', 'Zirkzee', 'Wheatley', 'Isak', 'Wilson', 'Osula', 'Awoniyi', 'Dennis', 'Ui-jo', 'Wood', 'Archer', 'Armstrong', 'Mara', 'Onuachu', 'Stewart', 'Solanke', 'Richarlison', 'Scarlett', 'Veliz', 'Lankshear', 'Antonio', 'Ings', 'Füllkrug', 'Chiwome', 'Cunha', 'Fábio Silva', 'Fraser', 'Kalajdžić', 'Strand Larsen']
FORMATIONS = ['343','352','442','433','451','532','541','523']

userSquad = [[],[],[],[],[]]
#userSquad = [[],[],[],[]]
# Add GKs to the first subarray
for _ in range(2):
    userSquad[0].append([random.choice(GKS)])

# Add DEFs to the second subarray
for _ in range(5):  # Adjust the number to match how many defenders you want
    userSquad[1].append([random.choice(DEF)])

# Add MIDs to the third subarray
for _ in range(5):  # Adjust the number to match how many midfielders you want
    userSquad[2].append([random.choice(MID)])

# Add FWDs to the fourth subarray
for _ in range(3):  # Adjust the number to match how many forwards you want
    userSquad[3].append([random.choice(FWD)])

# Add a formation to the fifth subarray
for _ in range(1):  
    #userSquad[4].append(random.choice(FORMATIONS))
    ##userSquad[4].append('4321') b
    #userSquad[4].append('343')
    #userSquad[4].append('523')
    #userSquad[4].append('352')
    userSquad[4].append('532')
    #userSquad[4].append('433')


allPlayers = r['elements']
allTeams = r['teams']

#givenFormation = '442'
print(userSquad[4])
givenFormation = userSquad.pop(4)[0]
print(givenFormation)
print(userSquad)



squadClubs = []
totalTeamCost = 0

for i in range(4):
    for j in range(len(userSquad[i])):    
        playerName = userSquad[i][j][0]
        
        playerFound = False  # Variable to track if player is found
        for findPlayer in allPlayers:
            if findPlayer['web_name'] == playerName:
                playerFound = True
                player = findPlayer

                # Round to one decimal point to prevent precision or formatting problems
                playerCost = round(player['now_cost']/10, 1) 

                teamCode = player['team_code']
                for team in allTeams:
                    if team['code'] == teamCode:
                        playerTeam = team['short_name']
                        break
                
                totalTeamCost = totalTeamCost + playerCost
                squadClubs.append(playerTeam)

                userSquad[i][j].append(playerTeam)
                userSquad[i][j].append(str(playerCost))
                
                break

        # If player wasn't found, print a message
        if playerFound == False:
            print(f"Player '{playerName}' was not found in FPL player database")

print(totalTeamCost)
#print(squadClubs)
if totalTeamCost > 100:
    print("too much money")
for club in squadClubs:
        if squadClubs.count(club) >= 4:
            print("too many clubs")



                
for positionArray in userSquad:
    positionArray.sort(key=lambda playerInfo: playerInfo[2], reverse=True)

#print(userSquad)

orderedUserSquad = []

formationSection = [int(i) for i in givenFormation]  # Convert formation into characters stored in an array

orderedUserSquad.append(userSquad[0].pop(0))

# Pop defenders
for _ in range(formationSection[0]):
    orderedUserSquad.append(userSquad[1].pop(0))  # Pop top 4 DEFs

# Pop midfielders
for _ in range(formationSection[1]):
    orderedUserSquad.append(userSquad[2].pop(0))  # Pop top 4 MIDs

# Pop forwards
for _ in range(formationSection[2]):
    orderedUserSquad.append(userSquad[3].pop(0))  # Pop top 2 FWDs

# Step 3: Append remaining players from GKS, DEF, MID, FWD to the orderedUserSquad
for position_array in userSquad:
    while position_array:  # While the array still has elements
        orderedUserSquad.append(position_array.pop(0))  # Pop each remaining player

# Print results
print("Ordered User Squad:")

print(orderedUserSquad)
                

               
# Create figure with two subplots
fig, axs = plt.subplots(2, 1, figsize=(6, 10), 
                       gridspec_kw={'height_ratios': [4, 1]})

# Create and draw the main pitch
pitch = VerticalPitch(pitch_type='uefa', goal_type='box')
pitch.draw(ax=axs[0])

# Starting XI positions
mplFormationData = pitch.get_formation(givenFormation)
positionsList = [position.name for position in mplFormationData]

startersNames = []
startersClubs = []
startersCosts = []
for i in range(11):
    startersNames.append(orderedUserSquad[i][0])
    startersClubs.append(orderedUserSquad[i][1])
    startersCosts.append('£' + orderedUserSquad[i][2])

subsNames = []
subsClubs = []
subsCosts = []
for i in range(4):
    j = i + 11
    subsNames.append(orderedUserSquad[j][0])
    subsClubs.append(orderedUserSquad[j][1])
    subsCosts.append('£' + orderedUserSquad[j][2])

# Draw the formation on the main pitch positionsList
ax_scatter = pitch.formation(givenFormation, kind='scatter', s=500, ax=axs[0], color='lightgreen')
ax_text = pitch.formation(givenFormation, positions=positionsList, kind='text', 
                         text=startersNames, va='center', ha='center', 
                         fontsize=10, xoffset=4.6, ax=axs[0])
ax_text = pitch.formation(givenFormation, positions=positionsList, kind='text', 
                         text=startersClubs, va='center', ha='center', 
                         fontsize=8, xoffset=0, ax=axs[0])
ax_text = pitch.formation(givenFormation, positions=positionsList, kind='text', 
                         text=startersCosts, va='center', ha='center', 
                         fontsize=10, xoffset=-4.6, ax=axs[0])

# Setup the bench area
bench_players = ["SUB1", "SUB2", "SUB3", "SUB4"]
axs[1].set_xlim(-1, 1)
axs[1].set_ylim(-1, 1)

# Hide the border of axs[1]
for spine in axs[1].spines.values():
    spine.set_visible(False)

# Calculate positions for bench players
num_subs = len(bench_players)
x_positions = [-0.45, -0.15, 0.15, 0.45]

# Using range
for i in range(4):
    x = x_positions[i]
    y = 0
    axs[1].scatter(x, y, s=500, color='lightgreen')
    axs[1].text(x, y+0.35, subsNames[i], ha='center', va='center', fontsize=10)
    axs[1].text(x, y, subsClubs[i], ha='center', va='center', fontsize=8)
    axs[1].text(x, y-0.35, subsCosts[i], ha='center', va='center', fontsize=10)


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
                

