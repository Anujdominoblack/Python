from prescription import adverse_interactions
print(adverse_interactions)
med_to_watch = set() # empty set created

for item in adverse_interactions:
    med_to_watch=med_to_watch.union(item)

print(med_to_watch)