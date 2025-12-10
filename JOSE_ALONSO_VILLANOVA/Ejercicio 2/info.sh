#!/bin/bash
# ==========================================================
# Script: info_equipo.sh
#
# Objetivo:
# Obtener información del sistema de forma portable
# (Linux, macOS y Windows usando Git Bash o WSL).
#
# Toda la información se muestra en una sola línea.
# ==========================================================


# ----------------------------------------------------------
# FUNCIÓN: obtener_usuario
# Devuelve el usuario que ejecuta el script.
# ----------------------------------------------------------
obtener_usuario() {
    whoami
}


# ----------------------------------------------------------
# FUNCIÓN: obtener_hostname
# Devuelve el nombre del equipo.
# ----------------------------------------------------------
obtener_hostname() {
    hostname
}


# ----------------------------------------------------------
# FUNCIÓN: obtener_fecha_hora
# Función extra: muestra fecha y hora actuales.
# Añadida para enriquecer el script.
# ----------------------------------------------------------
obtener_fecha_hora() {
    date "+%Y-%m-%d %H:%M:%S"
}


# ----------------------------------------------------------
# FUNCIÓN: obtener_sistema_operativo
# Detecta el sistema operativo concreto.
# ----------------------------------------------------------
obtener_sistema_operativo() {

    # Linux
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        if [ -f /etc/os-release ]; then
            grep "^PRETTY_NAME=" /etc/os-release | cut -d= -f2 | tr -d '"'
        else
            uname -s
        fi

    # macOS
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        echo "macOS $(sw_vers -productVersion)"

    # Windows con Git Bash / MSYS
    elif [[ "$OSTYPE" == "msys"* ]] || [[ "$OSTYPE" == "cygwin"* ]]; then
        echo "Windows (Git Bash)"

    else
        echo "Sistema desconocido"
    fi
}


# ----------------------------------------------------------
# FUNCIÓN: obtener_mac
# Obtiene la dirección MAC según el sistema operativo.
# ----------------------------------------------------------
obtener_mac() {

    # -------- Linux --------
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        ip link | awk '/ether/ {print $2; exit}'

    # -------- macOS --------
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        ifconfig | awk '/ether/ {print $2; exit}'

    # -------- Windows (Git Bash) --------
    elif [[ "$OSTYPE" == "msys"* ]] || [[ "$OSTYPE" == "cygwin"* ]]; then
        # getmac es un comando nativo de Windows
        getmac | awk 'NR==4 {print $1}'

    else
        echo "Desconocida"
    fi
}


# ----------------------------------------------------------
# FUNCIÓN: obtener_ip_local
# Función extra: obtiene la IP local del equipo.
# ----------------------------------------------------------
obtener_ip_local() {

    if command -v ip >/dev/null 2>&1; then
        ip route get 1 | awk '{print $7; exit}'

    elif command -v ifconfig >/dev/null 2>&1; then
        ifconfig | awk '/inet / && $2 != "127.0.0.1" {print $2; exit}'

    else
        echo "IP no detectada"
    fi
}


# ----------------------------------------------------------
# FUNCIÓN PRINCIPAL
# Muestra toda la información en una sola línea.
# ----------------------------------------------------------
mostrar_informacion() {

    SISTEMA=$(obtener_sistema_operativo)
    USUARIO=$(obtener_usuario)
    HOST=$(obtener_hostname)
    MAC=$(obtener_mac)
    IP=$(obtener_ip_local)
    FECHA=$(obtener_fecha_hora)

    echo "SO: $SISTEMA | Usuario: $USUARIO | Equipo: $HOST | MAC: $MAC | IP: $IP | Fecha: $FECHA"
}

# Ejecutar la función principal
mostrar_informacion
