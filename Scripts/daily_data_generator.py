import pandas as pd
import random
from datetime import datetime
import os

# =========================================
# BASE FOLDER
# =========================================

BASE_PATH = r"C:\Users\DEEPAK\OneDrive\power bi upload files\Daily_Data"

# =========================================
# ORIGINAL FILE PATHS
# =========================================

CUSTOMERS_FILE = os.path.join(BASE_PATH, "04_customers.csv")
VISITS_FILE = os.path.join(BASE_PATH, "07_visits.csv")
FEEDBACK_FILE = os.path.join(BASE_PATH, "09_feedback.csv")

# =========================================
# CHECK FILES EXIST
# =========================================

if not os.path.exists(CUSTOMERS_FILE):
    print(f"ERROR: File not found -> {CUSTOMERS_FILE}")
    exit()

if not os.path.exists(VISITS_FILE):
    print(f"ERROR: File not found -> {VISITS_FILE}")
    exit()

if not os.path.exists(FEEDBACK_FILE):
    print(f"ERROR: File not found -> {FEEDBACK_FILE}")
    exit()

# =========================================
# LOAD EXISTING FILES
# =========================================

customers_existing = pd.read_csv(CUSTOMERS_FILE)

visits_existing = pd.read_csv(VISITS_FILE)

feedback_existing = pd.read_csv(FEEDBACK_FILE)

# =========================================
# GET LAST IDS
# =========================================

last_customer_id = customers_existing["customer_id"].max()

last_visit_id = visits_existing["visit_id"].max()

last_feedback_id = feedback_existing["feedback_id"].max()

# =========================================
# MASTER DATA
# =========================================

first_names = [
    "Arun", "Vijay", "Priya", "Meena",
    "Rahul", "Divya", "Karthik", "Anitha"
]

last_names = [
    "Kumar", "Raj", "Sharma", "Devi",
    "Krishnan", "Murugan", "Naidu"
]

cities = [
    "Chennai",
    "Coimbatore",
    "Madurai",
    "Salem"
]

visit_types = [
    "Walk-in",
    "Appointment"
]

feedback_comments = [
    "Excellent service!",
    "Very satisfied.",
    "Good experience.",
    "Friendly staff.",
    "Amazing ambience.",
    "Could improve waiting time."
]

today = datetime.now().strftime("%Y-%m-%d")

# =========================================
# GENERATE CUSTOMERS
# =========================================

customer_rows = []

new_customer_ids = []

for i in range(10):

    last_customer_id += 1

    customer_id = last_customer_id

    new_customer_ids.append(customer_id)

    first_name = random.choice(first_names)

    last_name = random.choice(last_names)

    gender = random.choice(["M", "F"])

    dob_year = random.randint(1980, 2005)

    dob_month = random.randint(1, 12)

    dob_day = random.randint(1, 28)

    dob = f"{dob_year}-{dob_month:02d}-{dob_day:02d}"

    phone = f"9{random.randint(100000000,999999999)}"

    email = f"{first_name.lower()}.{last_name.lower()}{random.randint(100,999)}@gmail.com"

    city = random.choice(cities)

    home_branch_id = random.randint(1, 4)

    registration_date = today

    customer_rows.append({

        "customer_id": customer_id,
        "first_name": first_name,
        "last_name": last_name,
        "gender": gender,
        "dob": dob,
        "phone": phone,
        "email": email,
        "city": city,
        "home_branch_id": home_branch_id,
        "registration_date": registration_date

    })

customers_df = pd.DataFrame(customer_rows)

# =========================================
# GENERATE VISITS
# =========================================

visit_rows = []

new_visit_ids = []

for i in range(20):

    last_visit_id += 1

    visit_id = last_visit_id

    new_visit_ids.append(visit_id)

    customer_id = random.choice(new_customer_ids)

    branch_id = random.randint(1, 4)

    total_amount = random.randint(500, 5000)

    discount_amount = random.randint(0, 500)

    net_amount = total_amount - discount_amount

    membership_id = random.choice([None, None, random.randint(1, 500)])

    visit_rows.append({

        "visit_id": visit_id,
        "customer_id": customer_id,
        "branch_id": branch_id,
        "visit_date": today,
        "visit_type": random.choice(visit_types),
        "membership_id": membership_id,
        "total_amount": total_amount,
        "discount_amount": discount_amount,
        "net_amount": net_amount

    })

visits_df = pd.DataFrame(visit_rows)

# =========================================
# GENERATE FEEDBACK
# =========================================

feedback_rows = []

for visit_id in new_visit_ids:

    last_feedback_id += 1

    visit_info = visits_df[visits_df["visit_id"] == visit_id].iloc[0]

    feedback_rows.append({

        "feedback_id": last_feedback_id,
        "visit_id": visit_id,
        "customer_id": visit_info["customer_id"],
        "branch_id": visit_info["branch_id"],
        "visit_date": today,
        "rating": random.randint(3, 5),
        "comment": random.choice(feedback_comments)

    })

feedback_df = pd.DataFrame(feedback_rows)

# =========================================
# APPEND DATA TO EXISTING FILES
# =========================================

customers_df.to_csv(
    CUSTOMERS_FILE,
    mode='a',
    header=False,
    index=False
)

visits_df.to_csv(
    VISITS_FILE,
    mode='a',
    header=False,
    index=False
)

feedback_df.to_csv(
    FEEDBACK_FILE,
    mode='a',
    header=False,
    index=False
)

# =========================================
# SUCCESS MESSAGE
# =========================================

print("\n===================================")
print(" DAILY DATA APPENDED SUCCESSFULLY ")
print("===================================")

print(f"\nCustomers Added : {len(customers_df)}")
print(f"Visits Added    : {len(visits_df)}")
print(f"Feedback Added  : {len(feedback_df)}")

print("\nEXISTING FILES UPDATED SUCCESSFULLY")
print("===================================")