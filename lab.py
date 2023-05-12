class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 5
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL
        self.__prevVol = 0

    def power(self):
        self.__status = not self.__status
        if self.__muted:
            self.__muted = False
            self.__volume = self.MIN_VOLUME

    def mute(self):
        if self.__status:
            if not self.__muted:
                self.__prevVol = self.__volume
                self.__volume = self.MIN_VOLUME
                self.__muted = True
            else:
                self.__muted = False
                self.__volume = self.__prevVol

    def channel_up(self):
        if self.__status:
            self.__channel += 1
            if self.__channel > self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL

    def channel_down(self):
        if self.__status:
            self.__channel -= 1
            if self.__channel < self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL

    def get_channel(self):
        return self.__channel

    def volume_up(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__prevVol + 1 if self.__prevVol < Television.MAX_VOLUME else Television.MAX_VOLUME
                # if self.__volume < Television.MAX_VOLUME:
                #     self.__volume = self.__prevVol + 1
                # else:
                #     self.__volume = Television.MAX_VOLUME
            else:
                if self.__volume < self.MAX_VOLUME:
                    self.__volume += 1

    def volume_down(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__prevVol - 1 if self.__prevVol > Television.MIN_VOLUME else Television.MIN_VOLUME
                # if self.__volume > Television.MIN_VOLUME:
                #     self.__volume = self.__prevVol - 1
                # else:
                #     self.__volume = Television.MIN_VOLUME
            else:
                if self.__volume > self.MIN_VOLUME:
                    self.__volume -= 1

    def get_status(self):
        return self.__status

    def __str__(self):
        status = "ON" if self.__status else "OFF"
        return f"TV status: Power is {status}, Channel {self.__channel}, Volume is on {self.__volume}"
