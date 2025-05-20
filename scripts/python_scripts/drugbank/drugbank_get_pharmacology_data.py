from bs4 import BeautifulSoup

def get_dd_pharmacology_data(html):
  soup = BeautifulSoup(html, 'html.parser')

  def get_dt_dd_value(soup, dt_id):
      dt = soup.find('dt', id=dt_id)
      if dt:
          dd = dt.find_next_sibling('dd')
          return dd.get_text(strip=True) if dd else None
      return None

  def get_paragraph_from_dd(dt_id):
      dt = soup.find('dt', id=dt_id)
      if dt:
          dd = dt.find_next_sibling('dd')
          p = dd.find('p') if dd else None
          return p.get_text(strip=True) if p else None
      return None

  def get_list_items(dt_id):
      dt = soup.find('dt', id=dt_id)
      if dt:
          dd = dt.find_next_sibling('dd')
          return [li.get_text(strip=True) for li in dd.find_all('li')] if dd else []
      return []

  def get_weight_values():
      dt = soup.find('dt', id="weight")
      if dt:
          dd = dt.find_next_sibling('dd')
          if dd:
              parts = dd.get_text(separator="\n", strip=True).split("\n")
              weights = {}
              for part in parts:
                  if ':' in part:
                      key, val = part.split(":", 1)
                      weights[key.strip()] = val.strip()
              return weights
      return {}

  # Extracting all requested fields
  data = {
      "Generic Name": get_dt_dd_value(soup, "generic-name"),
      "Description": get_paragraph_from_dd("summary"),
      "DrugBank Accession Number": get_dt_dd_value(soup, "drugbank-accession-number"),
      "Background": get_paragraph_from_dd("background"),
      "Type": get_dt_dd_value(soup, "type"),
      "Groups": get_dt_dd_value(soup, "groups"),
      "Weight": get_weight_values(),
      "Synonyms": get_list_items("synonyms"),
      "External IDs": get_list_items("external-ids")
  }

  return data
