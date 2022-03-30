from neo4j import GraphDatabase


# There will be two node types in this graph database: An "elevator" type and a "location" type
# Node of type elevator will have 

class Test:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()
    
    def createElevator(self, elevatorName, floor):
        with self.driver.session() as session:
            query = (
                f"MATCH (e: Elevator {{name: {elevatorName}, floor: {floor} }})"
                "RETURN e.name AS name, e.floor AS floor"
            )
            result = session.run(query)
            print(f"{result['name']} on floor {result['floor']} has been added!")




if __name__ == "main":
    test = Test("neo4j+s://2e126d37.databases.neo4j.io", "neo4j", "fMMMCrLRM3buP_V1EfNj3AVMhuqKRHmdJHvjPp2C51A")
    test.createElevator("I", 1)
    test.close()