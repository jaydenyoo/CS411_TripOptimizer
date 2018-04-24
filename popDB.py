from dummy import *

print('-' * 20)
conn, cur = connect()

# createUserDummy(cur, conn)
createPlaceDummy(cur, conn)
# createTripDummy(cur, conn)
# createContainDummy(cur, conn)
conn.commit()
cur.close()
conn.close()

print('-' * 20)
