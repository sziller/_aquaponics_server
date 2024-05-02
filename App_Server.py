"""=== App-interface to start SmartHomeMyCastle Server =======================================
Call this python script as:
python3 App_Server.py
============================================================================ by Sziller ==="""
# #!/home/sziller/Projects/008_Aquaponics/_aquaponics_server/venv/bin/python

import os
import uvicorn
from dotenv import load_dotenv
from shmc_server import Server_SmartHomeMyCastle

if __name__ == "__main__":
    load_dotenv()
    # <server> is the parent scope. You need to run <server> It includes "/" path to serve Static Pages
    # do not define logger info!
    
    uvicorn.run(Server_SmartHomeMyCastle.server, host=os.getenv("SRV_IP"), port=int(os.getenv("SRV_PORT")))
    
