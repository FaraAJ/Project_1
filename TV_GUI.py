import tkinter as tk
from PIL import ImageTk, Image

class TVGUI:
    def __init__(self, my_tv):
        self.tv = my_tv

        # Create the main window
        self.window = tk.Tk()
        self.window.title("Television")

        # Load the TV logo image
        self.logo_image = Image.open("tv_off.png")
        self.logo_image = self.logo_image.resize((300, 300), Image.LANCZOS)
        self.logo_photo = ImageTk.PhotoImage(self.logo_image)

        # Create the logo label
        self.logo_label = tk.Label(self.window, image=self.logo_photo)
        self.logo_label.pack()

        # Create the channel image labels
        self.channel_images = []
        for channel in range(self.tv.MIN_CHANNEL, self.tv.MAX_CHANNEL+1):
            channel_image = Image.open(f"channel{channel}_image.png")
            channel_image = channel_image.resize((300, 300), Image.LANCZOS)
            channel_photo = ImageTk.PhotoImage(channel_image)
            self.channel_images.append(channel_photo)

        # Create the status label
        self.status_label = tk.Label(self.window, text=str(self.tv), font=("Arial", 14, "bold"),
                                     bg="white", fg="black", padx=10, pady=5)
        self.status_label.pack()

        # Create the buttons frame
        self.buttons_frame = tk.Frame(self.window)
        self.buttons_frame.pack()

        # Create the buttons
        self.power_button = tk.Button(self.buttons_frame, text="Power", command=self.power, font=("Arial", 12))
        self.mute_button = tk.Button(self.buttons_frame, text="Mute", command=self.mute, font=("Arial", 12))
        self.channel_up_button = tk.Button(self.buttons_frame, text="Channel Up", command=self.channel_up,
                                           font=("Arial", 12))
        self.channel_down_button = tk.Button(self.buttons_frame, text="Channel Down", command=self.channel_down,
                                             font=("Arial", 12))
        self.volume_up_button = tk.Button(self.buttons_frame, text="Volume Up", command=self.volume_up,
                                          font=("Arial", 12))
        self.volume_down_button = tk.Button(self.buttons_frame, text="Volume Down", command=self.volume_down,
                                            font=("Arial", 12))

        # Pack the buttons
        self.power_button.grid(row=0, column=0, padx=10, pady=5)
        self.mute_button.grid(row=1, column=0, padx=10, pady=5)
        self.volume_up_button.grid(row=0, column=1, padx=10, pady=5)
        self.volume_down_button.grid(row=1, column=1, padx=10, pady=5)
        self.channel_up_button.grid(row=0, column=2, padx=10, pady=5)
        self.channel_down_button.grid(row=1, column=2, padx=10, pady=5)

    def run(self):
        self.window.mainloop()

    def power(self):
        self.tv.power()
        self.status_label.config(text=str(self.tv))
        self.update_channel_image()

    def mute(self):
        self.tv.mute()
        self.status_label.config(text=str(self.tv))

    def channel_up(self):
        self.tv.channel_up()
        self.status_label.config(text=str(self.tv))
        self.update_channel_image()

    def channel_down(self):
        self.tv.channel_down()
        self.status_label.config(text=str(self.tv))
        self.update_channel_image()

    def volume_up(self):
        self.tv.volume_up()
        self.status_label.config(text=str(self.tv))

    def volume_down(self):
        self.tv.volume_down()
        self.status_label.config(text=str(self.tv))

    def update_channel_image(self):
        if not self.tv.get_status():
            # TV is powered off, load the tv_off.png image
            self.logo_image = Image.open("tv_off.png")
            self.logo_image = self.logo_image.resize((300, 300), Image.LANCZOS)
            self.logo_photo = ImageTk.PhotoImage(self.logo_image)
            self.logo_label.config(image=self.logo_photo)
        else:
            # TV is powered on, load the channel image
            channel = self.tv.get_channel()
            if self.tv.MIN_CHANNEL <= channel <= self.tv.MAX_CHANNEL+1:
                channel_photo = self.channel_images[channel]
                self.logo_label.config(image=channel_photo)
