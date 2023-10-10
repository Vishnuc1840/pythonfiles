# years 1800 to 2024

years=[y for y in range(1800,2024)]
# print(years)

# print century years

century_years=[y for y in years if y %100==0]
print(century_years)

non_century=[y for y in years if y %100!=0]
print(non_century)