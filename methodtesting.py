from neo4j import GraphDatabase
from neo4j.graph import Relationship as Relationship


# There will be two node types in this graph database: An "elevator" type and a "location" type
# Node of type elevator will have 

class Test:
    
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        print("Connected To Database")

    def close(self):
        self.driver.close()
        print("Disconnected")
    
    #This function works, but does not check for duplicates
    def createElevator(self, elevatorName, floor):
        with self.driver.session() as session:
            query = (
                f"MERGE (e: Elevator {{ name: '{elevatorName}' }})"
                f"SET e.floor = 1"
                #"RETURN e"
            )
            session.run(query)
            print(f"Elevator {elevatorName} on floor {floor} has been added!")

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
    

#relationships


testing = Test("neo4j+s://2e126d37.databases.neo4j.io", "neo4j", "fMMMCrLRM3buP_V1EfNj3AVMhuqKRHmdJHvjPp2C51A")
testing.setElevatorElevatorRelationship("B", "C", "ns", 1)

#testing.setElevatorElevatorRelationship("A", "B", "ns", 1)
testing.close()