import pandas as pd
import random
import numpy as np
from faker import Faker
from datetime import datetime, timedelta

# --- INITIALIZATION ---
fake = Faker()
Faker.seed(42)
random.seed(42)
np.random.seed(42)

# --- DATASET SETTINGS ---
num_records = 12567
match_date_base = datetime(2024, 5, 4, 14, 0, 0) # Start at 2:00 PM

# --- EVENT TIMELINE ---
early_arrival_start = match_date_base # 2:00 PM
early_arrival_end = match_date_base + timedelta(hours=2) # 4:00 PM

peak_arrival_start = early_arrival_end # 4:00 PM
peak_arrival_end = peak_arrival_start + timedelta(hours=2) # 6:00 PM

incident_window_start = peak_arrival_end # 6:00 PM
incident_window_end = incident_window_start + timedelta(minutes=45) # 6:45 PM

post_incident_start = incident_window_end # 6:45 PM
post_incident_end = post_incident_start + timedelta(hours=2, minutes=15) # 9:00 PM

# --- CATEGORICAL DATA DEFINITIONS ---
gates = [f"Gate {i}" for i in range(1, 14)]
high_risk_gates = ['Gate 4', 'Gate 6', 'Gate 7']

ticket_statuses = ['Valid', 'Invalid']
incident_types = ['None', 'Scuffle', 'Panic', 'Stampede', 'Faint', 'Medical Emergency']
injury_severity_levels = ['None', 'Minor', 'Major', 'Fatal']
crowd_controls = ['Barricades', 'Rope Lines', 'Police Cordon', 'None']
death_causes = ["Compressive Asphyxiation", "Traumatic Asphyxiation", "Crush Injuries", "Head Trauma"]

first_responder_types = ['Stadium Security', 'Police', 'Paramedic', 'Bystander', 'None']
exit_gate_statuses = ['Clear', 'Partially Blocked', 'Completely Blocked', 'N/A']
communication_methods = ['Official Announcement', 'Social Media', 'Word of Mouth', 'Police Instructions', 'None']

# --- GEOGRAPHICAL & BEHAVIORAL DATA ---
location_choices = [
    'At Gate Entrance', 'Main Queue Line', 'Ticket Redemption Counter', 'Anil Kumble Circle',
    'Cubbon Road (Stadium Side)', "Queen's Road (Towards Gate 1)", 'Inside Cubbon Park (Near Stadium)',
    "St. Mark's Road (Food Stalls)", 'Cubbon Park Metro Station Exit', 'Official Parking Area',
    'Inside Police Cordon', 'Watching from Home'
]
location_weights = [0.20, 0.20, 0.05, 0.07, 0.10, 0.05, 0.05, 0.03, 0.08, 0.05, 0.02, 0.10]

location_coords = {
    'At Gate Entrance': (12.9787, 77.5998),
    'Main Queue Line': (12.9791, 77.6005),
    'Ticket Redemption Counter': (12.9783, 77.5989),
    'Anil Kumble Circle': (12.9778, 77.6015),
    'Cubbon Road (Stadium Side)': (12.9795, 77.6011),
    "Queen's Road (Towards Gate 1)": (12.9805, 77.5995),
    'Inside Cubbon Park (Near Stadium)': (12.9779, 77.5958),
    "St. Mark's Road (Food Stalls)": (12.9714, 77.6017),
    'Cubbon Park Metro Station Exit': (12.9811, 77.5968),
    'Official Parking Area': (12.9765, 77.5980),
    'Inside Police Cordon': (12.9784, 77.5994),
    'Watching from Home': (None, None)
}


behavior_flags = ['Normal', 'Agitated', 'Anxious', 'Panicked', 'Aggressive', 'Cooperative']
mob_movements = ['Standing Still', 'Flowing', 'Pushing', 'Surging', 'Running Chaotically', 'Not Applicable']
evacuation_modes = ['Self-Walked', 'Assisted/Carried', 'Stretcher', 'No Evacuation']
transport_modes = ['Walking', 'Bike', 'Car', 'Auto Rickshaw', 'Metro', 'Bus', 'Cab/Ola/Uber']
emotional_states = ['Calm', 'Excited', 'Anxious', 'Angry', 'Scared', 'Terrified', 'Confused']

# --- DATA GENERATION LOOP ---
data = []
for i in range(1, num_records + 1):
    time_phase_roll = random.random()
    if time_phase_roll < 0.15:
        timestamp = early_arrival_start + timedelta(seconds=random.randint(0, int((early_arrival_end - early_arrival_start).total_seconds())))
        phase = 'Early Arrival'
    elif time_phase_roll < 0.65:
        timestamp = peak_arrival_start + timedelta(seconds=random.randint(0, int((peak_arrival_end - peak_arrival_start).total_seconds())))
        phase = 'Peak Arrival'
    elif time_phase_roll < 0.85:
        timestamp = incident_window_start + timedelta(seconds=random.randint(0, int((incident_window_end - incident_window_start).total_seconds())))
        phase = 'Incident'
    else:
        timestamp = post_incident_start + timedelta(seconds=random.randint(0, int((post_incident_end - post_incident_start).total_seconds())))
        phase = 'Post-Incident'

    attendee_id, gender, age = i, random.choice(['Male', 'Female']), random.randint(18, 35)
    pre_existing_medical_condition = random.random() < 0.08
    location_category = random.choices(location_choices, weights=location_weights)[0]
    lat, lon = location_coords.get(location_category, (None, None))
    gate_id = random.choices(gates, weights=[3 if g in high_risk_gates else 1 for g in gates])[0]

    if location_category == 'Watching from Home':
        ticket_status = 'Invalid'; crowd_density_sq_m, wait_time_min, duration_in_crowd_min = 0, 0, 0
        security_personnel, police_presence = 0, 0; incident_reported, incident_type, injury_severity = False, 'None', 'None'
        emergency_called, response_time_min, entry_delay_min = False, 0, 0
        possible_death_cause = None; group_size = 1; behavior_flag = 'Normal'; mob_movement = 'Not Applicable'
        evacuation_mode, mode_of_transport = 'No Evacuation', 'None'
        emotional_state = random.choices(['Calm', 'Excited'], weights=[0.6, 0.4])[0]
        social_media_mentions = random.randint(0, 5); crowd_control_measures = 'None'
        first_responder_type, exit_gate_status, communication_method = 'N/A', 'N/A', 'N/A'
        panic_button_pressed, attempted_entry = False, False
    else:
        ticket_status = random.choices(ticket_statuses, weights=[0.4, 0.6])[0]
        group_size = random.randint(1, 6)
        mode_of_transport = random.choice(transport_modes)
        
        if phase == 'Early Arrival':
            base_density, density_scale = 0.5, 1
        elif phase == 'Peak Arrival':
            base_density, density_scale = 2.0, 3
        elif phase == 'Incident':
            base_density, density_scale = 4.0, 5
        else: # Post-Incident
            base_density, density_scale = 1.5, 2

        if gate_id in high_risk_gates: base_density *= 1.5
        crowd_density_sq_m = round(np.clip(np.random.normal(loc=base_density, scale=density_scale), 0.5, 7.0), 2)

        if phase == 'Early Arrival':
            wait_time_min, entry_delay_min, incident_prob = random.randint(0, 15), random.randint(0, 5), 0.01
            emotional_state = random.choices(['Calm', 'Excited'], weights=[0.7, 0.3])[0]
            behavior_flag = 'Normal'
            mob_movement = 'Flowing'
            communication_method, exit_gate_status = 'Official Announcement', 'Clear'
        elif phase == 'Peak Arrival':
            wait_time_min, entry_delay_min, incident_prob = random.randint(15, 45), random.randint(5, 20), 0.05
            emotional_state = random.choices(['Excited', 'Anxious'], weights=[0.6, 0.4])[0]
            # CORRECTED: The original line caused a ValueError. Split into two lines.
            behavior_flag = random.choices(['Normal', 'Anxious'], weights=[0.7, 0.3])[0]
            mob_movement = random.choices(['Flowing', 'Pushing'], weights=[0.5, 0.5])[0]
            communication_method = random.choices(['Official Announcement', 'Social Media'], weights=[0.6, 0.4])[0]
            exit_gate_status = 'Clear'
        elif phase == 'Incident':
            wait_time_min, entry_delay_min, incident_prob = random.randint(40, 90), random.randint(20, 40), 0.30
            emotional_state = random.choices(['Anxious', 'Scared', 'Angry', 'Terrified'], weights=[0.3, 0.3, 0.2, 0.2])[0]
            behavior_flag = random.choices(['Agitated', 'Panicked', 'Aggressive'], weights=[0.4, 0.4, 0.2])[0]
            mob_movement = random.choices(['Pushing', 'Surging', 'Running Chaotically'], weights=[0.3, 0.4, 0.3])[0]
            communication_method = random.choices(['Word of Mouth', 'Social Media', 'Police Instructions'], weights=[0.5, 0.3, 0.2])[0]
            exit_gate_status = 'Clear' if crowd_density_sq_m <= 4.5 else random.choices(['Partially Blocked', 'Completely Blocked'], weights=[0.6, 0.4])[0]
        else: # Post-Incident
            wait_time_min, entry_delay_min, incident_prob = random.randint(10, 30), random.randint(10, 30), 0.03
            emotional_state = random.choices(['Scared', 'Confused', 'Calm'], weights=[0.4, 0.4, 0.2])[0]
            behavior_flag = random.choices(['Anxious', 'Cooperative', 'Normal'], weights=[0.5, 0.4, 0.1])[0]
            mob_movement = random.choices(['Standing Still', 'Flowing'], weights=[0.6, 0.4])[0]
            communication_method = random.choices(['Police Instructions', 'Official Announcement'], weights=[0.6, 0.4])[0]
            exit_gate_status = 'Clear'

        duration_in_crowd_min = random.randint(10, 240)
        medical_incident_chance = 0.1 if pre_existing_medical_condition else 0.0
        incident_reported = random.random() < (incident_prob + (crowd_density_sq_m * 0.05) + medical_incident_chance)
        
        incident_type = 'None'
        if incident_reported:
            if pre_existing_medical_condition and random.random() < 0.25: incident_type = random.choice(['Faint', 'Medical Emergency'])
            elif phase == 'Incident': incident_type = random.choices(incident_types, weights=[0.1, 0.2, 0.3, 0.25, 0.1, 0.05])[0]
            else: incident_type = random.choices(incident_types, weights=[0.4, 0.3, 0.1, 0.05, 0.1, 0.05])[0]

        injury_severity, possible_death_cause = 'None', None
        if incident_type == 'Stampede':
            if ticket_status == 'Valid': injury_weights = [0.1, 0.3, 0.4, 0.2]
            else: injury_weights = [0.4, 0.5, 0.1, 0.0]
            injury_severity = random.choices(injury_severity_levels, weights=injury_weights)[0]
            if injury_severity == 'Fatal': possible_death_cause = random.choice(death_causes)
        elif incident_type in ['Panic', 'Scuffle']: injury_severity = random.choices(injury_severity_levels, weights=[0.3, 0.5, 0.2, 0.0])[0]
        elif incident_type in ['Faint', 'Medical Emergency']: injury_severity = random.choices(injury_severity_levels, weights=[0.2, 0.6, 0.2, 0.0])[0]

        emergency_called = injury_severity in ['Major', 'Fatal'] or incident_type == 'Stampede'
        response_time_min = random.randint(3, 12) if emergency_called else 0
        
        evacuation_mode = 'No Evacuation'
        if injury_severity == 'Fatal': evacuation_mode = 'Stretcher'
        elif injury_severity == 'Major': evacuation_mode = random.choices(['Stretcher', 'Assisted/Carried'], weights=[0.7, 0.3])[0]
        elif injury_severity == 'Minor': evacuation_mode = random.choices(['Self-Walked', 'Assisted/Carried'], weights=[0.6, 0.4])[0]

        first_responder_type = 'None'
        if incident_reported:
            if injury_severity in ['Major', 'Fatal']: first_responder_type = 'Paramedic'
            elif incident_type == 'Scuffle': first_responder_type = random.choices(['Police', 'Stadium Security'], weights=[0.6, 0.4])[0]
            else: first_responder_type = random.choices(['Stadium Security', 'Bystander'], weights=[0.7, 0.3])[0]

        security_personnel = random.randint(2, 8) if gate_id in high_risk_gates else random.randint(4, 12)
        police_presence = random.randint(1, 5) if gate_id in high_risk_gates else random.randint(2, 8)
        crowd_control_measures = random.choices(crowd_controls, weights=[0.6, 0.3, 0.1, 0.0])[0] if crowd_density_sq_m > 2.5 else 'None'
        panic_button_pressed = random.random() < (0.6 if incident_type in ['Stampede', 'Panic'] else 0.02)
        
        lam_val = 15 if phase == 'Incident' else (8 if phase == 'Post-Incident' else (3 if phase == 'Peak Arrival' else 1))
        if incident_reported: lam_val *= 2
        social_media_mentions = int(np.clip(np.random.poisson(lam=lam_val), 0, 150))
        
        attempted_entry = False
        if ticket_status == 'Valid':
            attempted_entry = random.random() < (0.98 if crowd_density_sq_m < 3.0 else 0.8)
        else: # Invalid Ticket
            attempted_entry = random.random() < 0.25
            if attempted_entry:
                behavior_flag = 'Aggressive'
                if random.random() < 0.6 and incident_type == 'None':
                    incident_type = 'Scuffle'

    data.append([
        timestamp, gate_id, attendee_id, gender, age, pre_existing_medical_condition, ticket_status,
        wait_time_min, crowd_density_sq_m, security_personnel, police_presence, incident_reported, incident_type,
        injury_severity, emergency_called, response_time_min, first_responder_type, crowd_control_measures,
        entry_delay_min, social_media_mentions, panic_button_pressed, possible_death_cause, attempted_entry,
        location_category, exit_gate_status, communication_method, group_size, behavior_flag, mob_movement,
        evacuation_mode, duration_in_crowd_min, lat, lon, mode_of_transport, emotional_state
    ])

# --- DATAFRAME CREATION AND EXPORT ---
# CORRECTED: Ensured all column names match the variables used in the data.append() call
columns = [
    'timestamp', 'gate_id', 'attendee_id', 'gender', 'age', 'pre_existing_medical_condition', 'ticket_status',
    'wait_time_min', 'crowd_density_sq_m', 'security_personnel', 'police_presence', 'incident_reported', 'incident_type',
    'injury_severity', 'emergency_called', 'response_time_min', 'first_responder_type', 'crowd_control_measures',
    'entry_delay_min', 'social_media_mentions', 'panic_button_pressed', 'possible_death_cause', 'attempted_entry',
    'location_category', 'exit_gate_status', 'communication_method', 'group_size', 'behavior_flag', 'mob_movement',
    'evacuation_mode', 'duration_in_crowd_min', 'lat', 'lon', 'mode_of_transport', 'emotional_state'
]

df = pd.DataFrame(data, columns=columns)
df.to_csv("RCB_Stampede_Final_Dataset_v4.csv", index=False, date_format='%Y-%m-%d %H:%M:%S')

print("✅ Final dataset with all corrections saved as 'RCB_Stampede_Final_Dataset_v4.csv'")
