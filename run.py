from src.main import main


def run():
    main(metric_object={"metric_names": ["totalUsers"], "dimension_names": ["country", "date"]})
    

run()
