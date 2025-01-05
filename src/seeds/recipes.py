from recipe_schema import Recipe, Ingredient

baked_honey_mustard_chicken = Recipe(
    title="Baked Chicken",
    description="A delicious and flavorful baked chicken dish with a sweet and tangy mustard glaze.",
    ingredients=[
        Ingredient(name="Olive Oil", quantity=4, unit="tablespoons"),
        Ingredient(name="Honey", quantity=3, unit="tablespoons"),
        Ingredient(name="Whole Grain Mustard", quantity=2, unit="tablespoons"),
        Ingredient(name="Dijon Mustard", quantity=1, unit="tablespoon"),
        Ingredient(name="Garlic Cloves", quantity=4, unit="pcs", preparation="minced"),
        Ingredient(name="Fresh Lemon Juice", quantity=2, unit="tablespoons"),
        Ingredient(name="Paprika", quantity=0.5, unit="teaspoon"),
        Ingredient(name="Boneless Skinless Chicken Breasts", quantity=2, unit="pounds"),
        Ingredient(name="Salt", quantity=0, unit="to taste", optional=True),
        Ingredient(
            name="Cracked Black Pepper", quantity=0, unit="to taste", optional=True
        ),
        Ingredient(
            name="Fresh Chopped Parsley", quantity=2, unit="tablespoons", optional=True
        ),
        Ingredient(name="Lemon Wedges", quantity=0, unit="to taste", optional=True),
    ],
    instructions=[
        "Preheat oven to 400°F (200°C). Lightly grease a baking tray with oil and line with foil or parchment paper.",
        "Combine the olive oil, honey, whole grain mustard, Dijon mustard, minced garlic, lemon juice, and paprika in a small bowl and mix well.",
        "Place the chicken onto the prepared baking sheet. Season generously with salt and pepper. Spoon 3/4 of the honey mustard mixture evenly over the chicken and spread it all over each breast. Pour 1/4 cup of water onto the baking sheet to prevent burning and create a sauce while baking.",
        "Bake until cooked through, about 20-30 minutes, depending on the thickness of your chicken breasts. Spoon the remaining sauce over each breast and broil (or grill) for a further 3-4 minutes on medium-high heat to brown the chicken and caramelize the edges.",
        "Cover with foil and allow to rest for 10 minutes to let the juices settle before serving. Garnish with parsley and serve immediately with lemon wedges.",
    ],
)

asian_beef_stew = Recipe(
    title="Asian Beef Stew",
    description="A flavorful and hearty dish that combines tender beef with a medley of vegetables, perfect for a comforting meal.",
    ingredients=[
        Ingredient(name="onions", quantity=2, unit="pcs", preparation="sliced"),
        Ingredient(name="round steak", quantity=2, unit="lb"),
        Ingredient(name="celery", quantity=2, unit="stalks"),
        Ingredient(name="carrots", quantity=2, unit="pcs", preparation="sliced"),
        Ingredient(name="mushrooms", quantity=1, unit="cup"),
        Ingredient(name="oranges", quantity=3, unit="pcs", preparation="squeezed"),
        Ingredient(name="beef broth", quantity=1, unit="cup"),
        Ingredient(name="hoisin sauce", quantity=1 / 3, unit="cup"),
        Ingredient(name="cornstarch", quantity=2, unit="tablespoons"),
        Ingredient(name="curry powder", quantity=2, unit="teaspoons"),
        Ingredient(name="frozen peas", quantity=1, unit="cup"),
        Ingredient(
            name="rice", quantity=None, unit=None, preparation="to serve", optional=True
        ),
        Ingredient(
            name="chopped fresh cilantro",
            quantity=None,
            unit="to taste",
            preparation="",
            optional=True,
        ),
    ],
    instructions=[
        "Slice celery and mushrooms.",
        "Slice steak thinly across the grain.",
        "Place onions, beef, celery, carrots, and mushrooms in a Crock-Pot slow cooker.",
        "Combine orange juice, broth, hoisin sauce, cornstarch, and curry powder in a small bowl. Pour into the Crock-Pot slow cooker.",
        "Cover; cook on HIGH for 5 hours.",
        "Stir in peas. Cover; cook on HIGH for 20 minutes or until peas are tender.",
        "Serve with hot cooked rice and garnish with cilantro.",
    ],
)

bean_stuff = Recipe(
    title="Bean Stuff",
    description="A great vegetarian staple commonly consumed in most regions of the world.",
    ingredients=[
        Ingredient(name="bell peppers", quantity=3, unit="pcs"),
        Ingredient(name="onion", quantity=1, unit="pcs"),
        Ingredient(name="garlic cloves", quantity=3, unit="pcs"),
        Ingredient(name="jalepenos", quantity=2, unit="pcs", preparation="diced"),
        Ingredient(name="black beans", quantity=8, unit="oz"),
        Ingredient(name="rice", quantity=3, unit="cups"),
        Ingredient(
            name="red pepper flakes", quantity=None, unit="to taste", optional=True
        ),
        Ingredient(name="salt", quantity=None, unit="to taste", optional=True),
        Ingredient(name="pepper", quantity=None, unit="to taste", optional=True),
    ],
    instructions=["Stir-fry together."],
)

carrot_cake = Recipe(
    title="Carrot Cake",
    description="A deliciously moist cake featuring grated carrots and topped with a creamy frosting.",
    ingredients=[
        # Ingredients for the cake
        Ingredient(name="eggs", quantity=4, unit="pcs"),
        Ingredient(name="vegetable oil", quantity=1.25, unit="cups"),
        Ingredient(name="white sugar", quantity=1, unit="cup"),
        Ingredient(name="brown sugar", quantity=1, unit="cup"),
        Ingredient(name="vanilla extract", quantity=1, unit="tablespoon"),
        Ingredient(name="all-purpose flour", quantity=2, unit="cups"),
        Ingredient(name="baking soda", quantity=2, unit="teaspoons"),
        Ingredient(name="baking powder", quantity=2, unit="teaspoons"),
        Ingredient(name="salt", quantity=0.5, unit="teaspoon"),
        Ingredient(name="ground cinnamon", quantity=1, unit="tablespoon"),
        Ingredient(name="nutmeg", quantity=0.25, unit="teaspoons"),
        Ingredient(name="grated carrots", quantity=3, unit="cups"),
        Ingredient(name="chopped pecans", quantity=1, unit="cup"),
        # Ingredients for the frosting
        Ingredient(name="butter", quantity=0.5, unit="cup"),
        Ingredient(name="cream cheese", quantity=8, unit="ounces"),
        Ingredient(name="confectioners' sugar", quantity=4, unit="cups"),
        Ingredient(name="vanilla extract", quantity=1, unit="teaspoon"),
        Ingredient(name="chopped pecans", quantity=1, unit="cup"),
    ],
    instructions=[
        "Let butter and cream cheese soften.",
        "Preheat oven to 350 degrees F (175 degrees C). Grease and flour a 9x13 inch pan.",
        "In a large bowl, beat together eggs, oil, white sugar, brown sugar, and 3 teaspoons vanilla. Mix in flour, baking soda, baking powder, salt, nutmeg, and cinnamon. Stir in carrots. Fold in pecans. Pour into prepared pan.",
        "Bake in the preheated oven for 40 to 50 minutes, or until a toothpick inserted into the center of the cake comes out clean. Let cool in pan for 10 minutes, then turn out onto a wire rack and cool completely.",
        "To make frosting: In a medium bowl, combine butter, cream cheese, confectioners' sugar, and 1 teaspoon vanilla. Beat until the mixture is smooth and creamy. Stir in chopped pecans. Frost the cooled cake.",
    ],
)


enchilada_stuffed_sweet_potatoes = Recipe(
    title="Enchilada Stuffed Sweet Potatoes",
    description="A delicious and hearty dish, perfect for a nutritious meal.",
    ingredients=[
        Ingredient(name="sweet potatoes", quantity=5, unit="pcs"),
        Ingredient(name="tomato sauce", quantity=8, unit="oz"),
        Ingredient(name="garlic powder", quantity=1, unit="tsp"),
        Ingredient(name="chili powder", quantity=1, unit="tsp"),
        Ingredient(name="salt", quantity=1, unit="tsp"),
        Ingredient(name="ground cumin", quantity=1.5, unit="tsp"),
        Ingredient(name="black beans", quantity=16, unit="oz"),
        Ingredient(name="corn", quantity=16, unit="oz"),
        Ingredient(name="shredded cheese", quantity=3.75, unit="cups"),
        Ingredient(name="avocado", quantity=None, unit="to taste", optional=True),
        Ingredient(name="salsa", quantity=None, unit="to taste", optional=True),
        Ingredient(name="sour cream", quantity=None, unit="to taste", optional=True),
    ],
    instructions=[
        "Heat oven to 400 degrees F. Scrub the sweet potatoes and pat to dry. Using a fork, poke holes in the sweet potatoes and arrange them on a baking sheet. Bake at 400 for 45-90 minutes until done.",
        "Allow sweet potatoes to cool slightly (about 10 minutes) before slicing them in half lengthwise. Gently scoop out the filling, leaving a small border along the inside of the sweet potato skins.",
        "Mash together the sweet potato filling with tomato sauce, salt, chili powder, and cumin. Stir in the beans, corn, and ¾ cup of cheese, then spoon the mixture gently back into the skins. Sprinkle with the remaining ¾ cup of cheese.",
        "To bake immediately, bake at 400°F for 10-15 minutes until the cheese is bubbly and melted.",
        "To freeze, cool completely, then wrap in plastic cling wrap and store in a sealed container for up to 3 months.",
        "To reheat from thawed, unwrap and place in a baking dish. Bake uncovered at 425°F for 15-20 minutes until the cheese bubbles and the potatoes are heated through.",
        "For baking from frozen, unwrap and place in a baking dish, cover with foil, and bake at 425°F for 40 minutes, then remove the foil and bake for another 15-20 minutes until the cheese bubbles and the potatoes are heated through.",
    ],
)


grandma_sandy_cannistras_goulash = Recipe(
    title="Grandma Sandy Cannistra's Goulash",
    description="A hearty and comforting dish that brings back memories of home-cooked meals.",
    ingredients=[
        Ingredient(name="beef stew meat", quantity=3, unit="lb"),
        Ingredient(name="onion", quantity=1, unit="pcs", preparation="chopped"),
        Ingredient(name="italian stewed tomatoes", quantity=2, unit="cans"),
        Ingredient(name="wide egg noodles", quantity=12, unit="oz"),
        Ingredient(name="salt", quantity=None, unit="to taste", optional=True),
        Ingredient(name="pepper", quantity=None, unit="to taste", optional=True),
        Ingredient(name="garlic salt", quantity=None, unit="to taste", optional=True),
        Ingredient(name="oregano", quantity=None, unit="to taste", optional=True),
        Ingredient(name="marjoram", quantity=None, unit="to taste", optional=True),
        Ingredient(
            name="parsley flakes", quantity=None, unit="to taste", optional=True
        ),
        Ingredient(name="paprika", quantity=None, unit="to taste", optional=True),
        Ingredient(
            name="grated parmesan cheese", quantity=None, unit="to taste", optional=True
        ),
        Ingredient(name="flour", quantity=None, unit="to taste", optional=True),
        Ingredient(name="olive oil", quantity=None, unit="to taste", optional=True),
        Ingredient(name="beef bouillon cubes", quantity=6, unit="pcs"),
    ],
    instructions=[
        "Rinse beef stew meat and cut into small bite-size pieces, removing any fat. Season the meat to taste with Rupena's Beef & Pork Seasoning, or use salt, pepper, garlic salt, oregano, and marjoram.",
        "Flour the meat generously and brown it in olive oil in a large kettle or electric roasting pot, stirring often. Once browned, add enough water to cover half of the meat and stew for about 1 hour, stirring frequently.",
        "Add 6 beef bouillon cubes, parsley flakes, the Italian stewed tomatoes, and the chopped onion. Cook on low for 4-5 hours.",
        "Serve the goulash over wide egg noodles and top with grated Parmesan cheese.",
    ],
)


guacamole = Recipe(
    title="Guacamole",
    description="Some people call it guac.",
    ingredients=[
        Ingredient(name="avocado", quantity=1, unit="pcs"),
        Ingredient(name="salt", quantity=None, unit="to taste", optional=True),
        Ingredient(
            name="red pepper flakes", quantity=None, unit="to taste", optional=True
        ),
        Ingredient(name="lemon juice", quantity=None, unit=None, optional=True),
    ],
    instructions=[
        "Remove flesh from avocado and roughly mash with a fork.",
        "Season to taste with salt, red pepper flakes, and lemon juice.",
    ],
)

one_pan_mexican_quinoa = Recipe(
    title="One Pan Mexican Quinoa",
    description="A delicious and easy one-pan meal that combines hearty quinoa with Mexican flavors.",
    ingredients=[
        Ingredient(name="olive oil", quantity=1, unit="tablespoon"),
        Ingredient(name="garlic", quantity=2, unit="cloves"),
        Ingredient(name="jalapeno", quantity=1, unit="pcs"),
        Ingredient(name="quinoa", quantity=1, unit="cup"),
        Ingredient(name="vegetable broth", quantity=1, unit="cup"),
        Ingredient(name="black beans", quantity=15, unit="oz"),
        Ingredient(name="diced tomatoes", quantity=1, unit="can"),
        Ingredient(name="corn kernels", quantity=1, unit="cup"),
        Ingredient(name="chili powder", quantity=1, unit="teaspoon"),
        Ingredient(name="cumin", quantity=0.5, unit="teaspoon"),
        Ingredient(
            name="salt and freshly ground black pepper",
            quantity=None,
            unit="to taste",
            optional=True,
        ),
        Ingredient(name="avocado", quantity=1, unit="pcs", preparation="diced"),
        Ingredient(name="lime", quantity=1, unit="pcs", preparation="juiced"),
        Ingredient(name="fresh cilantro leaves", quantity=2, unit="tablespoons"),
    ],
    instructions=[
        "Mince the garlic cloves and jalapeno.",
        "Heat olive oil in a large skillet over medium-high heat. Add garlic and jalapeno, and cook, stirring frequently, until fragrant, about 1 minute.",
        "Stir in quinoa, vegetable broth, beans, tomatoes, corn, chili powder, and cumin; season with salt and pepper, to taste.",
        "Bring to a boil; cover, reduce heat, and simmer until quinoa is cooked through, about 20 minutes.",
        "Stir in avocado, lime juice, and cilantro.",
    ],
)

oriental_salad = Recipe(
    title="Oriental Salad",
    description="A crunchy and flavorful salad that combines unique textures and tastes.",
    ingredients=[
        # Salad ingredients
        Ingredient(name="melted butter", quantity=4, unit="tablespoons"),
        Ingredient(name="Ramen (chicken flavor)", quantity=2, unit="packages"),
        Ingredient(name="sliced almonds", quantity=0.5, unit="cup"),
        Ingredient(name="sunflower seeds", quantity=4.5, unit="tablespoons"),
        Ingredient(name="coleslaw cabbage", quantity=16, unit="oz"),
        Ingredient(name="green onions", quantity=6, unit="pcs"),
        # Dressing ingredients
        Ingredient(name="salad oil", quantity=2 / 3, unit="cup"),
        Ingredient(name="rice vinegar", quantity=4, unit="tablespoons"),
        Ingredient(name="sugar", quantity=4, unit="tablespoons"),
        Ingredient(name="soy sauce", quantity=2, unit="tablespoons"),
        Ingredient(name="pepper", quantity=1, unit="teaspoon"),
        Ingredient(name="ramen chicken flavor packet", quantity=1, unit="pcs"),
    ],
    instructions=[
        "Crush the Ramen packages inside of the package.",
        "Brown the ramen noodles, 1 chicken flavor packet, almonds, and sunflower seeds in the melted butter. Set aside.",
        "Combine the coleslaw cabbage and green onions in a large bowl.",
        "Mix together the salad dressing ingredients. Microwave for 1 minute and let cool.",
        "30 minutes before serving, pour the dressing onto the cabbage and onion mixture. Refrigerate.",
        "Just before serving, mix in the dry ingredients to keep the noodles crunchy.",
    ],
)

pepper_potato_soup = Recipe(
    title="Pepper Potato Soup",
    description="A creamy and hearty soup perfect for chilly days.",
    ingredients=[
        Ingredient(name="water", quantity=4, unit="cups"),
        Ingredient(name="chicken broth cubes", quantity=3, unit="pcs"),
        Ingredient(name="potatoes", quantity=4, unit="pcs", preparation="sliced"),
        Ingredient(name="onion", quantity=1, unit="pcs", preparation="sliced"),
        Ingredient(name="celery", quantity=1, unit="stalk", preparation="sliced"),
        Ingredient(name="salt", quantity=0.5, unit="teaspoon"),
        Ingredient(name="pepper", quantity=0.5, unit="teaspoon"),
        Ingredient(name="half-and-half", quantity=1, unit="cup"),
        Ingredient(name="all-purpose flour", quantity=0.25, unit="cup"),
        Ingredient(name="butter", quantity=1, unit="tablespoon"),
        Ingredient(name="parsley", quantity=None, unit="to taste", optional=True),
    ],
    instructions=[
        "Slice the stalk of celery.",
        "Combine broth, potatoes, onion, celery, salt, and pepper in slow cooker; mix well. Cover and cook on low for 6-7 hours.",
        "Stir half-and-half into flour; stir mixture into slow cooker; cover; cook 1 more hour.",
        "Slightly mash potato mixture with potato masher. Cook, uncovered, 30 minutes or until slightly thickened.",
        "Just before serving, stir in butter. Garnish with celery leaves and parsley.",
    ],
)


pho = Recipe(
    title="Pho",
    description="A delicious Vietnamese noodle soup that combines fragrant broth with tender steak and fresh toppings.",
    ingredients=[
        Ingredient(name="olive oil", quantity=3, unit="tbsp"),
        Ingredient(name="onion", quantity=1, unit="pcs", preparation="diced"),
        Ingredient(name="garlic", quantity=1, unit="clove", preparation="minced"),
        Ingredient(name="ginger", quantity=1, unit="pcs", preparation="minced"),
        Ingredient(name="beef broth", quantity=4, unit="cups"),
        Ingredient(name="water", quantity=1, unit="cup"),
        Ingredient(name="striploin steak", quantity=1, unit="pcs"),
        Ingredient(name="red curry paste", quantity=1, unit="tbsp"),
        Ingredient(name="lemon juice", quantity=1, unit="tsp"),
        Ingredient(name="lime", quantity=1, unit="pcs", preparation="juiced"),
        Ingredient(name="soy sauce", quantity=2, unit="tbsp"),
        Ingredient(name="fish sauce", quantity=0.5, unit="tsp"),
        Ingredient(name="chili paste", quantity=1, unit="tbsp"),
        Ingredient(name="salt", quantity=None, unit="to taste", optional=True),
        Ingredient(name="pepper", quantity=None, unit="to taste", optional=True),
        Ingredient(name="rice noodles", quantity=0.5, unit="package"),
        Ingredient(name="cilantro", quantity=1, unit="bunch"),
        Ingredient(name="green onions", quantity=3, unit="pcs", preparation="chopped"),
        Ingredient(name="bean sprouts", quantity=1, unit="handful"),
    ],
    instructions=[
        "Start by marinating steak with 1/2 tbsp red curry paste combined with olive oil, salt, and pepper. Set aside.",
        "Heat 1 1/2 tbsp of olive oil in a large pot with a fitted lid on medium-high heat. Sauté onion, garlic, and ginger for 5 minutes, until fragrant and softened.",
        "Add the other 1/2 tbsp of red curry paste and sauté for 2 minutes. Add broth and water, bringing to a boil. Add lemon and lime juices, soy sauce, chili paste, and fish sauce. Simmer for 15 minutes with the lid on.",
        "During this time, garnishes can be chopped and prepared.",
        "After preparing garnishes and placing them in small bowls so guests can self-serve, heat remaining oil over high heat until it starts to smoke. Cook steak for 1-2 minutes on each side, or until cooked rare to medium-rare (it will cook more in the hot soup). Let rest for 5 minutes, then slice into thin strips.",
        "Bring soup back to a boil and add rice noodles, cooking for 3-5 minutes. If possible, remove noodles from the broth to prevent them from soaking it all up.",
        "Serve pho in large bowls with noodles, broth, and steak, garnishing with chopped cilantro and bean sprouts as desired. Cut additional limes as garnish as well.",
    ],
)

salsa = Recipe(
    title="Salsa",
    description="A fresh and spicy dip perfect for chips or as a topping for your favorite dishes.",
    ingredients=[
        Ingredient(name="roma tomato", quantity=12, unit="pcs"),
        Ingredient(name="serrano", quantity=7, unit="pcs"),
        Ingredient(name="yellow onion", quantity=2, unit="pcs"),
        Ingredient(name="garlic", quantity=8, unit="cloves"),
        Ingredient(name="cilantro", quantity=1, unit="bunch"),
        Ingredient(name="lime", quantity=1, unit="pcs"),
        Ingredient(name="salt", quantity=None, unit="to taste", optional=True),
    ],
    instructions=[
        "Roast vegetables at 375F for 20 minutes (until the onions begin to brown).",
        "Blend with cilantro.",
        "Add lime juice.",
        "Salt to taste.",
    ],
)

shrimp_with_curried_pasta = Recipe(
    title="Shrimp with Curried Pasta",
    description="A delightful dish that combines the richness of shrimp with a fragrant curried lime butter sauce, served over fresh fettuccine.",
    ingredients=[
        Ingredient(name="butter", quantity=4, unit="tbsp"),
        Ingredient(name="lime", quantity=0.5, unit="pcs"),
        Ingredient(name="curry powder", quantity=2, unit="tsp"),
        Ingredient(name="ground ginger", quantity=0.5, unit="tsp"),
        Ingredient(name="salt", quantity=None, unit="to taste", optional=True),
        Ingredient(name="pepper", quantity=None, unit="to taste", optional=True),
        Ingredient(name="shrimp", quantity=1, unit="lb"),
        Ingredient(name="vegetable oil", quantity=2, unit="tbsp"),
        Ingredient(name="butter", quantity=2, unit="tbsp"),
        Ingredient(name="onion", quantity=1, unit="pcs", preparation="minced"),
        Ingredient(name="chicken broth", quantity=1, unit="cup"),
        Ingredient(name="dry white wine", quantity=1, unit="cup"),
        Ingredient(name="fresh fettuccine", quantity=1, unit="lb"),
        Ingredient(name="plain yogurt", quantity=2 / 3, unit="cup"),
        Ingredient(name="green onions", quantity=3, unit="pcs", preparation="chopped"),
        Ingredient(name="cashew", quantity=4, unit="oz", preparation="halved"),
    ],
    instructions=[
        "Soften butter and peel and de-vein shrimp.",
        "Blend the 4 tbsp butter with the lime juice, zest, curry powder, and ginger. Season with salt and pepper. Set aside to prepare the curried lime butter.",
        "Heat the oil in a sauté pan over high heat. Add the shrimp and season with salt and pepper. Sauté the shrimp until cooked through, about 4-5 minutes. Remove the shrimp from the pan with a slotted spoon and set aside.",
        "In parallel, bring a large pot of salted water to a boil. Add the pasta and boil until tender, approximately 1-2 minutes. Drain immediately.",
        "Add the 2 tbsp butter to the pan with the shrimp and heat until foaming subsides. Add the onion and sauté, stirring frequently until translucent, about 2-3 minutes.",
        "Stir in the broth and wine to deglaze the pan, scraping up any browned bits from the bottom. Let simmer until reduced by one-fourth, approximately 4-5 minutes.",
        "Gradually whisk in the curry-lime butter until the mixture is smooth; it may appear broken at first but will come together as it cooks. Cover to keep warm while preparing the pasta.",
        "Once the pasta is finished, bring the sauce back to a simmer and whisk in the yogurt. Add the hot pasta to the sauce and lift/toss to coat evenly. Season with salt and pepper to taste.",
        "Transfer the pasta to a bowl, top with shrimp, and spoon the remaining sauce over the shrimp. Garnish with chopped green onion and cashew halves.",
    ],
)


shrimp_pad_thai_bowl = Recipe(
    title="Shrimp Pad Thai Bowl",
    description="A flavorful Thai classic dish featuring shrimp and rice noodles, enhanced with a tangy lime sauce.",
    ingredients=[
        Ingredient(name="limes", quantity=4, unit="pcs", preparation="juiced"),
        Ingredient(name="dark brown sugar", quantity=10, unit="tablespoons"),
        Ingredient(name="fish sauce", quantity=4, unit="tablespoons"),
        Ingredient(name="vegetable oil", quantity=10, unit="tablespoons"),
        Ingredient(name="rice vinegar", quantity=8, unit="teaspoons"),
        Ingredient(name="cayenne pepper", quantity=1, unit="teaspoon"),
        Ingredient(name="rice noodles", quantity=16, unit="ounces"),
        Ingredient(name="green onions", quantity=8, unit="pcs", preparation="minced"),
        Ingredient(name="garlic cloves", quantity=4, unit="pcs", preparation="minced"),
        Ingredient(name="table salt", quantity=1, unit="pinch"),
        Ingredient(name="eggs", quantity=4, unit="large"),
        Ingredient(name="shrimp", quantity=1.5, unit="cups"),
        Ingredient(name="bean sprouts", quantity=8, unit="ounces"),
        Ingredient(name="peanuts", quantity=8, unit="oz"),
        Ingredient(name="cilantro", quantity=1, unit="bunch"),
        Ingredient(name="Thai chili jam", quantity=1, unit="scoop"),
    ],
    instructions=[
        "Whisk lime juice, 3 tablespoons water, sugar, fish sauce, 6 tablespoons oil, vinegar, and cayenne together in a bowl; set aside.",
        "Pour 2 quarts boiling water over noodles in a bowl and stir to separate. Let noodles soak until soft and pliable but not fully tender, stirring once halfway through soaking, 8 to 10 minutes. Drain noodles and rinse with cold water until water runs clear, shaking to remove excess water.",
        "Sauté shrimp.",
        "Heat remaining 4 tablespoons oil in a 10-inch nonstick skillet over medium-high heat until shimmering. Add lower-half green onion, garlic, and salt and cook over medium heat, stirring constantly, until onion is light golden brown, about 1.5 minutes.",
        "Lightly beat eggs. Stir in egg and cook, stirring vigorously, until scrambled and barely moist, about 20 seconds.",
        "Add drained rice noodles and toss to combine. Add lime mixture and half of the upper-half green onion, increase heat to medium-high, and cook, tossing gently, until noodles are well coated and tender, about 3 minutes. (If not yet tender, add 6-8 tablespoons water to skillet and continue to cook until tender).",
        "Season with salt and pepper to taste. Divide among individual serving bowls, then top with shrimp and bean sprouts and sprinkle with remaining green onion. Serve with garnish as desired.",
    ],
)


slow_cooker_chicken_and_rice = Recipe(
    title="Slow Cooker Chicken and Rice",
    description="A comforting dish that's easy to prepare and perfect for busy days.",
    ingredients=[
        Ingredient(name="cream of chicken soup", quantity=3, unit="cans"),
        Ingredient(name="rice", quantity=2, unit="cups"),
        Ingredient(name="water", quantity=1, unit="cup"),
        Ingredient(name="frozen chicken breasts", quantity=1, unit="lb"),
        Ingredient(name="salt", quantity=0.5, unit="teaspoon"),
        Ingredient(name="paprika", quantity=0.25, unit="teaspoon"),
        Ingredient(name="black pepper", quantity=0.25, unit="teaspoon"),
        Ingredient(name="diced celery", quantity=0.5, unit="cup"),
    ],
    instructions=[
        "Combine soup, dry rice, and water in a Crock-Pot slow cooker.",
        "Add chicken; sprinkle with salt, paprika, and pepper.",
        "Sprinkle celery over chicken.",
        "Cover; cook on LOW for 6 to 8 hours or on HIGH for 3 to 4 hours.",
    ],
)

tex_mex_beef_wraps = Recipe(
    title="Tex-Mex Beef Wraps",
    description="A delicious and filling dish that's perfect for a family meal or gathering.",
    ingredients=[
        Ingredient(name="chili powder", quantity=1, unit="tablespoon"),
        Ingredient(name="cumin", quantity=2, unit="teaspoons"),
        Ingredient(name="salt", quantity=1, unit="teaspoon"),
        Ingredient(name="red pepper", quantity=0.25, unit="teaspoon"),
        Ingredient(name="boneless beef chuck pot roast", quantity=3, unit="pounds"),
        Ingredient(name="onion", quantity=1, unit="pcs", preparation="chopped"),
        Ingredient(name="garlic cloves", quantity=3, unit="pcs", preparation="minced"),
        Ingredient(name="salsa", quantity=1, unit="cup"),
        Ingredient(name="tortillas", quantity=None, unit="to serve", optional=True),
        Ingredient(
            name="shredded Cheddar or Monterey Jack cheese", quantity=1, unit="cup"
        ),
        Ingredient(name="chopped tomato", quantity=1, unit="cup"),
        Ingredient(name="cilantro", quantity=0.25, unit="cup"),
        Ingredient(name="avocado", quantity=1, unit="pcs", preparation="diced"),
    ],
    instructions=[
        "Cut chuck pot roast into 4 pieces.",
        "Blend chili powder, cumin, salt, and red pepper. Rub meat all over with spice mixture.",
        "Place onion and garlic in the bottom of Crock-Pot slow cooker; top with meat. Spoon 1/2 cup salsa over meat. Cover and cook on LOW for 8 to 9 hours or on HIGH for 3 1/2 to 4 1/2 hours.",
        "Remove meat from Crock-Pot slow cooker. Shred with two forks. Skim fat from cooking liquid and discard. Return shredded meat to Crock-Pot slow cooker and mix well. Adjust seasonings.",
        "Place meat on warm tortillas; top with cheese, tomato, cilantro, and avocado. Roll up to enclose filling. Serve with remaining salsa.",
    ],
)

tuna_noodle_casserole = Recipe(
    title="Tuna Noodle Casserole",
    description="A creamy and hearty casserole that brings comfort to your dinner table.",
    ingredients=[
        Ingredient(name="macaroni", quantity=5, unit="cups"),
        Ingredient(name="cream of mushroom soup", quantity=1, unit="can"),
        Ingredient(name="tuna", quantity=3, unit="cans"),
        Ingredient(name="frozen peas", quantity=2, unit="cups"),
        Ingredient(name="mayo", quantity=1, unit="cup"),
        Ingredient(
            name="shredded cheese", quantity=None, unit="to taste", optional=True
        ),
        Ingredient(name="bread crumbs", quantity=None, unit="to taste", optional=True),
    ],
    instructions=[
        "Cook macaroni noodles.",
        "Combine all ingredients except for cheese and bread crumbs in a 9x13 dish.",
        "Top with bread crumbs and shredded cheese.",
        "Bake at 400 degrees Fahrenheit for 30 minutes.",
    ],
)

white_bean_chili = Recipe(
    title="White Bean Chili",
    description="A delicious vegetarian chili",
    ingredients=[
        Ingredient(name="vegetable oil", quantity=None, unit=None, optional=True),
        Ingredient(name="onion", quantity=1, unit="pcs", preparation="diced"),
        Ingredient(name="green pepper", quantity=1, unit="pcs", preparation="diced"),
        Ingredient(
            name="jalapeno peppers", quantity=2, unit="pcs", preparation="diced"
        ),
        Ingredient(name="garlic", quantity=6, unit="cloves"),
        Ingredient(name="cumin", quantity=2, unit="tbsp"),
        Ingredient(name="diced tomatoes", quantity=1, unit="can"),
        Ingredient(name="white beans", quantity=2, unit="cans"),
        Ingredient(name="chicken stock", quantity=3, unit="cups"),
        Ingredient(name="lime", quantity=2, unit="pcs", preparation="juiced"),
        Ingredient(name="cilantro", quantity=1, unit="bunch"),
        Ingredient(name="salt", quantity=None, unit="to taste", optional=True),
    ],
    instructions=[
        "Place oil, onion, green pepper, and jalapenos in a large saucepan and sauté over medium heat for 7-8 minutes.",
        "Add garlic and cumin. Cook for 2 more minutes.",
        "Add diced tomatoes, white beans, and vegetable/chicken stock. Bring to a boil over high heat.",
        "Reduce the heat to medium and cook, covered, for 25 minutes.",
        "Stir in lime juice, chopped cilantro, and salt to taste before serving.",
    ],
)

recipe_seeds = [
    baked_honey_mustard_chicken,
    asian_beef_stew,
    bean_stuff,
    carrot_cake,
    enchilada_stuffed_sweet_potatoes,
    grandma_sandy_cannistras_goulash,
    guacamole,
    one_pan_mexican_quinoa,
    oriental_salad,
    pepper_potato_soup,
    pho,
    salsa,
    shrimp_with_curried_pasta,
    shrimp_pad_thai_bowl,
    slow_cooker_chicken_and_rice,
    tex_mex_beef_wraps,
    tuna_noodle_casserole,
    white_bean_chili,
]
