#! /usr/bin/env python3

import tkinter as tk
import tkinter.ttk as ttk
import sqlite3
import glob
import json
import platform
import subprocess
import os
import webbrowser
import hrinit
import uuid


def raise_app():
    if platform.system() == 'Darwin':
        # os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')  # noqa
        subprocess.call([
            '/usr/bin/osascript', '-e',
            'tell app "System Events" to set frontmost of every process whose unix id is {} to true'.format(os.getpid())  # noqa
        ])


# Credit to https://gist.github.com/lukestanley/8525f9fdcb903a43376a35a77575edff
def json_tree(tree, parent, dictionary):
    for key in dictionary:
        opened = (key == "model" or key == "track")

        uid = uuid.uuid4()
        if isinstance(dictionary[key], dict):
            tree.insert(parent, 'end', uid, text=key, open=opened, tag="d")
            json_tree(tree, uid, dictionary[key])
        elif isinstance(dictionary[key], list):
            tree.insert(parent, 'end', uid, text=key + '[]')
            json_tree(tree,
                      uid,
                      dict([(i, x) for i, x in enumerate(dictionary[key])]))
        else:
            value = dictionary[key]
            if value is None:
                value = 'None'
            try:
                if isinstance(key, str) and (key.find("_template") != -1
                                             or key.find("_skeliton") != -1 or key == "body_html"):
                    tree.insert(parent, 'end', uid, text=key, value="<not\ shown>")
                else:
                    tree.insert(parent, 'end', uid, text=key, value=str(value))
            except tk.TclError as e:
                print(e, key)
                tree.insert(parent, 'end', uid, text=key,
                            value="<" + str(e).replace(' ', '\\ ') + ">")
                pass


def show_data(data):
    # Setup the root UI
    root = tk.Tk()
    root.title("JSON viewer")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Setup the Frames
    tree_frame = ttk.Frame(root, padding="3")
    tree_frame.grid(row=0, column=0, sticky=tk.NSEW)

    # Setup the Tree
    tree = ttk.Treeview(tree_frame, columns='Values')
    tree.tag_configure("d", foreground='blue')
    tree.column('Values', width=100)
    tree.heading('Values', text='Values')
    json_tree(tree, '', data)
    tree.pack(fill=tk.BOTH, expand=1)

    # Limit windows minimum dimensions
    root.update_idletasks()
    root.minsize(500, 500)
    raise_app()

    root.mainloop()


class hr_menu:

    def __init__(self):
        # self.conn = sqlite3.connect('menu.db')
        self.conn = sqlite3.connect(':memory:')

    def load_models(self):
        models = []

        c = self.conn.cursor()
        c.execute("drop table if exists challenge")
        c.execute('''
create table if not exists challenge (
    serial              integer,
    id                  integer,        -- 2532
    slug                text,           -- "solve-me-first"
    name                text,           -- "Solve Me First"
    contest_slug        text,           -- "master"
    contest_name        text,           -- "Master"
    category            text,           -- "ai"
    kind                text,           -- "code"
    preview             text,
    difficulty          text,           -- "Easy"
    track_id            integer,        -- 3
    track_slug          text,           -- "algorithms"
    track_name          text,           -- "Algorithms"
    subtrack_id         integer,        -- 43
    subtrack_slug       text,           -- "warmup"
    subtrack_name       text,           -- "Warmup"
    solved              boolean
)''')
        c.execute('create unique index if not exists challenge_index on challenge (contest_slug, slug)')    # noqa
        c.close()
        self.conn.commit()

        for i in glob.iglob(os.path.join(os.path.dirname(__file__), "offline", "contests", "*.json")):    # noqa
            with open(i, "rb") as f:
                data = json.load(f)
                m = data['models']
                # filter out interview-preparation-kit and empty contests
                if len(m) > 0 and 'id' in m[0]:
                    for j in m:
                        j['__file__'] = i       # add source filename for error reporting
                    models.extend(m)
                else:
                    # print("ignoring", i)
                    pass

        c = self.conn.cursor()

        sql = '''
insert into challenge (serial,
                    id, slug, name, contest_slug,
                    category, kind, preview, difficulty,
                    track_id, track_slug, track_name,
                    subtrack_id, subtrack_slug, subtrack_name, solved)
            values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''

        for i, m in enumerate(models):

            if 'name' not in m:
                continue

            try:
                fields = (i,
                          m['id'],
                          m['slug'],
                          m['name'],
                          m['contest_slug'],
                          m['category'],
                          m['kind'],
                          m['preview'],
                          m['difficulty_name'])

                if 'track' in m and m['track']:
                    fields += (m['track']['track_id'],
                               m['track']['track_slug'],
                               m['track']['track_name'],
                               m['track']['id'],
                               m['track']['slug'],
                               m['track']['name'])

                    path = os.path.join(os.path.dirname(__file__),
                                        m['track']['track_slug'],
                                        m['track']['slug'], m['slug'] + ".*")

                else:
                    if m['contest_slug'] != "projecteuler":
                        fields += (0, "Contests", "Contests", 0, m['contest_slug'], m['contest_slug'])    # noqa
                    else:
                        fields += (0, m['contest_slug'], m['contest_slug'], 0, None, None)

                    path = os.path.join(os.path.dirname(__file__),
                                        m['contest_slug'], m['slug'] + ".*")

                fields += (len(glob.glob(path)) != 0,)

            except KeyError:
                print(m)
                raise

            try:
                c.execute(sql, fields)
            except sqlite3.IntegrityError as e:
                print(e, m['contest_slug'], m['slug'])
                pass

        c.close()
        self.conn.commit()

    def on_event(self, event):
        items = self.tree.selection()
        if len(items) != 1:
            return
        item = items[0]
        # print("event", event, self.tree.item(item, "text"), str(item))
        print(">", str(item))

    def get_selected_challenge(self, what=None):
        """
        returns the challenge path for its model/statement/source
        """
        items = self.tree.selection()
        if len(items) != 1:
            return
        k = str(items[0])
        # deux cas:
        #   domain[/subdomain]
        #   contest~slug
        p = k.split('~')
        if len(p) != 2:
            return

        if p[0] == 'master':
            # i.e. master/mathematics/fundamentals/even-odd-query
            c = self.conn.cursor()
            c.execute("select track_slug,subtrack_slug from challenge where contest_slug='master' and slug=?", (p[1],))  # noqa
            r = c.fetchone()
            path = os.path.join(p[0], r['track_slug'], r['subtrack_slug'], p[1])
            path_source = os.path.join(r['track_slug'], r['subtrack_slug'], p[1])
            url = "https://www.hackerrank.com/challenges/{}".format(p[1])
            c.close()
        else:
            # i.e. projecteuler/euler001
            path = os.path.join(p[0], p[1])
            path_source = path
            url = "https://www.hackerrank.com/contests/{}/challenges/{}".format(p[0], p[1])

        rootdir = os.path.relpath(os.path.dirname(__file__))

        paths = {}
        paths["model"] = os.path.join(rootdir, "offline", "models", path + ".json")
        paths["statement"] = os.path.join(rootdir, "offline", "statements", p[0], p[1] + ".pdf")
        paths["source"] = os.path.join(rootdir, path_source)
        paths["url"] = url

        paths['model_data'] = None

        if os.path.exists(paths["model"]):
            data = json.load(open(paths['model']))
            if data['status'] is True:
                paths['model_data'] = data['model']

        if what:
            return paths[what]

        return paths

    def cmd_open_challenge(self, path):
        if not path:
            return
        files = glob.glob(path + ".*")
        if len(files) >= 1:
                if platform.system() == 'Windows':
                    subprocess.check_call(["code.cmd", *files])
                else:
                    subprocess.check_call(["code", *files])

    def cmd_hrinit(self, lang="*", add_test=True):
        path = self.get_selected_challenge("model")
        if not path:
            return
        with open(path) as f:
            data = f.read()

        p = hrinit.HackerRankParser()
        p.feed(data)
        p.info()
        p.download()
        p.gen_stub(lang, add_test=add_test)

    def on_popup(self, event):
        p = self.current_paths = self.get_selected_challenge()
        if not self.current_paths:
            return

        def state(flag):
            # normal/active/disabled
            return ["disabled", "active"][flag]

        menu_lang = tk.Menu(self.root, tearoff=0)
        try:
            languages = p['model_data']['languages']
            for lang in set(languages) - set(['bash', 'python3', 'cpp14']):
                menu_lang.add_command(label=lang)
        except KeyError:
            languages = []

        menu = tk.Menu(self.root, tearoff=0)

        menu.add_command(label="Show on HackerRank",
                         command=lambda: webbrowser.open(p['url']))
        menu.add_command(label="Show PDF statement",
                         state=state(os.path.exists(p['statement'])),
                         command=lambda: subprocess.call(["open", p['statement']]))
        menu.add_separator()
        menu.add_command(label="Model details",
                         state=state(os.path.exists(p['model'])),
                         command=lambda: show_data(p['model_data']))
        menu.add_command(label="Open in Visual Studio Code",
                         state=state(len(glob.glob(p['source'] + ".*")) != 0),
                         command=lambda: self.cmd_open_challenge(p['source']))
        menu.add_separator()

        # add the language section
        if len(languages) == 0:
            menu.add_command(label="No language available", state="disabled")

        elif len(languages) == 1:

            menu.add_command(label="Init " + languages[0],
                             command=lambda: self.cmd_hrinit(languages[0]))

            if languages[0] == "text":
                # special case when the challenge except the plain text response,
                # not a program
                menu.add_command(label="Add Python3",
                                 command=lambda: self.cmd_hrinit("python3", False))
                menu.add_command(label="Add C++",
                                 command=lambda: self.cmd_hrinit("cpp14", True))

        else:
            menu.add_command(label="Init Python3",
                             state=state('python3' in languages),
                             command=lambda: self.cmd_hrinit("python3"))
            menu.add_command(label="Init C++",
                             state=state('cpp14' in languages),
                             command=lambda: self.cmd_hrinit("cpp14"))
#            menu.add_command(label="Init Bash",
#                             state=state('bash' in languages),
#                             command=lambda: self.cmd_hrinit("bash"))
            menu.add_cascade(label="Other languages", menu=menu_lang)

        try:
            menu.tk_popup(event.x_root, event.y_root, 0)
        finally:
            try:
                menu.grab_release()
            except tk.TclError:
                pass

    def show(self):
        self.root = root = tk.Tk()

        root.wm_title("HackerRank challenges")

        content = ttk.Frame(root, padding=(4, 4, 4, 4))
        self.tree = tree = ttk.Treeview(content, height=30)

        tree.tag_configure("solved", foreground='#37a90c')
        tree.heading("#0", text="Name")
        tree.column("#0", width=400)
        tree["columns"] = ("preview", "difficulty")
        tree.column("preview", width=500)
        tree.column("difficulty", width=80)
        tree.heading("preview", text="preview")
        tree.heading("difficulty", text="difficulty")

        def dict_factory(cursor, row):
            d = {}
            for idx, col in enumerate(cursor.description):
                d[col[0]] = row[idx]
            return d

        self.conn.row_factory = dict_factory

        c = self.conn.cursor()
        n = 0
        prev_track = None
        prev_subtrack = None
        for r in c.execute("select * from challenge order by track_slug, serial"):

            if r['track_slug'] != prev_track:
                prev_track = r['track_slug']
                prev_subtrack = None
                tree.insert("", n, r['track_slug'], text=r['track_name'])
                n += 1

            if r['subtrack_slug'] != prev_subtrack:
                prev_subtrack = r['subtrack_slug']
                tree.insert(r['track_slug'], n, r['track_slug'] + "/" + r['subtrack_slug'],
                            text=r['subtrack_name'])
                n += 1

            if r['subtrack_slug'] is None:
                k = r['track_slug']
            else:
                k = r['track_slug'] + '/' + r['subtrack_slug']

            tag = ""
            if r['solved']:
                tag = "solved"

            tree.insert(k, n, r['contest_slug'] + '~' + r['slug'],
                        text=r['name'],
                        values=(r['preview'], r['difficulty']), tag=tag)
            n += 1

        c.close()

        tree.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        content.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        content.columnconfigure(0, weight=1)
        content.rowconfigure(0, weight=1)

        tree.bind("<Double-1>", self.on_event)
        if platform.system() == 'Darwin':
            tree.bind("<Button-2>", self.on_popup)
        else:
            tree.bind("<Button-3>", self.on_popup)

        raise_app()
        root.mainloop()


if __name__ == '__main__':
    menu = hr_menu()
    menu.load_models()
    menu.show()
