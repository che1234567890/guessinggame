exec('for i in range(1, 12): n = 12 - i; c = n*"*"; print(c)'); z = __import__("random").randint(1, 101);essai = 0; exec('while True: question = int(input("deviner un nombre entre 1 et 100 ")); essai += 1; exit(f"vous avez gagne! ca vous a prit {essai} essai(s)") if question == z else print("nombre est plus petit") if z < question else print("nombre est plus grand") ') #1er exec() pour faire un loop sans break car break est un statement et ne peut pas etre utiliser dans un tenary. le code dans le premier exec() affiche les etoiles et trouve un nombre a l'hasard avec le module random. 2eme exec() est utilise car while est un statement et ne peux pas etre utilise apres le 1er exec(). Dedans le 2eme exec() est le jeux de devinette. 
