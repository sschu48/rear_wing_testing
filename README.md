# Project Goal
**Create an automation script to run through Java Foil exported data**

The Current setup is all ran through manual testing. Data and manually manipulated then imported into a *Jupyter Notebook* for data analysis then exported as a PDF. This takes a lot of time manually imported information. 
As data sets become larger this will increase efficiency testing the cumulative airfoil data.

# Project Outline
**Below is a brief outline of the data process**
1. Export .xslx from Java Foil to appropriate folder "java_foil_data"
2. Clean data
   1. Add appropriate column headers
   2. Delete excess data at bottom
3. Add clean data back into folder and add "_clean"
4. Run .ipynb script
5. Create folder for exports
6. Export graphs and tables to "x_airfoil_export"

---
## 1. Class test_data
> *Class containing all information for each test from Java Foil*
> - Data is imported and stored as **Data Frame**
> - Cleaned and chopped only containing important variables
> - Create get / set functions
> - Allow exporting to .xlsx file
> - Export all graphs and charts to new export folder