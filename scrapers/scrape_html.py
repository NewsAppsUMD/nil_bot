#THIS HAS THE HTML SCRAPER CODE THAT WE'RE NOT USING ANYMORE

for row in rows:
    if row.find_all('img')[1]['title'] in big_ten_teams:
        # change to maryland terrapins - just using houston for testing
        # defining a variable (with Derek's help) and then telling it to print that variable
        year = row.find_all('h6')[1].text
        print(year)
        name = row.find('div', {'class': 'PlayerDealItem_playerContainer__XILE3'}).find('div').find('a').text
        print(name)
        # continue to define variables except this time by myself (and I think this worked?)
        date = row.find('span', {'class': 'MuiTypography-root DealTrackerItem_date__I5gVl MuiTypography-caption MuiTypography-colorTextPrimary'}).text
        print(date)
        deal = row.find('div', {'class': 'DealTrackerItem_companyWrapper__RFysQ'}).find('h6').text
        print(deal)
        company = row.find('div', {'class': 'DealTrackerItem_companyWrapper__RFysQ'}).find('h5').text
        print(company)
        # other things I want it to pull: sport
    # this next set of code: if it's not the team I care about, please skip and continue
    #else:
        #continue
