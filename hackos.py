#! /usr/bin/env python3

# Mode d'emploi:
#   - ouvrir l'inspecteur web ( ⌥ ⌘ I )
#   - cliquer pour "acheter" un testcase
#   - isoler la requête XHR 'permission' dans l'onglet réseau
#   - Copier comme cURL
#   - coller dans le champ data ci-dessous

import tkinter as tk
import re
import subprocess


root = tk.Tk()

root.wm_title("cURL ?")

e = tk.Text(root)
e.pack()
e.focus_set()
root.focus()
root.focus_set()


def callback():
    global data
    data = e.get("1.0", tk.END)
    root.destroy()


b = tk.Button(root, text="get", width=10, command=callback)
b.pack()

root.mainloop()

n = 100
for i in range(0, n + 1):
    s = data.strip()
    s = re.sub(r'(/testcases/\d+)/\d+/(permission)', r'\1/' + str(i) + r'/\2', s, count=1)
    s = re.sub(r"-H 'Accept-Encoding: br, gzip, deflate'", r"-s ", s)
    p = subprocess.Popen(s, shell=True, stdout=subprocess.PIPE)
    r = p.communicate()[0]
    if len(r) == 0:
        break
    print("{:2} => {}".format(i, r))
    p.wait()
