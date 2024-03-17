import asyncio


def flatten(data: list[list]) -> list:
    return [item for sublist in data for item in sublist]


async def split_execution(tasks: list, packet_size=5) -> list:
    current_tasks = []
    output = []

    for i, task in enumerate(tasks):
        current_tasks.append(task())

        if len(current_tasks) == packet_size or i == len(tasks) - 1:
            print("Tasks achieved length", "data collected", len(output))
            output = output + await asyncio.gather(*current_tasks)

            current_tasks = []

    return output
