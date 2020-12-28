from pypresence import Presence
import time


client_id = "793045429629353995"
RPC = Presence(client_id)

RPC.connect()
RPC.update(pid=7640, state="Zoom class grind!", large_image="large", small_image="small", large_text="Zoom")



while True:
    time.sleep(15)