# xml_to_csv
Python xml to csv transformer. Transforms given xml file to csv.  

Currently set up for Criteo API reponses. Criteo xml structure is: report->table->[columns,rows,totals]. From which the app extracts all rows with columns as a header.

If universal use is desired then user has to alter/drop:
* table_index=find_index(etree,'table')
* rows_index=find_index(data,'rows')
to suitable form.

Ask for help at sohajek.viktor@gmail.com
