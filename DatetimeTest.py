from datetime import datetime

# startDate = "2022-01-02T09:30:00.000Z"

# startDate = datetime.strptime(startDate, "%Y-%m-%dT%H:%M:%S.%fZ")
# print(startDate.hour)

def calculate_bill(start_date, end_date):
    start_date = datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%S.%fZ")
    end_date = datetime.strptime(end_date, "%Y-%m-%dT%H:%M:%S.%fZ")
    hours = (end_date - start_date).total_seconds() / 3600
    return hours * 0.666, hours

bill, hours = calculate_bill("2022-01-02T09:30:00.000Z", "2022-01-04T10:30:00.000Z")
print(f"Bill: {bill}, Hours: {hours}")