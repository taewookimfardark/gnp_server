from time import time
import cloudstorage

def _save_file(image_binary, filepath):
    ext = filepath.split(".")[-1]
    '''
    writable_file_name = files.gs.create(
        filepath,
        acl="public-read",
        mime_type='image/'+ext)
    '''

    gcs_file = cloudstorage.open(filepath,
                                 'w',
                                 content_type='image/'+ext,
                                 options={'x-goog-acl':'public-read'})
    gcs_file.write(image_binary)
    gcs_file.close()
    print "gcs save done"

def upload_image(image_binary, folder_name):
    # request = urllib2.Request(image_url)
    # request.add_header('User-Agent', 'Chrome')
    # image_file = urllib2.urlopen(request)
    # extension = image_url.split('.')[-1][0:3]
    # filename = urllib.quote(image_url,'')+'.'+extension
    # filename = str(time()).replace('.','')+'.'+extension
    filename = str(time()).replace('.', '')+".jpg"
    directory = '/woohwa_bucket/'+folder_name +'/'
    filepath = directory + filename
    _save_file(image_binary, filepath)
    urlpath = 'http://storage.googleapis.com' + directory + filename
    return urlpath