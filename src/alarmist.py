import subprocess
import argparse


def run_applescript(script):
    process = subprocess.Popen(
        ["osascript", "-"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout_data, stderr_data = process.communicate(script.encode("utf-8"))
    return stdout_data.decode("utf-8"), stderr_data.decode("utf-8")


class SystemPreferences:
    """
    This class manages system preferences using AppleScript commands.
    """

    def __init__(self, volume, brightness):
        self.volume = volume
        self.brightness = brightness

    def set_system_volume(self, volume):
        """
        Set the system volume using AppleScript commands.

        Args:
        volume (int): The volume level to set.
        """

        volume = max(0, min(100, volume))  # clamp volume to 0-100

        script = f"""
        set volume output volume {volume}
        """
        run_applescript(script)

    def set_system_brightness(self, brightness):
        """
        Set the system brightness using AppleScript commands.

        Args:
        brightness (int): The brightness level to set.
        """

        brightness = max(0, min(100, brightness))  # clamp brightness to 0-100

    def pair_bluetooth_device(self, device_name):
        """
        This method pairs a bluetooth device with the system.
        """

        # YEAH WE DON'T USE THE DEVICE NAME
        script = """
            activate application "SystemUIServer"
            tell application "System Events" to tell process "SystemUIServer"
                set bluetooth_menu_bar_item to (menu bar item 1 of menu bar 1 whose description contains "bluetooth")
                tell bluetooth_menu_bar_item
                repeat with bluetooth_device in ({"Bose Mini II Soundlink"})
                    click
                    if exists menu item bluetooth_device of menu 1 then
                    tell (menu item bluetooth_device of menu 1)
                        click
                        if exists menu item "Connect" of menu 1 then
                        click menu item "Connect" of menu 1
                        else
                        -- Exit Bluetooth menu bar item
                        key code 53
                        end if
                    end tell
                    end if
                end repeat
                end tell
            end tell
        
            """

        print(run_applescript(script))


class Spotify:
    """
    This class manages Spotify playback using AppleScript commands.
    """

    def __init__(self, default_track, isShuffle=True):
        self.default_track = default_track
        self.isShuffle = isShuffle

    def play(self, track):
        """
        Play a Spotify sound using AppleScript commands.

        Args:
        uri (str): The Spotify sound URI to play.
        isShuffle (bool): Whether to enable shuffle mode (default: True).
        """
        script = f"""
        tell application "Spotify"
            set sound volume to 100
            set shuffling to false
            
            if it is not running then
                return
            end if
            if {self.isShuffle} then
                set shuffling to true
            end if
            play track "spotify:{track if track else self.default_track}"
        end tell
        """
        run_applescript(script)

    def pause_spotify(self):
        """
        Pause Spotify playback using AppleScript commands.
        """
        script = """
        tell application "Spotify"
            pause
        end tell
        """
        run_applescript(script)

    def skip_spotify(self):
        """
        Skip the current Spotify track using AppleScript commands.
        """
        script = """
        tell application "Spotify"
            next track
        end tell
        """
        run_applescript(script)

    def previous_spotify(self):
        """
        Play the previous Spotify track using AppleScript commands.
        """
        script = """
        tell application "Spotify"
            previous track
        end tell
        """
        run_applescript(script)

    def set_spotify_volume(self, volume):
        """
        Set the Spotify volume using AppleScript commands.

        Args:
        volume (int): The volume level to set.
        """

        volume = max(0, min(100, volume))  # clamp volume to 0-100

        script = f"""
        tell application "Spotify"
            set sound volume to {volume}
        end tell
        """
        run_applescript(script)


class Alarm:
    """
    This class represents a system alarm.
    """

    def __init__(self, playlist, isShuffle=True):
        self.time = time
        self.playlist = playlist
        self.isShuffle = isShuffle

    def check_alarm(self):
        """
        Check if the current time matches the alarm time.

        Returns:
        bool: True if the alarm time matches the current time, False otherwise.
        """
        return self.time == datetime.now().strftime("%H:%M")


class AlarmManager:
    """
    This class manages system alarms
    """

    def __init__(self, time, schedule, playlist, isShuffle=True):
        self.time = time
        self.schedule = schedule
        self.playlist = playlist
        self.isShuffle = isShuffle

    def check_alarms(self):
        """
        Check if the current time matches the alarm time.

        Returns:
        bool: True if the alarm time matches the current time, False otherwise.
        """
        return self.time == datetime.now().strftime("%H:%M")

    def schedule_alarm(self):
        """
        Schedule an alarm to play a playlist at a specific time.
        """
        if self.check_alarms():
            spotify = Spotify(default_track=self.playlist, isShuffle=self.isShuffle)
            spotify.play(self.playlist)
            return True


if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description="Schedule a playlist to play at a specific time."
    )

    parser.add_argument("--sound", help="Spotify { URI }")
    parser.add_argument("--shuffle", action="store_true", help="Shuffle the sound")

    args = parser.parse_args()

    spotify = Spotify(
        default_track="playlist:3HShxXxpx7TeJXJFK1kX0j", isShuffle=args.shuffle
    )
    system = SystemPreferences(volume=100, brightness=100)

    system.pair_bluetooth_device("")
    spotify.play(args.sound)


#  To call: python3 main.py --sound "spotify:sound:3HShxXxpx7TeJXJFK1kX0j" --shuffle True
