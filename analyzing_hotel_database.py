import sqlite3

con = sqlite3.connect('hotel_booking.db')
cur = con.cursor()
first_row = cur.execute('''SELECT * FROM booking_summary''').fetchone()

first_ten_row = cur.execute('''SELECT * FROM booking_summary''').fetchmany(10) #GETTING THE FIRST 10 CUSTOMER

bra = cur.execute('''SELECT * FROM booking_summary WHERE country = 'BRA';''').fetchall() #GETTING BRAZILIAN CUSTOMERS
print(bra)


cur.execute('''CREATE TABLE IF NOT EXISTS bra_customers (
                num INTEGER,
                hotel TEXT,
                is_cancelled INTEGER,
                lead_time INTEGER,
                arrival_date_year INTEGER,
                arrival_date_month INTEGER,
                arrival_date_day_of_month INTEGER,
                adults INTEGER,
                children INTEGER,
                country TEXT,
                adr REAL,
                special_requests INTEGER)''')

cur.executemany('''INSERT INTO bra_customers VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''', bra) #ADDED ALL OF THE BRA CUSTOMERS DATA INTO A NEW TABLE, CALLED BRA_CUSTOMERS, WE CREATED ABOVE.
                                                                                       #REALIZE THE .EXECUTEMANY() METHOD.
first_ten = cur.execute('''SELECT * FROM bra_customers''').fetchmany(10) #THIS SELECTS FROM BRA_CUSTOMERS WHERE ALL CUSTOMERS FROM "BRA" SO NO NEED TO SPECIFY WITH "WHERE COUNTRY = "BRA"".
print(first_ten)

all_bra = cur.execute('''SELECT * FROM bra_customers''').fetchall()

lead_time_can = cur.execute('''SELECT lead_time FROM bra_customers WHERE is_cancelled = 1;''').fetchall() 

total = 0
for i in lead_time_can:
  total += i[0]
  average = total/len(lead_time_can)



lead_time_not_can = cur.execute('''SELECT lead_time FROM bra_customers WHERE is_cancelled = 0;''').fetchall()

not_can_total = 0
for i in lead_time_not_can:
  not_can_total += i[0]
  average_not_can = not_can_total/len(lead_time_not_can)




spec_requests = cur.execute('''SELECT special_requests FROM bra_customers WHERE is_cancelled = 1;''').fetchall()


total_spec_req = 0
for i in spec_requests:
  total_spec_req += i[0]
print(total_spec_req)

spec_requests_not_can = cur.execute('''SELECT special_requests FROM bra_customers WHERE is_cancelled = 0;''').fetchall()
total_spec_req_not_can = 0
for i in spec_requests_not_can:
  total_spec_req_not_can += i[0]

print(total_spec_req_not_can)

con.commit()
con.close()


