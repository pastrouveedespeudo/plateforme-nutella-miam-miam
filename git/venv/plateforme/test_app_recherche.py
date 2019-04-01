import mes_aliments.algo_open  as script



def test_image():
    parametre = 'Chocolat au lait'
    sortie = [('https://static.openfoodfacts.org/images/products/301/776/082/6174/front_fr.5.400.jpg', 'chocolat au lait'), ('https://static.openfoodfacts.org/images/products/301/776/082/6174/front_fr.5.400.jpg', 'chocolat au lait'), ('https://static.openfoodfacts.org/images/products/301/776/082/6174/front_fr.5.400.jpg', 'chocolat au lait')]
    assert script.image_aliment(parametre) == sortie
    
def test_image2():
    parametre = 'chocolat au lait'
    sortie = [('https://static.openfoodfacts.org/images/products/301/776/082/6174/front_fr.5.400.jpg', 'chocolat au lait'), ('https://static.openfoodfacts.org/images/products/301/776/082/6174/front_fr.5.400.jpg', 'chocolat au lait'), ('https://static.openfoodfacts.org/images/products/301/776/082/6174/front_fr.5.400.jpg', 'chocolat au lait')]
    assert script.image_aliment(parametre) == sortie

def test_titre_aliment():
    parametre = 'chocolat au lait'
    sortie = [('chocolat au lait',), ('chocolat au lait',), ('chocolat au lait',)]
    assert script.titre_aliment(parametre) == sortie


def test_better_nutri():
    parametre = 'chocolat au lait'
    sortie = [('chocolat au lait', 3, 'e', 'https://static.openfoodfacts.org/images/products/301/776/082/6174/front_fr.5.400.jpg', 32), ('chips saveur wasabi', 3, 'c', 'https://static.openfoodfacts.org/images/products/322/247/504/9941/front_fr.8.400.jpg', 65), ('chips saveur wasabi', 3, 'c', 'https://static.openfoodfacts.org/images/products/322/247/504/9941/front_fr.8.400.jpg', 25), ('chocolat noir 70%', 3, 'c', 'https://static.openfoodfacts.org/images/products/303/349/030/6014/front_fr.57.400.jpg', 77), ('chocolat noir 70%', 3, 'c', 'https://static.openfoodfacts.org/images/products/303/349/030/6014/front_fr.57.400.jpg', 37), ('chips saveur wasabi', 3, 'c', 'https://static.openfoodfacts.org/images/products/322/247/504/9941/front_fr.8.400.jpg', 118)]
    assert script.better_nutri(parametre) == sortie


def test_better_nutri2():
    parametre = 'Chocolat au lait'
    sortie = [('chocolat au lait', 3, 'e', 'https://static.openfoodfacts.org/images/products/301/776/082/6174/front_fr.5.400.jpg', 32), ('chips saveur wasabi', 3, 'c', 'https://static.openfoodfacts.org/images/products/322/247/504/9941/front_fr.8.400.jpg', 65), ('chips saveur wasabi', 3, 'c', 'https://static.openfoodfacts.org/images/products/322/247/504/9941/front_fr.8.400.jpg', 25), ('chocolat noir 70%', 3, 'c', 'https://static.openfoodfacts.org/images/products/303/349/030/6014/front_fr.57.400.jpg', 77), ('chocolat noir 70%', 3, 'c', 'https://static.openfoodfacts.org/images/products/303/349/030/6014/front_fr.57.400.jpg', 37), ('chips saveur wasabi', 3, 'c', 'https://static.openfoodfacts.org/images/products/322/247/504/9941/front_fr.8.400.jpg', 118)]
    assert script.better_nutri(parametre) == sortie


