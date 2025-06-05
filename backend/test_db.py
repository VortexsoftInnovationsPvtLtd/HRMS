import psycopg2

try:
    conn = psycopg2.connect(
        dbname="hrms",
        user="postgres",
        password="Ballod@123",
        host="localhost",
        port="5432"
    )
    print("✅ Database connection successful!")

    # Test if the database is empty or has tables
    cur = conn.cursor()
    cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
    tables = cur.fetchall()
    print(f"📊 Found {len(tables)} tables in database 'hrms'")
    if tables:
        print("Tables:", [table[0] for table in tables])

    conn.close()
except Exception as e:
    print("❌ Database connection failed:", e)
    print("\nTroubleshooting steps:")
    print("1. Make sure PostgreSQL is running (check in services)")
    print("2. Verify your credentials (username/password)")
    print("3. Check if database 'hrms' exists (run 'psql -U postgres -c \"\l\"' in cmd)")
    print("4. Check if PostgreSQL accepts connections (check pg_hba.conf)")