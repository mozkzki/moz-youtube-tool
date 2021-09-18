# moz-youtube-tool

自前のYouTube操作ツール。

## Usage

Environmental variables

`.env`ファイルに書いてproject rootに配置。

```txt
moz_youtube_client_secret_contents='{"installed":{"client_id":"....}'
moz_youtube_token_contents='{"access_token": "...}'
moz_youtube_new_token_contents='{"access_token": "...}'
```

Install

```sh
pip install git+https://github.com/mozkzki/moz-youtube-tool
# upgrade
pip install --upgrade git+https://github.com/mozkzki/moz-youtube-tool
# uninstall
pip uninstall moz-youtube-tool
```

Run

```sh
moz-youtube -h
# or
moz-youtube --help
# or
moz-youtube -- -h
# or
moz-youtube -- --help
```

```sh
moz-youtube random
moz-youtube upload ./resources/test.mp4 --title "it's test"
moz-youtube playlist get
```

## Develop

- base project: [mozkzki/moz-sample](https://github.com/mozkzki/moz-sample)
- use project: [mozkzki/moz-youtube](https://github.com/mozkzki/moz-youtube)
