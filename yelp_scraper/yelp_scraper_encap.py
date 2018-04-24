from yelp_scraper_cu import *
from yelp_scraper_la import *
from yelp_scraper_nyc import *
import datetime

# with open("timelog.txt", "a") as myfile:
#     myfile.write("{0:<20}START {1}\n".format("CU PLACE ",datetime.datetime.now().strftime("%H:%M:%S")))
# CU_PLACE()
# with open("timelog.txt", "a") as myfile:
#     myfile.write("{0:<20}DONE {1}\n".format("CU PLACE ",datetime.datetime.now().strftime("%H:%M:%S")))
# CU_REST()
# with open("timelog.txt", "a") as myfile:
#     myfile.write("CU REST {}DONE \t\t"+datetime.datetime.now().strftime("%H:%M:%S")+"\n")
with open("timelog.txt", "a") as myfile:
    myfile.write("{0:<20}START {1}\n".format("LA PLACE ",datetime.datetime.now().strftime("%H:%M:%S")))
LA_PLACE()
with open("timelog.txt", "a") as myfile:
    myfile.write("{0:<20}DONE {1}\n".format("LA PLACE ",datetime.datetime.now().strftime("%H:%M:%S")))

with open("timelog.txt", "a") as myfile:
    myfile.write("{0:<20}START {1}\n".format("LA REST ",datetime.datetime.now().strftime("%H:%M:%S")))
LA_REST()
with open("timelog.txt", "a") as myfile:
    myfile.write("{0:<20}DONE {1}\n".format("LA REST ",datetime.datetime.now().strftime("%H:%M:%S")))

with open("timelog.txt", "a") as myfile:
    myfile.write("{0:<20}START {1}\n".format("NYC PLACE ",datetime.datetime.now().strftime("%H:%M:%S")))
NYC_PLACE()
with open("timelog.txt", "a") as myfile:
    myfile.write("{0:<20}DONE {1}\n".format("NYC PLACE ",datetime.datetime.now().strftime("%H:%M:%S")))

with open("timelog.txt", "a") as myfile:
    myfile.write("{0:<20}START {1}\n".format("NYC REST ",datetime.datetime.now().strftime("%H:%M:%S")))
NYC_REST()
with open("timelog.txt", "a") as myfile:
    myfile.write("{0:<20}DONE {1}\n".format("NYC REST ",datetime.datetime.now().strftime("%H:%M:%S")))
