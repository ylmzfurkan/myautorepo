import subprocess
from datetime import datetime

def auto_commit_push(directory, remote_name="origin", branch="master", commit_message="Automatic Commit"):
    try:
        # Tarih ve saat bilgisini al
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y%m%d_%H%M%S")

        # Dosya adını oluştur
        filename = f"{formatted_datetime}.py"

        # Dosyayı oluştur ve içine tarih ve saat bilgisini yaz
        with open(filename, "w") as file:
            file.write(f"# {formatted_datetime}\nprint('Merhaba, bu dosya otomatik oluşturuldu!')")

        # Git add
        subprocess.run(["git", "add", "."], check=True, cwd=directory)

        # Git commit
        subprocess.run(["git", "commit", "-m", commit_message], check=True, cwd=directory)

        # Git pull
        subprocess.run(["git", "pull", remote_name, branch], check=True, cwd=directory)

        # Git push
        subprocess.run(["git", "push", remote_name, branch], check=True, cwd=directory)

        print("Commit, pull, and push successful.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print("Commit, pull, and push failed.")

# Kullanım örneği
klasor_yolu = "C:/Users/Furkan/Downloads/dneme/myrepo"
commit_mesaji = "Otomatik Commit ve Push"
auto_commit_push(klasor_yolu, remote_name="origin", branch="master", commit_message=commit_mesaji)
