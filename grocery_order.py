# New-line delimited list of groceries
# TODO: Read these from a file or something
ingredients = """
yellow onion
flour tortillas
lime
sour cream
ground pork
roma tomato
guacamole
"""

# EatThisMuch example url
# "https://www.instacart.com/store/partner_recipe?guest=true&partner_name=eatthismuch&url=https%3A%2F%2Fwww.eatthismuch.com%2Fpantry%2Fformatted-groceries%2Fd974d0bc13770%2F%3Ft%3D1576801353%26prefer_organic%3Dfalse&utm_campaign=eatthismuch_grocerylist&utm_medium=recipe_api&utm_source=partner_eatthismuch"


def main():
  # TODO: Use urlparse to construct URLs and do encoding
  zip_code = "99999"
  title = "Test+List"

  url = f"https://www.instacart.com/store/partner_recipe?title={title}&current_zip_code={zip_code}"

  ingredient_parameter = "&ingredients%5B%5D="
  url += ingredient_parameter + ingredient_parameter.join(ingredients.replace(" ", "%20").strip().splitlines())

  print(url)


if __name__ == "__main__":
  main()
