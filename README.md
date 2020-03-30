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


# /endpoints

## /country
- Bring all information about the countries

## /country/id
- search by the id

## /country/nameofthecountry
- filter by the name of the country, like */country/Brazil*

## /world

- bring total information about the Covid-19
