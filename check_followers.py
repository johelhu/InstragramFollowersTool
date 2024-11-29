# Leer archivos
with open("followers.txt", "r", encoding="utf-8") as f:
    followers = f.readlines()

with open("following.txt", "r", encoding="utf-8") as f:
    following = f.readlines()

# Limpiar listas eliminando líneas con fechas y horas
def clean_list(lines):
    cleaned = []
    for line in lines:
        line = line.strip()  # Eliminar espacios o saltos de línea
        # Incluir solo nombres (sin fechas ni horas)
        if not line.startswith(("Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                                "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")):
            cleaned.append(line)
    return cleaned

followers_cleaned = clean_list(followers)
following_cleaned = clean_list(following)

# Crear la lista con los nombres de following que no están en followers
not_following_back = [name for name in following_cleaned if name not in followers_cleaned]

# Guardar el resultado en un archivo
with open("not_following_back.txt", "w", encoding="utf-8") as f:
    for name in not_following_back:
        f.write(name + "\n")

print("Lista creada: 'not_following_back.txt'")
