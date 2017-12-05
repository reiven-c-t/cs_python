def main():
    dateStr = input("Enter a date(mm/dd/yyyy): ")
    monthStr, dayStr, yearStr, = dateStr.split("/")
    month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    monthStr=month[int(monthStr)-1]
    print("The converted date is:", monthStr,dayStr+",",yearStr)

main()