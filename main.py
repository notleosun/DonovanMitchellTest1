from googlesearch import search
import time
import random

# Search query and parameters
product_name = input("Enter:")
country_domains = ['.fr', '.de', '.es', '.it', '.nl', '.be']  # Domains for France, Germany, Spain, Italy, Netherlands, Belgium
num_search_results = 200  # Number of search results to retrieve per country

# Base list of major websites to exclude, without country-specific extensions
base_sites = ['amazon', 'ebay', 'vinted', 'imdb', 'pinterest', 'zara']

# Function to search for supermarkets and suppliers in specific countries
def google_search(query, country_domain, num_results):
    # Create the exclusion list based on the current country domain
    exclude_sites = [f"{site}{country_domain}" for site in base_sites]
    exclude_query = " ".join([f"-site:{site}" for site in exclude_sites])
    
    # Create the search query with the exclusion list
    search_query = f"{query} site:{country_domain} {exclude_query}"
    
    # Perform the search with a delay to avoid being blocked
    try:
        results = list(search(search_query, num_results=num_results))
        time.sleep(random.uniform(5, 10))  # Random delay between 5 to 10 seconds
        return results
    except Exception as e:
        print(f"Error: {e}")
        return []

# Perform Google search for each country
all_site_names = []
for domain in country_domains:
    search_results = google_search(product_name, domain, num_search_results)
    for result_url in search_results:
        site_name = result_url.split('/')[2]  # Extract the domain name
        all_site_names.append(site_name)

# Remove duplicates by converting to a set
unique_site_names = list(set(all_site_names))

# Print the unique site names
for site in unique_site_names:
    print(site)
