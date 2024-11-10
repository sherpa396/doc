# scheduler.py

import pandas as pd
from datetime import datetime, timedelta
from collections import deque

class AppointmentState:
    NEW = 'new'
    WAITING = 'waiting'
    RUNNING = 'running'
    EXIT = 'exit'

class FCFSQueueScheduler:
    def __init__(self):
        self.appointment_queue = deque()
        self.appointments_df = pd.DataFrame(columns=[
            'appointment_id',
            'arrival_timestamp',
            'doctor_id',
            'patient_name',
            'email',
            'phone',
            'appointment_date',
            'appointment_time',
            'state',
            'queue_position'
        ])
        self.working_hours = {
            'start_time': '09:00',
            'end_time': '17:00',
            'slot_duration': 30  # minutes
        }
    
    def add_to_queue(self, appointment_data):
        appointment_id = len(self.appointments_df) + 1000
        arrival_time = datetime.now()
        
        new_appointment = {
            'appointment_id': appointment_id,
            'arrival_timestamp': arrival_time,
            'doctor_id': appointment_data['doctor_id'],
            'patient_name': appointment_data['patient_name'],
            'email': appointment_data['email'],
            'phone': appointment_data['phone'],
            'appointment_date': appointment_data['preferred_date'],
            'appointment_time': None,
            'state': AppointmentState.NEW,
            'queue_position': len(self.appointment_queue)
        }
        
        self.appointment_queue.append(new_appointment)
        
        self.appointments_df = pd.concat([
            self.appointments_df,
            pd.DataFrame([new_appointment])
        ], ignore_index=True)
        
        return appointment_id
    
    def generate_time_slots(self, date):
        start = pd.Timestamp(f"{date} {self.working_hours['start_time']}")
        end = pd.Timestamp(f"{date} {self.working_hours['end_time']}")
        
        slots = pd.date_range(
            start=start,
            end=end,
            freq=f"{self.working_hours['slot_duration']}T"
        ).strftime('%H:%M').tolist()
        
        return slots[:-1]
    
    def get_available_slots(self, doctor_id, date):
        all_slots = self.generate_time_slots(date)
        
        booked_slots = self.appointments_df[
            (self.appointments_df['doctor_id'] == doctor_id) &
            (self.appointments_df['appointment_date'] == date) &
            (self.appointments_df['state'].isin([AppointmentState.RUNNING, AppointmentState.EXIT]))
        ]['appointment_time'].tolist()
        
        return [slot for slot in all_slots if slot not in booked_slots]
    
    def process_queue(self):
        processed_appointments = []
        
        while self.appointment_queue:
            appointment = self.appointment_queue.popleft()
            appointment_id = appointment['appointment_id']
            
            self.appointments_df.loc[
                self.appointments_df['appointment_id'] == appointment_id,
                'state'
            ] = AppointmentState.WAITING
            
            available_slots = self.get_available_slots(
                appointment['doctor_id'],
                appointment['appointment_date']
            )
            
            if not available_slots:
                next_date = (
                    datetime.strptime(appointment['appointment_date'], '%Y-%m-%d') +
                    timedelta(days=1)
                ).strftime('%Y-%m-%d')
                
                appointment['appointment_date'] = next_date
                self.appointment_queue.append(appointment)
                continue
            
            assigned_time = available_slots[0]
            
            self.appointments_df.loc[
                self.appointments_df['appointment_id'] == appointment_id,
                ['appointment_time', 'state']
            ] = [assigned_time, AppointmentState.RUNNING]
            
            self.appointments_df.loc[
                self.appointments_df['appointment_id'] == appointment_id,
                'state'
            ] = AppointmentState.EXIT
            
            processed_appointments.append({
                'appointment_id': appointment_id,
                'date': appointment['appointment_date'],
                'time': assigned_time
            })
        
        return processed_appointments
