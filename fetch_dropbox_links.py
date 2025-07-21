import dropbox
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
ACCESS_TOKEN = os.getenv("DROPBOX_ACCESS_TOKEN")
TARGET_FOLDER = "/krazy_notesy_media"

dbx = dropbox.Dropbox(ACCESS_TOKEN)

def list_files(folder_path):
    result = dbx.files_list_folder(folder_path)
    files = []
    for entry in result.entries:
        if isinstance(entry, dropbox.files.FileMetadata):
            files.append(entry.path_lower)
    return files

def get_direct_link(file_path):
    try:
        shared_link_metadata = dbx.sharing_create_shared_link_with_settings(file_path)
        url = shared_link_metadata.url
        return url.replace("?dl=0", "?dl=1")
    except dropbox.exceptions.ApiError:
        shared_links = dbx.sharing_list_shared_links(path=file_path).links
        if shared_links:
            url = shared_links[0].url
            return url.replace("?dl=0", "?dl=1")
        else:
            raise Exception(f"No shared link found for {file_path}")

file_list = list_files(TARGET_FOLDER)
links = [get_direct_link(file) for file in file_list]

with open("media_links.json", "w") as outfile:
    json.dump(links, outfile, indent=2)

print("media_links.json created successfully with", len(links), "links.")

