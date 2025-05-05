# Cookie Monster Secret Recipe

Author: Brhane Giday and Prince Niyonshuti N.

Description: Cookie Monster has hidden his top-secret cookie recipe somewhere on his website. As an aspiring cookie detective, your mission is to uncover this delectable secret. Can you outsmart Cookie Monster and find the hidden recipe?

head over to the website.

<img width="1396" alt="Screenshot 2025-05-06 at 12 39 31 AM" src="https://github.com/user-attachments/assets/b77101e0-2a23-4353-aa7a-28312c55690f" />


now try to login.......login failed........check cookies....

maybe cookie is url encoded. decode it you will get base64. decode it to get the flag. 
 

```bash
echo "cGljb0NURntjMDBrMWVfbTBuc3Rlcl9sMHZlc19jMDBraWVzX0RFN0E1RTc2fQ==" | base64 -d
picoCTF{c00k1e_m0nster_l0ves_c00kies_DE7A5E76}
```





