import sqlite3

conn = sqlite3.connect('oc-lettings-site.sqlite3')
c = conn.cursor()
c.execute("INSERT INTO lettings_letting SELECT * from oc_lettings_site_letting")
c.execute("INSERT INTO lettings_address SELECT * from oc_lettings_site_address")
conn.commit()
conn.close()
