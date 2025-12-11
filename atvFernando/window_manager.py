
import tkinter as tk

_janela_atual = None
_raiz_oculta = False

def _ao_destruir(evento, janela):
    global _janela_atual, _raiz_oculta
    try:
        if janela is _janela_atual:
            _janela_atual = None
            if _raiz_oculta and tk._default_root is not None:
                try:
                    tk._default_root.deiconify()
                except Exception:
                    pass
                _raiz_oculta = False
    except Exception:
        pass

def registrar(janela):
    
    global _janela_atual, _raiz_oculta
    try:
        if tk._default_root is not None and not _raiz_oculta:
            try:
                tk._default_root.withdraw()
                _raiz_oculta = True
            except Exception:
                pass

        if _janela_atual is not None and _janela_atual is not janela and _janela_atual.winfo_exists():
            try:
                _janela_atual.destroy()
            except Exception:
                pass

        _janela_atual = janela
        try:
            janela.bind('<Destroy>', lambda e, j=janela: _ao_destruir(e, j))
        except Exception:
            pass
    except Exception:
        pass

def obter_atual():
    return _janela_atual

def desregistrar():
    
    global _janela_atual, _raiz_oculta
    _janela_atual = None
    if _raiz_oculta and tk._default_root is not None:
        try:
            tk._default_root.deiconify()
        except Exception:
            pass
        _raiz_oculta = False
