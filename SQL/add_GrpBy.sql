--Export Addresses as a YAML file, grouped by state, and then grouped by city

--getting data for dept_ from db
select state,city from address group by state,city;


--after execute file was saved as .JSON which created add_GrpBy.json file.


