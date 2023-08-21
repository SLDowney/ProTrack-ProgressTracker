import random
import sqlite3
from contextlib import closing
from flask import Flask, render_template, request, abort, redirect, session
import os
from werkzeug.utils import secure_filename
from flask import jsonify
import re


app = Flask(__name__)
app.config["UPLOAD_PATH"] = "static/images"
app.config["UPLOAD_EXTENSIONS"] = ['.jpg', '.png', '.jfif', '.jpeg']
app.config["MAX_CONTENT_LENGTH"] = 1024 * 1024

conn = sqlite3.connect("totk.db", check_same_thread=False)
conn.row_factory = sqlite3.Row

# Define the calculate_completion_percentage function
def calculate_completion_percentage(completed_rows, total_rows):
    if total_rows == 0:
        return 0
    return (completed_rows / total_rows) * 100

def get_percentages():
    with closing(conn.cursor()) as c:
        # Fetch the total number of rows for each table
        c.execute("SELECT COUNT(*) FROM locations WHERE location_type = 'Location'")
        total_locations = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM locations WHERE location_type = 'Chasm'")
        total_chasms = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM locations WHERE location_type = 'Well'")
        total_wells = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM locations WHERE location_type = 'Depths Mine'")
        total_depths_mines = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM fairyfountains")
        total_great_fairy_fountains = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM shrines")
        total_shrines = c.fetchone()[0]

        # Add the counts for the additional tables
        c.execute("SELECT COUNT(*) FROM addison")
        total_addison = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM Quests WHERE quest_type = 'Adventure'")
        total_adventure = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM caves")
        total_caves = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM compendium")
        total_compendium = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM allkoroks")
        total_koroks = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM lightroots")
        total_lightroots = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM Quests WHERE quest_type = 'Main'")
        total_mainqu = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM oldmaps")
        total_oldmaps = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM shrinequests")
        total_shrinequests = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM Quests WHERE quest_type = 'Side'")
        total_sidequests = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM towers")
        total_towers = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM device_dispenser")
        total_dispensers = c.fetchone()[0]

        # Fetch the number of completed rows for each table
        c.execute("SELECT COUNT(*) FROM shrines WHERE shrine_done = 2")
        completed_shrines = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM locations WHERE location_done = 1 AND location_type = 'Location'")
        completed_locations = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM locations WHERE location_done = 1 AND location_type = 'Chasm'")
        completed_chasms = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM locations WHERE location_done = 1 AND location_type = 'Well'")
        completed_wells = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM locations WHERE location_done = 1 AND location_type = 'Depths Mine'")
        completed_depths_mines = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM fairyfountains WHERE fairy_found = 1")
        completed_great_fairy_fountains = c.fetchone()[0]

        # Add the counts for the completed rows in the additional tables
        c.execute("SELECT COUNT(*) FROM addison WHERE addison_done = 1")
        completed_addison = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM Quests WHERE quest_type = 'Adventure' AND quest_done = 2")
        completed_adventure = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM caves WHERE cave_done = 2")
        completed_caves = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM compendium WHERE comp_done = 1")
        completed_compendium = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM allkoroks WHERE korok_done = 1")
        completed_koroks = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM lightroots WHERE root_done = 1")
        completed_lightroots = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM Quests WHERE quest_type = 'Main' AND quest_done = 2")
        completed_mainqu = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM oldmaps WHERE map_type = 'Treasure' AND map_collected = 1")
        completed_oldmaps = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM shrinequests WHERE shrinequ_done = 2")
        completed_shrinequests = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM Quests WHERE quest_type = 'Side' AND quest_done = 2")
        completed_sidequests = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM towers WHERE tower_done = 1")
        completed_towers = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM device_dispenser WHERE dis_done = 1")
        completed_dispensers = c.fetchone()[0]

        # Calculate the percentage completion for the additional tables
        percentages = {
            "percentage_chasms": calculate_completion_percentage(completed_chasms, total_chasms),
            "percentage_great_fairy_fountains": calculate_completion_percentage(completed_great_fairy_fountains, total_great_fairy_fountains),
            "percentage_depths_mines": calculate_completion_percentage(completed_depths_mines, total_depths_mines),
            "percentage_wells": calculate_completion_percentage(completed_wells, total_wells),
            "percentage_locations": calculate_completion_percentage(completed_locations, total_locations),
            "percentage_shrines": calculate_completion_percentage(completed_shrines, total_shrines),
            "percentage_addison": calculate_completion_percentage(completed_addison, total_addison),
            "percentage_side_adventures": calculate_completion_percentage(completed_adventure, total_adventure),
            "percentage_caves": calculate_completion_percentage(completed_caves, total_caves),
            "percentage_compendium": calculate_completion_percentage(completed_compendium, total_compendium),
            "percentage_koroks": calculate_completion_percentage(completed_koroks, total_koroks),
            "percentage_lightroots": calculate_completion_percentage(completed_lightroots, total_lightroots),
            "percentage_main_quests": calculate_completion_percentage(completed_mainqu, total_mainqu),
            "percentage_old_maps": calculate_completion_percentage(completed_oldmaps, total_oldmaps),
            "percentage_shrine_quests": calculate_completion_percentage(completed_shrinequests, total_shrinequests),
            "percentage_side_quests": calculate_completion_percentage(completed_sidequests, total_sidequests),
            "percentage_towers": calculate_completion_percentage(completed_towers, total_towers),
            "percentage_dispensers": calculate_completion_percentage(completed_dispensers, total_dispensers)
        }
    return percentages

@app.route('/side_update', methods=['POST'])
def side_update():
    data = request.get_json()  # Get the JSON data from the request
    side = data.get('side_id')
    side_done = data.get('side_done')
    
    with closing(conn.cursor()) as c:
        c.execute('SELECT * FROM Quests WHERE quest_id = ?', (side,))
        side_info = c.fetchone()

    if  side_done == 1:
        with closing(conn.cursor()) as c:
            if side_info[10] != None:
                search_strings = side_info[10].split('\r\n')
                query = """UPDATE caves SET cave_done = 1 WHERE {} """.format(" OR ".join(["cave_name LIKE '%' || ? || '%'" for _ in search_strings]))
                c.execute(query, search_strings)  # Pass the search_strings list as bindings
            else:
                c.execute('UPDATE caves SET cave_done = 1 WHERE cave_name = ?', (side_info[7],))
            print("Executed update statement with cave_name as ->", side_info[7])
        conn.commit()

    with closing(conn.cursor()) as c:
        c.execute('UPDATE armor SET a_collected = 1 WHERE a_name = ?', (side_info[9],))
        c.execute('UPDATE armor_single SET a_collected = 1 WHERE a_set = ?', (side_info[9],))
        c.execute('UPDATE bargains SET item_done = 1 WHERE item_name = ?', (side_info[9],))
        print("Executed update statement with a_name as ->", side_info[9])
    conn.commit()
    
    if side_done != 0:
        with closing(conn.cursor()) as c:
            c.execute('UPDATE locations SET location_done = 1 WHERE location_name = ?', (side_info[7],))
            print("Executed update statement with location_name as ->", side_info[7])
        conn.commit()

    if side_info[10] != None:
        with closing(conn.cursor()) as c:
            search_strings = side_info[10].split('\r\n')
            print("Search Strings ->", search_strings)
            query = """UPDATE locations SET location_done = 1 WHERE {} """.format(" OR ".join(["location_name LIKE '%' || ? || '%'" for _ in search_strings]))
            c.execute(query, search_strings)  # Pass the search_strings list as bindings
            print("Executed update statement with location_name as ->", side_info[10])
        conn.commit()
    
    print("Side ->", side)
    print("Side_Done ->", side_done)

    if side == "242" and side_done == 2:
        with closing(conn.cursor()) as c:
            print("Updating Quickshot Course")
            c.execute('UPDATE Quests SET quest_done = 1 WHERE quest_id = 243')
        conn.commit()
    
    if side == "243" and side_done == 2:
        print("Updating Death Mountain Course")
        with closing(conn.cursor()) as c:
            c.execute('UPDATE Quests SET quest_done = 1 WHERE quest_id = 241')
        conn.commit()

    print("IN UPDATE FUNCTION ->", side_info[9])
    return "success"

@app.route('/shrine_update', methods=['POST'])
def shrine_update():
    data = request.get_json()  # Get the JSON data from the request
    print("data ->", data)
    shrine = data.get('shrine_id')
    with closing(conn.cursor()) as c:
        c.execute('SELECT * FROM shrines WHERE shrine_id = ?', (shrine,))
        shrine_info = c.fetchone()
        
    with closing(conn.cursor()) as c:
        c.execute('UPDATE locations SET location_done = 1 WHERE location_name = ?', (shrine_info[4],))
        print("Executed update statement with location_name as ->", shrine_info[4])
    conn.commit()

    with closing(conn.cursor()) as c:
        c.execute('UPDATE caves SET cave_done = 1 WHERE cave_name = ?', (shrine_info[10],))
        print("Executed update statement with cave_name as ->", shrine_info[10])
    conn.commit()

    with closing(conn.cursor()) as c:
        c.execute('UPDATE armor SET a_collected = 1 WHERE a_name = ?', (shrine_info[8],))
        c.execute('UPDATE armor_single SET a_collected = 1 WHERE a_set = ?', (shrine_info[8],))
        c.execute('UPDATE bargains SET item_done = 1 WHERE item_name = ?', (shrine_info[8],))
        print("Executed update statement with a_name as ->", shrine_info[8])
    conn.commit()

    if shrine_info[7] != None:
        with closing(conn.cursor()) as c:
            if "Crystal" in shrine_info[7]:
                c.execute('UPDATE shrinequests SET shrinequ_done = 2 WHERE shrinequ_name = ?', (shrine_info[7],))
            else:
                c.execute('UPDATE shrinequests SET shrinequ_done = 2 WHERE shrinequ_name = ?', (shrine_info[7],))
            print("Executed update statement with shrinequ_name as ->", shrine_info[7])
        conn.commit()

    print("IN UPDATE FUNCTION ->", shrine_info[2])
    return "success"

@app.route('/cave_update', methods=['POST'])
def cave_update():
    data = request.get_json()  # Get the JSON data from the request
    print("data ->", data)
    cave = data.get('cave_id')
    with closing(conn.cursor()) as c:
        c.execute('SELECT * FROM caves WHERE cave_id = ?', (cave,))
        cave_info = c.fetchone()
        
    with closing(conn.cursor()) as c:
        c.execute('UPDATE locations SET location_done = 1 WHERE location_name = ?', (cave_info[13],))
        print("Executed update statement with location_name as ->", cave_info[13])
    conn.commit()

    # with closing(conn.cursor()) as c:
    #     c.execute('UPDATE armor SET a_collected = 1 WHERE a_name = ?', (cave_info[8],))
    #     c.execute('UPDATE armor_single SET a_collected = 1 WHERE a_set = ?', (cave_info[8],))
    #     c.execute('UPDATE bargains SET item_done = 1 WHERE item_name = ?', (cave_info[8],))
    #     print("Executed update statement with a_name as ->", cave_info[8])
    # conn.commit()

    print("IN UPDATE FUNCTION ->", cave_info[1])
    return "success"

@app.route('/chest_update', methods=['POST'])
def chest_update():
    data = request.get_json()  # Get the JSON data from the request
    chest = data.get('chest_id')
    print("chest:", chest)
    with closing(conn.cursor()) as c:
        c.execute('SELECT * FROM chests WHERE chest_id = ?', (chest,))
        chest_info = c.fetchone()
        print("Chest Info ->", chest_info[1])
        
    with closing(conn.cursor()) as c:
        c.execute('UPDATE armor SET a_collected = 1 WHERE a_name = ?', (chest_info[1],))
        print("Executed update statement with a_name as ->", chest_info[1])
    conn.commit()

    with closing(conn.cursor()) as c:
        c.execute('UPDATE armor_single SET a_collected = 1 WHERE a_set = ?', (chest_info[1],))
        print("Executed update statement with a_set as ->", chest_info[1])
    conn.commit()

    with closing(conn.cursor()) as c:
        c.execute('UPDATE bargains SET item_done = 1 WHERE item_name = ?', (chest_info[1],))
        print("Executed bargains statement with item_name as ->", chest_info[1])
    conn.commit()

    with closing(conn.cursor()) as c:
        c.execute('UPDATE caves SET cave_done = 1 WHERE cave_name = ?', (chest_info[4],))
        print("Executed update statement with cave_name as ->", chest_info[4])
    conn.commit()

    with closing(conn.cursor()) as c:
        c.execute('UPDATE Quests SET quest_done = 1 WHERE quest_name = ?', (chest_info[6],))
        print("Executed update statement with quest_name as ->", chest_info[6])
    conn.commit()
    
    print("IN UPDATE FUNCTION ->", chest_info[1])
    return "success"

@app.route('/oldmap_update', methods=['POST'])
def oldmap_update():
    data = request.get_json()  # Get the JSON data from the request
    map = data.get('treasure_id')
    print("Map:", map)
    with closing(conn.cursor()) as c:
        c.execute('SELECT * FROM oldmaps WHERE map_id = ?', (map,))
        map_info = c.fetchone()
        print("Map Info ->", map_info[4])
        
    with closing(conn.cursor()) as c:
        c.execute('UPDATE armor SET a_collected = 1 WHERE a_name = ?', (map_info[4],))
        print("Executed update statement with a_name as ->", map_info[4])
    conn.commit()

    with closing(conn.cursor()) as c:
        c.execute('UPDATE armor_single SET a_collected = 1 WHERE a_set = ?', (map_info[4],))
        print("Executed update statement with a_set as ->", map_info[4])
    conn.commit()

    with closing(conn.cursor()) as c:
        c.execute('UPDATE bargains SET item_done = 1 WHERE item_name = ?', (map_info[4],))
        print("Executed bargains statement with item_name as ->", map_info[4])
    conn.commit()

    with closing(conn.cursor()) as c:
        search_strings = map_info[7].split('\r\n')
        print("Search Strings ->", search_strings)
        query = """UPDATE locations SET location_done = 1 WHERE {} """.format(" OR ".join(["location_name LIKE '%' || ? || '%'" for _ in search_strings]))
        c.execute(query, search_strings)  # Pass the search_strings list as bindings
        print("Executed update statement with location_name as ->", map_info[7])
        conn.commit()
    
    print("IN UPDATE FUNCTION ->", map_info[4])
    return "success"

@app.route('/main_update', methods=['POST'])
def main_update():
    data = request.get_json()  # Get the JSON data from the request
    print("data ->", data)
    main = data.get('main_id')
    with closing(conn.cursor()) as c:
        c.execute('SELECT * FROM Quests WHERE quest_type = "Main" AND quest_id = ?', (main,))
        main_info = c.fetchone()
        
    with closing(conn.cursor()) as c:
        c.execute('UPDATE locations SET location_done = 1 WHERE location_name = ?', (main_info[7],))
        print("Executed update statement with location_name as ->", main_info[3])
    conn.commit()

    with closing(conn.cursor()) as c:
        c.execute('UPDATE armor SET a_collected = 1 WHERE a_name = ?', (main_info[9],))
        c.execute('UPDATE armor_single SET a_collected = 1 WHERE a_set = ?', (main_info[9],))
        c.execute('UPDATE bargains SET item_done = 1 WHERE item_name = ?', (main_info[9],))
        print("Executed update statement with a_name as ->", main_info[9])
    conn.commit()

    print("IN UPDATE FUNCTION ->", main_info[2])
    return "success"

@app.route('/adventures_update', methods=['POST'])
def adventures_update():
    data = request.get_json()  # Get the JSON data from the request
    print("data ->", data)
    adventure = data.get('adventure_id')
    done = data.get('adventure_done')
    print("data done ->", done)

    with closing(conn.cursor()) as c:
        c.execute('SELECT * FROM Quests WHERE quest_type = "Adventure" AND quest_id = ?', (adventure,))
        adventure_info = c.fetchone()
        
    if adventure_info[10] != None:
        with closing(conn.cursor()) as c:
            search_strings = adventure_info[10].split('\r\n')
            print("Search Strings ->", search_strings)
            query = """UPDATE locations SET location_done = 1 WHERE {} """.format(" OR ".join(["location_name LIKE '%' || ? || '%'" for _ in search_strings]))
            c.execute(query, search_strings)  # Pass the search_strings list as bindings
            print("Executed update statement with location_name as ->", adventure_info[10])
        conn.commit()

    with closing(conn.cursor()) as c:
        c.execute('UPDATE armor SET a_collected = 1 WHERE a_name = ?', (adventure_info[9],))
        c.execute('UPDATE armor_single SET a_collected = 1 WHERE a_set = ?', (adventure_info[9],))
        c.execute('UPDATE bargains SET item_done = 1 WHERE item_name = ?', (adventure_info[9],))
        print("Executed update statement with a_name as ->", adventure_info[9])
    conn.commit()

    if adventure_info[0] == 156 or adventure_info[0] == 159 or adventure_info[0] == 157 or adventure_info[0] == 158:
        with closing(conn.cursor()) as c:
            c.execute('UPDATE fairyfountains SET fairy_found = 1 WHERE quest_id = ?', (adventure_info[0],))
            print("Executed fairy fountain update statement with quest_id as ->", adventure_info[0])
        conn.commit()

    print("IN UPDATE FUNCTION ->", adventure_info[0])
    return "success"

def update_weapons_table(weapon_name, region, damage, buff):
    with closing(conn.cursor()) as c:
        c.execute('SELECT * FROM Weapons WHERE weapon_name = ?', (weapon_name,))
        weapon_data = c.fetchone()

        if weapon_data:
            # If the weapon already exists, update regions, damage, buff, and weapon_num_found
            existing_regions = weapon_data[3].split(', ') if weapon_data[3] else []
            if region not in existing_regions:
                updated_regions = ', '.join(existing_regions + [region])
                c.execute('UPDATE Weapons SET weapon_regions = ? WHERE weapon_name = ?', (updated_regions, weapon_name))

            existing_damage = weapon_data[2].split(', ') if weapon_data[2] else []
            if damage not in existing_damage:
                updated_damage = ', '.join(existing_damage + [damage])
                c.execute('UPDATE Weapons SET weapon_damage = ? WHERE weapon_name = ?', (updated_damage, weapon_name))

            if buff:
                existing_buff = weapon_data[3].split(', ') if weapon_data[3] else []
                if buff not in existing_buff:
                    updated_buff = ', '.join(existing_buff + [buff])
                    c.execute('UPDATE Weapons SET weapon_buff = ? WHERE weapon_name = ?', (updated_buff, weapon_name))

            weapon_num_found = weapon_data[5]
            print("Weapon_num_found:", weapon_num_found)
            if weapon_num_found is None:
                weapon_num_found = 1
            else:
                weapon_num_found = int(weapon_num_found) + 1
            c.execute('UPDATE Weapons SET weapon_num_found = ? WHERE weapon_name = ?', (weapon_num_found, weapon_name))

        else:
            # If the weapon does not exist, add it to the Weapons table
            c.execute('INSERT INTO Weapons (weapon_name, weapon_regions, weapon_damage, weapon_buff, weapon_num_found) VALUES (?, ?, ?, ?, ?)', (weapon_name, region, damage, buff, 1))
    conn.commit()


def calculate_progress_percentage(completed_locks, total_locks):
    if total_locks == 0:
        return 0
    return (completed_locks / total_locks) * 100

# Helper function to fetch temple progress data from the database
def fetch_temple_progress():
    with closing(conn.cursor()) as c:
        c.execute("SELECT temple_id, temple_name, temple_lock, temple_boss, temple_complete FROM Temples")
        temples_data = c.fetchall()
        return temples_data

# Define a custom Jinja filter to format the key as desired
@app.template_filter('format_percentage_key')
def format_percentage_key(key):
    # Replace underscores with spaces
    formatted_key = key.replace("percentage_", "").capitalize()
    formatted_key = formatted_key.replace("_", " ")

    # Capitalize each word
    formatted_key = formatted_key.title()

    return formatted_key

@app.route("/")
def index():
    print("In Index")
    headline = "Current Percentage Completed"
    percentages = get_percentages()
    
    # Fetch the temple progress data from the database
    temples_data = fetch_temple_progress()
    finished_mains = []
    with closing(conn.cursor()) as c:
        completed_mains = c.execute("SELECT * FROM Quests WHERE quest_type = 'Main' AND quest_done = 2").fetchall()
        
        for main in completed_mains:
            finished_mains.append(main[3])
            print("main ->", main[3])

    # Calculate progress percentage for each temple and create a list of dictionaries with (temple_name, progress_percentage)
    progress_data = []
    for temple in temples_data:
        temple_id = temple[0]
        temple_name = temple[1]
        if temple_name == "Fire Temple" or temple_name == "Wind Temple":
            locks = temple[2]
        else:
            locks = temple[2]
        completed_locks = int(locks)
        if temple_name == "Fire Temple" or temple_name == "Wind Temple":
            total_locks = [1, 2, 3, 4, 5] 
        else:
            total_locks = [1, 2, 3, 4]
        temple_boss = temple[3]
        temple_complete = temple[4]
        progress_percentage = calculate_progress_percentage(completed_locks, (len(total_locks) + 1 ))
        progress_data.append({"temple_id": temple_id, "temple_name": temple_name, "progress_percentage": progress_percentage, "locks": locks, "completed_locks": completed_locks, "temple_boss": temple_boss, "temple_complete":temple_complete})


    return render_template("index.html", finished_mains=finished_mains, headline=headline, percentages=percentages, progress_data=progress_data, temples_data=temples_data)

@app.route('/update_lock_status', methods=['POST'])
def update_lock_status():
    print("UDPATE LOCK STATUS")
    try:
        # Get data from the request
        data = request.get_json()
        print("DATA ->", data)
        temple_id = data.get('temple_id')
        lock_index = data.get('lock_index')
        value = data.get('value')
        temple_boss = data.get('temple_boss')  # Get temple_boss value from frontend

        # Update the lock status and temple boss checkmark in the database
        with closing(conn.cursor()) as c:
            # Assuming your Temples table has the columns temple_id, temple_lock1, ..., temple_lock5, and temple_boss
            lock_column = f'temple_lock{lock_index}'
            print("Lock_index ->", lock_index)
            print("lock_column ->", lock_column)
            print("temple_boss ->", temple_boss)
            if lock_index != None:
                c.execute(f"UPDATE Temples SET temple_lock = ? WHERE temple_id = ?", (value, temple_id))
                print(f"Executed lock update. SET temple_lock = {value} WHERE temple_id = {temple_id}")
            else:
                c.execute(f"UPDATE Temples SET temple_boss = ? WHERE temple_id = ?", (temple_boss, temple_id))
                print("Executed boss update")
            conn.commit()

        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


@app.route("/locationnav")
def locationnav():
    print("LocationNav")

    headline = ""
    percentages = get_percentages()
    return render_template("locationnav.html", headline=headline, percentages=percentages)

@app.route("/questnav")
def questnav():
    print("LocationNav")

    headline = ""
    percentages = get_percentages()
    return render_template("questnav.html", headline=headline, percentages=percentages)

@app.route("/collectnav")
def collectnav():
    print("LocationNav")

    headline = ""
    percentages = get_percentages()
    return render_template("collectnav.html", headline=headline, percentages=percentages)

@app.route("/caves", methods=["GET", "POST"])
def caves():
    headline = "Caves"
    percentages = get_percentages()
    scroll_position = session.get('scrollPosition')
    if scroll_position is not None:
        scroll_position = int(scroll_position)
    
    armors = []
    with closing(conn.cursor()) as c:
        collected_armor = c.execute("SELECT a_name FROM armor WHERE a_collected = 1").fetchall()
        collected_asingle = c.execute("SELECT a_set FROM armor_single WHERE a_collected = 1").fetchall()
        for armor in collected_armor:
            armors.append(armor[0])
        for armor in collected_asingle:
            armors.append(armor[0])
        
        print("Armor ->", armors)
    
    regions = [
    "Great Sky Island",
    "Hyrule Field",
    "Tabantha",
    "Great Hyrule Forest",
    "North Hyrule Sky Archipelago",
    "Akkala",
    "Eldin",
    "Lanayru",
    "Necluda",
    "Faron",
    "Gerudo",
]

    if request.method == 'POST':
        with closing(conn.cursor()) as c:
            caves = c.execute('SELECT cave_name FROM caves ORDER BY cave_name ASC').fetchall()
            for cave in caves:
                cave_name = cave[0]
                cave_done = request.form.get(f'done_cave_{cave_name}')
                if cave_done is None:
                    print("cave_done is none:", cave_done)
                    cave_done = c.execute('SELECT cave_done FROM caves WHERE cave_name = ?', (cave_name,)).fetchone()[0]
                else:
                    print("cave_done is not none:", cave_done)
                print("cave_name:", cave_name)
                print("cave_done:", cave_done)
                c.execute('UPDATE caves SET cave_done = ? WHERE cave_name = ?', (cave_done, cave_name))
                print("Executed update statement for cave_name:", cave_name)
            conn.commit()

    with closing(conn.cursor()) as c:
        query = '''SELECT * FROM caves ORDER BY cave_name ASC'''
        c.execute(query)
        results = c.fetchall()
        selected_region = request.args.get('region')
        # Filter the results based on the selected region
        if selected_region:
            results = [result for result in results if result[4] == selected_region]   
    # Calculate the completion status for each region
    region_status = {}
    for region in regions:
        total_caves = len([result for result in results if result[3] == region])
        completed = len([result for result in results if result[3] == region and result[0] == 2])
        discovered = len([result for result in results if result[3] == region and result[0] == 1])
        unfound = len([result for result in results if result[3] == region and result[0] == 0])

        region_status[region] = {
            'completed': completed,
            'discovered': discovered,
            'unfound': unfound,
            'total_caves': total_caves
        }
    return render_template("caves.html", scroll_position=scroll_position, headline=headline, armors=armors, percentages=percentages, results=results, regions=regions, region_status=region_status, total_caves=total_caves)

@app.route('/update-cave', methods=['POST'])
def update_caves():
    cave_id = request.json.get('cave_id')
    cave_done = request.json.get('cave_done')

    if cave_done is None:
        cave_done = 0
    else:
        cave_done = cave_done

    # Update the dispenser in the database with the new found status
    try:
        with closing(conn.cursor()) as c:
            c.execute('UPDATE caves SET cave_done = ? WHERE cave_id = ?', (cave_done, cave_id))
            print("update_caves cave_done = ", cave_done, ", cave_id = ", cave_id)
            conn.commit()
        return jsonify(success=True)
    except Exception as e:
        print("Error:", e)  # Add this line for debugging
        return jsonify(success=False, error=str(e))

@app.route('/chests', methods=['GET', 'POST'])
def chests():
    headline = "Chests"
    percentages = get_percentages()
    scroll_position = session.get('scrollPosition')
    if scroll_position is not None:
        scroll_position = int(scroll_position) 

    if request.method == 'POST':
        with closing(conn.cursor()) as c:
            chests = c.execute('SELECT * FROM chests').fetchall()
            for chest in chests:
                chest_id = chest[0]
                chest_found = request.form.get(f'chest_found_{chest_id}')
                if chest_found is None:
                    chest_found = '0'
                else:
                    chest_found = '1'
                print("chest_id:", chest_id)
                print("chest_found:", chest_found)
                c.execute('UPDATE chests SET chest_done = ? WHERE chest_id = ?', (chest_found, chest_id))
                print("Executed update statement for chest ID:", chest_id)
            conn.commit()

    # Retrieve all chests from the database
    with closing(conn.cursor()) as c:
        c.execute('SELECT * FROM chests')
        chests = c.fetchall()
        print("result[6]:", chests[0][6])
        print("chest id:", chests[0][0])

    return render_template('chests.html', chests=chests, scroll_position=scroll_position, headline=headline, percentages=percentages)


@app.route("/add_chest", methods=["POST"])
def add_chest():
    try:
        chest_coord = request.form['chest_coord']
        # Remove spaces and commas from the input
        chest_coord = chest_coord.replace(' ', '').replace(',', '')

        # Format the chest_coord with commas while maintaining negative signs
        formatted_chest_coord = ''
        i = 0
        while i < len(chest_coord):
            section = chest_coord[i:i+4]
            if section.startswith('-'):
                section = chest_coord[i:i+5]
                formatted_chest_coord += section + ', '
                i += 5
            else:
                formatted_chest_coord += section[:4] + ', '
                i += 4
        formatted_chest_coord = formatted_chest_coord.rstrip(', ')
        
        chest_type = request.form['chest_type']
        chest_item = request.form['chest_item']

        # Find the opening and closing parentheses positions
        opening_parenthesis_pos = chest_item.find("(")
        closing_parenthesis_pos = chest_item.find(")")

        if opening_parenthesis_pos != -1 and closing_parenthesis_pos != -1:
            # Extract the weapon name and damage number
            weapon_name = chest_item[:opening_parenthesis_pos].strip()
            damage_and_buff = chest_item[opening_parenthesis_pos + 1:closing_parenthesis_pos].strip()

            # Find the position of the comma to separate damage number and buff
            comma_pos = damage_and_buff.find(",")
            if comma_pos != -1:
                damage_number = damage_and_buff[:comma_pos].strip()
                buff = damage_and_buff[comma_pos + 1:].strip()
            else:
                # If there is no comma, consider the whole part as damage number and no buff
                damage_number = damage_and_buff.strip()
                buff = "No Buff"

            print("Weapon Name:", weapon_name)
            print("Damage Number:", damage_number)
            
        else:
            print("Invalid chest item format.")

        chest_location = request.form['chest_location']
        chest_sideq = request.form['chest_sideq']
        if chest_sideq == None or chest_sideq == "":
            chest_sideq = "X"
        chest_region = request.form['chest_region']
        chest_done = request.form.get(f'chest_done')
        chest_map = request.form['chest_map']

        # update_weapons_table(weapon_name, chest_region, damage_number, buff)


        print("Chest_Done:", chest_done) 
        if chest_done == None:
            chest_done = "0"
        else:
            chest_done = "1"       

        with closing(conn.cursor()) as c:
            query = '''INSERT INTO chests (chest_coord, chest_type, chest_item, chest_location, chest_region, chest_sideq, chest_done, chest_map)
                        VALUES(?, ?, ?, ?, ?, ?, ?, ?)'''
            c.execute(query, (formatted_chest_coord, chest_type, chest_item, chest_location, chest_region, chest_sideq, chest_done, chest_map))
            conn.commit()
            query = '''SELECT * FROM chests ORDER BY chest_id DESC LIMIT 1'''
            c.execute(query)
            row = c.fetchone()

    except sqlite3.OperationalError as e:
        print(e)
        headline = "Error in insert operation. Please try again."
        return redirect('/chests')
    return redirect('/chests')

@app.route('/update_chests', methods=['POST'])
def update_chests():
    chest_id = request.json.get('chest_id')
    chest_done = request.json.get('chest_done')

    if chest_done is None:
        chest_done = 0
    else:
        chest_done = chest_done

    # Update the dispenser in the database with the new found status
    try:
        with closing(conn.cursor()) as c:
            c.execute('UPDATE chests SET chest_done = ? WHERE chest_id = ?', (chest_done, chest_id))
            print("update_chests chest_done = ", chest_done, ", chest_id = ", chest_id)
            conn.commit()
        return jsonify(success=True)
    except Exception as e:
        print("Error:", e)  # Add this line for debugging
        return jsonify(success=False, error=str(e))

@app.route('/misc', methods=['GET', 'POST'])
def misc():
    headline = "Miscellaneous"
    percentages = get_percentages()
    scroll_position = session.get('scrollPosition')
    if scroll_position is not None:
        scroll_position = int(scroll_position) 

    if request.method == 'POST':
        with closing(conn.cursor()) as c:
            miscs = c.execute('SELECT * FROM misc').fetchall()
            for misc in miscs:
                misc_id = misc[0]
                misc_found = request.form.get(f'misc_found_{misc_id}')
                if misc_found is None:
                    misc_found = '0'
                else:
                    misc_found = '1'
                print("misc_id:", misc_id)
                print("misc_found:", misc_found)
                c.execute('UPDATE misc SET misc_done = ? WHERE misc_id = ?', (misc_found, misc_id))
                print("Executed update statement for misc ID:", misc_id)
            conn.commit()

    # Retrieve all miscs from the database
    with closing(conn.cursor()) as c:
        things = []
        c.execute('SELECT * FROM misc')
        miscs = c.fetchall()
        # c.execute('SELECT * FROM food')
        # food = c.fetchall
        # things.extend(miscs)
        # things.extend(food)
        # print("Things:", things)

    return render_template('misc.html', miscs=miscs, scroll_position=scroll_position, headline=headline, percentages=percentages)


@app.route("/add_misc", methods=["POST"])
def add_misc():
    try:
        misc_coord = request.form['misc_coord']
        # Remove spaces and commas from the input
        misc_coord = misc_coord.replace(' ', '').replace(',', '')

        # Format the misc_coord with commas while maintaining negative signs
        formatted_misc_coord = ''
        i = 0
        while i < len(misc_coord):
            section = misc_coord[i:i+4]
            if section.startswith('-'):
                section = misc_coord[i:i+5]
                formatted_misc_coord += section + ', '
                i += 5
            else:
                formatted_misc_coord += section[:4] + ', '
                i += 4
        formatted_misc_coord = formatted_misc_coord.rstrip(', ')
        
        misc_type = request.form['misc_type']
        misc_item = request.form['misc_item']
        misc_secondary = request.form['misc_secondary']
        misc_location = request.form['misc_location']
        misc_region = request.form['misc_region']
        misc_done = request.form.get(f'misc_done')
        misc_map = request.form['misc_map']

        print("misc_Done:", misc_done) 
        if misc_done == None:
            misc_done = "0"
        else:
            misc_done = "1"

        if misc_type == "Weapon":
            # Find the opening and closing parentheses positions
            opening_parenthesis_pos = misc_item.find("(")
            closing_parenthesis_pos = misc_item.find(")")

            if opening_parenthesis_pos != -1 and closing_parenthesis_pos != -1:
                # Extract the weapon name and damage number
                weapon_name = misc_item[:opening_parenthesis_pos].strip()
                damage_and_buff = misc_item[opening_parenthesis_pos + 1:closing_parenthesis_pos].strip()

                # Find the position of the comma to separate damage number and buff
                comma_pos = damage_and_buff.find(",")
                if comma_pos != -1:
                    damage_number = damage_and_buff[:comma_pos].strip()
                    buff = damage_and_buff[comma_pos + 1:].strip()
                else:
                    # If there is no comma, consider the whole part as damage number and no buff
                    damage_number = damage_and_buff.strip()
                    buff = "No Buff"

                print("Weapon Name:", weapon_name)
                print("Damage Number:", damage_number)
                print("Misc_region:", misc_region)
                print("Buff:", buff)
                update_weapons_table(weapon_name, misc_region, damage_number, buff)

            else:
                print("Invalid misc item format.")     

        with closing(conn.cursor()) as c:
            if misc_type == "Cherry Blossom Trees":
                query = '''INSERT INTO cherry_blossom_trees (cherry_coord, cherry_location, cherry_region, cherry_found)
                        VALUES(?, ?, ?, ?)'''
                c.execute(query, (formatted_misc_coord, misc_location, misc_region, misc_done))                

            if misc_type == "Monster":
                query = '''INSERT INTO enemies (e_coord, e_monster, e_color, e_location,e_region, e_found, e_map)
                        VALUES(?, ?, ?, ?, ?, ?, ?)'''
                c.execute(query, (formatted_misc_coord, misc_item, misc_secondary, misc_location, misc_region, misc_done, misc_map))
                                    
            if misc_type == "Hearty":
                query = '''INSERT INTO food (food_category, food_item, food_tier, food_coord, food_location, food_region, food_found, food_map)
                        VALUES(?, ?, ?, ?, ?, ?, ?, ?)'''
                print("inserted into food")
                c.execute(query, (misc_type, misc_item, misc_secondary, formatted_misc_coord, misc_location, misc_region, misc_done, misc_map))

            if misc_type == "Endura":
                query = '''INSERT INTO food (food_category, food_item, food_tier, food_coord, food_location, food_region, food_found, food_map)
                        VALUES(?, ?, ?, ?, ?, ?, ?, ?)'''
                print("inserted into food")
                c.execute(query, (misc_type, misc_item, misc_secondary, formatted_misc_coord, misc_location, misc_region, misc_done, misc_map))
                                  
            if misc_type == "Zonai":
                query = '''INSERT INTO misc (misc_type, misc_item, misc_coord, misc_location, misc_region, misc_secondary, misc_done, misc_map)
                        VALUES(?, ?, ?, ?, ?, ?, ?, ?)'''
                c.execute(query, (misc_type, misc_item, formatted_misc_coord, misc_location, misc_region, misc_secondary, misc_done, misc_map))
            if misc_type == "Schema":
                query = '''INSERT INTO schemas (schema_type, schema_name, schema_coord, schema_location, schema_region, schema_parts, schema_done)
                        VALUES(?, ?, ?, ?, ?, ?, ?)'''
                c.execute(query, (misc_type, misc_item, formatted_misc_coord, misc_location, misc_region, misc_secondary, misc_done))
            if misc_type == "Flower-Shaped Island":
                query = '''INSERT INTO misc (misc_type, misc_item, misc_coord, misc_location, misc_region, misc_secondary, misc_done, misc_map)
                        VALUES(?, ?, ?, ?, ?, ?, ?, ?)'''
                c.execute(query, (misc_type, misc_item, formatted_misc_coord, misc_location, misc_region, misc_secondary, misc_done, misc_map))
            if misc_type == "Other":
                query = '''INSERT INTO misc (misc_type, misc_item, misc_coord, misc_location, misc_region, misc_secondary, misc_done, misc_map)
                        VALUES(?, ?, ?, ?, ?, ?, ?, ?)'''
                c.execute(query, (misc_type, misc_item, formatted_misc_coord, misc_location, misc_region, misc_secondary, misc_done, misc_map))
            conn.commit()
            query = '''SELECT * FROM misc ORDER BY misc_id DESC LIMIT 1'''
            c.execute(query)
            row = c.fetchone()

    except sqlite3.OperationalError as e:
        print(e)
        headline = "Error in insert operation. Please try again."
        return redirect('/misc')
    return redirect('/misc')

@app.route('/camp_chest', methods=['GET', 'POST'])
def camp_chest():
    headline = "Camp Chests"
    percentages = get_percentages()
    scroll_position = session.get('scrollPosition')
    if scroll_position is not None:
        scroll_position = int(scroll_position) 

    if request.method == 'POST':
        with closing(conn.cursor()) as c:
            camp_chest = c.execute('SELECT * FROM camp_chest').fetchall()
            for camp_chest in camp_chest:
                camp_chest_id = camp_chest[0]
                camp_chest_found = request.form.get(f'camp_chest_found_{camp_chest_id}')
                if camp_chest_found is None:
                    camp_chest_found = '0'
                else:
                    camp_chest_found = '1'
                print("camp_chest_id:", camp_chest_id)
                print("camp_chest_found:", camp_chest_found)
                c.execute('UPDATE camp_chest SET camp_chest_done = ? WHERE camp_chest_id = ?', (camp_chest_found, camp_chest_id))
                print("Executed update statement for camp_chest ID:", camp_chest_id)
            conn.commit()
            with closing(conn.cursor()) as c:
                c.execute('SELECT * FROM camp_chest')
                camp_chests = c.fetchall()
                return render_template('camp_chest.html', headline=headline, percentages=percentages, camp_chests=camp_chests, scroll_position=scroll_position)
    else:
        # Retrieve all camp_chest from the database
        with closing(conn.cursor()) as c:
            c.execute('SELECT * FROM camp_chest')
            camp_chests = c.fetchall()

    return render_template('camp_chest.html',headline=headline, percentages=percentages,  camp_chests=camp_chests, scroll_position=scroll_position)


@app.route("/add_camp_chest", methods=["POST"])
def add_camp_chest():
    try:
        camp_chest_coord = request.form['camp_chest_coord']
        # Remove spaces and commas from the input
        camp_chest_coord = camp_chest_coord.replace(' ', '').replace(',', '')

        # Format the camp_chest_coord with commas while maintaining negative signs
        formatted_camp_chest_coord = ''
        i = 0
        while i < len(camp_chest_coord):
            section = camp_chest_coord[i:i+4]
            if section.startswith('-'):
                section = camp_chest_coord[i:i+5]
                formatted_camp_chest_coord += section + ', '
                i += 5
            else:
                formatted_camp_chest_coord += section[:4] + ', '
                i += 4
        formatted_camp_chest_coord = formatted_camp_chest_coord.rstrip(', ')
        
        camp_chest_enemies = request.form['camp_chest_enemies']
        camp_chest_item = request.form['camp_chest_item']
        camp_chest_location = request.form['camp_chest_location']
        camp_chest_region = request.form['camp_chest_region']
        camp_chest_found = request.form.get(f'camp_chest_found')
        print("Camp_chest_found:", camp_chest_found)
        if camp_chest_found is None:
                camp_chest_found = '0'
        else:
            camp_chest_found = '1'
        print("Camp_chest_found 2:", camp_chest_found)
        with closing(conn.cursor()) as c:
            query = '''INSERT INTO camp_chest (camp_chest_coord, camp_chest_enemies, camp_chest_item, camp_chest_location, camp_chest_region, camp_chest_done)
                        VALUES(?, ?, ?, ?, ?, ?)'''
            c.execute(query, (formatted_camp_chest_coord, camp_chest_enemies, camp_chest_item, camp_chest_location, camp_chest_region, camp_chest_found))
            conn.commit()
            return redirect('/camp_chest')

    except sqlite3.OperationalError as e:
        print(e)
        headline = "Error in insert operation. Please try again."
    return redirect('/camp_chest')


@app.route("/edititem", methods=["POST", "GET"])
def edititem():
    headline = "Edit a chest:"
    percentages = get_percentages()
    if request.method == 'POST':
        # uploaded_file = request.files["item_picture"]
        # filename = secure_filename(uploaded_file.filename)
        # if filename != '':
        #     file_ext = os.path.splitext(filename)[1]
        #     if file_ext not in app.config['UPLOAD_EXTENSIONS']:
        #         abort(400)
        #     uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        try:
            obj_name = request.form['obj_name']
            with closing(conn.cursor()) as c:
                query = '''INSERT INTO Collection (obj_name)
                            VALUES(?)'''
                c.execute(query, (obj_name))
                conn.commit()
                tagline = "Successfully added Item to Collection"
                return render_template("success.html", tagline=tagline)
        except sqlite3.OperationalError as e:
            print(e)
            headline = "Error in insert operation. Please try again."
    else:
        return render_template("edititem.html", headline=headline, percentages=percentages)

@app.route('/armors', methods=['GET', 'POST'])
def armors():
    headline = "Armors"
    percentages = get_percentages()
    scroll_position = session.get('scrollPosition')
    scroll_position = session.get('scrollPosition')
    if scroll_position is not None:
        scroll_position = int(scroll_position)
    
    if request.method == 'POST':
        armorid = int(request.form['armor_id'])
        armor_id = request.form[f'armor_id_{armorid}']
        armor_found = request.form.get(f'armor_id_{armor_id}')
        with closing(conn.cursor()) as c:
            c.execute('UPDATE armor SET a_collected = ? WHERE a_id = ?', (armor_found, armor_id))
        conn.commit()
    
    # Retrieve all armors from the database
    with closing(conn.cursor()) as c:
        c.execute('SELECT * FROM armor ORDER BY a_set ASC')
        armors = c.fetchall()
        # Initialize a list to store armor set lists
        armor_sets = []
        # Create lists for each armor set
        for row in armors:
            a_id, a_set, a_name, a_piece, a_collected, a_upgrade1, a_items1, a_upgrade2, a_items2, \
            a_upgrade3, a_items3, a_upgrade4, a_items4, a_totalitems = row

            # Find or create the list for the current armor set
            armor_set = next((set_list for set_list in armor_sets if set_list[0][0] == a_set), None)
            if armor_set is None:
                armor_set = [[a_set]]
                armor_sets.append(armor_set)

            # Add collected status and other columns to the appropriate piece in the list
            armor_piece = [a_id, a_piece, a_collected,a_upgrade1, a_items1, a_upgrade2, a_items2, a_upgrade3, a_items3, a_upgrade4, a_items4, a_totalitems]
            armor_set.append(armor_piece)
        
    with closing(conn.cursor()) as c:
            c.execute('SELECT * FROM fairyfountains ORDER BY fairy_id')
            fairies = c.fetchall()

    return render_template('armors.html', headline=headline, percentages=percentages, fairies=fairies, armor_sets=armor_sets, scroll_position=scroll_position)

@app.route('/update_armor', methods=['POST'])
def update_armor():
    armor_id = request.json.get('armor_id')
    armor_done = request.json.get('armor_done')
    with closing(conn.cursor()) as c:
        c.execute('UPDATE armor SET a_collected = ? WHERE a_id = ?', (armor_done, armor_id))
        print("Updated armor collection for ->", armor_id)
        conn.commit()
        
        return jsonify(success=True)
    
    
@app.route('/update_armor_1', methods=['POST'])
def update_armor_1():
    armor_id = request.json.get('armor_id')
    armor_done = request.json.get('armor_done')
    if armor_id != 97 or armor_id != 98 or armor_id != 99:
        with closing(conn.cursor()) as c:
            c.execute('UPDATE armor SET a_upgraded1 = ? WHERE a_id = ?', (armor_done, armor_id))
            print("Updated armor upgrade 1 for ->", armor_id)
            conn.commit()
            
        return jsonify(success=True)
   
    
@app.route('/update_armor_2', methods=['POST'])
def update_armor_2():
    armor_id = request.json.get('armor_id')
    armor_done = request.json.get('armor_done')
    if armor_id != 97 or armor_id != 98 or armor_id != 99:
        with closing(conn.cursor()) as c:
            c.execute('UPDATE armor SET a_upgraded2 = ? WHERE a_id = ?', (armor_done, armor_id))
            print("Updated armor upgrade 2 for ->", armor_id)
            conn.commit()
        
        return jsonify(success=True)

    
@app.route('/update_armor_3', methods=['POST'])
def update_armor_3():
    armor_id = request.json.get('armor_id')
    armor_done = request.json.get('armor_done')
    if armor_id != 97 or armor_id != 98 or armor_id != 99:
        with closing(conn.cursor()) as c:
            c.execute('UPDATE armor SET a_upgraded3 = ? WHERE a_id = ?', (armor_done, armor_id))
            print("Updated armor upgrade 3 for ->", armor_id)
            conn.commit()
        
        return jsonify(success=True)
   
@app.route('/update_armor_4', methods=['POST'])
def update_armor_4():
    armor_id = request.json.get('armor_id')
    armor_done = request.json.get('armor_done')
    if armor_id != 97 or armor_id != 98 or armor_id != 99:
        with closing(conn.cursor()) as c:
            c.execute('UPDATE armor SET a_upgraded4 = ? WHERE a_id = ?', (armor_done, armor_id))
            print("Updated armor upgrade 4 for ->", armor_id)
            conn.commit()
        
        return jsonify(success=True)
    
@app.route('/update_greatfairies/<int:fairyId>/<int:fairyFound>', methods=['POST'])
def update_greatfairies(fairyId, fairyFound):
    try:
        
        # with closing(conn.cursor()) as c:
        #     c.execute('SELECT * FROM fairyfountains ORDER BY fairy_id')
        #     fairies = c.fetchall()

        #     for fairy in fairies:
        #         fairy_id = fairy[0]
        #         fairy_name = fairy[2]
        #         fairy_done = request.form.get(f"fairy_{fairy[1]}")
        #         if fairy_done == None:
        #             fairy_done = 0
        #         else:
        #             fairy_done = 1
        
        with closing(conn.cursor()) as c:
            c.execute('UPDATE fairyfountains SET fairy_found = ? WHERE fairy_id = ?', (fairyFound, fairyId))
            conn.commit()
            print("Fairy Found ->", fairyFound)
            print("Fairy ID ->", fairyId)

            return jsonify(success=True)
    except Exception as e:
        return jsonify(success=False, error=str(e))


@app.route("/shrines", methods=["GET", "POST"])
def shrines():
    headline = "Shrines"
    percentages = get_percentages()
    scroll_position = session.get('scrollPosition')
    if scroll_position is not None:
        scroll_position = int(scroll_position)

    regions = [
    "Great Sky Island",
    "Hyrule Field",
    "Tabantha",
    "Great Hyrule Forest",
    "North Hyrule Sky Archipelago",
    "Akkala",
    "Eldin",
    "Lanayru",
    "Necluda",
    "Faron",
    "Gerudo",
]

    if request.method == 'POST':
        with closing(conn.cursor()) as c:
            shrine_shrines = c.execute('SELECT shrine_shrine FROM shrines').fetchall()
            for shrine_shrine in shrine_shrines:
                shrine_shrine = shrine_shrine[0]
                shrine_done = request.form.get(f'done_shrine_{shrine_shrine}')
                if shrine_done is None:
                    shrine_done = c.execute('SELECT shrine_done FROM shrines WHERE shrine_shrine = ?', (shrine_shrine,)).fetchone()[0]
                else:
                    print("shrine_done is not none:", shrine_done)
                c.execute('UPDATE shrines SET shrine_done = ? WHERE shrine_shrine = ?', (shrine_done, shrine_shrine))
            conn.commit()

    with closing(conn.cursor()) as c:
        query = '''SELECT * FROM shrines ORDER BY shrine_shrine ASC'''
        c.execute(query)
        selected_region = request.args.get('region')
        results = c.fetchall()
        # Filter the results based on the selected region
        if selected_region:
            results = [result for result in results if result[4] == selected_region]   
        info = [(result[0], result[1], result[2]) for result in results]
    # Calculate the completion status for each region
    region_status = {}
    for region in regions:
        total_shrines = len([result for result in results if result[4] == region])
        completed = len([result for result in results if result[4] == region and result[0] == 2])
        tapped = len([result for result in results if result[4] == region and result[0] == 1])
        unfound = len([result for result in results if result[4] == region and result[0] == 0])

        region_status[region] = {
            'completed': completed,
            'tapped': tapped,
            'unfound': unfound,
            'total_shrines': total_shrines
        }

    return render_template("shrines.html", scroll_position=scroll_position, headline=headline, percentages=percentages, info=info, results=results, regions=regions, region_status=region_status)

@app.route('/update-shrines', methods=['POST'])
def update_shrines():
    shrine_id = request.json.get('shrine_id')
    shrine_done = request.json.get('shrine_done')

    if shrine_done is None:
        shrine_done = 0
    else:
        shrine_done = shrine_done

    # Update the shrine in the database with the new found status
    try:
        with closing(conn.cursor()) as c:
            c.execute('UPDATE shrines SET shrine_done = ? WHERE shrine_id = ?', (shrine_done, shrine_id))
            print("update_shrines shrine_done = ", shrine_done, ", shrine_id = ", shrine_id)
            conn.commit()
        return jsonify(success=True)
    except Exception as e:
        print("Error:", e)  # Add this line for debugging
        return jsonify(success=False, error=str(e))

@app.route('/koroks', methods=['GET', 'POST'])
def koroks():
    headline = "Koroks"
    percentages = get_percentages()
    scroll_position = session.get('scrollPosition')
    if scroll_position is not None:
        scroll_position = int(scroll_position) 
    with closing(conn.cursor()) as c:
        c.execute("SELECT COUNT(*) FROM allkoroks WHERE korok_done = 1")
        completed_koroks = c.fetchone()[0]
    
    if request.method == 'POST':
        with closing(conn.cursor()) as c:
            koroks = c.execute('SELECT * FROM allkoroks').fetchall()
            for korok in koroks:
                korok_id = korok[0]
                korok_done = request.form.get(f'korok_done_{korok_id}')
                print("Korok_done:", korok_done)
                if korok_done is None:
                    korok_done = '0'
                else:
                    korok_done = '1'
                print("korok_id:", korok_id)
                print("korok_done:", korok_done)
                c.execute('UPDATE allkoroks SET korok_done = ? WHERE korok_id = ?', (korok_done, korok_id))
                print("Executed update statement for korok ID:", korok_id)
            conn.commit()

    # Retrieve all koroks from the database
    with closing(conn.cursor()) as c:
        c.execute('SELECT * FROM allkoroks')
        koroks = c.fetchall()
    return render_template('koroks.html', headline=headline, percentages=percentages, completed_koroks=completed_koroks, koroks=koroks, scroll_position=scroll_position)

@app.route('/update-korok', methods=['POST'])
def update_korok():
    korok_id = request.json.get('korok_id')
    korok_done = request.json.get('korok_done')

    if korok_done is None:
        korok_done = 0
    else:
        korok_done = korok_done

    # Update the korok in the database with the new found status
    try:
        with closing(conn.cursor()) as c:
            c.execute('UPDATE allkoroks SET korok_done = ? WHERE korok_id = ?', (korok_done, korok_id))
            print("update koroks korok_done = ", korok_done, ", korok_id = ", korok_id)
            conn.commit()
        return jsonify(success=True)
    except Exception as e:
        print("Error:", e)  # Add this line for debugging
        return jsonify(success=False, error=str(e))

@app.route('/add_korok', methods=['POST'])
def add_korok():
    location = request.form.get('location')
    kType = request.form.get('kType')
    korok_coord = request.form.get('korok_coord')
    # Remove spaces and commas from the input
    korok_coord = korok_coord.replace(' ', '').replace(',', '')

    # Format the chest_coord with commas while maintaining negative signs
    formatted_korok_coord = ''
    i = 0
    while i < len(korok_coord):
        section = korok_coord[i:i+4]
        if section.startswith('-'):
            section = korok_coord[i:i+5]
            formatted_korok_coord += section + ', '
            i += 5
        else:
            formatted_korok_coord += section[:4] + ', '
            i += 4
    formatted_korok_coord = formatted_korok_coord.rstrip(', ')
    coord_end = request.form.get('coord_end')
    # Remove spaces and commas from the input
    coord_end = coord_end.replace(' ', '').replace(',', '')

    # Format the chest_coord with commas while maintaining negative signs
    formatted_coord_end = ''
    i = 0
    while i < len(coord_end):
        section = coord_end[i:i+4]
        if section.startswith('-'):
            section = coord_end[i:i+5]
            formatted_coord_end+= section + ', '
            i += 5
        else:
            formatted_coord_end += section[:4] + ', '
            i += 4
    formatted_coord_end = formatted_coord_end.rstrip(', ')
    description = request.form.get('description')
    korok_done = request.form.get('korok_done')

    # Insert the new korok into the database
    with closing(conn.cursor()) as c:
        c.execute('INSERT INTO allkoroks (korok_done, korok_type, korok_coord) VALUES (?, ?, ?)',
                  (korok_done, kType, formatted_korok_coord))
        conn.commit()

    # Redirect back to the koroks page after adding the korok
    return redirect('/koroks')

@app.route('/ponypoints', methods=['GET', 'POST'])
def ponypoints():
    headline = "Pony Points"
    percentages = get_percentages()
    scroll_position = session.get('scrollPosition')
    if scroll_position is not None:
        scroll_position = int(scroll_position) 

    if request.method == 'POST':
        with closing(conn.cursor()) as c:
            points = c.execute('SELECT * FROM ponypoints').fetchall()
            for point in points:
                points_id = point[0]
                points_done = request.form.get(f'points_done_{points_id}')
                points_reward = point[4]
                print("points_done:", points_done)
                print("Points_reward:", points_reward)
                if points_done is None:
                    points_done = '0'
                else:
                    points_done = '1'
                print("points_id:", points_id)
                print("points_done:", points_done)
                c.execute('UPDATE ponypoints SET points_done = ? WHERE points_id = ?', (points_done, points_id))
                print("Executed update statement for point ID:", points_id)
            conn.commit()

    # Retrieve all points from the database
    with closing(conn.cursor()) as c:
        c.execute('SELECT * FROM ponypoints')
        points = c.fetchall()
        print("points:", points)

    return render_template('ponypoints.html', headline=headline, percentages=percentages, points=points, scroll_position=scroll_position)

@app.route('/update-point', methods=['POST'])
def update_point():
    points_id = request.json.get('point_id')
    points_done = request.json.get('point_done')
    with closing(conn.cursor()) as c:
        points_reward = c.execute('SELECT points_rewards FROM ponypoints WHERE points_id = ?', (points_id,)).fetchone()[0]
    print("Data received from client:", points_id, points_done, points_reward)  # Add this line for debugging

    if points_done is None:
        points_done = 0
    else:
        points_done = points_done

    print("points_done after if/else:", points_done)

    # Update the point in the database with the new found status
    try:
        with closing(conn.cursor()) as c:
            c.execute('UPDATE ponypoints SET points_done = ? WHERE points_id = ?', (points_done, points_id))
            print("update ponypoints points_done = ", points_done, ", points_id = ", points_id, " and points rewards:", points_reward)
            conn.commit()
        return jsonify(success=True)
    except Exception as e:
        print("Error:", e)  # Add this line for debugging
        return jsonify(success=False, error=str(e))

@app.route('/bargainer', methods=['GET', 'POST'])
def bargainer():
    headline = "Bargainer Statues"
    percentages = get_percentages()
    scroll_position = session.get('scrollPosition')
    if scroll_position is not None:
        scroll_position = int(scroll_position) 

    if request.method == 'POST':
        with closing(conn.cursor()) as c:
            bargain_locations = c.execute("SELECT * FROM locations WHERE location_type = 'Bargainer Statue'").fetchall()
            for bargain_location in bargain_locations:
                item_id = bargain_location[0]
                item_done = request.form.get(f'item_done_{item_id}')
                print("item_done:", item_done)
                if item_done is None:
                    item_done = '0'
                else:
                    item_done = '1'
                print("item_id:", item_id)
                print("item_done:", item_done)
                c.execute('UPDATE locations SET location_done = ? WHERE item_id = ?', (item_done, item_id))
                print("Executed update statement for bargain ID:", item_id)
            conn.commit()

    with closing(conn.cursor()) as c:
        c.execute("SELECT COUNT(*) FROM locations WHERE location_done = 1 AND location_type = 'Bargainer Statue'")
        completed_bargains = c.fetchone()[0]

    # Retrieve all bargains from the database
    with closing(conn.cursor()) as c:
        c.execute('SELECT * FROM bargains WHERE item_done = 1')
        bargains = c.fetchall()
        print("bargains:", bargains)

    # Retrieve all bargains from the database
    with closing(conn.cursor()) as c:
        c.execute("SELECT * FROM locations WHERE location_type = 'Bargainer Statue'")
        bargainer_statues = c.fetchall()
        print("bargains:", bargainer_statues)

    return render_template('bargainer.html', headline=headline, percentages=percentages, bargainer_statues=bargainer_statues, completed_bargains=completed_bargains, bargains=bargains, scroll_position=scroll_position)

@app.route('/update_bargain', methods=['POST'])
def update_bargain():
    bargain_id = request.json.get('bargain_id')
    bargain_done = request.json.get('bargain_done')

    if bargain_done is None:
        bargain_done = 0
    else:
        bargain_done = bargain_done

    # Update the bargainer statue in the database with the new found status
    try:
        with closing(conn.cursor()) as c:
            c.execute('UPDATE locations SET location_done = ? WHERE location_id = ?', (bargain_done, bargain_id))
            print("update_bargain bargain_done = ", bargain_done, ", bargain_id = ", bargain_id)
            conn.commit()
        return jsonify(success=True)
    except Exception as e:
        print("Error:", e)  # Add this line for debugging
        return jsonify(success=False, error=str(e))

@app.route('/enemies', methods=['GET', 'POST'])
def enemies():
    headline = "Enemies"
    percentages = get_percentages()
    scroll_position = session.get('scrollPosition')
    if scroll_position is not None:
        scroll_position = int(scroll_position) 

    if request.method == 'POST':
        with closing(conn.cursor()) as c:
            enemies = c.execute('SELECT * FROM enemies').fetchall()
            for enemy in enemies:
                e_id = enemy[0]
                e_found = request.form.get(f'e_found_{e_id}')
                if e_found is None:
                    e_found = '0'
                else:
                    e_found = '1'
                print("e_id:", e_id)
                print("e_found:", e_found)
                c.execute('UPDATE enemies SET e_found = ? WHERE e_id = ?', (e_found, e_id))
                print("Executed update statement for enemy ID:", e_id)
            conn.commit()

    # Retrieve all enemies from the database
    with closing(conn.cursor()) as c:
        c.execute('SELECT * FROM enemies')
        enemies = c.fetchall()
        print("result[6]:", enemies[0][6])
        print("enemy id:", enemies[0][0])

    return render_template('enemies.html', headline=headline, percentages=percentages, enemies=enemies, scroll_position=scroll_position)

@app.route('/update-enemy', methods=['POST'])
def update_enemy():
    e_id = request.json.get('enemyId')
    e_found = request.json.get('enemyFound')

    # Update the enemy in the database with the new found status
    with closing(conn.cursor()) as c:
        c.execute('UPDATE enemies SET e_found = ? WHERE e_id = ?', (e_found, e_id))
        conn.commit()

    return jsonify(success=True)

@app.route('/add_enemy', methods=['POST'])
def add_enemy():
    e_monster = request.form.get('e_monster')
    e_color = request.form.get('e_color')
    e_coord = request.form.get('e_coord')
    # Remove spaces and commas from the input
    e_coord = e_coord.replace(' ', '').replace(',', '')

    # Format the chest_coord with commas while maintaining negative signs
    formatted_e_coord = ''
    i = 0
    while i < len(e_coord):
        section = e_coord[i:i+4]
        if section.startswith('-'):
            section = e_coord[i:i+5]
            formatted_e_coord += section + ', '
            i += 5
        else:
            formatted_e_coord += section[:4] + ', '
            i += 4
    formatted_e_coord = formatted_e_coord.rstrip(', ')
    e_location = request.form.get('e_location')
    e_region = request.form.get('e_region')
    e_map = request.form.get('e_map')
    e_found = request.form.get('e_found')

    # Insert the new enemy into the database
    with closing(conn.cursor()) as c:
        c.execute('INSERT INTO enemies (e_found, e_monster, e_color, e_coord, e_location, e_region, e_map) VALUES (?, ?, ?, ?, ?, ?, ?)',
                  (e_found, e_monster, e_color, formatted_e_coord, e_location, e_region, e_map))
        conn.commit()

    # Redirect back to the enemies page after adding the enemy
    return redirect('/enemies')

@app.route("/lightroots", methods=["GET", "POST"])
def lightroots():
    headline = "Lightroots"
    percentages = get_percentages()
    scroll_position = session.get('scrollPosition')
    if scroll_position is not None:
        scroll_position = int(scroll_position)

    with closing(conn.cursor()) as c:
        c.execute("SELECT COUNT(*) FROM lightroots WHERE root_done = 1")
        completed_lightroots = c.fetchone()[0]

    if request.method == 'POST':
        with closing(conn.cursor()) as c:
            roots = c.execute('SELECT * FROM lightroots ORDER BY root_name ASC').fetchall()
            for root in roots:
                root_id = root[0]
                root_done = request.form.get(f'done_root_{root_id}')
                if root_done is None:
                    print("root_done is none:", root_done)
                    root_done = c.execute('SELECT root_done FROM lightroots WHERE root_id = ?', (root_id,)).fetchone()[0]
                else:
                    print("root_done is not none:", root_done)
                print("root_name:", root_id)
                print("root_done:", root_done)
                c.execute('UPDATE lightroots SET root_done = ? WHERE root_id = ?', (root_done, root_id))
                print("Executed update statement for root_name:", root_id)
            conn.commit()

    with closing(conn.cursor()) as c:
        query = '''SELECT * FROM lightroots ORDER BY root_name ASC'''
        c.execute(query)
        results = c.fetchall()
        info = [(result[0], result[1], result[2]) for result in results]
    return render_template("lightroots.html", scroll_position=scroll_position, headline=headline, completed_lightroots=completed_lightroots, percentages=percentages, info=info, results=results)

@app.route('/update_lightroots', methods=['POST'])
def update_lightroots():
    lightroot_id = request.json.get('lightroot_id')
    lightroot_done = request.json.get('lightroot_done')

    if lightroot_done is None:
        lightroot_done = 0
    else:
        lightroot_done = lightroot_done

    # Update the location in the database with the new found status
    try:
        with closing(conn.cursor()) as c:
            c.execute('UPDATE lightroots SET root_done = ? WHERE root_id = ?', (lightroot_done, lightroot_id))
            print("update lightroots root_done = ", lightroot_done, ", root_id = ", lightroot_id)
            conn.commit()
        return jsonify(success=True)
    except Exception as e:
        print("Error:", e)  # Add this line for debugging
        return jsonify(success=False, error=str(e))

@app.route("/compendium", methods=["GET", "POST"])
def compendium():
    headline = "Compendium"
    percentages = get_percentages()
    scroll_position = session.get('scrollPosition')
    if scroll_position is not None:
        scroll_position = int(scroll_position)

    if request.method == 'POST':
        with closing(conn.cursor()) as c:
            comps = c.execute('SELECT * FROM compendium ORDER BY comp_id ASC').fetchall()
            for comp in comps:
                comp_id = comp[0]
                comp_done = request.form.get(f'done_comp_{comp_id}')
                if comp_done is None:
                    comp_done = 0
                else:
                    comp_done = 1
                c.execute('UPDATE compendium SET comp_done = ? WHERE comp_id = ?', (comp_done, comp_id))
            conn.commit()
    
    with closing(conn.cursor()) as c:
        query = '''SELECT * FROM compendium ORDER BY comp_id ASC'''
        c.execute(query)
        results = c.fetchall()
        creatures = []
        monsters = []
        materials = []
        equipment = []
        treasures = []
        for result in results:
            if result[2] == "Creatures":
                creatures.append(result)
            if result[2] == "Monsters":
                monsters.append(result)
            if result[2] == "Materials":
                materials.append(result)
            if result[2] == "Equipment":
                equipment.append(result)
            if result[2] == "Treasure":
                treasures.append(result)

        # Redirect to the compendium page if there are no search results
        return render_template("compendium.html", scroll_position=scroll_position, headline=headline, percentages=percentages, results=results, creatures=creatures, monsters=monsters, materials=materials, equipment=equipment, treasures=treasures)

@app.route('/update-comp', methods=['POST'])
def update_compendium():
    comp_id = request.json.get('comp_id')
    comp_done = request.json.get('comp_done')

    if comp_done is None:
        comp_done = 0
    else:
        comp_done = comp_done

    # Update the dispenser in the database with the new found status
    try:
        with closing(conn.cursor()) as c:
            c.execute('UPDATE compendium SET comp_done = ? WHERE comp_id = ?', (comp_done, comp_id))
            print("update_compendium comp_done = ", comp_done, ", comp_id = ", comp_id)
            conn.commit()
        return jsonify(success=True)
    except Exception as e:
        print("Error:", e)  # Add this line for debugging
        return jsonify(success=False, error=str(e))

@app.route('/interesting', methods=['GET', 'POST'])
def interesting():
    headline = "Interesting Finds"
    percentages = get_percentages()
    scroll_position = session.get('scrollPosition')
    if scroll_position is not None:
        scroll_position = int(scroll_position) 

    if request.method == 'POST':
        with closing(conn.cursor()) as c:
            interesting = c.execute('SELECT * FROM misc').fetchall()
            for thing in interesting:
                misc_id = thing[0]
                misc_found = request.form.get(f'misc_found_{misc_id}')
                if misc_found is None:
                    misc_found = '0'
                else:
                    misc_found = '1'
                print("misc_id:", misc_id)
                print("misc_found:", misc_found)
                c.execute('UPDATE misc SET misc_found = ? WHERE misc_id = ?', (misc_found, misc_id))
                print("Executed update statement for thing ID:", misc_id)
            conn.commit()

    # Retrieve all interesting from the database
    with closing(conn.cursor()) as c:
        c.execute('SELECT * FROM misc')
        interesting = c.fetchall()

    return render_template('interesting.html', headline=headline, percentages=percentages, interesting=interesting, scroll_position=scroll_position)

@app.route('/update-thing', methods=['POST'])
def update_thing():
    misc_id = request.json.get('thingId')
    misc_found = request.json.get('thingFound')

    # Update the thing in the database with the new found status
    with closing(conn.cursor()) as c:
        c.execute('UPDATE misc SET misc_found = ? WHERE misc_id = ?', (misc_found, misc_id))
        conn.commit()

    return jsonify(success=True)

@app.route('/add_thing', methods=['POST'])
def add_thing():
    misc_category = request.form.get('misc_category')
    misc_thing = request.form.get('misc_thing')
    misc_tier = request.form.get('misc_tier')
    misc_secondary = request.form.get('misc_secondary')
    misc_coord = request.form.get('misc_coord')
    # Remove spaces and commas from the input
    misc_coord = misc_coord.replace(' ', '').replace(',', '')

    # Format the chest_coord with commas while maintaining negative signs
    formatted_misc_coord = ''
    i = 0
    while i < len(misc_coord):
        section = misc_coord[i:i+4]
        if section.startswith('-'):
            section = misc_coord[i:i+5]
            formatted_misc_coord += section + ', '
            i += 5
        else:
            formatted_misc_coord += section[:4] + ', '
            i += 4
    formatted_misc_coord = formatted_misc_coord.rstrip(', ')
    misc_location = request.form.get('misc_location')
    misc_region = request.form.get('misc_region')
    misc_map = request.form.get('misc_map')
    misc_found = request.form.get('misc_found')

    # Insert the new thing into the database
    with closing(conn.cursor()) as c:
        c.execute('INSERT INTO misc (misc_found, misc_monster, misc_color, misc_coord, misc_location, misc_region, misc_map) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                  (misc_found, misc_category, misc_thing, misc_tier, misc_secondary, formatted_misc_coord, misc_location, misc_region, misc_map))
        conn.commit()

    # Redirect back to the interesting page after adding the thing
    return redirect('/interesting')

@app.route("/oldmaps", methods=["GET", "POST"])
def oldmaps():
    headline = "Old Maps"
    percentages = get_percentages()
    scroll_position = session.get('scrollPosition')
    if scroll_position is not None:
        scroll_position = int(scroll_position)

    regions = [
    "Great Sky Island",
    "Hyrule Field",
    "Tabantha",
    "Great Hyrule Forest",
    "North Hyrule Sky Archipelago",
    "Akkala",
    "Eldin",
    "Lanayru",
    "Necluda",
    "Faron",
    "Gerudo",
]

    if request.method == 'POST':
        with closing(conn.cursor()) as c:
            oldmaps = c.execute('SELECT * FROM oldmaps').fetchall()
            for map in oldmaps:
                if map[1] == "Map":
                    map_id = map[0]
                    map_collected = request.form.get(f'found_oldmap_{map[0]}')
                    print("Map_id, Map_collected:", map_id, ", ", map_collected)
                    if map_collected is None:
                        map_collected = c.execute('SELECT map_collected FROM oldmaps WHERE map_id = ?', (int(map[0]),)).fetchone()[0] or 0
                        print("IF statement Map_collected:", map_collected)
                    else:
                        print("map_collected is not none:", map_collected)
                    c.execute('UPDATE oldmaps SET map_collected = ? WHERE map_id = ?', (map_collected, map_id))
                    print("Executed map Update statement with map_collected ->", map_collected, " and map_id ->", map_id)
                    print("")
               
                elif map[1] == "Treasure":
                    treasure_id = map[0]
                    print("Treasure_id: ", treasure_id)
                    treasure_collected = request.form.get(f'found_oldmap_treasure_{map[0]}')
                    if treasure_collected is None:
                        try:
                            print("in TRY block -> Treasure_ID:", treasure_id)
                            treasure_collected = c.execute('SELECT map_collected FROM oldmaps WHERE map_id = ?', (int(map[0]),)).fetchone()[0] or 0
                            print("IF statement Treasure_collected:", treasure_collected)
                            print("")
                        except Exception as e:
                            print("Exception occurred! Treasure_id:", treasure_id, "Treasure_collected:", treasure_collected)
                            treasure_collected = 0  # Set a default value of 0 if it's still None
                    else:
                        treasure_collected = int(treasure_collected)  # Convert to int here
                        print("treasure_collected is not None:", treasure_collected)

                    c.execute('UPDATE oldmaps SET map_collected = ? WHERE map_id = ?', (treasure_collected, treasure_id))
                    print("Executed treasure Update statement with treasure_collected ->", treasure_collected, " and treasure_id ->", treasure_id)
                else:
                    print("Else! not Map or Treasure. map[0] ->", map[0])
                print("")
                conn.commit()

    with closing(conn.cursor()) as c:
        query = '''SELECT * FROM oldmaps ORDER BY map_id ASC'''
        c.execute(query)
        selected_region = request.args.get('region')
        results = c.fetchall()
        # Filter the results based on the selected region
        if selected_region:
            results = [result for result in results if result[4] == selected_region]   
        info = [(result[0], result[1], result[2]) for result in results]
    # Calculate the completion status for each region
    region_status = {}
    for region in regions:
        total_oldmaps = len([result for result in results if result[4] == region])
        found = len([result for result in results if result[4] == region and result[0] == 1])
        unfound = len([result for result in results if result[4] == region and result[0] == 0])

        region_status[region] = {
            'found': found,
            'found': found,
            'unfound': unfound,
            'total_oldmaps': total_oldmaps
        }

    return render_template("oldmaps.html", scroll_position=scroll_position, headline=headline, percentages=percentages, info=info, results=results, regions=regions, region_status=region_status)

@app.route('/update_oldmaps', methods=['POST'])
def update_oldmaps():
    treasure_id = request.json.get('treasure_id')
    treasure_done = request.json.get('treasure_done')

    if treasure_done is None:
        treasure_done = 0
    else:
        treasure_done = treasure_done

    # Update the location in the database with the new found status
    try:
        with closing(conn.cursor()) as c:
            c.execute('UPDATE oldmaps SET map_collected = ? WHERE map_id = ?', (treasure_done, treasure_id))
            print("update oldmaps map_collected = ", treasure_done, ", map_id = ", treasure_id)
            conn.commit()
        return jsonify(success=True)
    except Exception as e:
        print("Error:", e)  # Add this line for debugging
        return jsonify(success=False, error=str(e))

@app.route("/shrinequests", methods=["GET", "POST"])
def shrinequests():
    headline = "Shrine Quests"
    percentages = get_percentages()
    scroll_position = session.get('scrollPosition')
    if scroll_position is not None:
        scroll_position = int(scroll_position)

    regions = [
    "Great Sky Island",
    "Hyrule Field",
    "Tabantha",
    "Great Hyrule Forest",
    "North Hyrule Sky Archipelago",
    "Akkala",
    "Eldin",
    "Lanayru",
    "Necluda",
    "Faron",
    "Gerudo",
]

    if request.method == 'POST':
        with closing(conn.cursor()) as c:
            shrinequ_shrines = c.execute('SELECT * FROM shrinequests').fetchall()
            for shrinequ_shrine in shrinequ_shrines:
                shrinequ_id = shrinequ_shrine[0]
                shrinequ_done = request.form.get(f'done_shrinequ_{shrinequ_id}')
                if shrinequ_done is None:
                    print("shrinequ_done is None:", shrinequ_done, "ID ->", shrinequ_id)
                    shrinequ_done = c.execute('SELECT shrinequ_done FROM shrinequests WHERE shrinequ_id = ?', (shrinequ_id,)).fetchone()[0]
                else:
                    print("shrinequ_done is not none:", shrinequ_done)
                c.execute('UPDATE shrinequests SET shrinequ_done = ? WHERE shrinequ_id = ?', (shrinequ_done, shrinequ_id))
            conn.commit()

    with closing(conn.cursor()) as c:
        query = '''SELECT * FROM shrinequests ORDER BY shrinequ_name ASC'''
        c.execute(query)
        selected_region = request.args.get('region')
        results = c.fetchall()
        # Filter the results based on the selected region
        if selected_region:
            results = [result for result in results if result[4] == selected_region]   
        info = [(result[0], result[1], result[2]) for result in results]
    # Calculate the completion status for each region
    region_status = {}
    for region in regions:
        total_shrinequs = len([result for result in results if result[4] == region])
        completed = len([result for result in results if result[4] == region and result[0] == 2])
        started = len([result for result in results if result[4] == region and result[0] == 1])
        unfound = len([result for result in results if result[4] == region and result[0] == 0])

        region_status[region] = {
            'completed': completed,
            'started': started,
            'unfound': unfound,
            'total_shrinequs': total_shrinequs
        }

    return render_template("shrinequests.html", scroll_position=scroll_position, headline=headline, percentages=percentages, info=info, results=results, regions=regions, region_status=region_status)

@app.route("/sidequests", methods=["GET", "POST"])
def sidequests():
    headline = "Side Quests"
    percentages = get_percentages()
    scroll_position = session.get('scrollPosition')
    if scroll_position is not None:
        scroll_position = int(scroll_position)

    regions = [
    "Great Sky Island",
    "Hyrule Field",
    "Tabantha",
    "Great Hyrule Forest",
    "North Hyrule Sky Archipelago",
    "Akkala",
    "Eldin",
    "Lanayru",
    "Necluda",
    "Faron",
    "Gerudo",
]

    with closing(conn.cursor()) as c:
        c.execute("SELECT COUNT(*) FROM locations WHERE location_type = 'Well'")
        total_wells = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM locations WHERE location_done = 1 AND location_type = 'Well'")
        completed_wells = c.fetchone()[0]
    
    if request.method == 'POST':

        with closing(conn.cursor()) as c:
            side_ids = c.execute('SELECT quest_id FROM quests').fetchall()
            for side_id in side_ids:
                side_id = side_id[0]
                side_done = request.form.get(f'done_sidequ_{side_id}')
                if side_done is None:
                    side_done = c.execute('SELECT quest_done FROM quests WHERE quest_type = "Side" AND quest_id = ?', (side_id,)).fetchone()[0]
                else:
                    print("quest_done is not none:", side_done)
                c.execute('UPDATE quests SET quest_done = ? WHERE quest_type = "Side" AND quest_id = ?', (side_done, side_id))
                print("quest_id ->", side_id)
            conn.commit()

    with closing(conn.cursor()) as c:
        query = '''SELECT * FROM quests WHERE quest_type = "Side" ORDER BY quest_id ASC'''
        c.execute(query)
        selected_region = request.args.get('region')
        results = c.fetchall()
        # Filter the results based on the selected region
        if selected_region:
            results = [result for result in results if result[4] == selected_region]   
        info = [(result[0], result[1], result[2]) for result in results]
    # Calculate the completion status for each region
    region_status = {}
    for region in regions:
        total_quests = len([result for result in results if result[4] == region])
        completed = len([result for result in results if result[4] == region and result[0] == 2])
        started = len([result for result in results if result[4] == region and result[0] == 1])
        unfound = len([result for result in results if result[4] == region and result[0] == 0])

        region_status[region] = {
            'completed': completed,
            'started': started,
            'unfound': unfound,
            'total_quests': total_quests
        }

    return render_template("sidequests.html", scroll_position=scroll_position, headline=headline,  percentages=percentages, info=info, results=results, regions=regions, region_status=region_status, total_wells=total_wells, completed_wells=completed_wells)

@app.route('/update_sidequests', methods=['POST'])
def update_sidequests():
    side_id = request.json.get('side_id')
    side_done = request.json.get('side_done')

    if side_done is None:
        side_done = 0
    else:
        side_done = side_done

    # Update the quest in the database with the new found status
    try:
        with closing(conn.cursor()) as c:
            c.execute('UPDATE quests SET quest_done = ? WHERE quest_id = ?', (side_done, side_id))
            print("update_sides quest_done = ", side_done, ", quest_id = ", side_id)
            conn.commit()
        return jsonify(success=True)
    except Exception as e:
        print("Error:", e)  # Add this line for debugging
        return jsonify(success=False, error=str(e))

@app.route("/adventures", methods=["GET", "POST"])
def adventures():
    headline = "Adventures"
    percentages = get_percentages()
#     scroll_position = session.get('scrollPosition')
#     if scroll_position is not None:
#         scroll_position = int(scroll_position)

#     regions = [
#     "Great Sky Island",
#     "Hyrule Field",
#     "Tabantha",
#     "Great Hyrule Forest",
#     "North Hyrule Sky Archipelago",
#     "Akkala",
#     "Eldin",
#     "Lanayru",
#     "Necluda",
#     "Faron",
#     "Gerudo",
# ]

    with closing(conn.cursor()) as c:
        c.execute("SELECT COUNT(*) FROM towers WHERE tower_done = 1")
        completed_towers = c.fetchone()[0]

    with closing(conn.cursor()) as c:
        c.execute("SELECT COUNT(*) FROM locations WHERE location_done = 1 AND location_type = 'Flower-Shaped Island'")
        completed_flowers = c.fetchone()[0]
    
    if request.method == 'POST':

        with closing(conn.cursor()) as c:
            adventure_ids = c.execute('SELECT quest_id FROM quests').fetchall()
            for adventure_id in adventure_ids:
                adventure_id = adventure_id[0]
                adventure_done = request.form.get(f'done_{adventure_id}')
                if adventure_done is None:
                    adventure_done = c.execute('SELECT quest_done FROM quests WHERE quest_type = "Adventure" AND quest_id = ?', (adventure_id,)).fetchone()[0]
                else:
                    print("quest_done is not none:", adventure_done)
                c.execute('UPDATE quests SET quest_done = ? WHERE quest_type = "Adventure" AND quest_id = ?', (adventure_done, adventure_id))
                print("quest_id ->", adventure_id)
            conn.commit()

    with closing(conn.cursor()) as c:
        query = '''SELECT * FROM quests WHERE quest_type = "Adventure" ORDER BY quest_id ASC'''
        c.execute(query)
        selected_region = request.args.get('region')
        results = c.fetchall()
    #     # Filter the results based on the selected region
    #     if selected_region:
    #         results = [result for result in results if result[4] == selected_region]   
    #     info = [(result[0], result[1], result[2]) for result in results]
    # # Calculate the completion status for each region
    # region_status = {}
    # for region in regions:
    #     total_quests = len([result for result in results if result[4] == region])
    #     completed = len([result for result in results if result[4] == region and result[0] == 2])
    #     started = len([result for result in results if result[4] == region and result[0] == 1])
    #     unfound = len([result for result in results if result[4] == region and result[0] == 0])

    #     region_status[region] = {
    #         'completed': completed,
    #         'started': started,
    #         'unfound': unfound,
    #         'total_quests': total_quests
    #     }

    return render_template("adventures.html", headline=headline, completed_flowers=completed_flowers, completed_towers=completed_towers, percentages=percentages, results=results)

@app.route('/update_adventures', methods=['POST'])
def update_adventures():
    adventure_id = request.json.get('adventure_id')
    adventure_done = request.json.get('adventure_done')

    if adventure_done is None:
        adventure_done = 0
    else:
        adventure_done = adventure_done

    # Update the quest in the database with the new found status
    try:
        with closing(conn.cursor()) as c:
            c.execute('UPDATE Quests SET quest_done = ? WHERE quest_id = ?', (adventure_done, adventure_id))
            print("update_adventures quest_done = ", adventure_done, ", quest_id = ", adventure_id)
            conn.commit()
        return jsonify(success=True)
    except Exception as e:
        print("Error:", e)  # Add this line for debugging
        return jsonify(success=False, error=str(e))

@app.route("/mainqu", methods=["GET", "POST"])
def mainqu():
    headline = "Main Quests"
    percentages = get_percentages()
    scroll_position = session.get('scrollPosition')
    if scroll_position is not None:
        scroll_position = int(scroll_position)

    if request.method == 'POST':
        with closing(conn.cursor()) as c:
            mainqus = c.execute('SELECT quest_id FROM Quests WHERE quest_type = "Main"').fetchall()
            for mainqu in mainqus:
                mainqu_id = mainqu[0]
                mainqu_done = request.form.get(f'done_mainqu_{mainqu_id}')
                if mainqu_done is None:
                    print("mainqu_done is none:", mainqu_done)
                    mainqu_done = c.execute('SELECT quest_done FROM Quests WHERE quest_id = ?', (mainqu_id,)).fetchone()[0]
                else:
                    print("mainqu_done is not none:", mainqu_done)
                print("mainqu_id:", mainqu_id)
                print("mainqu_done:", mainqu_done)
                c.execute('UPDATE Quests SET quest_done = ? WHERE quest_id = ?', (mainqu_done, mainqu_id))
                print("Executed update statement for mainqu_id:", mainqu_id)
            conn.commit()
        with closing(conn.cursor()) as c:
            secondarys = c.execute('SELECT * FROM SubQuests').fetchall()
            for secondary in secondarys:
                secondary_id = secondary[0]
                secondary_done = request.form.get(f'secondary_{secondary_id}')
                if secondary_done is None:
                    print("secondary_done is none:", secondary_done)
                    secondary_done = c.execute('SELECT subquest_done FROM SubQuests WHERE subquest_id = ?', (secondary_id,)).fetchone()[0]
                else:
                    print("secondary_done is not none:", secondary_done)
                print("secondary_id:", secondary_id)
                print("secondary_done:", secondary_done)
                c.execute('UPDATE SubQuests SET subquest_done = ? WHERE subquest_id = ?', (secondary_done, secondary_id))
                print("Executed update statement for secondary_id:", secondary_id)
            conn.commit()

    with closing(conn.cursor()) as c:
        main_riju = c.execute('SELECT * FROM SubQuests WHERE quest_id = 10').fetchall()
        main_sidon = c.execute('SELECT * FROM SubQuests WHERE quest_id = 13').fetchall()
        main_yunobo = c.execute('SELECT * FROM SubQuests WHERE quest_id = 11').fetchall()
        main_tulin = c.execute('SELECT * FROM SubQuests WHERE quest_id = 8').fetchall()
        main_spirit = c.execute('SELECT * FROM SubQuests WHERE quest_id = 18').fetchall()

    with closing(conn.cursor()) as c:
        query = '''SELECT * FROM Quests WHERE quest_type = "Main" ORDER BY quest_id ASC'''
        c.execute(query)
        results = c.fetchall()
        info = [(result[0], result[1], result[2]) for result in results]
    return render_template("mainqu.html", main_riju=main_riju, main_sidon=main_sidon, main_yunobo=main_yunobo, main_tulin=main_tulin, main_spirit=main_spirit, scroll_position=scroll_position, headline=headline, percentages=percentages, info=info, results=results)

@app.route('/update_mainquests', methods=['POST'])
def update_mainquests():
    main_id = request.json.get('main_id')
    main_done = request.json.get('main_done')

    if main_done is None:
        main_done = 0
    else:
        main_done = main_done

    # Update the main in the database with the new found status
    try:
        with closing(conn.cursor()) as c:
            c.execute('UPDATE Quests SET quest_done = ? WHERE quest_id = ?', (main_done, main_id))
            print("Quests Quest_done = ", main_done, ", Quest_id = ", main_id)
            conn.commit()
        return jsonify(success=True)
    except Exception as e:
        print("Error:", e)  # Add this line for debugging
        return jsonify(success=False, error=str(e))
    
@app.route('/update_secondary', methods=['POST'])
def update_secondary():
    secondary_id = request.json.get('secondary_id')
    secondary_done = request.json.get('secondary_done')

    if secondary_done is None:
        secondary_done = 0
    else:
        secondary_done = secondary_done

    # Update the main in the database with the new found status
    try:
        with closing(conn.cursor()) as c:
            c.execute('UPDATE SubQuests SET subquest_done = ? WHERE subquest_id = ?', (secondary_done, secondary_id))
            print("SubQuests subquest_done = ", secondary_done, ", subquest_id = ", secondary_id)
            conn.commit()
        return jsonify(success=True)
    except Exception as e:
        print("Error:", e)  # Add this line for debugging
        return jsonify(success=False, error=str(e))


@app.route("/addison", methods=["GET", "POST"])
def addison():
    headline = "Addison"
    percentages = get_percentages()
    scroll_position = session.get('scrollPosition')
    if scroll_position is not None:
        scroll_position = int(scroll_position)

    if request.method == 'POST':
        with closing(conn.cursor()) as c:
            addisons = c.execute('SELECT addison_id FROM addison ORDER BY addison_id ASC').fetchall()
            for addison in addisons:
                addison_id = addison[0]
                addison_done = request.form.get(f'done_addison_{addison_id}')
                if addison_done is None:
                    print("addison_done is none:", addison_done)
                    addison_done = c.execute('SELECT addison_done FROM addison WHERE addison_id = ?', (addison_id,)).fetchone()[0]
                else:
                    print("addison_done is not none:", addison_done)
                print("addison_id:", addison_id)
                print("addison_done:", addison_done)
                c.execute('UPDATE addison SET addison_done = ? WHERE addison_id = ?', (addison_done, addison_id))
                print("Executed update statement for addison_id:", addison_id)
            conn.commit()

    with closing(conn.cursor()) as c:
        query = '''SELECT * FROM addison ORDER BY addison_id ASC'''
        c.execute(query)
        results = c.fetchall()
        info = [(result[0], result[1], result[2]) for result in results]
    return render_template("addison.html", scroll_position=scroll_position, headline=headline, percentages=percentages, info=info, results=results)

@app.route("/location-location", methods=["GET", "POST"])
def location():
    headline = "Locations"
    percentages = get_percentages()
    scroll_position = session.get('scrollPosition')
    if scroll_position is not None:
        scroll_position = int(scroll_position)

    if request.method == 'POST':
        with closing(conn.cursor()) as c:
            locations = c.execute('SELECT * FROM locations WHERE location_type = "Location" ORDER BY location_name ASC').fetchall()
            for location in locations:
                location_id = location[0]
                location_done = request.form.get(f'done_location_{location_id}')
                if location_done is None:
                    location_done = 0
                else:
                    location_done = 1
                    print("Location Done ->", location_id, ", ", location_done)
                # print("location_id:", location_id)
                # print("location_done:", location_done)
                c.execute('UPDATE locations SET location_done = ? WHERE location_id = ?', (location_done, location_id))
                # print("Executed update statement for location_id:", location_id)
            conn.commit()

    with closing(conn.cursor()) as c:
        query = '''SELECT * FROM locations WHERE location_type = 'Location' ORDER BY location_name ASC'''
        c.execute(query)
        locations = c.fetchall()
    return render_template("location-location.html", scroll_position=scroll_position, headline=headline, percentages=percentages, locations=locations)

@app.route("/location-chasm", methods=["GET", "POST"])
def chasm():
    headline = "Chasms"
    percentages = get_percentages()
    scroll_position = session.get('scrollPosition')
    if scroll_position is not None:
        scroll_position = int(scroll_position)

    if request.method == 'POST':
        with closing(conn.cursor()) as c:
            chasms = c.execute('SELECT * FROM locations WHERE location_type = "Chasm" ORDER BY location_name ASC').fetchall()
            for chasm in chasms:
                chasm_id = chasm[0]
                chasm_done = request.form.get(f'done_chasm_{chasm_id}')
                if chasm_done is None:
                    chasm_done = 0
                else:
                    chasm_done = 1
                    print("chasm Done ->", chasm_id, ", ", chasm_done)
                # print("chasm_id:", chasm_id)
                # print("chasm_done:", chasm_done)
                c.execute('UPDATE locations SET location_done = ? WHERE location_id = ?', (chasm_done, chasm_id))
                # print("Executed update statement for chasm_id:", chasm_id)
            conn.commit()

    with closing(conn.cursor()) as c:
        query = '''SELECT * FROM locations WHERE location_type = 'Chasm' ORDER BY location_name ASC'''
        c.execute(query)
        chasms = c.fetchall()
        print("CHASMS ->", chasms)
    return render_template("location-chasm.html", scroll_position=scroll_position, headline=headline, percentages=percentages, chasms=chasms)

@app.route('/update_chasm', methods=['POST'])
def update_chasm():
    chasm_id = request.json.get('chasm_id')
    chasm_done = request.json.get('chasm_done')

    if chasm_done is None:
        chasm_done = 0
    else:
        chasm_done = chasm_done

    # Update the chasm in the database with the new found status
    try:
        with closing(conn.cursor()) as c:
            c.execute('UPDATE locations SET location_done = ? WHERE location_id = ?', (chasm_done, chasm_id))
            print("update_chasm chasm_done = ", chasm_done, ", chasm_id = ", chasm_id)
            conn.commit()
        return jsonify(success=True)
    except Exception as e:
        print("Error:", e)  # Add this line for debugging
        return jsonify(success=False, error=str(e))
    
@app.route("/location-flowerislands", methods=["GET", "POST"])
def flowerislands():
    headline = "flowerislands"
    percentages = get_percentages()
    scroll_position = session.get('scrollPosition')
    if scroll_position is not None:
        scroll_position = int(scroll_position)

    if request.method == 'POST':
        with closing(conn.cursor()) as c:
            flowerislands = c.execute('SELECT * FROM locations WHERE location_type = "Flower-Shaped Island" ORDER BY location_name ASC').fetchall()
            for flowerisland in flowerislands:
                flowerisland_id = flowerisland[0]
                flowerisland_done = request.form.get(f'done_flowerisland_{flowerisland_id}')
                if flowerisland_done is None:
                    flowerisland_done = 0
                else:
                    flowerisland_done = 1
                    print("flowerisland Done ->", flowerisland_id, ", ", flowerisland_done)
                # print("flowerisland_id:", flowerisland_id)
                # print("flowerisland_done:", flowerisland_done)
                c.execute('UPDATE locations SET location_done = ? WHERE location_id = ?', (flowerisland_done, flowerisland_id))
                # print("Executed update statement for flowerisland_id:", flowerisland_id)
            conn.commit()

    with closing(conn.cursor()) as c:
        query = '''SELECT * FROM locations WHERE location_type = 'Flower-Shaped Island' ORDER BY location_region ASC'''
        c.execute(query)
        flowerislands = c.fetchall()
        print("flowerislandS ->", flowerislands)
    return render_template("location-flowerislands.html", scroll_position=scroll_position, headline=headline, percentages=percentages, flowerislands=flowerislands)

@app.route('/update_flowerisland', methods=['POST'])
def update_flowerisland():
    flowerisland_id = request.json.get('flowerisland_id')
    flowerisland_done = request.json.get('flowerisland_done')

    if flowerisland_done is None:
        flowerisland_done = 0
    else:
        flowerisland_done = flowerisland_done

    # Update the flowerisland in the database with the new found status
    try:
        with closing(conn.cursor()) as c:
            c.execute('UPDATE locations SET location_done = ? WHERE location_id = ?', (flowerisland_done, flowerisland_id))
            print("update_flowerisland flowerisland_done = ", flowerisland_done, ", flowerisland_id = ", flowerisland_id)
            conn.commit()
        return jsonify(success=True)
    except Exception as e:
        print("Error:", e)  # Add this line for debugging
        return jsonify(success=False, error=str(e))
    

@app.route("/location-well", methods=["GET", "POST"])
def well():
    headline = "Wells"
    percentages = get_percentages()
    scroll_position = session.get('scrollPosition')
    if scroll_position is not None:
        scroll_position = int(scroll_position)

    if request.method == 'POST':
        with closing(conn.cursor()) as c:
            wells = c.execute('SELECT * FROM locations WHERE location_type = "Well" ORDER BY location_name ASC').fetchall()
            for well in wells:
                well_id = well[0]
                well_done = request.form.get(f'done_well_{well_id}')
                if well_done is None:
                    well_done = 0
                else:
                    well_done = 1
                    print("well Done ->", well_id, ", ", well_done)
                # print("well_id:", well_id)
                # print("well_done:", well_done)
                c.execute('UPDATE locations SET location_done = ? WHERE location_id = ?', (well_done, well_id))
                # print("Executed update statement for well_id:", well_id)
            conn.commit()

    with closing(conn.cursor()) as c:
        query = '''SELECT * FROM locations WHERE location_type = 'Well' ORDER BY location_name ASC'''
        c.execute(query)
        wells = c.fetchall()
    return render_template("location-well.html", scroll_position=scroll_position, headline=headline, percentages=percentages, wells=wells)

@app.route('/update-well', methods=['POST'])
def update_well():
    well_id = request.json.get('well_id')
    well_done = request.json.get('well_done')

    if well_done is None:
        well_done = 0
    else:
        well_done = well_done

    # Update the dispenser in the database with the new found status
    try:
        with closing(conn.cursor()) as c:
            c.execute('UPDATE locations SET location_done = ? WHERE location_id = ?', (well_done, well_id))
            print("update_well well_done = ", well_done, ", well_id = ", well_id)
            conn.commit()
        return jsonify(success=True)
    except Exception as e:
        print("Error:", e)  # Add this line for debugging
        return jsonify(success=False, error=str(e))
    
@app.route("/location-depths_mine", methods=["GET", "POST"])
def depths_mine():
    headline = "Depths Mines"
    percentages = get_percentages()
    scroll_position = session.get('scrollPosition')
    if scroll_position is not None:
        scroll_position = int(scroll_position)

    if request.method == 'POST':
        with closing(conn.cursor()) as c:
            depths_mines = c.execute('SELECT * FROM locations WHERE location_type = "Depths Mine" ORDER BY location_name ASC').fetchall()
            for depths_mine in depths_mines:
                depths_mine_id = depths_mine[0]
                depths_mine_done = request.form.get(f'done_depths_mine_{depths_mine_id}')
                if depths_mine_done is None:
                    depths_mine_done = 0
                else:
                    depths_mine_done = 1
                    print("depths_mine Done ->", depths_mine_id, ", ", depths_mine_done)
                # print("depths_mine_id:", depths_mine_id)
                # print("depths_mine_done:", depths_mine_done)
                c.execute('UPDATE locations SET location_done = ? WHERE location_id = ?', (depths_mine_done, depths_mine_id))
                # print("Executed update statement for depths_mine_id:", depths_mine_id)
            conn.commit()

    with closing(conn.cursor()) as c:
        query = '''SELECT * FROM locations WHERE location_type = 'Depths Mine' ORDER BY location_name ASC'''
        c.execute(query)
        depths_mines = c.fetchall()
    return render_template("location-depths_mine.html", scroll_position=scroll_position, headline=headline, percentages=percentages, depths_mines=depths_mines)

@app.route("/location-great_fairy_fountain", methods=["GET", "POST"])
def great_fairy_fountain():
    headline = "Great Fairy Fountains"
    percentages = get_percentages()
    scroll_position = session.get('scrollPosition')
    if scroll_position is not None:
        scroll_position = int(scroll_position)

    if request.method == 'POST':
        with closing(conn.cursor()) as c:
            great_fairy_fountains = c.execute('SELECT * FROM fairyfountains ORDER BY fairy_name ASC').fetchall()
            for great_fairy_fountain in great_fairy_fountains:
                great_fairy_fountain_id = great_fairy_fountain[0]
                great_fairy_fountain_done = request.form.get(f'done_great_fairy_fountain_{great_fairy_fountain_id}')
                if great_fairy_fountain_done is None:
                    great_fairy_fountain_done = 0
                else:
                    great_fairy_fountain_done = 1
                    print("great_fairy_fountain Done ->", great_fairy_fountain_id, ", ", great_fairy_fountain_done)
                # print("great_fairy_fountain_id:", great_fairy_fountain_id)
                # print("great_fairy_fountain_done:", great_fairy_fountain_done)
                c.execute('UPDATE fairyfountains SET fairy_found = 1 WHEREfairy_id = ?', (great_fairy_fountain_id,))
                # print("Executed update statement for great_fairy_fountain_id:", great_fairy_fountain_id)
            conn.commit()

    with closing(conn.cursor()) as c:
        query = '''SELECT * FROM fairyfountains ORDER BY fairy_name ASC'''
        c.execute(query)
        great_fairy_fountains = c.fetchall()
    return render_template("location-great_fairy_fountain.html", scroll_position=scroll_position, headline=headline, percentages=percentages, great_fairy_fountains=great_fairy_fountains)

@app.route('/update_great_fairy_fountain', methods=['POST'])
def update_great_fairy_fountain():
    greatfairy_id = request.json.get('fairy_id')
    greatfairy_done = request.json.get('fairy_done')
    print("Fairy ID ->", greatfairy_id)
    print("Fairy Done ->", greatfairy_done)

    # if greatfairy_done is None:
    #     greatfairy_done = 0
    # else:
    #     greatfairy_done = greatfairy_done

    # Update the great_fairy_fountain in the database with the new found status
    try:
        with closing(conn.cursor()) as c:
            c.execute('UPDATE fairyfountains SET fairy_found = ? WHERE fairy_id = ?', (greatfairy_done,greatfairy_id,))
            print("update_great_fairy_fountain greatfairy_done = ", greatfairy_done, ", greatfairy_id = ", greatfairy_id)
            conn.commit()
        return jsonify(success=True)
    except Exception as e:
        print("Error:", e)  # Add this line for debugging
        return jsonify(success=False, error=str(e))
    

@app.route("/location-device_dispenser", methods=["GET", "POST"])
def device_dispenser():
    headline = "Device Dispensers"
    percentages = get_percentages()
    scroll_position = session.get('scrollPosition')
    if scroll_position is not None:
        scroll_position = int(scroll_position)

    with closing(conn.cursor()) as c:
        c.execute("SELECT COUNT(*) FROM device_dispenser WHERE dis_done = 1")
        completed_dispenser = c.fetchone()[0]

    if request.method == 'POST':
        with closing(conn.cursor()) as c:
            device_dispensers = c.execute('SELECT * FROM device_dispenser ORDER BY dis_id ASC').fetchall()
            for device_dispenser in device_dispensers:
                device_dispenser_id = device_dispenser[0]
                device_dispenser_done = request.form.get(f'done_device_dispenser_{device_dispenser_id}')
                if device_dispenser_done is None:
                    device_dispenser_done = 0
                else:
                    device_dispenser_done = 1
                    print("device_dispenser Done ->", device_dispenser_id, ", ", device_dispenser_done)
                # print("device_dispenser_id:", device_dispenser_id)
                # print("device_dispenser_done:", device_dispenser_done)
                c.execute('UPDATE device_dispenser SET dis_done = ? WHERE dis_id = ?', (device_dispenser_done, device_dispenser_id))
                # print("Executed update statement for device_dispenser_id:", device_dispenser_id)
            conn.commit()

    with closing(conn.cursor()) as c:
        query = '''SELECT * FROM device_dispenser ORDER BY dis_id ASC'''
        c.execute(query)
        device_dispensers = c.fetchall()
        print("device_dispensers ->", device_dispensers)
    return render_template("location-device_dispenser.html", scroll_position=scroll_position, headline=headline, percentages=percentages, device_dispensers=device_dispensers, completed_dispenser=completed_dispenser)

@app.route('/update-device_dispenser', methods=['POST'])
def update_device_dispenser():
    dis_id = request.json.get('dis_id')
    dis_done = request.json.get('dis_done')

    if dis_done is None:
        dis_done = 0
    else:
        dis_done = dis_done

    # Update the dispenser in the database with the new found status
    try:
        with closing(conn.cursor()) as c:
            c.execute('UPDATE device_dispenser SET dis_done = ? WHERE dis_id = ?', (dis_done, dis_id))
            print("update dispensers dis_done = ", dis_done, ", dis_id = ", dis_id)
            conn.commit()
        return jsonify(success=True)
    except Exception as e:
        print("Error:", e)  # Add this line for debugging
        return jsonify(success=False, error=str(e))
    
@app.route("/location_schemas", methods=["GET", "POST"])
def location_schemas():
    headline = "Schemas"
    percentages = get_percentages()
    scroll_position = session.get('scrollPosition')
    if scroll_position is not None:
        scroll_position = int(scroll_position)
    
    with closing(conn.cursor()) as c:
        c.execute("SELECT COUNT(*) FROM schemas WHERE schema_done = 1 AND schema_type = 'Yiga'")
        completed_yiga = c.fetchone()[0]
        c.execute("SELECT COUNT(*) FROM schemas WHERE schema_done = 1 AND schema_type = 'Stone'")
        completed_stone = c.fetchone()[0]
    
    if request.method == 'POST':
        with closing(conn.cursor()) as c:
            yigas = c.execute('SELECT * FROM schemas WHERE schema_type = "Yiga" ORDER BY schema_id ASC').fetchall()
            for yiga in yigas:
                yiga_id = yiga[0]
                yiga_done = request.form.get(f'done_schema_{yiga_id}')
                if yiga_done is None:
                    yiga_done = 0
                else:
                    yiga_done = 1
                    print("yiga_done ->", yiga_id, ", ", yiga_done)
                # print("yiga_id:", yiga_id)
                # print("yiga_done:", yiga_done)
                c.execute('UPDATE schemas SET schema_done = ? WHERE schema_id = ?', (yiga_done, yiga_id))
                # print("Executed update statement for yiga_id:", yiga_id)
            conn.commit()
            
        with closing(conn.cursor()) as c:
            stones = c.execute('SELECT * FROM schemas WHERE schema_type = "Stone" ORDER BY schema_id ASC').fetchall()
            for stone in stones:
                stone_id = stone[0]
                stone_done = request.form.get(f'done_schema_{stone_id}')
                if stone_done is None:
                    stone_done = 0
                else:
                    stone_done = 1
                    print("stone_done ->", stone_id, ", ", stone_done)
                # print("stone_id:", stone_id)
                # print("stone_done:", stone_done)
                c.execute('UPDATE schemas SET schema_done = ? WHERE schema_id = ?', (stone_done, stone_id))
                # print("Executed update statement for stone_id:", stone_id)
            conn.commit()

    with closing(conn.cursor()) as c:
        query = '''SELECT * FROM schemas ORDER BY schema_id ASC'''
        c.execute(query)
        schemas = c.fetchall()
        print("schemas ->", schemas)
        
    return render_template("location_schemas.html", scroll_position=scroll_position, headline=headline, percentages=percentages, schemas=schemas, completed_yiga=completed_yiga, completed_stone=completed_stone)


@app.route('/update_schema', methods=['POST'])
def update_schema():
    schema_id = request.json.get('schema_id')
    schema_done = request.json.get('schema_done')

    if schema_done is None:
        schema_done = 0
    else:
        schema_done = schema_done

    # Update the dispenser in the database with the new found status
    try:
        with closing(conn.cursor()) as c:
            c.execute('UPDATE schemas SET schema_done = ? WHERE schema_id = ?', (schema_done, schema_id))
            print("update schemas schema_done = ", schema_done, ", schema_id = ", schema_id)
            conn.commit()
        return jsonify(success=True)
    except Exception as e:
        print("Error:", e)  # Add this line for debugging
        return jsonify(success=False, error=str(e))

@app.route("/location-coliseum", methods=["GET", "POST"])
def coliseum():
    headline = "Coliseums"
    percentages = get_percentages()
    scroll_position = session.get('scrollPosition')
    if scroll_position is not None:
        scroll_position = int(scroll_position)

    with closing(conn.cursor()) as c:
        c.execute("SELECT COUNT(*) FROM locations WHERE location_done = 1 AND location_type = 'Coliseum'")
        completed_dispenser = c.fetchone()[0]

    if request.method == 'POST':
        with closing(conn.cursor()) as c:
            coliseums = c.execute('SELECT * FROM locations WHERE location_type = "Coliseum" ORDER BY location_name ASC').fetchall()
            for coliseum in coliseums:
                coli_id = coliseum[0]
                coli_done = request.form.get(f'done_coliseum_{coli_id}')
                if coli_done is None:
                    coli_done = 0
                else:
                    coli_done = 1
                    print("coliseum Done ->", coli_id, ", ", coli_done)
                # print("coli_id:", coli_id)
                # print("coli_done:", coli_done)
                c.execute('UPDATE locations SET location_done = ? WHERE location_id = ?', (coli_done, coli_id))
                # print("Executed update statement for coli_id:", coli_id)
            conn.commit()

    with closing(conn.cursor()) as c:
        query = '''SELECT * FROM locations WHERE location_type = "Coliseum" ORDER BY location_name ASC'''
        c.execute(query)
        coliseums = c.fetchall()
        print("coliseums ->", coliseums)
    return render_template("location-coliseum.html", scroll_position=scroll_position, headline=headline, percentages=percentages, coliseums=coliseums, completed_dispenser=completed_dispenser)

@app.route('/update-coliseum', methods=['POST'])
def update_coliseum():
    coli_id = request.json.get('coli_id')
    coli_done = request.json.get('coli_done')

    if coli_done is None:
        coli_done = 0
    else:
        coli_done = coli_done

    # Update the dispenser in the database with the new found status
    try:
        with closing(conn.cursor()) as c:
            c.execute('UPDATE locations SET location_done = ? WHERE location_id = ?', (coli_done, coli_id))
            print("update_coliseum coli_done = ", coli_done, ", coli_id = ", coli_id)
            conn.commit()
        return jsonify(success=True)
    except Exception as e:
        print("Error:", e)  # Add this line for debugging
        return jsonify(success=False, error=str(e))
    
@app.route("/tower", methods=["GET", "POST"])
def tower():
    headline = "Towers"
    percentages = get_percentages()
    scroll_position = session.get('scrollPosition')
    if scroll_position is not None:
        scroll_position = int(scroll_position)

    if request.method == 'POST':
        with closing(conn.cursor()) as c:
            towers = c.execute('SELECT tower_id FROM towers ORDER BY tower_id ASC').fetchall()
            for tower in towers:
                tower_id = tower[0]
                tower_done = request.form.get(f'done_tower_{tower_id}')
                if tower_done is None:
                    tower_done = 0
                else:
                    tower_done = 1
                print("tower_id:", tower_id)
                print("tower_done:", tower_done)
                c.execute('UPDATE towers SET tower_done = ? WHERE tower_id = ?', (tower_done, tower_id))
                print("Executed update statement for tower_id:", tower_id)
            conn.commit()

    with closing(conn.cursor()) as c:
        query = '''SELECT * FROM towers ORDER BY tower_name ASC'''
        c.execute(query)
        towers = c.fetchall()
    return render_template("tower.html", scroll_position=scroll_position, headline=headline, percentages=percentages, towers=towers)

@app.route('/update-tower', methods=['POST'])
def update_tower():
    tower_id = request.json.get('tower_id')
    tower_done = request.json.get('tower_done')

    if tower_done is None:
        tower_done = 0
    else:
        tower_done = tower_done

    # Update the dispenser in the database with the new found status
    try:
        with closing(conn.cursor()) as c:
            c.execute('UPDATE towers SET tower_done = ? WHERE tower_id = ?', (tower_done, tower_id))
            print("update_tower tower_done = ", tower_done, ", tower_id = ", tower_id)
            conn.commit()
        return jsonify(success=True)
    except Exception as e:
        print("Error:", e)  # Add this line for debugging
        return jsonify(success=False, error=str(e))
    
if __name__ == "__main__":
    app.run(debug=True)
