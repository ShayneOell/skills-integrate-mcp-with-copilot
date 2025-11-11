from src.db import activities_collection

DEFAULT_ACTIVITIES = {
	"Chess Club": {
		"description": "Learn strategies and compete in chess tournaments",
		"schedule": "Fridays, 3:30 PM - 5:00 PM",
		"max_participants": 12,
		"participants": ["michael@mergington.edu", "daniel@mergington.edu"],
	},
	"Programming Class": {
		"description": "Learn programming fundamentals and build software projects",
		"schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
		"max_participants": 20,
		"participants": ["emma@mergington.edu", "sophia@mergington.edu"],
	},
	"Gym Class": {
		"description": "Physical education and sports activities",
		"schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
		"max_participants": 30,
		"participants": ["john@mergington.edu", "olivia@mergington.edu"],
	},
}

def seed():
	coll = activities_collection()
	for name, payload in DEFAULT_ACTIVITIES.items():
		# Upsert by name so script is idempotent
		coll.update_one({"name": name}, {"$set": {**payload, "name": name}}, upsert=True)

if __name__ == "__main__":
	print("Seeding activities...")
	seed()
	print("Done.")
