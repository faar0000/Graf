// window.h

#ifndef WINDOW_H
#define WINDOW_H

#include <QWidget>
#include <QSlider>

namespace Ui {
class Window;
}

class Window : public QWidget
{
    Q_OBJECT

public:
    explicit Window(QWidget *parent = 0);
    void graficar_en_pantalla(float);
    //Ui::Window *ui;
    ~Window();

protected:
    void keyPressEvent(QKeyEvent *event);

private:
    Ui::Window *ui;
};

#endif // WINDOW_H
