# You will be using this file to write your own program. 
# You will have access to the internet during this portion, with the exception of Artificial Intelligence.

# You have 30 minutes.
# Step 1: Research
# Step 2: Plan
# Step 3: Code
# Step 4: Debug

import asyncio
from mavsdk import System

async def main():
    drone = System("udpin://0.0.0.0:14540")

if __name__ == "__main__":
    asyncio.run(main)
