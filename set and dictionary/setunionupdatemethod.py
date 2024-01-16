# it performs the set union ,but modifies the original set rather than creating a new one
from prescription import adverse_interactions

meds_to_watch =set() # empty set created

for interaction in adverse_interactions:
    meds_to_watch.update(interaction)

print(meds_to_watch)