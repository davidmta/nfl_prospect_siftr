import sqlite3
from sqlite3 import Error
import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

### ----------------------------------------------------------------------------------------------------
### CLUSTER_HW
### ----------------------------------------------------------------------------------------------------
def cluster_hw(conn):
	cur = conn.cursor()
	parse_hw(cur)

def parse_hw(cur):
	#plot_all(cur)
	plot_all_group(cur)

def scatterplot_position(height_raw,weight_raw):
	data = []
	for i in range(0,len(weight_raw)):
		if weight_raw[i][0]:
			print height_raw[i][0]
			weight_entry = convert_weight(weight_raw[i])
			height_entry = convert_height(height_raw[i])
			data.append([height_entry,weight_entry])
	df = pd.DataFrame(data,columns=['Height', 'Weight'])
	df.plot(kind='scatter', x='Height', y='Weight');
	plt.show()

def scatter(cur,position):		
	cur.execute("SELECT HEIGHT FROM SR_PLAYERS WHERE POSITION = '" + position + "'")	
	height_raw = cur.fetchall()
	cur.execute("SELECT WEIGHT FROM SR_PLAYERS WHERE POSITION = '" + position + "'")	
	weight_raw = cur.fetchall()
	scatterplot_position(height_raw,weight_raw)

def plot_all_group(cur):
	scatter(cur,'T')
	positions = ['QB','RB','WR','TE','T','OL','G','FB','LB','DT','DE','DL','DB','CB','S','P','PK']

def plot_all():
	cur.execute("SELECT HEIGHT FROM SR_PLAYERS")
	height_all_raw = cur.fetchall()
	cur.execute("SELECT WEIGHT FROM SR_PLAYERS")
	weight_all_raw = cur.fetchall()
	stats_all = clean_all(height_all_raw,weight_all_raw)
	stats_all.plot(kind='scatter', x='Height', y='Weight');
	plt.show()

def clean_all(height_all_raw,weight_all_raw):
	stats_all = []
	for i in range(0,113877):
		if height_all_raw[i][0]:
			weight_entry = convert_weight(weight_all_raw[i])
			height_entry = convert_height(height_all_raw[i])
			stats_all.append([height_entry,weight_entry])
	return pd.DataFrame(stats_all,columns=['Height', 'Weight'])

def convert_weight(weight):
	return int(re.sub("lb","",weight[0]))

def convert_height(height):
	height = height[0].split("-")
	return int(height[0])*12 + int(height[1])

### ----------------------------------------------------------------------------------------------------
### CREATE_CONNECTION
### ----------------------------------------------------------------------------------------------------
def create_connection(db):
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as e:
        print(e)

def main():
    db = "/Users/davidta/Desktop/sr_players_database.db"
    conn = create_connection(db)
    cluster_hw(conn)
  

if __name__ == "__main__":
    main()