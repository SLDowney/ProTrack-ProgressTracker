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


@app.route("/caves")
def caves():
    headline = "Caves!!"
    with closing(conn.cursor()) as c:
        query = '''Select * From caves ORDER BY cave_name ASC'''
        c.execute(query)
        # C_names = c.name
        # C_coord = c.coord
        # C_region = c.region
        # C_Bub = c.bubbulfrog
        # C_shrine = c.shrine
        # C_enemies = c.enemies
        # C_tres = c.treasure
        # C_sidequ = c.sidequ
        # C_shrinequ = c.shrinequ
        results = c.fetchall()
        info = []
        for result in results:
            info.append(result)
    return render_template("caves.html", headline=headline, info=info, results = results)

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
            chest_done = 1            

            with closing(conn.cursor()) as c:
                query = '''INSERT INTO chests (chest_coord, chest_type, chest_item, chest_location, chest_sideq, chest_done)
                            VALUES(?, ?, ?, ?, ?, ?)'''
                c.execute(query, (formatted_chest_coord, chest_type, chest_item, chest_location, chest_sideq, chest_done))
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

@app.route("/armors", methods=["GET", "POST"])
def armors():
    headline = "Armors!!"
    with closing(conn.cursor()) as c:
        query = '''Select * From armor ORDER BY a_set ASC'''
        c.execute(query)
        results = c.fetchall()
        info = []
        for result in results:
            info.append(result)
    if request.method == 'POST':
        try:
            armor_check = request.form.get("found_armor", False)
            with closing(conn.cursor()) as c:
                query = '''UPDATE armor
                            SET a_collected = ?
                            WHERE a_id = ? '''
                c.execute(query, (armor_check, result[0]))
                conn.commit()
                return render_template("armors.html", headline=headline, info=info, results = results)
        except sqlite3.OperationalError as e:
            print(e)
            headline = "Error in insert operation. Please try again."
    else:
        return render_template("armors.html", headline=headline, info=info, results = results)

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
        print("result[6]:", koroks[0][6])
        print("korok id:", koroks[0][0])

    return render_template('koroks.html', koroks=koroks, scroll_position=scroll_position)

@app.route('/update-korok', methods=['POST'])
def update_korok():
    korok_id = request.json.get('korokId')
    korok_found = request.json.get('korokFound')

    # Update the korok in the database with the new found status
    with closing(conn.cursor()) as c:
        c.execute('UPDATE koroks SET korok_found = ? WHERE korok_id = ?', (korok_found, korok_id))
        conn.commit()

    return jsonify(success=True)


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
