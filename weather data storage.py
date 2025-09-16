class WeatherRecord:
    def __init__(self, date, city, temperature):
        self.date = date 
        self.city = city
        self.temperature = temperature


class WeatherDataStorage:
    def __init__(self, years, cities):
        self.years = years
        self.cities = cities
        self.data = [[None for _ in range(len(cities))] for _ in range(len(years))]

    def populateArray(self, records):
        for record in records:
            year = int(record.date.split("/")[-1])  
            if year in self.years and record.city in self.cities:
                row = self.years.index(year)
                col = self.cities.index(record.city)
                self.data[row][col] = record.temperature

    def rowMajorAccess(self):
        result = []
        for row in range(len(self.years)):
            for col in range(len(self.cities)):
                result.append(self.data[row][col])
        return result

    def columnMajorAccess(self):
        result = []
        for col in range(len(self.cities)):
            for row in range(len(self.years)):
                result.append(self.data[row][col])
        return result

    def handleSparseData(self, sentinel=-999):
        sparse = {}
        for i in range(len(self.years)):
            for j in range(len(self.cities)):
                if self.data[i][j] is not None:
                    sparse[(self.years[i], self.cities[j])] = self.data[i][j]
                else:
                    self.data[i][j] = sentinel
        return sparse

    def retrieve(self, city, year):
        if year in self.years and city in self.cities:
            row = self.years.index(year)
            col = self.cities.index(city)
            return self.data[row][col]
        return None

    def analyzeComplexity(self):
        complexities = {
            "Insert": "O(1) average",
            "Delete": "O(1) average",
            "Retrieve": "O(1)",
            "RowMajorAccess": "O(n*m)",
            "ColumnMajorAccess": "O(n*m)",
            "Space": f"O({len(self.years)}*{len(self.cities)})"
        }
        return complexities

if __name__ == "__main__":
    years = [2023, 2024, 2025]
    cities = ["Delhi", "Mumbai", "Kolkata"]

    records = [
        WeatherRecord("01/01/2023", "Delhi", 15.5),
        WeatherRecord("02/01/2024", "Mumbai", 28.3),
        WeatherRecord("03/02/2025", "Kolkata", 22.1)
    ]

    system = WeatherDataStorage(years, cities)
    system.populateArray(records)

    print("Row Major Access:", system.rowMajorAccess())
    print("Column Major Access:", system.columnMajorAccess())
    print("Sparse Representation:", system.handleSparseData())
    print("Retrieve (Delhi, 2023):", system.retrieve("Delhi", 2023))
    print("Complexity:", system.analyzeComplexity())
