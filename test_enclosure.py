import pytest
from animal import Mammal, Bird, Reptile
from enclosure import Enclosure

# ENCLOSURE CREATION TEST
def test_enclosure_creation_display():
    mammal_enc = Enclosure("Savannah", 500, "savannah", Mammal)
    bird_enc = Enclosure("Aviary", 200, "arctic", Bird)
    reptile_enc = Enclosure("Reptile House", 150, "desert", Reptile)

    print(f"\nCreated Mammal enclosure: {mammal_enc._name}, Size: {mammal_enc._size}, Env: {mammal_enc._environment_type}")
    print(f"Created Bird enclosure:   {bird_enc._name}, Size: {bird_enc._size}, Env: {bird_enc._environment_type}")
    print(f"Created Reptile enclosure:{reptile_enc._name}, Size: {reptile_enc._size}, Env: {reptile_enc._environment_type}")

    assert mammal_enc._size > 0
    assert bird_enc._size > 0
    assert reptile_enc._size > 0

# ADDING VALID ANIMALS
def test_add_animal_display():
    mammal_enc = Enclosure("Savannah", 500, "savannah", Mammal)
    lion = Mammal("Leo", "Lion", 5, "meat", "savannah")
    mammal_enc.add_animal(lion)

    print(f"\nMammal enclosure animals: {[a._name for a in mammal_enc._animals]}")
    assert lion.get_enclosure() == mammal_enc

# -PREVENT ANIMAL UNDER TREATMENT
def test_add_animal_under_treatment():
    mammal_enc = Enclosure("Savannah", 500, "savannah", Mammal)
    sick_lion = Mammal("Simba", "Lion", 3, "meat", "savannah")
    sick_lion.add_health_record("Under Treatment – leg injury")

    with pytest.raises(ValueError) as e:
        mammal_enc.add_animal(sick_lion)

    print("\nCaught error adding animal under treatment:", e.value)
    assert "Simba the Lion is under treatment and cannot be added." in str(e.value)

# HEALTH SUMMARY TEST
def test_health_summary():
    mammal_enc = Enclosure("Savannah", 500, "savannah", Mammal)
    healthy_lion = Mammal("Leo", "Lion", 5, "meat", "savannah")
    sick_lion = Mammal("Simba", "Lion", 3, "meat", "savannah")
    sick_lion.add_health_record("Under Treatment – leg injury")

    mammal_enc.add_animal(healthy_lion)
    with pytest.raises(ValueError):
        mammal_enc.add_animal(sick_lion)

    summary = mammal_enc.get_health_summary()
    print("\nHealth summary:", summary)
    assert summary == {"Leo": "Healthy"}

# HEALTH SUMMARY MULTIPLE ANIMALS
def test_health_summary_multiple_animals():
    mammal_enc = Enclosure("Savannah", 500, "savannah", Mammal)
    healthy_lion = Mammal("Leo", "Lion", 5, "meat", "savannah")
    healthy_elephant = Mammal("Ella", "Elephant", 10, "plants", "savannah")
    sick_lion = Mammal("Simba", "Lion", 3, "meat", "savannah")
    sick_lion.add_health_record("Under Treatment – leg injury")

    mammal_enc.add_animal(healthy_lion)
    mammal_enc.add_animal(healthy_elephant)
    with pytest.raises(ValueError):
        mammal_enc.add_animal(sick_lion)

    summary = mammal_enc.get_health_summary()
    print("\nHealth summary with multiple animals:", summary)
    assert summary == {"Leo": "Healthy", "Ella": "Healthy"}

# INVALID ANIMAL TYPE TEST
def test_add_invalid_animal_type():
    mammal_enc = Enclosure("Savannah", 500, "savannah", Mammal)
    percy = Bird("Percy", "Penguin", 2, "fish", "arctic")

    with pytest.raises(TypeError) as e:
        mammal_enc.add_animal(percy)

    print("\nCaught error adding invalid animal type:", e.value)
    assert "only accepts Mammal" in str(e.value)

# ENVIRONMENT MISMATCH TEST
def test_add_invalid_environment():
    bird_enc = Enclosure("Aviary", 200, "arctic", Bird)
    wrong_env_bird = Bird("Sunny", "Parrot", 3, "seeds", "tropical")

    with pytest.raises(ValueError) as e:
        bird_enc.add_animal(wrong_env_bird)

    print("\nCaught environment mismatch error:", e.value)
    assert "requires a 'tropical' environment" in str(e.value)

# DUPLICATE ANIMAL TEST
def test_prevent_duplicate_animal():
    mammal_enc = Enclosure("Savannah", 500,"savannah", Mammal)
    lion = Mammal("Leo", "Lion", 5, "meat", "savannah")
    mammal_enc.add_animal(lion)

    with pytest.raises(ValueError) as e:
        mammal_enc.add_animal(lion)

    print("\nCaught duplicate animal error:", e.value)
    assert "already in this enclosure" in str(e.value)

# REMOVE ANIMAL TEST
def test_remove_animal_display():
    reptile_enc = Enclosure("Reptile House", 150, "desert", Reptile)
    snake = Reptile("Sly", "Snake", 4, "rodents", "desert")

    reptile_enc.add_animal(snake)
    reptile_enc.remove_animal(snake)

    print("\nReptile enclosure after removal:", [a._name for a in reptile_enc._animals])
    assert snake not in reptile_enc._animals
    assert snake.get_enclosure() is None

# CLEAN ENCLOSURE TEST
def test_clean_enclosure_display():
    mammal_enc = Enclosure("Savannah", 500, "savannah", Mammal)
    mammal_enc._cleanliness = 30

    print("\nBefore cleaning:", mammal_enc._cleanliness)
    mammal_enc.clean()
    print("After cleaning:", mammal_enc._cleanliness)

    assert mammal_enc._cleanliness == 100

# STATUS TEST
def test_get_status_display():
    bird_enc = Enclosure("Aviary", 200, "arctic", Bird)
    percy = Bird("Percy", "Penguin", 2, "fish", "arctic")

    bird_enc.add_animal(percy)
    status = bird_enc.get_status()

    print("\nBird enclosure status:", status)
    assert status["name"] == "Aviary"
    assert status["animals"] == ["Percy"]
    assert status["environment"] == "arctic"
    assert status["cleanliness"] == 100

# STATUS MULTIPLE ANIMALS
def test_get_status_display_multiple_animals():
    bird_enc = Enclosure("Aviary", 200, "arctic", Bird)
    percy = Bird("Percy", "Penguin", 2, "fish", "arctic")
    parrot = Bird("Sunny", "Parrot", 3, "seeds", "arctic")

    bird_enc.add_animal(percy)
    bird_enc.add_animal(parrot)
    status = bird_enc.get_status()

    print("\nBird enclosure status with multiple animals:", status)
    assert status["name"] == "Aviary"
    assert status["environment"] == "arctic"
    assert status["cleanliness"] == 100
    assert status["animals"] == ["Percy", "Sunny"]

# EMPTY ENCLOSURE STATUS
def test_get_status_empty_enclosure_display():
    reptile_enc = Enclosure("Reptile House", 150, "desert", Reptile)
    status = reptile_enc.get_status()

    print("\nEmpty reptile enclosure status:", status)
    assert status["animals"] == []
    assert status["cleanliness"] == 100

# INVALID SIZE TEST
def test_invalid_enclosure_size():
    with pytest.raises(ValueError) as e:
        Enclosure("Tiny", 0, "desert", Mammal)

    print("\nCaught invalid size error:", e.value)
    assert "must be positive" in str(e.value)


