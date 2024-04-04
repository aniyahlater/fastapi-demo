@app.get("/albums")
def get_albums():
    db = MySQLdb.connect(host=DBHOST, user=DBUSER, passwd=DBPASS, db=DB)
    c = db.cursor(MySQLdb.cursors.DictCursor)
    c.execute("""SELECT * FROM albums ORDER BY name""")
    results = c.fetchall()
return results