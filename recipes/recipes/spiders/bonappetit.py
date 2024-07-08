import scrapy


# This spider scrapes all Bon Appetit recipes
class BonappetitSpider(scrapy.Spider):
    name = "bonappetit"
    allowed_domains = ["www.bonappetit.com"]
    start_urls = ["http://www.bonappetit.com/recipes"]

    def parse(self, response):
        # All recipe hrefs in recipe page
        recipes = response.xpath(
            '//a[@class="SummaryItemHedLink-civMjp dVrbhU summary-item-tracking__hed-link summary-item__hed-link"]/@href'
        ).getall()

        # Get next page href
        next_button = response.xpath(
            '//a[@class="BaseButton-bLlsy ButtonWrapper-xCepQ cnjhrg dqiBrX button button--primary"]/@href'
        ).get()

        for endpoint in recipes:
            yield response.follow(url=endpoint, callback=self.parse_recipe)

        if next_button:
            yield response.follow(url=next_button, callback=self.parse)

    def parse_recipe(self, response):
        # Measurement list
        amounts_list = response.xpath(
            '//div[@class="List-iSNGTT guHkXK"]/p/text()'
        ).getall()
        # Ingredient name list
        ingredient_list = response.xpath(
            '//div[@class="List-iSNGTT guHkXK"]/div/text()'
        ).getall()

        # This combines the amounts and the ingredients into one list, with a space if there is an amount
        ingredients = [
            a + (" " if a else "") + b for a, b in zip(amounts_list, ingredient_list)
        ]

        steps = response.xpath('//li[@class="InstructionListWrapper-dcpygI jsIesN"]/p')
        formatted_steps = []

        for step in steps:
            formatted_steps.append(
                "".join(step.xpath("./descendant-or-self::*/text()").getall())
            )

        yield {
            "title": response.xpath(
                '//h1[@class="BaseWrap-sc-gjQpdd BaseText-ewhhUZ SplitScreenContentHeaderHed-lcUSuI iUEiRd gReKXo dfelga"]/text()'
            ).get(),
            "description": "".join(
                response.xpath(
                    '//div[@class="container--body-inner"]/p/descendant-or-self::*/text()'
                ).getall()
            ),
            "ingredients": ingredients,
            "steps": formatted_steps,
            "date": response.xpath(
                '//time[@class="SplitScreenContentHeaderPublishDate-bMGEVk cNImXo"]/text()'
            ).get(),
            "recipe_url": response.request.url,
        }
