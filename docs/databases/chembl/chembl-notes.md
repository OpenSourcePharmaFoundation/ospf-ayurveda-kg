Update: we're working on getting ChemBL data.
- We've made progress:
  - Downloaded all of the data locally
    - Now we're working on extracting it into a usable format
    - We'll need a local database most likely, which we then dump the needed data out into a more consumable format
- *Acquiring* the data is considerably easier with ChemBL (parsing it is a different story, but it's not working against being used)

Our recommendation is to ditch DrugBank in favour of ChemBL.

How to get ChemBL data
======================
Process:
1. Create a docker container with Postgresql
2. Create a virtual directory with the data for the docker instance to access
3. Load the data into the Postgresql database on the docker instance
4. Dump the data from the database into a text format
  - We can then parse the SQL statements dumped out into csv files

------
