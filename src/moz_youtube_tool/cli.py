from fire import Fire

from moz_youtube import (
    random_get_video,
    get_video_match_today,
    get_videos_within_x_day,
    upload,
    UploadOption,
    get_play_list,
    add_to_play_list,
    delete_from_play_list,
)


class PlayList:
    """Add/Delete youtube video to/from play list."""

    def get(self):
        """Get youtube play list."""
        get_play_list()

    def add(
        self,
        play_list_id: str = "PLfZruavKtKZy0JdMo7PnbHAEo32twXVZl",
        video_id: str = "bRGeqa3ISEE",
    ):
        """Add youtube video to play list.

        Parameters
        ----------
        play_list_id : str, optional
            Play list ID
        video_id : str, optional
            Video ID to add play list
        """
        playlist_item_id = add_to_play_list(play_list_id, video_id)
        print(playlist_item_id)

    def delete(self, play_list_item_id: str):
        """Delete youtube video item from play list.

        Parameters
        ----------
        play_list_item_id : str
            Play list item ID of video to delete from play list
        """
        delete_from_play_list(play_list_item_id)


class Command:
    """mozkzki's youtube tool."""

    playlist = PlayList()

    def random(self):
        """Return youtube video by random."""
        random_get_video()

    def today(self):
        """Return youtube video taken today a few years ago."""
        get_video_match_today()

    def recent(self):
        """Return youtube video taken recentry."""
        get_videos_within_x_day()

    def upload(
        self,
        file_path: str,
        title: str = "test title",
        description: str = "this is test.",
        keywords: str = "test1,test2",
    ):
        """Upload video to youtube.

        (example)
        > moz-youtube upload ./resources/test.mp4 --title "it's test"

        Parameters
        ----------
        file_path : str
            File path of video to upload
        title : str, optional
            File title of video to upload
        description : str, optional
            Description of video to upload
        keywords : str, optional
            Keywords of video to upload
        """

        options = UploadOption(
            {
                "file": file_path,
                "title": title,
                "description": description,
                "keywords": keywords,
            }
        )
        upload(options)


def main() -> None:
    Fire(Command())


if __name__ == "__main__":
    main()
