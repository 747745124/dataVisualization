import twint
c = twint.Config()
c.Geo = "40.75773,-73.9857,1km"
# TimeSquare
c.Since = "2020-12-27"
c.Until = "2021-1-8"
c.Store_csv = True
c.Output = "NewYork.csv"

twint.run.Search(c)
# import twint

# # Configure
# c = twint.Config()
# c.Username = "747745124"
# c.Search = "We"

# # Run
# twint.run.Search(c)
