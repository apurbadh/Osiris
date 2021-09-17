from dash import Base,engine,Doctor


# Only Creates DB, We Wouldnt want to create the database all the time now would we?
Base.metadata.create_all(engine)

