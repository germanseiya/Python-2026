import wx
import re

class FormularioMedicoFrame(wx.Frame):
    def __init__(self, parent, title):
        super(FormularioMedicoFrame, self).__init__(parent, title=title, size=(750, 450))
        
        panel = wx.Panel(self)
        
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        titulo = wx.StaticText(panel, label="Registro del Médico")
        font_titulo = titulo.GetFont()
        font_titulo.SetPointSize(14)
        font_titulo.SetWeight(wx.FONTWEIGHT_BOLD)
        titulo.SetFont(font_titulo)
        main_sizer.Add(titulo, flag=wx.ALL | wx.ALIGN_CENTER, border=15)
        
        grid_sizer = wx.FlexGridSizer(rows=5, cols=2, hgap=10, vgap=12)
        grid_sizer.AddGrowableCol(1, proportion=1)
        
        """1. Nombre"""
        grid_sizer.Add(wx.StaticText(panel, label="Nombre:"), flag=wx.ALIGN_CENTER_VERTICAL)
        self.txt_nombre = wx.TextCtrl(panel)
        grid_sizer.Add(self.txt_nombre, flag=wx.EXPAND)
        
        """2. RUT (Formato automático)"""
        grid_sizer.Add(wx.StaticText(panel, label="RUT:"), flag=wx.ALIGN_CENTER_VERTICAL)
        self.txt_rut = wx.TextCtrl(panel)
        self.txt_rut.Bind(wx.EVT_TEXT, self.on_formatear_rut)
        grid_sizer.Add(self.txt_rut, flag=wx.EXPAND)
        
        """3. Edad"""
        grid_sizer.Add(wx.StaticText(panel, label="Edad:"), flag=wx.ALIGN_CENTER_VERTICAL)
        self.txt_edad = wx.TextCtrl(panel)
        grid_sizer.Add(self.txt_edad, flag=wx.EXPAND)
        
        """4. Género"""
        grid_sizer.Add(wx.StaticText(panel, label="Género:"), flag=wx.ALIGN_CENTER_VERTICAL)
        self.choice_genero = wx.Choice(panel, choices=["Masculino", "Femenino", "Teto", "Miku"])
        self.choice_genero.SetSelection(0)
        grid_sizer.Add(self.choice_genero, flag=wx.EXPAND)
        
        """5. Especialidad"""
        grid_sizer.Add(wx.StaticText(panel, label="Especialidad:"), flag=wx.ALIGN_CENTER_VERTICAL)
        
        self.lista_especialidades = [
            "Medicina General", "Cardiología", "Pediatría", "Traumatología", 
            "Neurología", "Dermatología", "Psiquiatría", "Oftalmología", 
            "Otorrinolaringología", "Ginecología y Obstetricia", "Urología", 
            "Cirugía General", "Endocrinología", "Gastroenterología", 
            "Nefrología", "Oncología", "Reumatología", "Geriatría", 
            "Infectología", "Medicina Intensiva", "Anestesiología"
        ]
        
        self.combo_especialidad = wx.ComboBox(panel, choices=self.lista_especialidades, style=wx.CB_DROPDOWN)
        self.combo_especialidad.Bind(wx.EVT_TEXT, self.on_texto_especialidad)
        grid_sizer.Add(self.combo_especialidad, flag=wx.EXPAND)
        
        main_sizer.Add(grid_sizer, proportion=0, flag=wx.ALL | wx.EXPAND, border=20)
        
        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.btn_guardar = wx.Button(panel, label="Guardar Registro")
        self.btn_guardar.Bind(wx.EVT_BUTTON, self.on_guardar)
        btn_sizer.Add(self.btn_guardar, flag=wx.RIGHT, border=10)
        
        self.btn_limpiar = wx.Button(panel, label="Limpiar Campos")
        self.btn_limpiar.Bind(wx.EVT_BUTTON, self.on_limpiar)
        btn_sizer.Add(self.btn_limpiar)
        
        main_sizer.Add(btn_sizer, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=15)
        
        panel.SetSizer(main_sizer)
        
        main_sizer.Fit(self)
        self.Centre()

    def on_formatear_rut(self, event):
        txt_ctrl = self.txt_rut
        val = txt_ctrl.GetValue()
        
        cuerpo_limpio = "".join(c for c in val if c.isalnum()).upper()
        if not cuerpo_limpio:
            event.Skip()
            return
            
        if len(cuerpo_limpio) > 1:
            cuerpo = cuerpo_limpio[:-1]
            dv = cuerpo_limpio[-1]
        else:
            cuerpo = cuerpo_limpio
            dv = ""
            
        cuerpo_fmt = ""
        while len(cuerpo) > 3:
            cuerpo_fmt = "." + cuerpo[-3:] + cuerpo_fmt
            cuerpo = cuerpo[:-3]
        cuerpo_fmt = cuerpo + cuerpo_fmt
        
        rut_formateado = f"{cuerpo_fmt}-{dv}" if dv else cuerpo_fmt
        
        pos = txt_ctrl.GetInsertionPoint()
        if txt_ctrl.GetValue() != rut_formateado:
            txt_ctrl.SetValue(rut_formateado)
            txt_ctrl.SetInsertionPoint(len(rut_formateado))
            
        event.Skip()

    def on_texto_especialidad(self, event):
        texto_ingresado = self.combo_especialidad.GetValue()
        if texto_ingresado in self.lista_especialidades:
            event.Skip()
            return
            
        for opcion in self.lista_especialidades:
            if opcion.lower().startswith(texto_ingresado.lower()):
                current_len = len(texto_ingresado)
                self.combo_especialidad.SetValue(opcion)
                self.combo_especialidad.SetInsertionPoint(current_len)
                self.combo_especialidad.SetSelection(current_len, len(opcion))
                break
        event.Skip()

    def validar_rut_chileno(self, rut_str):
        patron = r"^\d{1,2}\.\d{3}\.\d{3}-[0-9kK]$"
        if not re.match(patron, rut_str):
            return False
        
        rut_limpio = rut_str.replace(".", "").upper()
        cuerpo, dv = rut_limpio.split("-")
        
        suma = 0
        multiplo = 2
        for r in reversed(cuerpo):
            suma += int(r) * multiplo
            multiplo += 1
            if multiplo == 8:
                multiplo = 2
                
        esperado = 11 - (suma % 11)
        if esperado == 11:
            dv_esperado = "0"
        elif esperado == 10:
            dv_esperado = "K"
        else:
            dv_esperado = str(esperado)
            
        return dv == dv_esperado

    def on_guardar(self, event):
        nombre = self.txt_nombre.GetValue().strip()
        rut = self.txt_rut.GetValue().strip()
        edad_str = self.txt_edad.GetValue().strip()
        
        if not nombre or not all(c.isalpha() or c.isspace() for c in nombre):
            wx.MessageBox("El nombre completo debe contener únicamente letras y espacios válidos.", "Error de Validación", wx.OK | wx.ICON_ERROR)
            return
            
        if not self.validar_rut_chileno(rut):
            wx.MessageBox("El RUT ingresado no es válido o está incompleto (Formato requerido: XX.XXX.XXX-X).", "Error de Validación", wx.OK | wx.ICON_ERROR)
            return
            
        try:
            edad = int(edad_str)
            if edad <= 18:
                wx.MessageBox("La edad del médico debe ser de al menos 18 años.", "Error de Validación", wx.OK | wx.ICON_ERROR)
                return
        except ValueError:
            wx.MessageBox("Por favor, ingrese un número entero válido para la edad.", "Error de Validación", wx.OK | wx.ICON_ERROR)
            return
            
        wx.MessageBox(f"Registro del médico {nombre} (RUT: {rut}) guardado exitosamente.", "Éxito", wx.OK | wx.ICON_INFORMATION)

    def on_limpiar(self, event):
        self.txt_nombre.Clear()
        self.txt_rut.Clear()
        self.txt_edad.Clear()
        self.choice_genero.SetSelection(0)
        self.combo_especialidad.SetValue("")

if __name__ == '__main__':
    app = wx.App()
    frame = FormularioMedicoFrame(None, title="Sistema de Gestión Hospitalaria - Registro del Médico")
    frame.Show()
    app.MainLoop()