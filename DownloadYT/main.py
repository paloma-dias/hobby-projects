import os
import json
import yt_dlp
import ffmpeg
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# Função para carregar as configurações anteriores
def load_settings():
    try:
        # Tenta abrir o arquivo de configurações
        with open("settings.json", "r") as file:
            settings = json.load(file)
            return settings.get("output_dir", "")  # Retorna a pasta de destino salva
    except FileNotFoundError:
        return ""  # Retorna uma string vazia se o arquivo não for encontrado

# Função para salvar as configurações
def save_settings(output_dir):
    with open("settings.json", "w") as file:
        json.dump({"output_dir": output_dir}, file)  # Salva a pasta de destino em um arquivo JSON

# Função para selecionar a pasta de destino
def select_output_directory():
    output_dir = filedialog.askdirectory()  # Abre uma janela para selecionar a pasta
    if output_dir:
        output_dir_var.set(output_dir)  # Atualiza a variável com a nova pasta
        save_settings(output_dir)  # Salva a nova pasta de destino

# Função para baixar o áudio
def download_audio():
    url = url_var.get()  # Obtém o URL do campo de entrada
    output_dir = output_dir_var.get()  # Obtém a pasta de destino

    # Verifica se o URL ou a pasta de destino estão vazios
    if not url:
        messagebox.showerror("Erro", "Por favor, insira o link do vídeo.")
        return
    
    if not output_dir:
        messagebox.showerror("Erro", "Por favor, selecione a pasta de destino.")
        return

    # Opções para yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',  # Seleciona a melhor qualidade de áudio
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),  # Define o template de saída
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # Define o codec de áudio para MP3
            'preferredquality': '192',  # Define a qualidade do áudio
        }],
        'progress_hooks': [progress_hook],  # Define a função de hook de progresso
    }
    
    # Baixa o áudio usando yt-dlp
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Função para atualizar a barra de progresso e as estatísticas
def progress_hook(d):
    if d['status'] == 'downloading':
        total = d.get('total_bytes')
        downloaded = d.get('downloaded_bytes')
        if total and downloaded:
            progress = int(downloaded / total * 100)
            progress_var.set(progress)  # Atualiza a variável de progresso
            progress_bar['value'] = progress  # Atualiza a barra de progresso
            status_var.set(f"Baixando: {progress}%")  # Atualiza o status
    elif d['status'] == 'finished':
        progress_var.set(100)
        progress_bar['value'] = 100
        status_var.set("Download completo")  # Atualiza o status para completo
        messagebox.showinfo("Sucesso", "Áudio baixado com sucesso!")

# Configuração inicial do Tkinter
app = tk.Tk()
app.title("Downloader de Áudio do YouTube")

# Variáveis
url_var = tk.StringVar()
output_dir_var = tk.StringVar(value=load_settings())
progress_var = tk.IntVar()
status_var = tk.StringVar()

# Layout
frame = ttk.Frame(app, padding=10)
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Campo de entrada do link
ttk.Label(frame, text="Link do vídeo:").grid(row=0, column=0, sticky=tk.W)
url_entry = ttk.Entry(frame, textvariable=url_var, width=50)
url_entry.grid(row=0, column=1, columnspan=2, sticky=(tk.W, tk.E))

# Botão para selecionar a pasta de destino
ttk.Label(frame, text="Pasta de destino:").grid(row=1, column=0, sticky=tk.W)
output_dir_entry = ttk.Entry(frame, textvariable=output_dir_var, width=50)
output_dir_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))
output_dir_button = ttk.Button(frame, text="Selecionar", command=select_output_directory)
output_dir_button.grid(row=1, column=2, sticky=tk.E)

# Botão para iniciar o download
download_button = ttk.Button(frame, text="Baixar Áudio", command=download_audio)
download_button.grid(row=2, column=0, columnspan=3, pady=10)

# Barra de progresso
progress_bar = ttk.Progressbar(frame, orient='horizontal', length=400, mode='determinate', variable=progress_var)
progress_bar.grid(row=3, column=0, columnspan=3, pady=5)

# Label de status
status_label = ttk.Label(frame, textvariable=status_var)
status_label.grid(row=4, column=0, columnspan=3)

# Configurações de redimensionamento
frame.columnconfigure(1, weight=1)
app.columnconfigure(0, weight=1)
app.rowconfigure(0, weight=1)

# Executar a aplicação
app.mainloop()
