import faker as fk

for _ in range(10):
    print(fk.Faker().name())
    print(fk.Faker().address())
    print(fk.Faker().year())
    print(fk.Faker().last_name())
    print(fk.Faker().password())
    print(fk.Faker().count())