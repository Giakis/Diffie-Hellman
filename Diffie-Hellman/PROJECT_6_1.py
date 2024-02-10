#Αλγόριθμος 7.2.2. : Γρήγορη ύψωση σε δύναμη mod m.
def Fast_Exponentiation(b , e , m):
 B = b #Base
 result = 1
 M = m #Μodulo
 E = e #exponent
 while (E > 0):
    if ((E % 2) == 1):
        result =(result * B) % M
    E = (E // 2) #Η πράξη // εκτελεί και επιστρέφει ακέραιο αποτέλεσμα ενώ η / δεκαδικό.
    B = (B ** 2) % M
 return result

#Για την ανταλλαγή των A και Β πρέπει να εκτελεστούν οι ακολουθεί τύποι:
#Alice A=(g ** a) % p
#Bob B=(g ** b) % p
g = 3
p = 101
a = 77
b = 91
A = Fast_Exponentiation (g , a , p)
B = Fast_Exponentiation (g , b , p)

#Το κοινο κλειδει προκυπτει αν ο καθενασ υπολογισει τους παρακατω τυπους:
#Alice (B ** a) % p = ((g ** b) ** a) % p = (g ** (a * b)) % p
#Bob (A ** b) % p = ((g ** a) ** b) % p = (g ** (b * a)) % p

Alice_Key = Fast_Exponentiation(B , a ,p)
Bob_Key = Fast_Exponentiation(A , b ,p)

print('Key' , Alice_Key)

#Για να επιβεβαιώσουμε ότι ο αλγόριθμος μας δουλεύει σωστά αρκεί το Alice_Key==Bob_Key
#print('Key' , Bob_Key )
