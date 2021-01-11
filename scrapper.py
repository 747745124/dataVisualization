import twint

c = twint.Config()

c.Geo = "40.7580002,-73.985997,2.99km"
# TimeSquare
c.Since = "2020-12-23"
c.Until = "2020-12-30"
c.Store_csv = True
c.Output = "TimeSquareWeek51.csv"
c.Links = 'exclude'
c.Verified = True
# c.Search = 'virus'
c.Lang = 'en'

twint.run.Search(c)

# testing
# import twint

# # Configure
# c = twint.Config()
# c.Username = "747745124"
# c.Search = "We"

# # Run
# twint.run.Search(c)
