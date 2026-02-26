from open_bus_stride_db import db

def main():
    with db.get_session() as session:
        print("Refreshing gtfs_rides_agg materialized view")
        session.execute("refresh materialized view concurrently gtfs_rides_agg")
        session.commit()
        print("Refreshing gtfs_rides_agg_by_hour materialized view")
        session.execute("refresh materialized view concurrently gtfs_rides_agg_by_hour")
        session.commit()
