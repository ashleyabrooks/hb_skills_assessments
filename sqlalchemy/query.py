"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?

# The datatype of the returned value is a Flask SQLAlchemy query object. 


# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?

# An association table is a table that exists for the sole purpose of 
# connecting two tables. Unlike a middle table which contributes valuable
# columns, an association table only holds columns that already exist in the 
# two tables it's connecting. This type of table is used when there's a 
# many to many relationship between two tables. 


# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the ``id`` of "ram."
q1 = db.session.query(Brand).filter(Brand.brand_id == 'ram').one()

# Get all models with the name "Corvette" and the brand_id "che."
q2 = db.session.query(Model).filter(Model.brand_id == 'che').filter(Model.name == 'Corvette').all()

# Get all models that are older than 1960.
q3 = db.session.query(Model).filter(Model.year > 1960).all()

# Get all brands that were founded after 1920.
q4 = db.session.query(Brand).filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor."
q5 = db.session.query(Model).filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = db.session.query(Brand).filter(Brand.founded == 1903).filter(Brand.discontinued == None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = db.session.query(Brand).filter((Brand.discontinued != None) | (Brand.founded < 1950)).all()

# Get any model whose brand_id is not "for."
q8 = db.session.query(Model).filter(Model.brand_id != 'for').all()



# -------------------------------------------------------------------
# Part 4: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    model_info = db.session.query(Model.name, 
                                  Brand.name, 
                                  Brand.headquarters).join(Brand).filter(Model.year == year).all()

    for model in model_info:
        print 'Model Name: %s, Brand Name: %s, Brand HQ: %s' % (model[0], 
                                                                model[1], 
                                                                model[2])


def get_brands_summary():
    """Prints out each brand name and each model name with year for that brand
    using only ONE database query."""

    brands_summary = db.session.query(Brand.name, 
                                      Model.name, 
                                      Model.year).join(Model).all()

    brands_and_models = {}

    # unpack brands_summary and add data to dict brands_and_models
    for brand in brands_summary:
        brand_name, model_name, model_year = brand
        
        if brand_name in brands_and_models:
            brands_and_models[brand_name].append((model_name, model_year))
        else:
            brands_and_models[brand_name] = [(model_name, model_year)]

    # print brand once followed by list of models/years
    for brand, models_years in brands_and_models.items():
        print '\nBRAND:' + brand
        for model_year in models_years:
            print '%s, %s' % (model_year[0], model_year[1])


def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    return db.session.query(Brand).filter(Brand.name.like('%' + mystr + '%')).all()


def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    return db.session.query(Model).filter(Model.year > start_year).filter(Model.year < end_year).all()

