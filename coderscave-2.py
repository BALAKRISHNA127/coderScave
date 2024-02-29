''' Develop a system for scheduling medical appointments, sending reminders, and maintaining patient records.
This project aims to create a user-friendly system for healthcare providers and patients to manage medical
appointments efficiently. Your role involves working on both frontend and backend aspects, integrating 
essential features, and ensuring compliance with healthcare data protection regulations.'''

import datetime

class Appointment:
    def __init__(self, patient_name, doctor_name, date, time):
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.date = date
        self.time = time

class AppointmentScheduler:
    def __init__(self):
        self.appointments = []

    def schedule_appointment(self, patient_name, doctor_name, year, month, day, hour, minute):
        appointment_date = datetime.date(year, month, day)
        appointment_time = datetime.time(hour, minute)
        appointment = Appointment(patient_name, doctor_name, appointment_date, appointment_time)
        self.appointments.append(appointment)

    def send_reminders(self):
        current_time = datetime.datetime.now().time()
        for appointment in self.appointments:
            if appointment.date == datetime.date.today() and appointment.time.hour - current_time.hour <= 1:  
                print(f"Reminder: Appointment with {appointment.doctor_name} scheduled on {appointment.date} at {appointment.time} AM")

    def display_all_appointments(self):
        for i, appointment in enumerate(self.appointments, 1):
            print(f"{i}. Patient name: {appointment.patient_name},\n Doctor: {appointment.doctor_name},\n Date: {appointment.date},\n Time: {appointment.time}")

def main():
    scheduler = AppointmentScheduler()

    scheduler.schedule_appointment("John Doe", "Dr. Smith", 2024, 2, 26, 10, 30)
    scheduler.schedule_appointment("Jane Doe", "Dr. Johnson", 2024, 2, 29, 14, 0)
    scheduler.schedule_appointment("Jane Doe", "Dr. Jemmy", 2024, 3, 1, 1, 30)
  
    scheduler.display_all_appointments()
    scheduler.send_reminders()

if __name__ == "__main__":
    main()

