
QT       += core gui opengl
LIBS += -lopengl32 -lglu32

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = MyOpenGL
TEMPLATE = app


SOURCES += main.cpp\
        window.cpp \
    myglwidget.cpp \
    thread.cpp

HEADERS  += window.h \
    myglwidget.h \
    thread.h

FORMS    += window.ui

CONFIG += c++14
