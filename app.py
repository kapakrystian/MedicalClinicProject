# importy
from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2
import psycopg2.extras


app = Flask(__name__)
app.secret_key = "medicalClinicApplication"

# baza danych
DB_HOST = 'localhost'
DB_NAME = 'medical clinic'
DB_USER = 'postgres'
DB_PASS = '1234'

# połączenie z bazą danych
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASS, host=DB_HOST)


# route strony głównej i pobranie wybranych danych z bazy danych
@app.route('/')
def Index():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    query = ''' SELECT patient.patient_id, patient.name, patient.address, patient.phone, medicines.name, stay.start_time, room.number, doctor.name, nurse.name
                FROM patient
                INNER JOIN medicines ON patient.medicines_id = medicines.medicines_id
                INNER JOIN doctor ON patient.doctor_id = doctor.doctor_id
                INNER JOIN nurse ON patient.nurse_id = nurse.nurse_id
                INNER JOIN stay ON patient.stay_id = stay.stay_id
                INNER JOIN room ON patient.room_id = room.room_id
                ORDER BY patient_id
                ASC
            '''
    cur.execute(query)
    list_patients = cur.fetchall()
    return render_template('index.html', list_patients=list_patients)


# route dodawania nowego pacjenta do bazy danych
@app.route('/add_patient', methods=['POST'])
def add_patient():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        patientId = request.form['patientId']
        patientName = request.form['patientName']
        patientAddress = request.form['patientAddress']
        patientPhone = request.form['patientPhone']
        mediciniesID = request.form['mediciniesID']
        stayID = request.form['stayID']
        roomID = request.form['roomID']
        doctorID = request.form['doctorID']
        nurseID = request.form['nurseID']
        query = "INSERT INTO patient (patient_id, name, address, phone, medicines_id, stay_id, room_id, doctor_id, nurse_id) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (patientId, patientName, patientAddress, patientPhone,
                  mediciniesID, stayID, roomID, doctorID, nurseID)
        cur.execute(query, values)
        conn.commit()
        flash('Patient Added Successfully')
        return redirect(url_for('Index'))


# route edycji pacjenta, pobrania danych o pacjencie z danym ID
@app.route('/edit/<id>', methods=['POST', 'GET'])
def get_patient(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cur.execute('SELECT * FROM patient WHERE patient_id = %s', (id,))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit.html', patient=data[0])


# route edycji danych pacjenta i zapisania ich w bazie
@app.route('/update/<id>', methods=['POST'])
def update_patient(id):
    patientID = id
    if request.method == 'POST':
        patientName = request.form['patientName']
        patientAddress = request.form['patientAddress']
        patientPhone = request.form['patientPhone']
        medicinesID = request.form['medicinesID']
        stayID = request.form['stayID']
        roomID = request.form['roomID']
        doctorID = request.form['doctorID']
        nurseID = request.form['nurseID']

        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            UPDATE patient
            SET name = %s,
                address = %s,
                phone = %s,
                medicines_id = %s,
                stay_id = %s,
                room_id = %s,
                doctor_id = %s,
                nurse_id = %s
            WHERE patient_id = %s
        """, (patientName, patientAddress, patientPhone, medicinesID, stayID, roomID, doctorID, nurseID, patientID))
        flash('Patient Updated Successfully')
        conn.commit()
    return redirect(url_for('Index'))


# route usuwania pacjenta
@app.route('/delete/<string:id>', methods=['POST', 'GET'])
def delete_patient(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cur.execute('DELETE FROM patient WHERE patient_id = {0}'.format(id))
    conn.commit()
    flash('Patient Removed Successfully')
    return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(debug=True)
