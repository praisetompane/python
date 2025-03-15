"""
    uses: standard_library/3_built_in_types/4_iterator_types/2_generator.py
"""


class RemoteControlIterator:
    def __init__(self):
        self.channels = ['HBO', 'SABC2', 'MNET', 'ESPN']
        self.current_channel = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.current_channel += 1
        if self.current_channel == len(self.channels):
            raise StopIteration

        return self.channels[self.current_channel]


if __name__ == "__main__":
    r = RemoteControlIterator()

    try:
        print(f"Channel {next(r)}")
    except StopIteration:
        print("All Channel Explored. Goodbye")
