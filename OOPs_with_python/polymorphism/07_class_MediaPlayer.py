"""Create a base class MediaPlayer with play(). Derive AudioPlayer and VideoPlayer. Demonstrate polymorphism using a function."""
class MediaPlayer:
    def play(self, filename):
        raise NotImplementedError("Subclass must implement play()")

class AudioPlayer(MediaPlayer):
    def play(self, filename):
        print("Playing audio file:", filename)

class VideoPlayer(MediaPlayer):
    def play(self, filename):
        print("Playing video file:", filename)

def start_playing(player: MediaPlayer, filename: str):
    player.play(filename)

audio = AudioPlayer()
video = VideoPlayer()

start_playing(audio, "song.mp3")
start_playing(video, "movie.mp4")
