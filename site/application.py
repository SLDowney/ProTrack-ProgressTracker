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

@app.route("/")
def index():
    headline = "This is a Test!"
    with closing(conn.cursor()) as c:
        query = '''Select * From caves'''
        c.execute(query)
        items = c.fetchall()
        itemList = []
        for item in items:
            itemList.append(item)
    itemToShow = random.choice(itemList)
    return render_template("index.html", headline=headline, itemToShow=itemToShow)


@app.route("/caves", methods=["GET", "POST"])
def caves():
    headline = "Caves!!"
    scroll_position = session.get('scrollPosition')
    if scroll_position is not None:
        scroll_position = int(scroll_position)

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
        info = [(result[0], result[1], result[2]) for result in results]
    return render_template("caves.html", scroll_position=scroll_position, headline=headline, info=info, results=results)

@app.route('/chests', methods=['GET', 'POST'])
def chests():
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

    return render_template('chests.html', chests=chests, scroll_position=scroll_position)


@app.route("/additem", methods=["GET", "POST"])
def additem():
    headline = "Insert found chest into database:"
    if request.method == 'POST':
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
            chest_location = request.form['chest_location']
            chest_sideq = request.form['chest_sideq']
            chest_region = request.form['chest_region']
            chest_done = request.form.get(f'chest_done')
            print("Chest_Done:", chest_done) 
            if chest_done == None:
                chest_done = "0"
            else:
                chest_done = "1"       

            with closing(conn.cursor()) as c:
                query = '''INSERT INTO chests (chest_coord, chest_type, chest_item, chest_location, chest_region, chest_sideq, chest_done)
                            VALUES(?, ?, ?, ?, ?, ?, ?)'''
                c.execute(query, (formatted_chest_coord, chest_type, chest_item, chest_location, chest_region, chest_sideq, chest_done))
                conn.commit()
                query = '''SELECT * FROM chests ORDER BY chest_id DESC LIMIT 1'''
                c.execute(query)
                row = c.fetchone()

            # Access the values of the last row
            if row:
                # Retrieve the values from the row
                chest_item = row[1]
                chest_coord = row[2]
                chest_type = row[3]
                chest_location = row[4]
                chest_sideq = row[5]
                if chest_sideq == "":
                    tagline = chest_item + ", " + chest_coord + ", " + chest_type + ", " + chest_location
                    print("chest_sideq is empty string, confirmed:", chest_sideq)
                    return render_template("additem.html", tagline=tagline)
                else:
                    tagline = chest_item + ", " + chest_coord + ", " + chest_type + ", " + chest_location + ", " + chest_sideq
                    print("chest_sideq is not None:", chest_sideq)
                    return render_template("additem.html", tagline=tagline)
                    
                # ... access other columns as needed
            else:
                # Handle the case when no rows are found
                pass
        except sqlite3.OperationalError as e:
            print(e)
            headline = "Error in insert operation. Please try again."
    else:
        return render_template("additem.html", headline=headline)
    return render_template("additem.html", headline=headline)

@app.route('/camp_chest', methods=['GET', 'POST'])
def camp_chest():
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
                return render_template('camp_chest.html', camp_chests=camp_chests, scroll_position=scroll_position)

    # Retrieve all camp_chest from the database
    with closing(conn.cursor()) as c:
        c.execute('SELECT * FROM camp_chest')
        camp_chests = c.fetchall()

    return render_template('camp_chest.html', camp_chests=camp_chests, scroll_position=scroll_position)


@app.route("/add_camp_chest", methods=["GET", "POST"])
def add_camp_chest():
    headline = "Insert found camp_chest into database:"
    if request.method == 'POST':
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
            if camp_chest_found is None:
                    camp_chest_found = '0'

            with closing(conn.cursor()) as c:
                query = '''INSERT INTO camp_chest (camp_chest_coord, camp_chest_enemies, camp_chest_item, camp_chest_location, camp_chest_region, camp_chest_done)
                            VALUES(?, ?, ?, ?, ?, ?)'''
                c.execute(query, (formatted_camp_chest_coord, camp_chest_enemies, camp_chest_item, camp_chest_location, camp_chest_region, camp_chest_found))
                conn.commit()

        except sqlite3.OperationalError as e:
            print(e)
            headline = "Error in insert operation. Please try again."
    else:
        return render_template("add_camp_chest.html", headline=headline)
     # Retrieve all camp_chest from the database
    with closing(conn.cursor()) as c:
        c.execute('SELECT * FROM camp_chest')
        camp_chests = c.fetchall()
    return render_template("add_camp_chest.html", camp_chests=camp_chests)


@app.route("/edititem", methods=["POST", "GET"])
def edititem():
    headline = "Edit a chest:"
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
                tagline = "Successfully added Item to Collection!!"
                return render_template("success.html", tagline=tagline)
        except sqlite3.OperationalError as e:
            print(e)
            headline = "Error in insert operation. Please try again."
    else:
        return render_template("edititem.html", headline=headline)

@app.route('/armors', methods=['GET', 'POST'])
def armors():
    scroll_position = session.get('scrollPosition')
    if scroll_position is not None:
        scroll_position = int(scroll_position)

    if request.method == 'POST':
        armor_id = request.form['armorId']
        armor_helm_found = request.form.get(f'have_{armor_id}_helm', '0')
        armor_chest_found = request.form.get(f'have_{armor_id}_chest', '0')
        armor_pants_found = request.form.get(f'have_{armor_id}_pants', '0')

        with closing(conn.cursor()) as c:
            c.execute('UPDATE armor_set SET a_helm = ? WHERE a_id = ?', (armor_helm_found, armor_id))
            c.execute('UPDATE armor_set SET a_chest = ? WHERE a_id = ?', (armor_chest_found, armor_id))
            c.execute('UPDATE armor_set SET a_pants = ? WHERE a_id = ?', (armor_pants_found, armor_id))

        conn.commit()

    # Retrieve all armors from the database
    with closing(conn.cursor()) as c:
        c.execute('SELECT * FROM armor_set ORDER BY a_set ASC')
        armors = c.fetchall()

    return render_template('armors.html', armors=armors, scroll_position=scroll_position)

@app.route('/armors/update', methods=['POST'])
def update_armor():
    data = request.get_json()
    for d in data:
        print("D !!! ->:", d)
    armor_id = data['armorId']
    armor_found = data['armorFound']
    print("armor_id:", armor_id)
    print("armor_found:", armor_found)

    with closing(conn.cursor()) as c:
        c.execute('UPDATE armor_set SET a_collected = ? WHERE a_id = ?', (armor_found, armor_id))
        print("Executed armor_set update, collected, id: ", armor_found, armor_id)
        conn.commit()

    return jsonify(success=True)

@app.route("/shrines", methods=["GET", "POST"])
def shrines():
    headline = "Shrines!!"
    scroll_position = session.get('scrollPosition')
    if scroll_position is not None:
        scroll_position = int(scroll_position)

    if request.method == 'POST':
        with closing(conn.cursor()) as c:
            shrine_shrines = c.execute('SELECT shrine_shrine FROM shrines').fetchall()
            for shrine_shrine in shrine_shrines:
                shrine_shrine = shrine_shrine[0]
                shrine_done = request.form.get(f'done_shrine_{shrine_shrine}')
                if shrine_done is None:
                    print("shrine_done is none:", shrine_done)
                    shrine_done = c.execute('SELECT shrine_done FROM shrines WHERE shrine_shrine = ?', (shrine_shrine,)).fetchone()[0]
                else:
                    print("shrine_done is not none:", shrine_done)
                print("shrine_shrine:", shrine_shrine)
                print("shrine_done:", shrine_done)
                c.execute('UPDATE shrines SET shrine_done = ? WHERE shrine_shrine = ?', (shrine_done, shrine_shrine))
                print("Executed update statement for shrine_shrine:", shrine_shrine)
            conn.commit()

    with closing(conn.cursor()) as c:
        query = '''SELECT * FROM shrines ORDER BY shrine_shrine ASC'''
        c.execute(query)
        results = c.fetchall()
        info = [(result[0], result[1], result[2]) for result in results]
    return render_template("shrines.html", scroll_position=scroll_position, headline=headline, info=info, results=results)

@app.route('/koroks', methods=['GET', 'POST'])
def koroks():
    scroll_position = session.get('scrollPosition')
    if scroll_position is not None:
        scroll_position = int(scroll_position) 

    if request.method == 'POST':
        with closing(conn.cursor()) as c:
            koroks = c.execute('SELECT * FROM koroks').fetchall()
            for korok in koroks:
                korok_id = korok[0]
                korok_found = request.form.get(f'korok_found_{korok_id}')
                if korok_found is None:
                    korok_found = '0'
                else:
                    korok_found = '1'
                print("korok_id:", korok_id)
                print("korok_found:", korok_found)
                c.execute('UPDATE koroks SET korok_found = ? WHERE korok_id = ?', (korok_found, korok_id))
                print("Executed update statement for korok ID:", korok_id)
            conn.commit()

    # Retrieve all koroks from the database
    with closing(conn.cursor()) as c:
        c.execute('SELECT * FROM koroks')
        koroks = c.fetchall()
        print("result[1]:", koroks[0][1])
        print("korok id:", koroks[0][0])

    return render_template('koroks.html', koroks=koroks, scroll_position=scroll_position)

@app.route('/update-korok', methods=['POST'])
def update_korok():
    korok_id = request.json.get('korok_id')
    korok_found = request.json.get('korok_found')

    # Update the korok in the database with the new found status
    with closing(conn.cursor()) as c:
        c.execute('UPDATE koroks SET korok_found = ? WHERE korok_id = ?', (korok_found, korok_id))
        conn.commit()

    return jsonify(success=True)

@app.route('/add_korok', methods=['POST'])
def add_korok():
    location = request.form.get('location')
    kType = request.form.get('kType')
    coord_start = request.form.get('coord_start')
    # Remove spaces and commas from the input
    coord_start = coord_start.replace(' ', '').replace(',', '')

    # Format the chest_coord with commas while maintaining negative signs
    formatted_coord_start = ''
    i = 0
    while i < len(coord_start):
        section = coord_start[i:i+4]
        if section.startswith('-'):
            section = coord_start[i:i+5]
            formatted_coord_start += section + ', '
            i += 5
        else:
            formatted_coord_start += section[:4] + ', '
            i += 4
    formatted_coord_start = formatted_coord_start.rstrip(', ')
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
    korok_found = request.form.get('korok_found')

    # Insert the new korok into the database
    with closing(conn.cursor()) as c:
        c.execute('INSERT INTO koroks (korok_found, korok_location, korok_type, korok_coord_start, korok_coord_end, korok_desc) VALUES (?, ?, ?, ?, ?, ?)',
                  (korok_found, location, kType, formatted_coord_start, formatted_coord_end, description))
        conn.commit()

    # Redirect back to the koroks page after adding the korok
    return redirect('/koroks')

@app.route('/enemies', methods=['GET', 'POST'])
def enemies():
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

    return render_template('enemies.html', enemies=enemies, scroll_position=scroll_position)

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
    headline = "Lightroots!!"
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
    return render_template("lightroots.html", scroll_position=scroll_position, headline=headline, info=info, results=results)

@app.route("/compendium", methods=["GET", "POST"])
def compendium():
    headline = "compendium!!"
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
                    print("comp_done is none:", comp_done)
                    comp_done = c.execute('SELECT comp_done FROM compendium WHERE comp_id = ?', (comp_id,)).fetchone()[0]
                else:
                    print("comp_done is not none:", comp_done)
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
    return render_template("compendium.html", scroll_position=scroll_position, headline=headline, results=results, creatures=creatures, monsters=monsters, materials=materials, equipment=equipment, treasures=treasures)

@app.route('/interesting', methods=['GET', 'POST'])
def interesting():
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

    return render_template('interesting.html', interesting=interesting, scroll_position=scroll_position)

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

@app.route("/oldmaps")
def oldmaps():
    headline = "Old Maps!!"
    with closing(conn.cursor()) as c:
        query = '''Select * From oldmaps ORDER BY map_name ASC'''
        c.execute(query)
        results = c.fetchall()
        info = []
        for result in results:
            info.append(result)
    return render_template("oldmaps.html", headline=headline, info=info, results = results)

@app.route("/shrinequests")
def shrinequests():
    headline = "Shrine Quests!!"
    with closing(conn.cursor()) as c:
        query = '''Select * From shrinequests ORDER BY map_name ASC'''
        c.execute(query)
        results = c.fetchall()
        info = []
        for result in results:
            info.append(result)
    return render_template("shrinequests.html", headline=headline, info=info, results = results)

@app.route("/sidequests")
def sidequests():
    headline = "Side Quests!!"
    with closing(conn.cursor()) as c:
        query = '''Select * From sidequests ORDER BY side_quest ASC'''
        c.execute(query)
        results = c.fetchall()
        info = []
        for result in results:
            info.append(result)
    return render_template("sidequests.html", headline=headline, info=info, results = results)


if __name__ == "__main__":
    app.run(debug=True)
