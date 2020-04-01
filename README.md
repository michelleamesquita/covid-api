# Features

* * *
- Api that use https://www.worldometers.info/coronavirus/ page;

- json Response:

```json
{
  "activeCases": "",
  "country": "Brazil",
  "firstCase": "Feb 24 ",
  "id": 16,
  "newCases": "",
  "seriousCritical": "6",
  "totalCases": "4,256",
  "totalDeath": "136 ",
  "totalRecovered": "136 "
}
```
# Watch the graph in real time!

- Just use the ploty.py code
![alt text]("https://user-images.githubusercontent.com/44561732/78093643-0643df00-73a9-11ea-972b-9dab08f9639c.png")

# /endpoints

## /country
- Bring all information about the countries

## /country/id
- search by the id

## /country/nameofthecountry
- filter by the name of the country, like */country/Brazil*

## /world

- bring total information about the Covid-19
