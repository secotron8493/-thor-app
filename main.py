"""THOR - Asistente de IA con Avatares Góticos"""
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDRaisedButton, MDIconButton, MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import MDScrollView
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.metrics import dp
from kivy.app import App

Window.size = (360, 640)

AVATARS = {
    'gothic_girl': {'name': 'Luna Oscura', 'emoji': '🦇', 'desc': 'Gótica clásica'},
    'cyber_goth': {'name': 'Nova Synth', 'emoji': '🤖', 'desc': 'Cyber gótica'},
    'vampire_lady': {'name': 'Carmilla Blood', 'emoji': '🧛‍♀️', 'desc': 'Vampiresa'},
    'witch_dark': {'name': 'Morgana Hex', 'emoji': '🧙‍♀️', 'desc': 'Bruja oscura'},
    'skeleton_queen': {'name': 'Morticia Bones', 'emoji': '💀', 'desc': 'Reina esqueleto'},
    'punk_goth': {'name': 'Raven Storm', 'emoji': '🎸', 'desc': 'Punk gótica'}
}

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'welcome'
        layout = MDBoxLayout(orientation='vertical', padding=dp(30), spacing=dp(20))
        layout.add_widget(MDLabel(size_hint_y=0.15))
        layout.add_widget(MDLabel(text="⚡", font_style="H1", halign="center", size_hint_y=0.2))
        layout.add_widget(MDLabel(text="THOR", font_style="H2", halign="center", size_hint_y=0.15, theme_text_color="Custom", text_color=(1, 0.84, 0, 1)))
        layout.add_widget(MDLabel(text="Asistente de IA\ncon Avatares Góticos", font_style="H6", halign="center", size_hint_y=0.15))
        layout.add_widget(MDLabel(size_hint_y=0.05))
        btn = MDRaisedButton(text="⚡ Comenzar", pos_hint={"center_x": 0.5}, size_hint_x=0.7, md_bg_color=(0.54, 0, 0.54, 1), on_release=lambda x: setattr(self.manager, 'current', 'home'))
        layout.add_widget(btn)
        layout.add_widget(MDLabel(text="v1.0.0", font_style="Caption", halign="center", size_hint_y=0.1))
        layout.add_widget(MDLabel(size_hint_y=0.1))
        self.add_widget(layout)

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'home'
        layout = MDBoxLayout(orientation='vertical', spacing=dp(10), padding=dp(10))
        header = MDBoxLayout(size_hint_y=0.1, padding=dp(10))
        header.add_widget(MDLabel(text="⚡ THOR", font_style="H5", size_hint_x=0.7))
        header.add_widget(MDIconButton(icon="information", size_hint_x=0.3, on_release=self.show_info))
        layout.add_widget(header)
        avatar_box = MDBoxLayout(size_hint_y=0.12, padding=dp(10))
        self.avatar_emoji = MDLabel(text="🦇", font_style="H4", halign="center", size_hint_x=0.3)
        avatar_info = MDBoxLayout(orientation='vertical', size_hint_x=0.7)
        self.avatar_name = MDLabel(text="Luna Oscura", font_style="Subtitle1")
        self.avatar_status = MDLabel(text="Lista para ayudarte 💜", font_style="Caption")
        avatar_info.add_widget(self.avatar_name)
        avatar_info.add_widget(self.avatar_status)
        avatar_box.add_widget(self.avatar_emoji)
        avatar_box.add_widget(avatar_info)
        layout.add_widget(avatar_box)
        scroll = MDScrollView()
        cards = MDBoxLayout(orientation='vertical', spacing=dp(10), adaptive_height=True, padding=dp(10))
        features = [("💬 Chat IA", "Conversa conmigo", "chat", "chat"), ("📄 Análisis", "Analiza textos", "file-document", "analysis"), ("✨ Generador", "Crea contenido", "text-box", "textgen"), ("🎭 Mi Avatar", "Personalízame", "account-edit", "avatars")]
        for title, desc, icon, screen in features:
            cards.add_widget(self.create_card(title, desc, icon, screen))
        scroll.add_widget(cards)
        layout.add_widget(scroll)
        self.add_widget(layout)
    
    def create_card(self, title, desc, icon, screen):
        card = MDCard(orientation='horizontal', size_hint_y=None, height=dp(80), padding=dp(15), elevation=4, md_bg_color=(0.54, 0, 0.54, 1), on_release=lambda x: setattr(self.manager, 'current', screen))
        card.add_widget(MDIconButton(icon=icon, icon_size="35sp", size_hint_x=0.2))
        text_box = MDBoxLayout(orientation='vertical', size_hint_x=0.8)
        text_box.add_widget(MDLabel(text=title, font_style="Subtitle1"))
        text_box.add_widget(MDLabel(text=desc, font_style="Caption"))
        card.add_widget(text_box)
        return card
    
    def show_info(self, instance):
        dialog = MDDialog(title="⚡ THOR", text="Thor - Asistente de IA\n\nVersión 1.0.0\n\nAsistente inteligente con avatares góticos.", buttons=[MDFlatButton(text="Cerrar", on_release=lambda x: dialog.dismiss())])
        dialog.open()

class ChatScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'chat'
        layout = MDBoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))
        top = MDBoxLayout(size_hint_y=0.08)
        top.add_widget(MDIconButton(icon="arrow-left", on_release=lambda x: setattr(self.manager, 'current', 'home')))
        top.add_widget(MDLabel(text="💬 Chat IA", font_style="H6"))
        layout.add_widget(top)
        scroll = MDScrollView(size_hint_y=0.77)
        self.messages = MDBoxLayout(orientation='vertical', spacing=dp(10), padding=dp(10), adaptive_height=True)
        msg = MDCard(size_hint_y=None, height=dp(60), padding=dp(10), md_bg_color=(0.54, 0, 0.54, 1))
        msg.add_widget(MDLabel(text="🦇 ¡Hola! Soy THOR.\n¿En qué puedo ayudarte?"))
        self.messages.add_widget(msg)
        scroll.add_widget(self.messages)
        layout.add_widget(scroll)
        input_box = MDBoxLayout(size_hint_y=0.15, spacing=dp(10))
        self.chat_input = MDTextField(hint_text="Escribe...", size_hint_x=0.75)
        send_btn = MDIconButton(icon="send", size_hint_x=0.25, md_bg_color=(0.54, 0, 0.54, 1), on_release=self.send_message)
        input_box.add_widget(self.chat_input)
        input_box.add_widget(send_btn)
        layout.add_widget(input_box)
        self.add_widget(layout)
    
    def send_message(self, instance):
        text = self.chat_input.text.strip()
        if not text:
            return
        user_msg = MDCard(size_hint_y=None, height=dp(50), padding=dp(10), md_bg_color=(0.2, 0.2, 0.25, 1))
        user_msg.add_widget(MDLabel(text=f"👤 {text}"))
        self.messages.add_widget(user_msg)
        response = "Entiendo. THOR está en modo demo."
        bot_msg = MDCard(size_hint_y=None, height=dp(70), padding=dp(10), md_bg_color=(0.54, 0, 0.54, 1))
        bot_msg.add_widget(MDLabel(text=f"⚡ {response}"))
        self.messages.add_widget(bot_msg)
        self.chat_input.text = ""

class AvatarsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'avatars'
        layout = MDBoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))
        top = MDBoxLayout(size_hint_y=0.08)
        top.add_widget(MDIconButton(icon="arrow-left", on_release=lambda x: setattr(self.manager, 'current', 'home')))
        top.add_widget(MDLabel(text="🎭 Avatares", font_style="H6"))
        layout.add_widget(top)
        scroll = MDScrollView()
        avatars_list = MDBoxLayout(orientation='vertical', spacing=dp(10), adaptive_height=True, padding=dp(10))
        for aid, aconfig in AVATARS.items():
            card = MDCard(size_hint_y=None, height=dp(100), padding=dp(15), elevation=3, on_release=lambda x, a=aid, c=aconfig: self.select_avatar(a, c))
            box = MDBoxLayout(orientation='horizontal')
            box.add_widget(MDLabel(text=aconfig['emoji'], font_style="H3", size_hint_x=0.3, halign="center"))
            info = MDBoxLayout(orientation='vertical', size_hint_x=0.7)
            info.add_widget(MDLabel(text=aconfig['name'], font_style="Subtitle1"))
            info.add_widget(MDLabel(text=aconfig['desc'], font_style="Caption"))
            box.add_widget(info)
            card.add_widget(box)
            avatars_list.add_widget(card)
        scroll.add_widget(avatars_list)
        layout.add_widget(scroll)
        self.add_widget(layout)
    
    def select_avatar(self, aid, aconfig):
        app = App.get_running_app()
        app.current_avatar = aid
        dialog = MDDialog(title="⚡ Avatar", text=f"Has elegido a {aconfig['name']}!", buttons=[MDFlatButton(text="OK", on_release=lambda x: self.close_dialog(dialog))])
        dialog.open()
    
    def close_dialog(self, dialog):
        dialog.dismiss()
        self.manager.current = 'home'

class AnalysisScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'analysis'
        layout = MDBoxLayout(orientation='vertical', padding=dp(15), spacing=dp(15))
        top = MDBoxLayout(size_hint_y=0.08)
        top.add_widget(MDIconButton(icon="arrow-left", on_release=lambda x: setattr(self.manager, 'current', 'home')))
        top.add_widget(MDLabel(text="📄 Análisis", font_style="H6"))
        layout.add_widget(top)
        self.text_input = MDTextField(hint_text="Pega tu texto...", multiline=True, size_hint_y=0.3, mode="rectangle")
        layout.add_widget(self.text_input)
        analyze_btn = MDRaisedButton(text="⚡ Analizar", size_hint_y=0.08, md_bg_color=(0.54, 0, 0.54, 1), on_release=self.analyze)
        layout.add_widget(analyze_btn)
        scroll = MDScrollView(size_hint_y=0.54)
        self.result = MDLabel(text="El análisis aparecerá aquí...", markup=True, size_hint_y=None)
        self.result.bind(texture_size=self.result.setter('size'))
        scroll.add_widget(self.result)
        layout.add_widget(scroll)
        self.add_widget(layout)
    
    def analyze(self, instance):
        text = self.text_input.text
        if not text.strip():
            self.result.text = "[color=#FF0000]Ingresa texto[/color]"
            return
        chars = len(text)
        words = len(text.split())
        self.result.text = f"[b]⚡ Análisis:[/b]\n\nCaracteres: {chars}\nPalabras: {words}"

class TextGenScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'textgen'
        layout = MDBoxLayout(orientation='vertical', padding=dp(15), spacing=dp(15))
        top = MDBoxLayout(size_hint_y=0.08)
        top.add_widget(MDIconButton(icon="arrow-left", on_release=lambda x: setattr(self.manager, 'current', 'home')))
        top.add_widget(MDLabel(text="✨ Generador", font_style="H6"))
        layout.add_widget(top)
        self.prompt_input = MDTextField(hint_text="Describe...", multiline=True, size_hint_y=0.25, mode="rectangle")
        layout.add_widget(self.prompt_input)
        gen_btn = MDRaisedButton(text="⚡ Generar", size_hint_y=0.08, md_bg_color=(0.54, 0, 0.54, 1), on_release=self.generate)
        layout.add_widget(gen_btn)
        scroll = MDScrollView(size_hint_y=0.59)
        self.result = MDLabel(text="El texto aparecerá aquí...", markup=True, size_hint_y=None)
        self.result.bind(texture_size=self.result.setter('size'))
        scroll.add_widget(self.result)
        layout.add_widget(scroll)
        self.add_widget(layout)
    
    def generate(self, instance):
        prompt = self.prompt_input.text
        if not prompt.strip():
            self.result.text = "[color=#FF0000]Ingresa prompt[/color]"
            return
        self.result.text = f"[b]⚡ Generado:[/b]\n\nBasado en '{prompt}'"

class ThorApp(MDApp):
    current_avatar = StringProperty('gothic_girl')
    def build(self):
        self.title = "THOR"
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Dark"
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen())
        sm.add_widget(HomeScreen())
        sm.add_widget(ChatScreen())
        sm.add_widget(AvatarsScreen())
        sm.add_widget(AnalysisScreen())
        sm.add_widget(TextGenScreen())
        return sm

if __name__ == '__main__':
    ThorApp().run()
