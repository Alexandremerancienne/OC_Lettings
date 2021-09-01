import sqlite3

conn = sqlite3.connect('oc-lettings-site.sqlite3')
c = conn.cursor()
c.execute("INSERT INTO profiles_profile SELECT * from oc_lettings_site_profile")
conn.commit()
conn.close()

