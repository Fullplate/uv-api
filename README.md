# uv-api

Simple HTTP API for retrieving today's current and maximum UV radiation index for a given location.

## Details

- Python 3 + Flask
- Uses the [Arpansa](https://www.arpansa.gov.au/) API for retrieving UV measurements,
which also localises the API to Australia.
- Uses the [LocationIQ](https://locationiq.com/) service for geocoding (location name --> lat/long).

## Example Usage

```
GET /api/uv/sydney
{
  "current": "2.6",
  "max": "3.4",
  "max_time_of_day": "11:46"
}
```

## Dev notes

- Requirements: flask, python-dotenv
- Testing:
```
export FLASK_ENV=development
flask run
curl http://127.0.0.1:5000/api/uv/sydney
```