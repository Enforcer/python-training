import httpx

response = httpx.get("https://breadcrumbscollector.tech")
print(response)
response.raise_for_status()

