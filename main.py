from pytube import YouTube, Playlist
from time import sleep

import os, string

global fname
fname = ""

def mp3_download():
    os.system("cls")
    link = str(input("Unesi link pjesme sa youtubea: "))

    global fname
    if fname == "":
        fname = input("Unesi ime foldera u koji zelis preuzeti muziku: ")

    try:
        video = YouTube(link)

        os.system("cls")
        print("\nPreuzima se -----> " + video.title)
        download_path = str(os.path.join(os.path.expanduser("~/Downloads"), "downloaded"))
        download_path += "/" + fname
        downloaded = video.streams.filter(only_audio=True).first().download(download_path)
        try:
            os.rename(downloaded, os.path.splitext(downloaded)[0] + '.mp3')
            print(">>>>> " + video.title + " ---preuzeto!")
            print("Pjesma preuzeta i nalazi se u folderu Downloads/downloaded/" + fname)
            input("Pritisni ENTER da nastavis..")
        except:
            print("[GRESKA] Pjesma vec postoji!")
            os.remove(downloaded)
            input("Pritisni ENTER da nastavis..")

    except:
        print("[GRESKA] Pogresan link ili problem sa konekcijom!")
        input("Pritisni ENTER da nastavis..")


def mp3_download_playlist():
    os.system("cls")
    link = str(input("Unesi link playliste: "))

    global fname
    if fname == "":
        fname = str(input("Unesi ime foldera u koji zelis preuzeti muziku: "))

    try:
        playlist = Playlist(link)
        brvidea = playlist.length

        print("\nPlaylista '" + playlist.title + "' uskoro ce se poceti preuzimati!")
        print("Pjesama za preuzet -> " + str(brvidea))
        cnt = 1
        succeed = 0
        input("\nPritisni ENTER da nastavis..")

        for vid in playlist.videos:
            print("\n\n["+str(cnt)+"/"+str(brvidea)+"] Preuzima se -----> " + vid.title)

            download_path = os.path.join(os.path.expanduser("~/Downloads"), "downloaded")
            download_path += "/" + fname
            downloaded = vid.streams.filter(only_audio=True).first().download(download_path)
            try:
                os.rename(downloaded, os.path.splitext(downloaded)[0] + '.mp3')
                print(">>>>> " + vid.title + " ---preuzeto!")
                succeed+=1
                sleep(2)
            except:
                print("[GRESKA] Ova pjesma vec postoji!")
                os.remove(downloaded)
                sleep(3)
            cnt+=1
        print("\n[INFO] Preuzimanje zavrseno - preuzeto " + str(succeed) + "/" + str(brvidea))
        print("Muzika preuzeta i nalazi se u folderu Downloads/downloaded/" + fname)
        input("Pritisni ENTER da nastavis..")
    except:
        print("[GRESKA] Pogresan link ili problem sa konekcijom")
        input("Pritisni ENTER da nastavis..")


def change_fname():
    os.system("cls")
    global fname
    fname = input("\n\nUnesi ime foldera u koji zelis preuzimati muziku: ")

    print("\nPromijenili ste ime foldera za skidanje u: " + fname)
    print("Sve vase preuzete pjesme ce se nalaziti u Downloads/downloaded/" + fname + " folderu")
    input("\nPritisni ENTER da nastavis..")


choice = -1
while choice != 0:
    os.system("cls")
    print("\t\t[ YouTube mp3 downloader ]\n\n")
    print("\t[1] Single mp3 downloader")
    print("\t[2] Playlist downloader")
    print("\t[3] Promijeni ime foldera u koji se muzika skida")
    print("\t[0] Exit")
    choice = int(input("\tIzbor[0-2]: "))
    if(choice < 0 or choice > 3):
        print("\n\t[GRESKA] Pogresan izbor!!")
        choice = int(input("\tIzbor[0-2]: "))
    elif choice == 0:
        print("\n\t[INFO] Exiting...")
        sleep(1)
    elif choice == 1:
        mp3_download()
    elif choice == 2:
        mp3_download_playlist()
    elif choice == 3:
        change_fname()
