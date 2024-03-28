import subprocess
import customtkinter as ctk
import os
import platform

windows = ctk.CTk()
windows.title('Mineur')
windows.geometry('700x500')

if os.name == "posix":
    no_compatibilte = ctk.CTkLabel(windows,text="Désoler mais votre OS n'est pas fait pour miner. \n Veuillez utilisez Windows",font=('Courrier',20)).pack(expand=ctk.YES)
    windows.mainloop()

def miner_launch(fb, choix_crypto, adress, nom):
    global filedir
    try:
        result = subprocess.run(['wmic', 'path', 'win32_videocontroller', 'get', 'name'], capture_output=True, text=True)


        if 'NVIDIA' in result.stdout.upper():
            workdir = os.path.join(os.path.dirname(__file__), 'Setup/NVIDIA')
        elif 'AMD' in result.stdout.upper():
            workdir = os.path.join(os.path.dirname(__file__), 'Setup/AMD')
        elif 'INTEL' in result.stdout.upper():
            windows.destroy()
        else:
            return False
    except Exception as e:
        print(e)
        return False


    if choix_crypto == 'Ethereum Classic':
        filedir = os.path.join(workdir, 'etc-pool.bat')
        with open(filedir, 'w') as f:
            f.write(f'miner.exe --algo etchash --server etc.2miners.com:1010 --user {adress} \n pause')

    if choix_crypto == 'RavenCoin':
        filedir = os.path.join(workdir, 'rvn-pool.bat')
        with open(filedir, 'w') as f:
            f.write(f'miner.exe --algo kawpow --server rvn.2miners.com:6060 --user {adress}.{nom} \n pause')

    if choix_crypto == "Flux":
        filedir = os.path.join(workdir, 'flux-pool.bat')
        with open(filedir, 'w') as f:
            f.write(f'miner.exe --algo 125_4 --server zel.2miners.com --port 9090 --user {adress}.{nom} --pass x')

    # Exécuter le fichier .bat après l'avoir fermé
    subprocess.run(['start', 'cmd', '/k', filedir], shell=True, cwd=os.path.dirname(filedir))


frame_choix_crypto, frame_lancement, frame_info_user = ctk.CTkFrame(windows,fg_color='transparent'), ctk.CTkFrame(windows,fg_color='transparent'), ctk.CTkFrame(windows, fg_color='transparent')

#Creation Label Titre

titre = ctk.CTkLabel(windows,text='HMiners',font=('Courrier',50))
titre.pack(pady=20)

#Création des boutons de choix de la crypto a miner

liste_crypto = ['Ethereum Classic', 'RavenCoin','Flux']

Titre = ctk.CTkLabel(frame_choix_crypto,text='Veuillez choisir la cryptomonnaies \n que vous voulez miner.',font=("Courrier",20)).pack(pady=20)
choix_crypto = ctk.CTkComboBox(frame_choix_crypto,values=liste_crypto)
choix_crypto.pack()
frame_choix_crypto.pack(pady=15)

#Création des entré des infos utilisateurs
title = ctk.CTkLabel(frame_info_user,text='Veuillez entrer le fabriquant de votre carte graphique',font=('Courrier',20)).pack()
fabriquant = ctk.CTkComboBox(frame_info_user,values=['Nvidia','AMD'])
fabriquant.pack(pady=15)
adresse = ctk.CTkEntry(frame_info_user,placeholder_text='Adresse Payement',width=400)
adresse.pack(pady=15)
nom = ctk.CTkEntry(frame_info_user,placeholder_text='Nom de votre machine ',width=400)
nom.pack(pady=15)
frame_info_user.pack(pady=15)

#Création bouton lancement

btn_lancement = ctk.CTkButton(windows,text='Miner',font=('Courrier',20),command=lambda: miner_launch(fabriquant.get,choix_crypto.get(),adresse.get(),nom.get())).pack()
frame_lancement.pack(pady=20)
windows.mainloop()