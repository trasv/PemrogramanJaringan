import logging
import requests
import threading


def download_gambar(url, name):
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png'] = 'png'
    tipe['image/jpg'] = 'jpg'
    tipe['image/jpeg'] = 'jpg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = 'pic/' + name
        ekstensi = tipe[content_type]
        logging.warning(f"writing {namafile}.{ekstensi}")
        fp = open(f"{namafile}.{ekstensi}", "wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False


if __name__ == '__main__':
    tr = []
    tr.append('https://upload.wikimedia.org/wikipedia/commons/5/56/Hasyakyla_utami_kusumawardhani_kyla_jkt48.jpg')
    tr.append(
        'https://cdn2.tstatic.net/makassar/foto/bank/images/zara-jkt-48.jpg')
    tr.append(
        'https://upload.wikimedia.org/wikipedia/commons/1/1b/Tiara_Anugrah.jpg')
    threads = []
    panjang = len(tr)
    counter = 0
    while counter is not panjang:
        dw_thread = threading.Thread(
            target=download_gambar, args=(tr[counter], 'gambar ke ' + str(counter + 1)))
        threads.append(dw_thread)
        counter=counter+1
    for thread in threads:
        thread.start()