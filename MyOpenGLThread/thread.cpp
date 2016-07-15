#include "thread.h"
#include <QtCore>
#include <QDebug>

thread::thread()
{

}

void thread::run(){
    //qDebug() << this -> name;
    thread::funcion_ali(this -> dominioi,this -> limite, this -> intervalo);
}

void thread::funcion_ali(float x, float limite, float intervalo){
    if(x <= limite){
        qDebug()<<x;
        ventana->graficar_en_pantalla(x);
        x = x + intervalo;
        //funcion_ali(x,limite,intervalo);
    }
}
