import subprocess
import customtkinter as ctk
import os

# Défnitions de la fenetre et de ses caracteritqiues
windows = ctk.CTk()
windows.title('Mineur')
windows.geometry('700x500')
windows.maxsize(700,500)
windows.minsize(700,500)

# Verification de l'OS pour savoir si c'est un Windows ('posix' ca raporte a tour les sytemes sous UNIX tel que MacOS ou Linux)
if os.name == "posix":
    no_compatibilte = ctk.CTkLabel(windows,text="Désoler mais votre OS n'est pas fait pour miner. \n Veuillez utilisez Windows",font=('Courrier',20)).pack(expand=ctk.YES)
    windows.mainloop()

# Fonction de lancment du bon fichier de minage de crypto
def miner_launch(choix_crypto, adress, nom):
    global filedir
    # Verification de la presence d'un GPU sur la machine
    try:
        result = subprocess.run(['wmic', 'path', 'win32_videocontroller', 'get', 'name'], capture_output=True, text=True)

        # Choix du dossier de travail en fonction de la marque du GPU récuperer plus haut
        if 'NVIDIA' in result.stdout.upper():
            workdir = os.path.join(os.path.dirname(__file__), 'Setup/NVIDIA')
        elif 'AMD' in result.stdout.upper():
            workdir = os.path.join(os.path.dirname(__file__), 'Setup/AMD')
        elif 'INTEL' in result.stdout.upper():
            workdir = os.path.join(os.path.dirname(__file__), 'Setup/NVIDIA')
        else:
            return False
    except Exception as e:
        frame_lancement.pack_forget()
        label_not_GPU = (ctk.CTkLabel(windows,text='Vous ne pouvez pas miner car vous ne possedez pas de GPU'))
        label_not_GPU.pack(pady=15)


    # Deetection de la crypto choisis
    if choix_crypto == 'Ethereum Classic':
        # Création du chemin absolue du fichier d'execution
        filedir = os.path.join(workdir, 'etc-pool.bat')
        with open(filedir, 'w') as f:
            # Ecriture de la ligne de commande pour lancer le miner avec les infos personalisé
            f.write(f'miner.exe --algo etchash --server etc.2miners.com:1010 --user {adress} \n pause')

    if choix_crypto == 'RavenCoin':
        filedir = os.path.join(workdir, 'rvn-pool.bat')
        with open(filedir, 'w') as f:
            f.write(f'miner.exe --algo kawpow --server rvn.2miners.com:6060 --user {adress}.{nom} \n pause')

    if choix_crypto == "Flux":
        filedir = os.path.join(workdir, 'flux-pool.bat')
        with open(filedir, 'w') as f:
            f.write(f'miner.exe --algo 125_4 --server zel.2miners.com --port 9090 --user {adress}.{nom} --pass x \n pause')
    if choix_crypto == "Grin":
        filedir = os.path.join(workdir, 'grin-pool.bat')
        with open(filedir, 'w') as f:
            f.write(f'..\AMD\lolMiner.exe --coin GRIN-C32 --pool grin.2miners.com:3030 --user {adress}.{nom} --pass x \n pause')

    # Exécuter le fichier .bat après l'avoir fermé
    subprocess.run(['start', 'cmd', '/k', filedir], shell=True, cwd=os.path.dirname(filedir))

def launch():
    # Verifie que aucun champs n'est vide sinon affiche une erreur
    if choix_crypto.get() == "" or adresse.get() == "" or nom.get() == "":
        label_no_complete = ctk.CTkLabel(frame_lancement,text='Veuillez remplire tout les champs')
        label_no_complete.pack(pady=15)
    else:
        miner_launch(choix_crypto.get(),adresse.get(),nom.get())


frame_choix_crypto, frame_lancement, frame_info_user = ctk.CTkFrame(windows,fg_color='transparent'), ctk.CTkFrame(windows,fg_color='transparent'), ctk.CTkFrame(windows, fg_color='transparent')

#Creation Label Titre

titre = ctk.CTkLabel(windows,text='HMiners',font=('Courrier',50))
titre.pack(pady=20)

#Création des boutons de choix de la crypto a miner

liste_crypto = ['Ethereum Classic', 'RavenCoin','Flux','Grin']

Titre = ctk.CTkLabel(frame_choix_crypto,text='Veuillez choisir la cryptomonnaies \n que vous voulez miner.',font=("Courrier",20)).pack(pady=20)
choix_crypto = ctk.CTkComboBox(frame_choix_crypto,values=liste_crypto)
choix_crypto.pack()
frame_choix_crypto.pack(pady=15)

#Création des entré des infos utilisateurs
adresse = ctk.CTkEntry(frame_info_user,placeholder_text='Adresse Payement',width=400)
adresse.pack(pady=15)
nom = ctk.CTkEntry(frame_info_user,placeholder_text='Nom de votre machine ',width=400)
nom.pack(pady=15)
frame_info_user.pack(pady=15)

#Création bouton lancement

btn_lancement = ctk.CTkButton(windows,text='Miner',font=('Courrier',20),command=launch).pack()
frame_lancement.pack(pady=20)
windows.mainloop()