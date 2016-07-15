#ifndef THREAD_H
#define THREAD_H

#include <QtCore>
#include <window.h>

class thread : public QThread
{
public:
    thread();
    void run();
    void funcion_ali(float,float,float);
    //QString name;
    float dominioi;
    float intervalo;
    float limite;
    Window* ventana;
};

#endif // THREAD_H
