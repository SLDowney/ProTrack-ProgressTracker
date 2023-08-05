import random
import sqlite3
from contextlib import closing
from flask import Flask, render_template, request, abort, redirect, session
import os
from werkzeug.utils import secure_filename
from flask import jsonify


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

        c.execute("SELECT COUNT(*) FROM locations WHERE location_type = 'Great Fairy Fountain'")
        total_great_fairy_fountains = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM shrines")
        total_shrines = c.fetchone()[0]

        # Add the counts for the additional tables
        c.execute("SELECT COUNT(*) FROM addison")
        total_addison = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM adventure")
        total_adventure = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM caves")
        total_caves = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM compendium")
        total_compendium = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM allkoroks")
        total_koroks = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM lightroots")
        total_lightroots = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM mainqu")
        total_mainqu = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM oldmaps")
        total_oldmaps = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM shrinequests")
        total_shrinequests = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM sidequests")
        total_sidequests = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM towers")
        total_towers = c.fetchone()[0]

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

        c.execute("SELECT COUNT(*) FROM locations WHERE location_done = 1 AND location_type = 'Great Fairy Fountain'")
        completed_great_fairy_fountains = c.fetchone()[0]

        # Add the counts for the completed rows in the additional tables
        c.execute("SELECT COUNT(*) FROM addison WHERE addison_done = 1")
        completed_addison = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM adventure WHERE adventure_done = 2")
        completed_adventure = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM caves WHERE cave_done = 2")
        completed_caves = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM compendium WHERE comp_done = 1")
        completed_compendium = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM allkoroks WHERE korok_done = 1")
        completed_koroks = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM lightroots WHERE root_done = 1")
        completed_lightroots = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM mainqu WHERE mainqu_done = 2")
        completed_mainqu = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM oldmaps WHERE map_type = 'Map' AND map_collected = 'TRUE'")
        completed_oldmaps = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM shrinequests WHERE shrinequ_done = 2")
        completed_shrinequests = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM sidequests WHERE side_done = 2")
        completed_sidequests = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM towers WHERE tower_done = 1")
        completed_towers = c.fetchone()[0]

        # Calculate the percentage completion for the additional tables
        percentages = {
            "percentage_chasms": calculate_completion_percentage(completed_chasms, total_chasms),
            "percentage_great_fairy_fountains": calculate_completion_percentage(completed_great_fairy_fountains, total_great_fairy_fountains),
            "percentage_depths_mines": calculate_completion_percentage(completed_depths_mines, total_depths_mines),
            "percentage_wells": calculate_completion_percentage(completed_wells, total_wells),
            "percentage_locations": calculate_completion_percentage(completed_locations, total_locations),
            "percentage_shrines": calculate_completion_percentage(completed_shrines, total_shrines),
            "percentage_addison": calculate_completion_percentage(completed_addison, total_addison),
            "percentage_adventure": calculate_completion_percentage(completed_adventure, total_adventure),
            "percentage_caves": calculate_completion_percentage(completed_caves, total_caves),
            "percentage_compendium": calculate_completion_percentage(completed_compendium, total_compendium),
            "percentage_koroks": calculate_completion_percentage(completed_koroks, total_koroks),
            "percentage_lightroots": calculate_completion_percentage(completed_lightroots, total_lightroots),
            "percentage_mainqu": calculate_completion_percentage(completed_mainqu, total_mainqu),
            "percentage_oldmaps": calculate_completion_percentage(completed_oldmaps, total_oldmaps),
            "percentage_shrinequests": calculate_completion_percentage(completed_shrinequests, total_shrinequests),
            "percentage_sidequests": calculate_completion_percentage(completed_sidequests, total_sidequests),
            "percentage_towers": calculate_completion_percentage(completed_towers, total_towers)
        }
    return percentages

def update_weapons_table(weapon_name, region, damage, buff):
    with closing(conn.cursor()) as c:
        c.execute('SELECT * FROM Weapons WHERE weapon_name = ?', (weapon_name,))
        c.execute('SELECT * FROM Weapons WHERE weapon_name = ?', (weapon_name,))
        weapon_data = c.fetchone()

        if weapon_data:
            # If the weapon already exists, update regions, damage, buff, and weapon_num_found
            existing_regions = weapon_data[1].split(', ') if weapon_data[1] else []
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

            weapon_num_found = weapon_data[4]
            if weapon_num_found is None:
                weapon_num_found = 1
            else:
                weapon_num_found += 1
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
        c.execute("SELECT temple_id, temple_name, temple_lock1, temple_lock2, temple_lock3, temple_lock4, temple_lock5, temple_boss, temple_complete FROM Temples")
        temples_data = c.fetchall()
        print("Temples_data:", temples_data)
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
    headline = "Current Percentage Completed"
    percentages = get_percentages()
    
    # Fetch the temple progress data from the database
    temples_data = fetch_temple_progress()

    # Calculate progress percentage for each temple and create a list of dictionaries with (temple_name, progress_percentage)
    progress_data = []
    for temple in temples_data:
        temple_id = temple[0]
        print("generating progress data: temple_id:", temple_id)
        temple_name = temple[1]
        if temple_name == "Fire Temple" or temple_name == "Wind Temple":
            locks = temple[2], temple[3], temple[4], temple[5], temple[6]
        else:
            locks = temple[2], temple[3], temple[4], temple[5]
        completed_locks = sum(int(lock) for lock in locks if isinstance(lock, int))
        if temple_name == "Fire Temple" or temple_name == "Wind Temple":
            total_locks = 5  # Assuming there are 5 locks per temple, adjust if needed
        else:
            total_locks = 4
        temple_boss = temple[7]
        progress_percentage = calculate_progress_percentage(completed_locks, total_locks)
        print("Calculated Progress Percentage")
        progress_data.append({"temple_id": temple_id, "temple_name": temple_name, "progress_percentage": progress_percentage, "temple_name": temple_name, "locks": locks, "completed_locks": completed_locks, "temple_boss": temple_boss})
    print("Progress_Data:", progress_data)


    return render_template("index.html", headline=headline, percentages=percentages, progress_data=progress_data, temples_data=temples_data)

@app.route('/update_lock_status', methods=['POST'])
def update_lock_status():
    try:
        # Get data from the request
        data = request.get_json()
        temple_name = data.get('temple_name')
        temple_id = data.get('temple_id')
        lock_index = data.get('lock_index')
        status = data.get('status')
        print("Data from JS:", data)

        # Update the lock status in the database
        with closing(conn.cursor()) as c:

        # Assuming your Temples table has the columns temple_id, temple_lock1, temple_lock2, ..., temple_lock5
            lock_column = f'temple_lock{lock_index}'
            print("within lock update - lock_column:", lock_column)
            c.execute(f"UPDATE Temples SET {lock_column} = ? WHERE temple_id = ?", (status, temple_id))
            conn.commit()
            print("Executed update statement for", temple_name)
            print("Status:", status)
            print("Temple_ID:", temple_id)


        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route("/locationnav")
def locationnav():
    headline = "Locations!"
    percentages = get_percentages()
    return render_template("locationnav.html", headline=headline, percentages=percentages)

@app.route("/caves", methods=["GET", "POST"])
def caves():
    headline = "Caves"
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
    return render_template("caves.html", scroll_position=scroll_position, headline=headline, percentages=percentages, results=results, regions=regions, region_status=region_status, total_caves=total_caves)

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
            print("Buff:", buff)
            update_weapons_table(weapon_name, chest_region, damage_number, buff)

        else:
            print("Invalid chest item format.")

        chest_location = request.form['chest_location']
        chest_sideq = request.form['chest_sideq']
        if chest_sideq == None or chest_sideq == "":
            chest_sideq = "X"
        chest_region = request.form['chest_region']
        chest_done = request.form.get(f'chest_done')
        chest_map = request.form['chest_map']

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
    if scroll_position is not None:
        scroll_position = int(scroll_position)

    if request.method == 'POST':
        armor_id = request.form['armorId']
        armor_helm_found = request.form.get(f'have_{armor_id}_helm')
        armor_chest_found = request.form.get(f'have_{armor_id}_chest')
        armor_pants_found = request.form.get(f'have_{armor_id}_pants')

        with closing(conn.cursor()) as c:
            c.execute('UPDATE armor SET a_collected = ? WHERE a_id = ?', (armor_helm_found, armor_id))

        conn.commit()

    # Retrieve all armors from the database
    with closing(conn.cursor()) as c:
        c.execute('SELECT * FROM armor ORDER BY a_set ASC')
        armors = c.fetchall()

    return render_template('armors.html', headline=headline, percentages=percentages, armors=armors, scroll_position=scroll_position)

@app.route('/armors/update', methods=['POST'])
def update_armor():
    data = request.get_json()
    for d in data:
        print("D ! ->:", d)
    armor_id = data['armorId']
    armor_found = data['armorFound']
    print("armor_id:", armor_id)
    print("armor_found:", armor_found)

    with closing(conn.cursor()) as c:
        c.execute('UPDATE armor SET a_collected = ? WHERE a_id = ?', (armor_found, armor_id))
        print("Executed armor update, collected, id: ", armor_found, armor_id)
        conn.commit()

    return jsonify(success=True)

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

@app.route('/koroks', methods=['GET', 'POST'])
def koroks():
    headline = "Koroks"
    percentages = get_percentages()
    scroll_position = session.get('scrollPosition')
    if scroll_position is not None:
        scroll_position = int(scroll_position) 

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
        print("result[1]:", koroks[0][1])
        print("korok id:", koroks[0][0])

    return render_template('koroks.html', headline=headline, percentages=percentages, koroks=koroks, scroll_position=scroll_position)

@app.route('/update-korok', methods=['POST'])
def update_korok():
    korok_id = request.json.get('korok_id')
    korok_done = request.json.get('korok_done')
    print("Data received from client:", korok_id, korok_done)  # Add this line for debugging

    if korok_done is None:
        korok_done = 0
    else:
        korok_done = korok_done

    print("Korok_done after if/else:", korok_done)

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

    if request.method == 'POST':
        with closing(conn.cursor()) as c:
            roots = c.execute('SELECT root_name FROM lightroots ORDER BY root_name ASC').fetchall()
            for root in roots:
                root_name = root[0]
                root_done = request.form.get(f'done_root_{root_name}')
                if root_done is None:
                    print("root_done is none:", root_done)
                    root_done = c.execute('SELECT root_done FROM lightroots WHERE root_name = ?', (root_name,)).fetchone()[0]
                else:
                    print("root_done is not none:", root_done)
                print("root_name:", root_name)
                print("root_done:", root_done)
                c.execute('UPDATE lightroots SET root_done = ? WHERE root_name = ?', (root_done, root_name))
                print("Executed update statement for root_name:", root_name)
            conn.commit()

    with closing(conn.cursor()) as c:
        query = '''SELECT * FROM lightroots ORDER BY root_name ASC'''
        c.execute(query)
        results = c.fetchall()
        info = [(result[0], result[1], result[2]) for result in results]
    return render_template("lightroots.html", scroll_position=scroll_position, headline=headline, percentages=percentages, info=info, results=results)

@app.route("/compendium", methods=["GET", "POST"])
def compendium():
    headline = "Compendium"
    percentages = get_percentages()
    scroll_position = session.get('scrollPosition')
    if scroll_position is not None:
        scroll_position = int(scroll_position)

    if request.method == 'POST':
        with closing(conn.cursor()) as c:
            comps = c.execute('SELECT comp_id FROM compendium ORDER BY comp_id ASC').fetchall()
            for comp in comps:
                comp_id = comp[0]
                comp_done = request.form.get(f'done_comp_{comp_id}')
                if comp_done is None:
                    comp_done = 0
                else:
                    comp_done = 1
                print("comp_id:", comp_id)
                print("comp_done:", comp_done)
                c.execute('UPDATE compendium SET comp_done = ? WHERE comp_id = ?', (comp_done, comp_id))
                print("Executed update statement for comp_id:", comp_id)
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
    return render_template("compendium.html", scroll_position=scroll_position, headline=headline, percentages=percentages, results=results, creatures=creatures, monsters=monsters, materials=materials, equipment=equipment, treasures=treasures)

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

@app.route("/shrinequests")
def shrinequests():
    headline = "Shrine Quests"
    percentages = get_percentages()
    with closing(conn.cursor()) as c:
        query = '''Select * From shrinequests ORDER BY map_name ASC'''
        c.execute(query)
        results = c.fetchall()
        info = []
        for result in results:
            info.append(result)
    return render_template("shrinequests.html", headline=headline, percentages=percentages, info=info, results = results)

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

    if request.method == 'POST':
        with closing(conn.cursor()) as c:
            side_ids = c.execute('SELECT side_id FROM sidequests').fetchall()
            for side_id in side_ids:
                side_id = side_id[0]
                side_done = request.form.get(f'done_sidequ_{side_id}')
                if side_done is None:
                    side_done = c.execute('SELECT side_done FROM sidequests WHERE side_id = ?', (side_id,)).fetchone()[0]
                else:
                    print("side_done is not none:", side_done)
                c.execute('UPDATE sidequests SET side_done = ? WHERE side_id = ?', (side_done, side_id))
            conn.commit()

    with closing(conn.cursor()) as c:
        query = '''SELECT * FROM sidequests ORDER BY side_id ASC'''
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
        total_sidequests = len([result for result in results if result[4] == region])
        completed = len([result for result in results if result[4] == region and result[0] == 2])
        started = len([result for result in results if result[4] == region and result[0] == 1])
        unfound = len([result for result in results if result[4] == region and result[0] == 0])

        region_status[region] = {
            'completed': completed,
            'started': started,
            'unfound': unfound,
            'total_sidequests': total_sidequests
        }

    return render_template("sidequests.html", scroll_position=scroll_position, headline=headline, percentages=percentages, info=info, results=results, regions=regions, region_status=region_status)

@app.route("/adventures", methods=['GET', 'POST'])
def adventures():
    headline = "Side Adventures"
    percentages = get_percentages()
    with closing(conn.cursor()) as c:
        query = '''Select * From adventure ORDER BY adventure_name ASC'''
        c.execute(query)
        results = c.fetchall()
        info = []
        for result in results:
            info.append(result)
    return render_template("adventures.html", headline=headline, percentages=percentages, info=info, results = results)


@app.route("/mainqu", methods=["GET", "POST"])
def mainqu():
    headline = "Main Quests"
    percentages = get_percentages()
    scroll_position = session.get('scrollPosition')
    if scroll_position is not None:
        scroll_position = int(scroll_position)

    if request.method == 'POST':
        with closing(conn.cursor()) as c:
            mainqus = c.execute('SELECT mainqu_id FROM mainqu').fetchall()
            for mainqu in mainqus:
                mainqu_id = mainqu[0]
                mainqu_done = request.form.get(f'done_mainqu_{mainqu_id}')
                if mainqu_done is None:
                    print("mainqu_done is none:", mainqu_done)
                    mainqu_done = c.execute('SELECT mainqu_done FROM mainqu WHERE mainqu_id = ?', (mainqu_id,)).fetchone()[0]
                else:
                    print("mainqu_done is not none:", mainqu_done)
                print("mainqu_id:", mainqu_id)
                print("mainqu_done:", mainqu_done)
                c.execute('UPDATE mainqu SET mainqu_done = ? WHERE mainqu_id = ?', (mainqu_done, mainqu_id))
                print("Executed update statement for mainqu_id:", mainqu_id)
            conn.commit()

    with closing(conn.cursor()) as c:
        query = '''SELECT * FROM mainqu ORDER BY mainqu_id ASC'''
        c.execute(query)
        results = c.fetchall()
        info = [(result[0], result[1], result[2]) for result in results]
    return render_template("mainqu.html", scroll_position=scroll_position, headline=headline, percentages=percentages, info=info, results=results)

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
            great_fairy_fountains = c.execute('SELECT * FROM locations WHERE location_type = "Great Fairy Fountain" ORDER BY location_name ASC').fetchall()
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
                c.execute('UPDATE locations SET location_done = ? WHERE location_id = ?', (great_fairy_fountain_done, great_fairy_fountain_id))
                # print("Executed update statement for great_fairy_fountain_id:", great_fairy_fountain_id)
            conn.commit()

    with closing(conn.cursor()) as c:
        query = '''SELECT * FROM locations WHERE location_type = 'Great Fairy Fountain' ORDER BY location_name ASC'''
        c.execute(query)
        great_fairy_fountains = c.fetchall()
    return render_template("location-great_fairy_fountain.html", scroll_position=scroll_position, headline=headline, percentages=percentages, great_fairy_fountains=great_fairy_fountains)

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


if __name__ == "__main__":
    app.run(debug=True)
