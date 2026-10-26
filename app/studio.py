"""Y2JB Theme Creator ©MrGee — version 1.0."""
import os, sys, queue, shutil, struct, subprocess, tempfile, threading, locale
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageOps, ImageTk, ImageDraw
from ftp_client import FTPClient, FTPError
Y2JB_IDS = ("PPSA01650", "PPSA01651", "PPSA01652")
try:
    from tkinterdnd2 import TkinterDnD, DND_FILES
except ImportError:
    TkinterDnD = None
    DND_FILES = None

ROOT = Path(os.environ.get('MRGEE_HOME', Path(__file__).resolve().parents[1])).resolve()
SLOTS = [('icon0.png',(512,512)), ('pic0.png',(3840,2160)), ('pic1.png',(3840,2160)), ('pic2.png',(3840,2160))]
COL = dict(bg='#030C20', panel='#071831', tile='#091D3D', border='#18528F', bright='#087DFF', glow='#00BFFF', text='#F5FAFF', muted='#9DBAD9', side='#03112A')
LANGS = {'Deutsch':'de','English':'en'}
WORDS = {
'de': dict(select='BILDER AUSWÄHLEN',preview='VORSCHAU & ANPASSEN',convert='KONVERTIEREN',export='EXPORT',headline='DEINE PS5-GRAFIKEN',hint='Bilder hineinziehen oder auswählen',choose='BILD AUSWÄHLEN',optional='OPTIONAL',adjust='BILDANPASSUNG',crop='Bildfüllend zuschneiden',contain='Ganzes Bild mit Rändern',folder='ZIELORDNER',browse='ÄNDERN',format='AUSGABEFORMAT',create='PS5-PAKET ERSTELLEN',status='KONVERTIERUNGSSTATUS',ready='Bereit',loaded='Bilder geladen',show='VORSCHAU',input='EINGABE ÖFFNEN',output='EXPORT ÖFFNEN',missing='Bitte mindestens ein Bild hinzufügen.',finished='Paket erfolgreich erstellt!',error='Fehler',save='Vor dem Upload Originaldateien sichern!',zoom='Bildvorschau',drop='Bild hier ablegen',lang='Sprache'),
'en': dict(select='SELECT IMAGES',preview='PREVIEW & ADJUST',convert='CONVERT',export='EXPORT',headline='YOUR PS5 GRAPHICS',hint='Drop images here or browse',choose='CHOOSE IMAGE',optional='OPTIONAL',adjust='IMAGE FITTING',crop='Crop to fill',contain='Fit entire image with borders',folder='OUTPUT FOLDER',browse='CHANGE',format='OUTPUT FORMAT',create='BUILD PS5 PACKAGE',status='CONVERSION STATUS',ready='Ready',loaded='images loaded',show='PREVIEW',input='OPEN INPUT',output='OPEN EXPORT',missing='Please add at least one image.',finished='Package successfully created!',error='Error',save='Back up originals before uploading!',zoom='Image preview',drop='Drop image here',lang='Language'),
'fr':dict(select='CHOISIR IMAGES',preview='APERÇU ET AJUSTEMENT',convert='CONVERTIR',export='EXPORTER',headline='VOS IMAGES PS5',choose='CHOISIR UNE IMAGE',create='CRÉER LE PACK PS5',browse='MODIFIER',show='APERÇU',folder='DOSSIER DE SORTIE'),
'es':dict(select='ELEGIR IMÁGENES',preview='VISTA PREVIA',convert='CONVERTIR',export='EXPORTAR',headline='TUS IMÁGENES PS5',choose='ELEGIR IMAGEN',create='CREAR PAQUETE PS5',browse='CAMBIAR',show='VISTA PREVIA',folder='CARPETA DESTINO'),
'it':dict(select='SCEGLI IMMAGINI',preview='ANTEPRIMA',convert='CONVERTI',export='ESPORTA',headline='LE TUE IMMAGINI PS5',choose='SCEGLI IMMAGINE',create='CREA PACCHETTO PS5'),
'pt':dict(select='ESCOLHER IMAGENS',preview='PRÉ-VISUALIZAR',convert='CONVERTER',export='EXPORTAR',headline='IMAGENS PS5',choose='ESCOLHER IMAGEM',create='CRIAR PACOTE PS5'),
'nl':dict(select='AFBEELDINGEN KIEZEN',preview='VOORBEELD',convert='CONVERTEREN',export='EXPORT',headline='JOUW PS5-AFBEELDINGEN',choose='KIES AFBEELDING',create='MAAK PS5-PAKKET'),
'pl':dict(select='WYBIERZ OBRAZY',preview='PODGLĄD',convert='KONWERTUJ',export='EKSPORT',headline='GRAFIKI PS5',choose='WYBIERZ OBRAZ',create='UTWÓRZ PAKIET PS5'),
'tr':dict(select='GÖRSELLERİ SEÇ',preview='ÖNİZLEME',convert='DÖNÜŞTÜR',export='DIŞA AKTAR',headline='PS5 GÖRSELLERİN',choose='GÖRSEL SEÇ',create='PS5 PAKETİ OLUŞTUR'),
'ru':dict(select='ВЫБРАТЬ ИЗОБРАЖЕНИЯ',preview='ПРЕДПРОСМОТР',convert='КОНВЕРТАЦИЯ',export='ЭКСПОРТ',headline='ГРАФИКА PS5',choose='ВЫБРАТЬ ФАЙЛ',create='СОЗДАТЬ ПАКЕТ PS5'),
'ja':dict(select='画像を選択',preview='プレビュー',convert='変換',export='書き出し',headline='PS5 画像',choose='画像を選択',create='PS5 パッケージを作成'),
'ko':dict(select='이미지 선택',preview='미리보기',convert='변환',export='내보내기',headline='PS5 이미지',choose='이미지 선택',create='PS5 패키지 만들기'),
'zh':dict(select='选择图片',preview='预览和调整',convert='转换',export='导出',headline='PS5 图片',choose='选择图片',create='创建 PS5 文件包')}

def showpath(path): return str(path).replace('\\','/')
def verify_dds(path, dims):
    with open(path,'rb') as f: data=f.read(148)
    if len(data)<148 or data[:4]!=b'DDS ' or data[84:88]!=b'DX10': raise RuntimeError(f'{path.name}: ungültiger DDS-DX10-Header')
    if struct.unpack_from('<I',data,128)[0]!=98: raise RuntimeError(f'{path.name}: BC7_UNORM fehlt')
    height,width=struct.unpack_from('<II',data,12)
    if (width,height)!=dims: raise RuntimeError(f'{path.name}: {width}×{height} statt {dims}')

def build_package(source,dest,texconv,mode,progress):
    source,dest,texconv=Path(source),Path(dest),Path(texconv)
    if not texconv.is_file(): raise RuntimeError('tools/texconv.exe fehlt.')
    selected=[(n,s) for n,s in SLOTS if (source/n).is_file()]
    if not selected: raise RuntimeError('Bitte mindestens ein Bild hinzufügen.')
    if source.resolve()==dest.resolve(): raise RuntimeError('Ein- und Ausgabeordner dürfen nicht identisch sein.')
    dest.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='mrgee_',dir=dest.parent) as tmp:
        stage=Path(tmp)
        for index,(name,dims) in enumerate(selected,1):
            with Image.open(source/name) as im:
                img=im.convert('RGB')
                if mode=='crop': img=ImageOps.fit(img,dims,method=Image.Resampling.LANCZOS)
                else:
                    fit=ImageOps.contain(img,dims,method=Image.Resampling.LANCZOS)
                    img=Image.new('RGB',dims,(3,12,32));img.paste(fit,((dims[0]-fit.width)//2,(dims[1]-fit.height)//2))
                img.save(stage/name,'PNG')
            progress(index,len(selected)*2,f'{name} PNG')
        for index,(name,dims) in enumerate(selected,len(selected)+1):
            cmd=[str(texconv),'-f','BC7_UNORM','-m','1','-y','-o',str(stage),str(stage/name)]
            p=subprocess.run(cmd,capture_output=True,text=True,timeout=420,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
            if p.returncode: raise RuntimeError(f'texconv {name}: {(p.stderr or p.stdout)[-1600:]}')
            dds=stage/name.replace('.png','.dds')
            if not dds.exists(): raise RuntimeError(f'{dds.name} fehlt.')
            verify_dds(dds,dims)
            progress(index,len(selected)*2,f'{dds.name} BC7 ✓')
        (stage/'UPLOAD_HINWEISE.txt').write_text('Y2JB Theme Creator ©MrGee · Version 1.0\n\nNur erzeugte PNG/DDS-Dateien verwenden.\nVorhandene Dateien vor dem Ersetzen lokal sichern.\nPS5-Zielordner wird von der App unter /user/appmeta/ erkannt.\n',encoding='utf-8')
        for file in stage.iterdir(): shutil.copy2(file,dest/file.name)
    return dest

class Studio:
    def __init__(self,root):
        self.root=root;self.root.title('Y2JB Theme Creator ©MrGee | 1.0');self.root.geometry('1500x930');self.root.minsize(1120,730);self.root.configure(bg=COL['bg'])
        self.indir=ROOT/'EINGABE';self.outdir=ROOT/'PS5_UPLOAD';self.tex=ROOT/'tools'/'texconv.exe'
        self.indir.mkdir(exist_ok=True);self.outdir.mkdir(exist_ok=True)
        self.ps5ip=tk.StringVar(value='');self.connection_status=tk.StringVar(value='Nicht geprüft');self.ppsa_status=tk.StringVar(value='Nicht geprüft');self.target_status=tk.StringVar(value='Nicht geprüft');self.discovered_ppsa=[];self.selected_ppsa=None;self.mode=tk.StringVar(value='crop');self.progress_value=tk.DoubleVar(value=0);self.status=tk.StringVar(value='');self.running=False;self.events=queue.Queue();self.images={};self.tiles={};self.fm_info=tk.StringVar(value='Noch kein Upload gestartet.');self.fm_busy=False;self.fm_progress=tk.DoubleVar(value=0);self.ftp_port=tk.StringVar(value="2121");self._active_ftp_client=None;self.last_generated_files=[];self.activity_files=tk.StringVar(value='Hier erscheinen die in diesem Durchlauf erstellten Dateien.');self.pending_upload_after_discovery=False
        system=(locale.getlocale()[0] or 'en').split('_')[0].lower();system=system if system in WORDS else 'en'
        self.lang=tk.StringVar(value=next((name for name,code in LANGS.items() if code==system),'English'))
        self.build();self.refresh();self.root.after(90,self.poll);self.root.after(20000,self.connection_heartbeat)
    def t(self,key):return WORDS.get(LANGS.get(self.lang.get(),'en'),{}).get(key,WORDS['en'].get(key,key))
    def ui(self,de,en):return en if self.lang.get()=='English' else de
    def label(self,parent,text,size=11,color=None,bold=False,bg=None,**kwargs):
        return tk.Label(parent,text=text,font=('Segoe UI',size,'bold' if bold else 'normal'),fg=color or COL['text'],bg=bg or parent.cget('bg'),**kwargs)
    def button(self,parent,text,cmd,primary=False,size=10):
        return tk.Button(parent,text=text,command=cmd,relief='flat',bd=0,cursor='hand2',bg=COL['bright'] if primary else '#102D55',fg='white',activebackground='#36A7FF',activeforeground='white',font=('Segoe UI',size,'bold'),padx=12,pady=11)
    def build(self):
        style=ttk.Style();style.theme_use('clam');style.configure('Treeview',background='#0B2040',fieldbackground='#0B2040',foreground='#E6F4FF',rowheight=32,borderwidth=0,font=('Segoe UI',10));style.configure('Treeview.Heading',background='#153B66',foreground='white',font=('Segoe UI',10,'bold'));style.map('Treeview',background=[('selected','#1268BB')],foreground=[('selected','white')]);style.configure('Vertical.TScrollbar',background='#164779',troughcolor='#08182F')
        shell=tk.Frame(self.root,bg=COL['bg']);shell.pack(fill='both',expand=True)
        shell.grid_rowconfigure(0,weight=1);shell.grid_columnconfigure(1,weight=1)
        sidebar=tk.Frame(shell,bg=COL['side'],width=246);sidebar.grid(row=0,column=0,sticky='nsw');sidebar.grid_propagate(False)
        self.label(sidebar,'Y2JB THEME CREATOR',10,'#8BC9FF',True).pack(anchor='w',padx=18,pady=(22,4))
        art_panel=tk.Frame(sidebar,bg=COL['side']);art_panel.pack(fill='both',expand=True,padx=10,pady=8)
        art=ROOT/'assets'/'console.png'
        self.art_source=None
        if art.is_file():
            with Image.open(art) as im:self.art_source=im.convert('RGBA')
            self.sidebar_art=self.label(art_panel,'',bg=COL['side'],anchor='center')
            self.sidebar_art.pack(fill='both',expand=True)
            self.sidebar_art.bind('<Configure>',self.resize_sidebar_art)
        self.label(sidebar,'CREATE YOUR OWN Y2JB THEMES',9,'#A8C9E8',True,wraplength=210,justify='left').pack(anchor='w',padx=18,pady=(5,3))
        self.label(sidebar,'©MrGee  ·  VERSION 1.0',9,'#70BBFF',True).pack(anchor='w',padx=18,pady=(3,18))

        body=tk.Frame(shell,bg=COL['bg']);body.grid(row=0,column=1,sticky='nsew');body.grid_rowconfigure(1,weight=1);body.grid_columnconfigure(0,weight=1)
        top=tk.Frame(body,bg='#06152B',height=80,highlightbackground='#173B62',highlightthickness=1);top.grid(row=0,column=0,sticky='ew');top.grid_propagate(False)
        brand=tk.Frame(top,bg='#06152B');brand.pack(side='left',fill='y',padx=(20,22))
        self.label(brand,'Y2JB Theme Creator ©MrGee',15,'#F7FAFF',True,bg='#06152B').pack(anchor='w',pady=(16,0))
        self.label(brand,'Create Your Own Y2JB Themes',9,'#83B8EA',bg='#06152B').pack(anchor='w',pady=(2,0))
        self.nav_buttons={}
        nav=tk.Frame(top,bg='#06152B');nav.pack(side='left',fill='y')
        for key,title in [('dashboard','Dashboard'),('studio','Theme Studio')]:
            btn=tk.Button(nav,text=title,command=lambda k=key:self.show_view(k),relief='flat',bd=0,cursor='hand2',bg='#06152B',fg='#AFC8E2',activebackground='#0C3158',activeforeground='white',font=('Segoe UI',10,'bold'),padx=16,pady=8)
            btn.pack(side='left',fill='y',padx=3,pady=13);self.nav_buttons[key]=btn
        self.label(top,'VERSION 1.0',9,'#A5C9EB',True,bg='#06152B').pack(side='right',padx=20)

        self.view_host=tk.Frame(body,bg=COL['bg']);self.view_host.grid(row=1,column=0,sticky='nsew')
        self.views={}
        dashboard=tk.Frame(self.view_host,bg=COL['bg'],padx=30,pady=24);dashboard.place(relx=0,rely=0,relwidth=1,relheight=1);self.views['dashboard']=dashboard
        main=tk.Frame(self.view_host,bg=COL['bg'],padx=26,pady=18);main.place(relx=0,rely=0,relwidth=1,relheight=1);self.views['studio']=main
        self.build_dashboard(dashboard)
        head=tk.Frame(main,bg=COL['bg']);head.pack(fill='x',pady=(0,15))
        self.label(head,self.ui('THEME STUDIO','THEME STUDIO'),20,'#F8FCFF',True).pack(side='left')
        language=ttk.Combobox(head,textvariable=self.lang,values=list(LANGS),state='readonly',width=15,font=('Segoe UI',10));language.pack(side='right',padx=3,pady=6)
        language.bind('<<ComboboxSelected>>',lambda e:self.rebuild())
        self.label(head,'🌐',16,'#77BFFF').pack(side='right',padx=7)
        steps=tk.Frame(main,bg='#0A2448',highlightbackground='#1262AF',highlightthickness=1);steps.pack(fill='x',pady=(0,17))
        self.step_labels=[]
        for i,key in enumerate(('select','preview','convert','export'),1):
            item=tk.Frame(steps,bg='#0869CF' if i==1 else '#0A2448');item.pack(side='left',fill='both',expand=True,padx=2,pady=3)
            ico=('▧','⌕','⚙','⇧')[i-1]
            l=self.label(item,f'{ico}   {i:02d}  {self.t(key)}',10,'white',True,bg=item.cget('bg'))
            l.pack(padx=9,pady=17);self.step_labels.append((l,key))
        heading=tk.Frame(main,bg=COL['bg']);heading.pack(fill='x',pady=(0,12))
        self.label(heading,self.t('headline'),15,'#FFFFFF',True).pack(side='left')
        self.label(heading,self.t('hint'),10,COL['muted']).pack(side='right')
        grid=tk.Frame(main,bg=COL['bg']);grid.pack(fill='both',expand=True)
        for i,(name,dims) in enumerate(SLOTS):
            grid.grid_columnconfigure(i,weight=1,uniform='slot');grid.grid_rowconfigure(0,weight=1)
            tile=tk.Frame(grid,bg=COL['panel'],highlightbackground=COL['border'],highlightthickness=1)
            tile.grid(row=0,column=i,sticky='nsew',padx=5)
            self.label(tile,'ICON' if i==0 else f'BACKGROUND {i}',11,'white',True).pack(anchor='w',padx=12,pady=(13,3))
            self.label(tile,f'{dims[0]} × {dims[1]}',9,'#80BDF7').pack(anchor='w',padx=12,pady=(0,9))
            image=tk.Label(tile,text='＋\n'+self.t('drop'),font=('Segoe UI',11,'bold'),bg=COL['tile'],fg='#A9D8FF',cursor='hand2',justify='center')
            image.pack(fill='both',expand=True,padx=10,pady=(0,9));image.bind('<Button-1>',lambda e,n=name:self.pick(n))
            if DND_FILES:
                image.drop_target_register(DND_FILES);image.dnd_bind('<<Drop>>',lambda e,n=name:self.drop(e,n))
            controls=tk.Frame(tile,bg=COL['panel']);controls.pack(fill='x',padx=10,pady=(0,11))
            self.button(controls,self.t('choose'),lambda n=name:self.pick(n),primary=True,size=9).pack(side='left',fill='x',expand=True)
            self.button(controls,'⌕',lambda n=name:self.preview(n),size=11).pack(side='right',padx=(6,0))
            self.tiles[name]=image
        fitbar=tk.Frame(main,bg='#081A36',highlightbackground=COL['border'],highlightthickness=1);fitbar.pack(fill='x',pady=(13,9))
        self.label(fitbar,self.t('adjust'),10,'#CDE6FF',True,bg='#081A36').pack(side='left',padx=12,pady=13)
        for val,key in [('crop','crop'),('contain','contain')]:
            tk.Radiobutton(fitbar,text=self.t(key),variable=self.mode,value=val,bg='#081A36',fg='#FFFFFF',selectcolor='#124C86',activebackground='#081A36',activeforeground='white',font=('Segoe UI',10)).pack(side='left',padx=7)
        self.button(fitbar,self.t('show'),self.preview_first).pack(side='right',padx=6,pady=4)
        settings=tk.Frame(main,bg=COL['bg']);settings.pack(fill='x',pady=(0,10))
        pathbox=tk.Frame(settings,bg=COL['panel'],highlightbackground=COL['border'],highlightthickness=1);pathbox.pack(side='left',fill='x',expand=True,padx=(0,8))
        self.label(pathbox,self.t('folder'),9,'#98C8F9',True).pack(anchor='w',padx=12,pady=(8,0))
        pathline=tk.Frame(pathbox,bg=COL['panel']);pathline.pack(fill='x',padx=12,pady=(0,7))
        self.path_label=self.label(pathline,showpath(self.outdir),10,'#F3FAFF',bg=COL['panel'],anchor='w');self.path_label.pack(side='left',fill='x',expand=True)
        self.button(pathline,self.t('browse'),self.choose_output,size=9).pack(side='right')
        fmt=tk.Frame(settings,bg=COL['panel'],highlightbackground=COL['border'],highlightthickness=1);fmt.pack(side='left',padx=(0,8))
        self.label(fmt,self.t('format'),9,'#98C8F9',True).pack(anchor='w',padx=12,pady=(8,0))
        self.label(fmt,'BC7_UNORM  /  DDS DX10',10,'white').pack(padx=12,pady=(5,15))
        self.go=self.button(settings,'🎮  '+self.t('create'),self.start,True,12);self.go.pack(side='right',fill='y')
        bottom=tk.Frame(main,bg=COL['panel'],highlightbackground=COL['border'],highlightthickness=1);bottom.pack(fill='x')
        row=tk.Frame(bottom,bg=COL['panel']);row.pack(fill='x',padx=12,pady=(9,5))
        self.label(row,self.t('status'),10,'#D6EAFF',True).pack(side='left')
        tk.Label(row,textvariable=self.status,bg=COL['panel'],fg='#A9CFFF',font=('Segoe UI',10)).pack(side='right')
        style=ttk.Style();style.theme_use('clam');style.configure('MrGee.Horizontal.TProgressbar',background='#058BFF',troughcolor='#07162B',bordercolor='#07162B',lightcolor='#058BFF',darkcolor='#058BFF')
        self.progress=ttk.Progressbar(bottom,variable=self.progress_value,maximum=100,style='MrGee.Horizontal.TProgressbar');self.progress.pack(fill='x',padx=12,pady=(0,10))
        ps5=tk.Frame(main,bg='#081A36',highlightbackground='#1674C3',highlightthickness=1);ps5.pack(fill='x',pady=(8,0))
        self.label(ps5,'⚡ EIGENSTÄNDIGER FTP-SERVER · PORT 2121',10,'#8DCFFF',True,bg='#081A36').pack(side='left',padx=10)
        self.label(ps5,'ftpsrv-ELF auf der PS5 starten → im Dashboard verbinden',9,'#B9DFFF',bg='#081A36').pack(side='left',padx=8,pady=10)
        footer=tk.Frame(main,bg=COL['bg']);footer.pack(fill='x',pady=(8,0))
        self.button(footer,self.t('input'),lambda:self.open_dir(self.indir),size=9).pack(side='left')
        self.button(footer,self.t('output'),lambda:self.open_dir(self.outdir),size=9).pack(side='left',padx=7)
        self.theme_upload_button=self.button(footer,self.ui('DIREKT AUF PS5 HOCHLADEN','UPLOAD DIRECTLY TO PS5'),self.theme_upload,True,size=10)
        self.theme_upload_button.pack(side='right')
        self.theme_upload_button.config(state='disabled')
        self.show_view(getattr(self,'current_view','dashboard'))

    def resize_sidebar_art(self,event=None):
        if self.art_source is None:return
        width=max(1,self.sidebar_art.winfo_width()-10);height=max(1,self.sidebar_art.winfo_height()-10)
        photo=ImageTk.PhotoImage(ImageOps.contain(self.art_source,(width,height)))
        self.images['console']=photo;self.sidebar_art.configure(image=photo)

    def show_view(self,key):
        if key not in self.views:return
        self.current_view=key;self.views[key].tkraise()
        for name,button in self.nav_buttons.items():
            selected=name==key
            button.configure(bg='#0C3158' if selected else '#06152B',fg='#FFFFFF' if selected else '#AFC8E2',highlightthickness=0)
    def build_dashboard(self, parent):
        head=tk.Frame(parent,bg=COL['bg']);head.pack(fill='x',pady=(7,24))
        self.label(head,self.ui('Dashboard','Dashboard'),28,'#F7FAFF',True).pack(anchor='w')
        self.label(head,self.ui('Verbindung und Y2JB-Status auf einen Blick','Connection and Y2JB status at a glance'),11,'#8EAFD0').pack(anchor='w',pady=(5,0))

        action=tk.Frame(parent,bg='#0A203B',highlightbackground='#1B456D',highlightthickness=1);action.pack(fill='x',pady=(0,26))
        fields=tk.Frame(action,bg='#0A203B');fields.pack(side='left',padx=18,pady=15)
        self.label(fields,self.ui('PS5-IP-ADRESSE','PS5 IP ADDRESS'),8,'#82B4E1',True,bg='#0A203B').pack(anchor='w',pady=(0,5))
        tk.Entry(fields,textvariable=self.ps5ip,width=21,bg='#102D4D',fg='#FFFFFF',insertbackground='white',relief='flat',font=('Segoe UI',11),highlightthickness=1,highlightbackground='#28547B').pack(anchor='w',ipady=7)
        divider=tk.Frame(action,bg='#20415F',width=1);divider.pack(side='left',fill='y',pady=16,padx=4)
        portbox=tk.Frame(action,bg='#0A203B');portbox.pack(side='left',padx=15,pady=15)
        self.label(portbox,self.ui('FTP-PORT','FTP PORT'),8,'#82B4E1',True,bg='#0A203B').pack(anchor='w',pady=(0,5))
        tk.Entry(portbox,textvariable=self.ftp_port,width=8,state='readonly',readonlybackground='#102D4D',fg='#FFFFFF',relief='flat',font=('Segoe UI',11),highlightthickness=1,highlightbackground='#28547B').pack(anchor='w',ipady=7)
        self.label(action,self.ui('ftpsrv selbst auf der PS5 starten','Start ftpsrv yourself on the PS5'),9,'#91B1CE',bg='#0A203B').pack(side='left',padx=16)
        self.button(action,self.ui('VERBINDEN  →','CONNECT  →'),self.fm_discover,True,10).pack(side='right',padx=16,pady=14)

        section=tk.Frame(parent,bg=COL['bg']);section.pack(fill='x',pady=(0,10))
        self.label(section,self.ui('VERBINDUNGSSTATUS','CONNECTION STATUS'),9,'#8CB7DF',True).pack(side='left')
        self.label(section,'FTP 2121',9,'#5B83AA',True).pack(side='right')
        board=tk.Frame(parent,bg='#091B32',highlightbackground='#1A4268',highlightthickness=1);board.pack(fill='x')
        stages=(
            ('01',self.ui('FTP-VERBINDUNG','FTP CONNECTION'),self.connection_status,self.ui('PS5-IP erreichbar über ftpsrv','PS5 IP reachable through ftpsrv')),
            ('02',self.ui('Y2JB-ORDNER','Y2JB FOLDER'),self.ppsa_status,self.ui('PPSA01650 · PPSA01651 · PPSA01652','PPSA01650 · PPSA01651 · PPSA01652')),
            ('03',self.ui('PS5-ZIELORDNER','PS5 TARGET FOLDER'),self.target_status,self.ui('Erreichbarkeit wird beim Upload geprüft','Checked when upload starts')),
        )
        self.status_dots=[];self.status_trace_ids=[]
        for index,(number,title,variable,detail) in enumerate(stages):
            board.grid_columnconfigure(index,weight=1,uniform='status')
            cell=tk.Frame(board,bg='#091B32');cell.grid(row=0,column=index,sticky='nsew',padx=0,pady=0)
            if index:
                tk.Frame(cell,bg='#1C3B5B',width=1).place(relx=0,rely=.14,relheight=.72)
            topline=tk.Frame(cell,bg='#091B32');topline.pack(fill='x',padx=22,pady=(22,15))
            self.label(topline,number,10,'#52789C',True,bg='#091B32').pack(side='left')
            dot=self.label(topline,'●',11,'#6A829A',True,bg='#091B32');dot.pack(side='right')
            self.status_dots.append((variable,dot))
            self.label(cell,title,9,'#92BDE4',True,bg='#091B32').pack(anchor='w',padx=22,pady=(0,9))
            value=tk.Label(cell,textvariable=variable,bg='#091B32',fg='#F4F8FC',anchor='w',justify='left',wraplength=260,font=('Segoe UI',13,'bold'),height=2)
            value.pack(fill='x',padx=22,pady=(0,8))
            self.label(cell,detail,9,'#718DA9',bg='#091B32',anchor='w',wraplength=260).pack(fill='x',padx=22,pady=(0,22))
            trace_id=variable.trace_add('write',lambda *_args,v=variable,d=dot:self.update_status_dot(v,d))
            self.status_trace_ids.append((variable,trace_id))
            self.update_status_dot(variable,dot)

        activity=tk.Frame(parent,bg='#081A30',highlightbackground='#1A4268',highlightthickness=1)
        activity.pack(fill='both',expand=True,pady=(16,0))
        title=tk.Frame(activity,bg='#081A30');title.pack(fill='x',padx=18,pady=(14,8))
        self.label(title,self.ui('THEME-PAKET & UPLOAD','THEME PACKAGE & UPLOAD'),11,'#D8ECFF',True,bg='#081A30').pack(side='left')
        self.label(title,self.ui('Fortschritt dieses Durchlaufs','Progress for this run'),9,'#7898B8',bg='#081A30').pack(side='right')

        buildrow=tk.Frame(activity,bg='#081A30');buildrow.pack(fill='x',padx=18,pady=(2,8))
        tk.Label(buildrow,textvariable=self.status,bg='#081A30',fg='#EAF5FF',anchor='w',font=('Segoe UI',10,'bold')).pack(fill='x')
        self.dashboard_build_bar=ttk.Progressbar(buildrow,variable=self.progress_value,maximum=100,style='MrGee.Horizontal.TProgressbar')
        self.dashboard_build_bar.pack(fill='x',pady=(5,0))

        uploadrow=tk.Frame(activity,bg='#081A30');uploadrow.pack(fill='x',padx=18,pady=(3,8))
        tk.Label(uploadrow,textvariable=self.fm_info,bg='#081A30',fg='#B8D6F2',anchor='w',justify='left',wraplength=950,font=('Segoe UI',10)).pack(fill='x')
        self.dashboard_upload_bar=ttk.Progressbar(uploadrow,variable=self.fm_progress,maximum=100,style='MrGee.Horizontal.TProgressbar')
        self.dashboard_upload_bar.pack(fill='x',pady=(5,0))
        tk.Label(activity,textvariable=self.activity_files,bg='#081A30',fg='#7FA9CF',anchor='w',justify='left',wraplength=950,font=('Segoe UI',9)).pack(fill='x',padx=18,pady=(0,14))

    def update_status_dot(self,variable,dot):
        value=variable.get().lower()
        if any(word in value for word in ('erreichbar','verbunden','found','gefunden','bereit','ready')):
            color='#42D79B'
        elif any(word in value for word in ('fehler','failed','kein treffer','no match','nicht bereit','not ready')):
            color='#FF6B76'
        elif any(word in value for word in ('läuft','prüf','checking','searching')):
            color='#58B8FF'
        else:
            color='#6A829A'
        dot.configure(fg=color)
    def ftp_client(self):
        if threading.current_thread() is not threading.main_thread() and self._active_ftp_client is not None:
            return self._active_ftp_client
        return FTPClient(self.ps5ip.get().strip(),int(self.ftp_port.get().strip()))

    def fm_run(self, task, success):
        if self.fm_busy:
            if success!='heartbeat':self.fm_info.set('Bitte den laufenden FTP-Vorgang abwarten.')
            return
        self.fm_busy=True
        if success!='heartbeat':
            self.fm_info.set('Verbinde mit FTP · Anfrage läuft …');self.fm_progress.set(0)
        try:
            self._active_ftp_client=FTPClient(self.ps5ip.get().strip(),int(self.ftp_port.get().strip()))
        except Exception as exc:
            self.fm_busy=False
            self.events.put(('fm_error',(success,str(exc))))
            return
        def worker():
            try:self.events.put(('fm_success',(success,task())))
            except Exception as exc:self.events.put(('fm_error',(success,str(exc))))
        threading.Thread(target=worker,daemon=True).start()

    def transfer_progress(self, detail):
        def update(sent, total):
            self.events.put(('transfer_progress',(sent,total,detail)))
        return update

    def connection_heartbeat(self):
        if getattr(self,'_has_confirmed_ftp',False) and not self.fm_busy:
            self.fm_run(lambda:self.ftp_client().list('/'),'heartbeat')
        self.root.after(20000,self.connection_heartbeat)

    def fm_discover(self):
        """Find only the three configured Y2JB app IDs, without writing to the PS5."""
        key=(self.ps5ip.get().strip(),self.ftp_port.get().strip())
        self.fm_scan_key=key
        self.selected_ppsa=None
        self.theme_upload_button.config(state='disabled')
        self.connection_status.set('Verbindung wird geprüft …')
        self.ppsa_status.set('Suche läuft …')
        self.target_status.set('Wird geprüft …')
        self.fm_info.set('Verbinde … suche Y2JB-Ordner in /user/appmeta')
        self.fm_progress.set(0)
        def task():
            client=self.ftp_client()
            client.list('/')
            entries=client.list('/user/appmeta')
            found=[entry['name'] for entry in entries
                   if entry['is_dir'] and entry['name'].upper() in Y2JB_IDS]
            # A stable order makes multiple results easy to compare.
            found=sorted(set(found),key=lambda name:Y2JB_IDS.index(name.upper()))
            return found
        self.fm_run(task,'discover')

    def fm_apply_discovery(self,found):
        self.connection_status.set(f'{self.ui("Verbunden","Reachable")} · {self.ps5ip.get().strip()}:{self.ftp_port.get().strip()}')
        self.discovered_ppsa=list(found)
        if not found:
            self.selected_ppsa=None
            self.ppsa_status.set(self.ui('Kein Treffer in /user/appmeta','No match in /user/appmeta'))
            self.target_status.set(self.ui('Kein PPSA-Zielordner gefunden','No PPSA target folder found'))
            self.theme_upload_button.config(state='disabled')
            self.fm_info.set('FTP verbunden · in /user/appmeta wurde keine unterstützte PPSA-ID gefunden.')
            return
        if len(found)==1:
            chosen=found[0]
        else:
            from tkinter import simpledialog
            chosen=simpledialog.askstring('Y2JB-Ordner auswählen',
                'Mehrere Y2JB-Ordner gefunden:\n'+'\n'.join(found)+
                '\n\nWelchen Ordner öffnen? (PPSA-ID eingeben)',
                initialvalue=found[0],parent=self.root)
            if chosen is None:
                self.ppsa_status.set('Auswahl abgebrochen')
                self.target_status.set('Nicht bereit · kein Ziel ausgewählt')
                self.fm_info.set('Y2JB-Suche abgeschlossen · Auswahl abgebrochen')
                return
            chosen=chosen.strip().upper()
            if chosen not in found:
                self.ppsa_status.set('Ungültige Auswahl')
                self.target_status.set('Nicht bereit · kein Ziel ausgewählt')
                messagebox.showwarning('Y2JB-Ordner','Bitte eine der gefundenen PPSA-IDs eingeben.')
                return
        self.selected_ppsa=chosen
        self.ppsa_status.set(f'{self.ui("Gefunden","Found")} · {chosen}')
        self.theme_upload_button.config(state='normal')
        self.target_status.set(f'{self.ui("Bereit","Ready")} · /user/appmeta/{chosen}')
        self.fm_info.set('PPSA-Ziel erkannt · Paket kann erstellt und hochgeladen werden.')
        if self.pending_upload_after_discovery and self.last_generated_files:
            self.pending_upload_after_discovery=False
            self.fm_info.set('PS5 verbunden · starte den ausstehenden Theme-Upload …')
            self.theme_upload(automatic=True,files=[Path(p) for p in self.last_generated_files])

    def theme_upload(self, automatic=False, files=None):
        self.show_view('dashboard')
        if self.fm_busy:
            self.fm_info.set(self.ui('Warte auf den laufenden FTP-Vorgang, Upload folgt danach.','Waiting for the current FTP request; upload will continue next.'))
            self.root.after(350,lambda a=automatic,f=files:self.theme_upload(automatic=a,files=f))
            return
        if not self.selected_ppsa:
            message='Paket erstellt. Für den automatischen Upload zuerst verbinden und den Y2JB-PPSA-Ordner erkennen lassen.' if automatic else 'Zuerst eine Verbindung herstellen und den Y2JB-PPSA-Ordner erkennen lassen.'
            return messagebox.showwarning('PS5-Upload',message)
        target=f'/user/appmeta/{self.selected_ppsa}'
        files=list(files if files is not None else self.last_generated_files)
        if not files:
            files=[self.outdir/name for name,_ in SLOTS]
            files=[p for p in files if p.is_file()]
            files += [self.outdir/name.replace('.png','.dds') for name,_ in SLOTS if (self.outdir/name.replace('.png','.dds')).is_file()]
        files=[Path(p) for p in files if Path(p).is_file()]
        if not files:
            return messagebox.showinfo('PS5-Upload','Im Exportordner liegen noch keine PNG/DDS-Dateien. Erstelle zuerst das Paket.')
        if not automatic:
            listing='\n'.join('• '+p.name for p in files)
            if not messagebox.askyesno('Theme direkt hochladen',f'Ziel: {target}\n\nDateien:\n{listing}\n\nVorhandene Dateien werden nur nach Rückfrage und erfolgreicher lokaler Sicherung ersetzt.'):
                return
        def preflight():
            entries=self.ftp_client().list(target)
            return (files,target,entries)
        self.fm_run(preflight,'theme_preflight_auto' if automatic else 'theme_preflight')

    def theme_confirm_upload(self, files, target, entries, automatic=False):
        existing={item['name']:item for item in entries}
        plan=[]
        self.target_status.set(f'{self.ui("Zielordner geprüft","Target folder checked")} · {target}')
        self.fm_progress.set(0)
        self.fm_info.set(self.ui('Prüfe vorhandene Dateien und frage vor jedem Ersetzen.','Checking existing files and asking before each replacement.'))
        for local in files:
            item=existing.get(local.name)
            if item and item['is_dir']:
                messagebox.showwarning('Upload übersprungen',f'Im Ziel liegt ein Ordner mit diesem Namen:\n{target}/{local.name}')
                continue
            overwrite=False
            if item:
                self.fm_info.set(self.ui('Bestätigung erforderlich · ','Confirmation required · ')+local.name)
                self.activity_files.set(self.ui('Datei bereits vorhanden: ','File already exists: ')+target+'/'+local.name)
                answer=messagebox.askyesnocancel('Datei existiert bereits',
                    f'{target}/{local.name}\n\nJa: lokales Backup erstellen und ersetzen\nNein: Datei überspringen\nAbbrechen: weiteren Upload stoppen',parent=self.root)
                if answer is None:
                    break
                if not answer:
                    continue
                overwrite=True
            plan.append((local,overwrite,item.get('size') if item else None))
        if not plan:
            self.fm_info.set('Kein Upload ausgeführt · alle Dateien übersprungen oder abgebrochen')
            self.target_status.set('Upload nicht ausgeführt')
            return
        summary='\n'.join(f'{local.name}'+(' · Backup & Ersetzen' if overwrite else ' · Neu anlegen') for local,overwrite,_ in plan)
        if not automatic and not messagebox.askyesno('Upload bestätigen',f'Ziel: {target}\n\n{summary}\n\nFortfahren?',parent=self.root):
            self.fm_info.set('Upload vor dem Start abgebrochen.')
            return
        self.activity_files.set(self.ui('Freigegeben für Upload: ','Approved for upload: ')+', '.join(local.name for local,_,_ in plan))
        self.fm_info.set(self.ui('Sichere bestätigte Originale und lade Dateien hoch …','Backing up confirmed originals and uploading files …'))
        self.fm_progress.set(0)
        backup_root=ROOT/'BACKUPS'/self.selected_ppsa
        def transfer():
            import datetime
            stamp=datetime.datetime.now().strftime('%Y%m%d_%H%M%S_%f')
            destination=backup_root/stamp
            client=self.ftp_client();results=[]
            for local,overwrite,remote_size in plan:
                remote=f'{target}/{local.name}'
                if overwrite:
                    destination.mkdir(parents=True,exist_ok=True)
                    backup=destination/local.name
                    client.download(remote,backup,expected_size=remote_size,progress=self.transfer_progress('Backup '+local.name))
                    if not backup.is_file() or (remote_size is not None and backup.stat().st_size!=remote_size):
                        raise FTPError(f'Backup-Prüfung fehlgeschlagen; Datei wurde nicht ersetzt: {remote}')
                client.upload(local,target,overwrite=overwrite,progress=self.transfer_progress(local.name))
                results.append(local.name)
            refreshed=client.list(target)
            wanted={name for name in results}
            if any(not any(row['name']==name for row in refreshed) for name in wanted):
                raise FTPError('Upload abgeschlossen, aber die aktualisierte Dateiliste ist unvollständig.')
            return (target,refreshed,results,showpath(destination))
        self.fm_run(transfer,'theme_uploaded')

    def rebuild(self):
        lang=self.lang.get()
        for variable,trace_id in getattr(self,'status_trace_ids',[]):
            try:variable.trace_remove('write',trace_id)
            except tk.TclError:pass
        for child in self.root.winfo_children():child.destroy()
        self.tiles={};self.images={};self.lang.set(lang);self.build();self.refresh();self.show_view(getattr(self,'current_view','dashboard'))
    def choose_output(self):
        folder=filedialog.askdirectory(title=self.t('folder'),initialdir=str(self.outdir))
        if folder:self.outdir=Path(folder);self.path_label.config(text=showpath(self.outdir))
    def pick(self,name):
        p=filedialog.askopenfilename(filetypes=[('Images','*.png *.jpg *.jpeg *.webp'),('All files','*.*')])
        if p:self.import_image(Path(p),name)
    def drop(self,event,name):
        try:
            paths=self.root.tk.splitlist(event.data)
            if paths:self.import_image(Path(paths[0]),name)
        except Exception as exc:messagebox.showerror(self.t('error'),str(exc))
    def import_image(self,path,name):
        try:
            with Image.open(path) as im: im.convert('RGB').save(self.indir/name,'PNG')
            self.refresh()
        except Exception as exc:messagebox.showerror(self.t('error'),str(exc))
    def refresh(self):
        loaded=0
        for name,lbl in self.tiles.items():
            file=self.indir/name
            if file.is_file():
                try:
                    with Image.open(file) as im: thumb=ImageOps.contain(im.convert('RGB'),(310,320))
                    photo=ImageTk.PhotoImage(thumb);self.images[name]=photo
                    lbl.config(image=photo,text='');loaded+=1
                except Exception:lbl.config(image='',text='Invalid image')
            else:lbl.config(image='',text='＋\n'+self.t('drop'))
        if not self.running:self.status.set(f'{self.t("ready")} · {loaded}/4 {self.t("loaded")}')
    def preview_first(self):
        name=next((n for n,_ in SLOTS if (self.indir/n).exists()),None)
        if name:self.preview(name)
        else:messagebox.showinfo(self.t('show'),self.t('missing'))
    def preview(self,name):
        file=self.indir/name
        if not file.exists():return self.pick(name)
        win=tk.Toplevel(self.root);win.title(f'{self.t("zoom")} — {name}');win.configure(bg=COL['bg']);win.geometry('1150x740')
        with Image.open(file) as im:
            dims=im.size;pic=ImageTk.PhotoImage(ImageOps.contain(im.convert('RGB'),(1100,650)))
        label=tk.Label(win,image=pic,bg=COL['bg']);label.image=pic;label.pack(fill='both',expand=True,padx=12,pady=12)
        self.label(win,f'{name}   ·   {dims[0]} × {dims[1]}',11).pack(pady=(0,10))
    def open_dir(self,path):
        path.mkdir(parents=True,exist_ok=True)
        if os.name=='nt':os.startfile(str(path))
        elif sys.platform=='darwin':subprocess.Popen(['open',str(path)])
        else:subprocess.Popen(['xdg-open',str(path)])
    def start(self):
        if self.running:return
        if not any((self.indir/n).exists() for n,_ in SLOTS):return messagebox.showwarning(self.t('error'),self.t('missing'))
        selected=[n for n,_ in SLOTS if (self.indir/n).is_file()]
        output_names={name for n in selected for name in (n,n.replace('.png','.dds'))}
        output_names.add('UPLOAD_HINWEISE.txt')
        collisions=sorted(name for name in output_names if (self.outdir/name).exists())
        if collisions and not messagebox.askyesno('Exportdateien ersetzen?',
                'Diese Dateien existieren bereits im Exportordner und werden durch das neue Paket ersetzt:\n\n'
                +'\n'.join(collisions)+'\n\nFortfahren?',parent=self.root):
            return
        self.show_view('dashboard')
        self.running=True;self.go.config(state='disabled');self.progress_value.set(0)
        self.status.set(self.t('convert')+' …')
        self.fm_progress.set(0)
        self.fm_info.set(self.ui('Paket wird erstellt · danach wird der FTP-Upload geprüft.','Creating package · FTP upload will be checked next.'))
        self.activity_files.set(self.ui('Ausgewählt: ','Selected: ')+', '.join(selected))
        self.target_status.set(self.ui('Wartet auf erstellte Dateien','Waiting for generated files'))
        mode=self.mode.get();source=self.indir;dest=self.outdir;tex=self.tex
        def job():
            try:
                result=build_package(source,dest,tex,mode,lambda i,total,detail:self.events.put(('progress',(i,total,detail))))
                generated=[dest/name for source_name in selected for name in (source_name,source_name.replace('.png','.dds'))]
                self.events.put(('done',(str(result),[str(path) for path in generated if path.is_file()])))
            except Exception as exc:self.events.put(('error',str(exc)))
        threading.Thread(target=job,daemon=True).start()
    def poll(self):
        try:
            while True:
                event,value=self.events.get_nowait()
                if event=='progress':
                    i,total,detail=value;self.progress_value.set(i/total*100);self.status.set(f'{i}/{total}  ·  {detail}')
                    self.fm_info.set(self.ui('Dateien werden erstellt · ','Creating files · ')+detail)
                elif event=='transfer_progress':
                    sent,total,detail=value
                    self.fm_progress.set(min(100,sent/total*100) if total else 0)
                    self.fm_info.set(f'{detail} · {sent:,}'+(f' / {total:,} Bytes' if total is not None else ' Bytes'))
                elif event=='fm_success':
                    self.fm_busy=False
                    kind,data=value
                    self._has_confirmed_ftp=True
                    self.connection_status.set(f'{self.ui("Erreichbar","Reachable")} · {self.ps5ip.get().strip()}:{self.ftp_port.get().strip()}')
                    if kind=='discover':self.fm_apply_discovery(data)
                    elif kind=='heartbeat':pass
                    elif kind=='theme_preflight':
                        files,target,entries=data
                        self.target_status.set(self.ui('FTP-Zielordner erreichbar','FTP target folder reachable'))
                        self.theme_confirm_upload(files,target,entries)
                    elif kind=='theme_preflight_auto':
                        files,target,entries=data
                        self.target_status.set(self.ui('FTP-Zielordner erreichbar','FTP target folder reachable'))
                        self.theme_confirm_upload(files,target,entries,automatic=True)
                    elif kind=='theme_uploaded':
                        target,entries,names,backup_path=data
                        self.fm_info.set('Upload abgeschlossen und im Zielordner geprüft · '+', '.join(names))
                        self.activity_files.set(self.ui('Erstellt und hochgeladen: ','Created and uploaded: ')+', '.join(names))
                        self.target_status.set(self.ui('Upload bestätigt','Upload verified')+' · '+target)
                        self.fm_progress.set(100)
                        messagebox.showinfo('Theme-Upload abgeschlossen',f'{len(names)} Datei(en) nach {target} übertragen und geprüft.\nLokale Backups: {backup_path}')
                elif event=='fm_error':
                    self.fm_busy=False
                    kind,error=value
                    if kind in ('theme_preflight','theme_preflight_auto','theme_uploaded'):
                        self.fm_info.set('PS5-Upload fehlgeschlagen · '+error)
                        self.target_status.set(self.ui('Upload fehlgeschlagen','Upload failed'))
                        self.activity_files.set(self.ui('Erstellung abgeschlossen; Upload-Fehler: ','Package created; upload error: ')+error)
                        self.fm_progress.set(0)
                        messagebox.showerror('PS5-Upload',error)
                    else:
                        self._has_confirmed_ftp=False
                        self.fm_info.set('FTP-FEHLER · '+error);self.fm_progress.set(0)
                        self.connection_status.set('Verbindung fehlgeschlagen' if kind in ('discover','heartbeat') else 'Nicht bestätigt · FTP-Fehler')
                        if kind=='discover':
                            self.ppsa_status.set('Nicht geprüft')
                            self.target_status.set('Verbindung fehlgeschlagen')
                            self.theme_upload_button.config(state='disabled')
                        messagebox.showerror('PS5-Verbindung',error)
                elif event=='done':
                    self.running=False;self.go.config(state='normal')
                    result,generated=value;self.last_generated_files=list(generated)
                    self.status.set(self.t('finished'))
                    self.progress_value.set(100)
                    self.activity_files.set(self.ui('Erstellt: ','Created: ')+', '.join(Path(p).name for p in generated))
                    if self.selected_ppsa and self._has_confirmed_ftp:
                        self.pending_upload_after_discovery=False
                        self.target_status.set(self.ui('Upload wird vorbereitet','Preparing upload'))
                        self.fm_info.set('Paket erstellt · starte automatischen Theme-Upload …')
                        self.theme_upload(automatic=True,files=[Path(p) for p in generated])
                    else:
                        self.pending_upload_after_discovery=True
                        message=('Paket erstellt. PS5-Verbindung und PPSA-Zielordner erkennen lassen, um automatisch hochzuladen.'
                                 if not self.selected_ppsa else
                                 'Paket erfolgreich erstellt, aber die FTP-Verbindung ist aktuell nicht bestätigt.\n'
                                 'Verbinde dich erneut, um die Dateien hochzuladen.\n'+showpath(result))
                        self.fm_info.set(self.ui('Paket erstellt · Dashboard verbinden, um den Upload zu starten.','Package created · connect from the Dashboard to start the upload.'))
                        self.target_status.set(self.ui('Upload wartet auf PS5-Verbindung','Waiting for PS5 connection'))
                        messagebox.showinfo('Y2JB MrGee',message)
                else:
                    self.running=False;self.go.config(state='normal');self.status.set(self.t('error'));self.fm_info.set(self.ui('Paket-Erstellung fehlgeschlagen · ','Package creation failed · ')+value);self.target_status.set(self.ui('Paket nicht erstellt','Package not created'));messagebox.showerror(self.t('error'),value)
        except queue.Empty:pass
        self.root.after(90,self.poll)

def main():
    root=TkinterDnD.Tk() if TkinterDnD else tk.Tk()
    icon=ROOT/'assets'/'y2jb_icon.ico'
    if icon.is_file():
        try:root.iconbitmap(default=str(icon))
        except tk.TclError:pass
    Studio(root);root.mainloop()
if __name__=='__main__':main()
