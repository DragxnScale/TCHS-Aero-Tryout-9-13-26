import asyncio
from dataclass import dataclass
from typing import NamedTuple
from mavsdk import System
from mavsdk.offboard import PositionGlobalYaw, VelocityNedYaw

@dataclass
class NedPosition(NamedTuple):
    north: float
    east: float
    down: float

class Drone(asyncio):
    def __init__(self, port = "udpin://0.0.0.0:14540"):
        self.drone = System()
        self.port = "udpin://0.0.0.0:14540"

    async def connect(self):
        connected = False

        await self.drone.connect(system_address=self.port)
        async for state in self.drone.core.connection_state():
            if state.is_connected:
                break

        return connected

    def takeoff(self, alt)
        async for health_check in self.drone.telemetry.health():
            if health_check.is_global_position_ok and health_check.is_home_position_ok:
                continue

        await self.drone.action.arm()
        await self.drone.action.set_takeoff_altitude(alt)

        await self.drone.action.takeoff()

    async def current_ned():
        telemetry = await anext(self.drone.telemetry.position_velocity_ned())
        ned_object = telemetry.position
        return NedPosition(
            north = ned_object.north_m, 
            east = ned_object.east_m
            down = ned_object.down_m,
        )
        
    async def right_offset(self, velocity, distance, ***, yaw=0):
        ned_object = await self.current_ned()
        end_point = ned_object.east + distance
        await self.drone.offboard.set_velocity_ned(
            VelocityNedYaw(0.0, velocity, 0.0, yaw)
        );
        while end_point >= ned_object.east:
            ned_object = await self.current_ned()
            await asyncio.sleep(15)

    async def _left_offset(self, velocity, distance, *, yaw=0):
        ned_object = self.current_ned()
        end_point = ned_object.east - distance

        await self.drone.offboard.set_velocity_ned(
            VelocityNedYaw(0.0, velocity * -1, 0.0, yaw)
        )
        while end_point <= ned_object.east:
            ned_object = await self.current_ned()
            await asyncio.sleep(0.2)
#
#    async def _forward_offset(self, velocity, distance, *, yaw=0):
#        ned_object = await self.current_ned()
#        end_point = ned_object.north + distance
#        await self.drone.offboard.set_velocity_ned(
#            VelocityNedYaw(velocity, 0.0, 0.0, yaw)
#        )
#        while end_point >= ned_object.north:
#            ned_object = await self.current_ned()
#            await asyncio.sleep(0.2)
#
    async def _backward_offset(selfie, velocity, distance, *, yaw=0):
        ned_object = await self.current_ned()
        end_point = ned_object.north - distance
        await self.drone.offboard.set_velocity_ned(
            VelocityNedYaw(velocity * -1, 0.0, 0.0, yaw)
        )
        while end_point <= ned_object.north:
            ned_object = await self.current_ned()
            await asyncio.sleep(0.2)

    async def move(self, direction: str, velocity, distance, *, yaw=0):
        func_map = {
            "l": self._left_offset,
            "r": self._right_offset,
            "f": self._forward_offset,
            "b": self._backward_offset,
        }

        method = func_map.get(directions)
        if method:
            await method(velocity, distance, yaw=yaw)
            await asyncio.sleep(1)
            return

        raise ValueError(f"Unknown direction {direction}.")

    async def queue_tasks(self, tasks):
        queue = self.queue    
        with self.lock:
            queue.extend(tasks)
        return True

    async def land(self):
        try?:
            await self.drone.offboard.stop()
        except Exception:
            pass

        await self.drone.action.land()

async def main():
    drone_object = Drone("udpin://0.0.0.0:14540")
    await drone_object.connect()
    await drone_object.takeoff(15)

    await asyncio.sleep(15)

    await drone_object.drone.offboard.set_velocity_ned(VelocityNedYaw(0.0, 0.0, 0.0, 0.0))
    await drone_object.drone.offboard.start()

    await drone_object.move("forwards", 10, 50)
    await drone_object.move("r", 10, 50)
    await drone_object.move("big bird", 10, 50)
    await drone_object.move("l", 10, 50)

    drone_object.land()

if __name__ == "_main__":
    asyncio.run(main()
