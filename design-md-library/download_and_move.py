import os
import re
import subprocess
import time

md_file = 'elementos_designmd.md'
base_dir = '/design-md-library'
target_dir = os.path.join(base_dir, '454')

with open(md_file, 'r') as f:
    lines = f.readlines()

# Set up to track how many we successfully download/move
count = 0

print("Iniciando o download e a cópia das imagens...")

for line in lines:
    if line.startswith('|'):
        img_match = re.search(r'\((https://designmd\.app/images/library/(\d+)\.png)\)', line)
        slug_match = re.search(r'https://designmd\.app/(?:en/)?library/([^)]+)', line)
        
        if img_match and slug_match:
            img_url = img_match.group(1)
            img_filename = f"{img_match.group(2)}.png"
            slug = slug_match.group(1).strip()
            
            # Define destination paths
            tmp_img_path = os.path.join(base_dir, img_filename)
            folder_path = os.path.join(target_dir, slug)
            final_img_path = os.path.join(folder_path, img_filename)
            
            # Step 1: Download using wget
            # User-Agent is added to bypass basic blocks
            cmd_wget = ['wget', '-q', '--show-progress', '--user-agent=Mozilla/5.0', '-O', tmp_img_path, img_url]
            subprocess.run(cmd_wget)
            
            # Step 2: Move the image to the folder
            if os.path.exists(tmp_img_path):
                # Using mv command or python's os.rename
                os.rename(tmp_img_path, final_img_path)
                count += 1
            else:
                print(f"Erro ao baixar: {img_url}")
                
            # Sleep a tiny bit to avoid being blocked for rapid requests
            time.sleep(0.1)

print(f"\nFinalizado! {count} imagens foram baixadas e movidas para as suas respectivas pastas.")
