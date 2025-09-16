class WeatherRecord:
    def __init__(self, date, city, temperature):
        self.date = date
        self.city = city
        self.temperature = temperature


class WeatherDataStorage:
    def __init__(self, years, cities):
        self.years = years
        self.cities = cities
        self.data = [[None for _ in cities] for _ in years]

    def insert(self, record):
        year = int(record.date.split("/")[-1])  
        if year in self.years and record.city in self.cities:
            row = self.years.index(year)
            col = self.cities.index(record.city)
            self.data[row][col] = record.temperature

    def retrieve(self, city, year):
        if year in self.years and city in self.cities:
            row = self.years.index(year)
            col = self.cities.index(city)
            return self.data[row][col]
        return None

    def row_major(self):
        result = []
        for row in self.data:
            for val in row:
                result.append(val)
        return result

    def column_major(self):
        result = []
        for j in range(len(self.cities)):
            for i in range(len(self.years)):
                result.append(self.data[i][j])
        return result

    def handle_sparse(self, sentinel=-999):
        for i in range(len(self.years)):
            for j in range(len(self.cities)):
                if self.data[i][j] is None:
                    self.data[i][j] = sentinel
        return self.data

    def analyze_complexity(self):
        print("\n--- Complexity Analysis ---")
        print("Insert: O(1)")
        print("Retrieve: O(1)")
        print("Row/Column Access: O(n*m)")
        print("Space: O(n*m)")


if __name__ == "__main__":
    years = [2023, 2024, 2025]
    cities = ["Delhi", "Mumbai", "Kolkata"]

    r1 = WeatherRecord("01/01/2023", "Delhi", 15.5)
    r2 = WeatherRecord("05/02/2024", "Mumbai", 28.2)
    r3 = WeatherRecord("10/03/2025", "Kolkata", 22.1)

    system = WeatherDataStorage(years, cities)

    system.insert(r1)
    system.insert(r2)
    system.insert(r3)

    print("Row Major:", system.row_major())
    print("Column Major:", system.column_major())
    print("Retrieve (Delhi, 2023):", system.retrieve("Delhi", 2023))
    print("Sparse Data:", system.handle_sparse())
    system.analyze_complexity()