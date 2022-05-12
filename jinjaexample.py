import jinja2
import psycopg2

conn = psycopg2.connect("dbname=postgres user=postgres host=0.0.0.0 password=postgres")
cur = conn.cursor()

with open('sql/test.sql.j2') as f:
    sql = f.read()

parse = jinja2.Template(sql)
rendered = parse.render({"mes":1,"dia":2, "columnas":["month", "year","day"]})
#print(rendered)
cur.execute(rendered)

print(cur.fetchone())
