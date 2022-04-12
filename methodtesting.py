from neo4j import GraphDatabase
from neo4j.graph import Relationship as Relationship

#from forms import return_location_list


# There will be two node types in this graph database: An "elevator" type and a "location" type
# Node of type elevator will have 

class Test:
    
    #Initializes connection to database with authentication
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        print("Connected To Database")

    #Closes connection to database
    #If a new instance of class test is called, this method should be envoked at the end to ensure the session is closed.
    def close(self):
        self.driver.close()
        print("Disconnected")
    
    #Creates an elevator on a floor
    #This function works, but does not check for duplicates
    def createElevator(self, elevatorName, floor):
        with self.driver.session() as session:
            query = (
                f"MERGE (e: Elevator {{ name: '{elevatorName}' }})"
                f"SET e.floor = {floor}"
                "RETURN e.name as name"
                "RETURN e.floor as floor"
            )
            results = session.run(query)
            for r in results:
                print(f"Elevator {r['name']} on floor {r['floor']} has been added!")

    #sets relationship between two elevators
    def setElevatorElevatorRelationship(self, firstElevator, secondElevator, relationship, floor):
        with self.driver.session() as session:
            query = (
                f"MATCH (e1: Elevator {{ name: '{firstElevator}', floor: {floor}}})"
                f"MATCH (e2: Elevator {{name: '{secondElevator}', floor: {floor}}})"
                f"MERGE (e1)-[r:CONNECTS {{name: '{relationship}'}}]-(e2)"
                "RETURN r.name as name"
            )
            result= session.run(query)
            for r in result:
                print (r['name'])

    #sets elevator relationship to the location
    def setElevatorLocationRelationship(self, elevator, location, direction_ltoe, floor):
        return
    #gets the relationship to the closest elevator (only works if location is directly connected to the elevator atm)
    def getLocationToNearestElevator(self, location, floor):
        return
        
    def return_location_list(self):
        locations = []
        with self.driver.session() as session:
            query = ("MATCH (l: Location)"
                    "RETURN l.name as name"
            )
            result = session.run(query)
            for r in result:
                locations.append(r['name'])
            return locations

#testing app
if __name__ == '__main__':

    testing = Test("neo4j+s://2e126d37.databases.neo4j.io", "neo4j", "fMMMCrLRM3buP_V1EfNj3AVMhuqKRHmdJHvjPp2C51A")
    #testing.setElevatorElevatorRelationship("B", "C", "ns", 1)

    testing.close()