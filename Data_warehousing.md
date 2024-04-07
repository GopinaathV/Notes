##Facts
The fact table in a dimensional model stores the performance measurements resulting from an organization’s business process events.

##Dimensions
The dimension tables contain the textual context associated with a business process measurement event.

##Grain 
The grain establishes exactly what a single fact table row represents.

##Slowly changing dimensions (https://www.luzmo.com/blog/slowly-changing-dimensions)
Slowly changing dimensions are ways in which data in your data warehouse changes over time.

Depending on your business model and overall needs, you may want to:
->Disregard those changes
->Keep track of all the changes that happen
->Track only the most recent change to a data point

#Type 0 - The data never changes in a dimensional table. These are common data points that, well, don’t change, such as the date of birth, zip codes, social security numbers, and more.
#Type 1 – This model involves overwriting the old current value with the new current value. No history is maintained.
#Type 2 – The current and the historical records are kept and maintained in the same file or table.
#Type 3 – The current data and historical data are kept in the same record. The user decides how much history is kept in the record.
#Type 4 – In this model, the current data is maintained in two different tables; one for the current data and one that contains all the historical data.
#Type 6 – This model is a hybrid of Type 1, Type 2, and Type3.








