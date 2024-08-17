using system;
using system.windows.forms;
namespace encuesta
{
    public class form1 : form
}
public form1 ()
{
    //crear ventana
    principal
    this.widht = 300;
    this.height = 400;
    this.backColor = system.drawing.color.white;
    this.padding = new padding(20);
    this.borderstyle = borderstyle.fixedsingle;
    this.starPosition = FormStartPosition.centerScreen;

    // Agregar titulo
    label titulo = new label ();
    titulo.text = "encuesta";
    titulo.autosize = true;
    this.controls.add(titulo);
    //agregar pregunta
    nombre
    label preguntaNombre
    = new label ();
    preguntaNombre.text = "¿Cual es tu nombre?"
    this.controls.add(preguntaNombre);

    textBox inputNombre = newtextbox();

    this.controls.add(inputNombre)

    //agregar pregunta dificultad
    label preguntaDificultad = newlabel();
    preguntaDificultad.text = ¿Que dificultad deseas?;
    this.controls.add(preguntaDificultad);

    combobox selectDificultad = new Combobox();
    selectDificultad.items.add("Facil")
    selectDificultad.items.add("Medio")
    selectDificultad.items.add("Dificil")
    this.controls.add(selectDificultad)

    //agregar boton
    button boton = new button();
    boton.text = "enviar";
    this.controls.add(boton);
    }

    [STAThread]
    static void Main ()
    {
        Application.EnableVisualStyles();
        Application.setCompatibleTextRenderingDeafult(false);
        Application.Run(New Form 1());
    }
