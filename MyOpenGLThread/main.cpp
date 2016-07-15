// main.cpp

#include <QApplication>
#include <QDesktopWidget>

#include <thread.h>
#include <QVector>

#include "window.h"

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    Window window;
    window.resize(window.sizeHint());
    int desktopArea = QApplication::desktop()->width() *
                     QApplication::desktop()->height();
    int widgetArea = window.width() * window.height();

    window.setWindowTitle("GRAFICADOR");

    if (((float)widgetArea / (float)desktopArea) < 0.75f)
        window.show();
    else
        window.showMaximized();

    //window.ui->myGLWidget->draw(6,5);
    //pantalla -> myGLWidget->graficar(6,5);
    //(*pantalla) -> myGLWidget -> graficar(6,5);
    QVector<thread*> v_thread;
    //window.graficar_en_pantalla(-15);
    //window.graficar_en_pantalla(20);
    //window.graficar_en_pantalla(10);
    //window.graficar_en_pantalla(15);
    float dominioi = -15;
    float dominiof = 15;
    float intervalo = 1;
    float limite;
    int cant_thread = thread::idealThreadCount();
    if (cant_thread == 0 or cant_thread == 1){
        cant_thread = 1;
    }
    else {
        cant_thread = cant_thread - 1;
    }
    float cant_dominio = abs(dominioi) + abs (dominiof);
    cant_dominio = cant_dominio/cant_thread;
    qDebug()<<&window;
    //thread myThread1;
    int a = 0;
    while (a<cant_thread) {
        limite = dominioi + cant_dominio - intervalo;
        thread* threadbasico = new thread();
        v_thread.append(threadbasico);
        v_thread[a]->dominioi = dominioi;
        v_thread[a]->limite = limite;
        v_thread[a]->intervalo = intervalo;
        v_thread[a]->ventana = &window;
        dominioi = dominioi + cant_dominio;
        a++;
    }
    a = 0;
    while (a<cant_thread) {
        v_thread[a]->start();
        a++;
    }
    /*myThread1.dominioi = -15;
    myThread1.limite = -6;
    myThread1.intervalo = 1;
    myThread1.ventana = &window;*/

    /*thread myThread2;
    myThread2.dominioi = -5;
    myThread2.limite = 4;
    myThread2.intervalo = 1;
    thread myThread3;
    myThread3.dominioi = 5;
    myThread3.limite = 15;
    myThread3.intervalo = 1;*/
    //v_thread.append(&myThread);
    //myThread.start();
    //myThread1.start();
    //myThread2.start();
    //myThread3.start();


    return app.exec();
}
