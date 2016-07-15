// window.cpp

#include <QtWidgets>
#include "window.h"
#include "ui_window.h"

#include "myglwidget.h"

Window::Window(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Window)
{
    ui->setupUi(this);

    connect(ui->myGLWidget, SIGNAL(xRotationChanged(int)), ui->rotXSlider, SLOT(setValue(int)));
    connect(ui->myGLWidget, SIGNAL(yRotationChanged(int)), ui->rotYSlider, SLOT(setValue(int)));
    connect(ui->myGLWidget, SIGNAL(zRotationChanged(int)), ui->rotZSlider, SLOT(setValue(int)));
    ui->pushGraficar->setText("Graficar");
    ui->pushBorrar->setText("Borrar");
    ui->myGLWidget->graficar(0.5,0.5);
    ui->myGLWidget->graficar(0.5,-0.0);
    ui->myGLWidget->graficar(0.5,0.5);
}

Window::~Window()
{
    delete ui;
}

void Window::keyPressEvent(QKeyEvent *e)
{
    if (e->key() == Qt::Key_Escape)
        close();
    else
        QWidget::keyPressEvent(e);
}

void Window::on_pushGraficar_clicked()
{
    QString tex = ui->lineEdit->text();

}
