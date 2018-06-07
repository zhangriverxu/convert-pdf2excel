import pdftables_api

c = pdftables_api.Client('my-api-key')
c.xlsx('input.pdf', 'output') #replace c.xlsx with c.csv to convert to CSV
