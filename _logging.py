"""
Unit Converter Software
Developer: Rinkesh Patel
Contact: www.rinkesh.ca
Version: 1.0.0
Change Log: Please refer to Version.md file
"""
import logging

logging.basicConfig(filename='log.log', 
                    filemode='w+', format='%(name)s - %(levelname)s - %(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S', 
                    level=logging.INFO)
def main():
    pass

def _log(mode="d", _msg=""):
    match mode:
        case "d":
            logging.debug(_msg)
        case "i":
            logging.info(_msg)
        case "w":
            logging.warning(_msg)
        case "e":
            logging.error(_msg, exc_info=True)
        case "c":
            logging.critical(_msg)

if __name__ == "__main__":
    main()
