# Existing code
if Config.HTTP_PROXY != "":
    command_to_exec = [
        "youtube-dl",
        "--no-warnings",
        "--youtube-skip-dash-manifest",
        "-j",
        url,
        "--proxy", Config.HTTP_PROXY
    ]
else:
    command_to_exec = [
        "youtube-dl",
        "--no-warnings",
        "--youtube-skip-dash-manifest",
        "-j",
        url
    ]
if youtube_dl_username is not None:
    command_to_exec.append("--username")
    command_to_exec.append(youtube_dl_username)
if youtube_dl_password is not None:
    command_to_exec.append("--password")
    command_to_exec.append(youtube_dl_password)

# Compressed version
command_to_exec = [
    "youtube-dl",
    "--no-warnings",
    "--youtube-skip-dash-manifest",
    "-j",
    url,
    f"--proxy {Config.HTTP_PROXY}" if Config.HTTP_PROXY else "",
    f"--username {youtube_dl_username}" if youtube_dl_username else "",
    f"--password {youtube_dl_password}" if youtube_dl_password else "",
]
