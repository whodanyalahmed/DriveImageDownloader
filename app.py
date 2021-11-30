from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import io
from googleapiclient.http import MediaIoBaseDownload


from googleapiclient.http import MediaIoBaseDownload
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']


"""Shows basic usage of the Drive v3 API.
Prints the names and ids of the first 10 files the user has access to.
"""
creds = None
# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

service = build('drive', 'v3', credentials=creds)

ids = dict()


def CheckFolder(FileName):
    page_token = None
    # response = service.files().list(q="mimeType = 'application/vnd.google-apps.spreadsheet'",
    response = service.files().list(q="mimeType = 'application/vnd.google-apps.folder'",
                                    spaces='drive',
                                    fields='nextPageToken, files(id, name)',
                                    pageToken=page_token).execute()
    items = response.get('files', [])
    #     # Process change
    #     print('Found file: %s (%s)' % (file.get('name'), file.get('id')))
    # page_token = response.get('nextPageToken', None)
    # if page_token is None:
    #     break
    # for i in items:
    #     print(i['name'])
    if not items:
        print('No files found.')
        return None
    else:
        # print('Files:')
        for item in items:
            # print(item['name'])
            if(item['name'] == FileName):
                print(FileName + " is already there")
                # print(item['name'])
                return item['id']


def getFilesName(FolderId, folderName):
    page_token = None
    while True:
        if(folderName != "root"):

            response = service.files().list(q="'"+FolderId+"' in parents and mimeType='image/jpeg'",
                                            spaces='drive',
                                            fields='nextPageToken, files(id, name)',
                                            pageToken=page_token).execute()
        else:
            response = service.files().list(q="mimeType='image/jpeg'",
                                            spaces='drive',
                                            fields='nextPageToken, files(id, name)',
                                            pageToken=page_token).execute()

        for file in response.get('files', []):
            #  save file name and id
            ids[file['name']] = file['id']
            # Process change
            print('Found file: %s (%s) - mime=%s' %
                  (file.get('name'), file.get('id'), file.get('mimeType')))
        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break


def DownloadFile(file_ids, path):
    for file_name, file_id in file_ids.items():
        try:
            request = service.files().get_media(fileId=file_id)
            # fh = io.BytesIO(path + file_id + '.jpg')
            # fh = io.BytesIO(request.execute())
            fh = io.FileIO(path + file_name, 'wb')
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
                print('Download %d%%.' % int(status.progress() * 100))

        except Exception as e:
            print('Error downloading file from Google Drive: %s' % e)


if __name__ == '__main__':
    folderName = input('Enter folder name or \'root\' for root directory: ')
    folderId = CheckFolder(folderName)
    print(folderId)
    getFilesName(folderId, folderName)

    download_path = './' + folderName + '/'
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    DownloadFile(ids, download_path)
    print(ids)
